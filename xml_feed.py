import os, feedparser, os.path, subprocess
from os import walk
          
output1 = open("scriptpython.txt", "w+")
output = open("scriptpython.xml", "w+")
 
#mettre la version et l'encodage sur le fichier xml
output.write("<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n")
output.write("<sortie>\n")
 
#mise en place du dico pour les rubriques
print("économie, une, europe, société, intertional,idées, médias, sport, planète, culture, livres, cinéma, voyage, technologies, politique, sciences ")
choix = input("Quelle est la rubrique à traiter?")
 
rubriqueliste = {"économie": "0,2-3234,1-0,0",
            "une": "0,2-3208,1-0,0",
            "europe":"0,2-3214,1-0,0",
            "société":"0,2-3224,1-0,0",
            "international":"0,2-3210,1-0,0",
            "idées":"0,2-3232,1-0,0",
            "médias":"0,2-3236,1-0,0",
            "sport": "0,2-3242,1-0,0",
            "planète": "0,2-3244,1-0,0",
            "culture": "0,2-3246,1-0,0",
            "livres":"0,2-3260,1-0,0",
            "cinéma":"0,2-3476,1-0,0",
            "voyage":"0,2-3546,1-0,0",
            "technologies":"0,2-651865,1-0,0",
            "politique":"0,57-0,64-823353,0",
            "sciences":"env_sciences"
                 }
 
rubrique = rubriqueliste.get(choix)
 
 
 
#accès aux sous-fichiers, parcours de l'arborescence:
for root, directories, filenames in os.walk("/home/y/Documents/arbre"):
    for filename in filenames:
        if ".xml" in filename and rubrique in filename:
                file = os.path.join(root,filename) 
                
                   
                #parser les fichiers sÃ©lectionnÃ©s  
                d = feedparser.parse(file)
                entry = d.entries[1]

                for entry in d.entries:

                    #écriture dans les fichiers de sortie avec les balises
                    output.write("<item>"+"\n")
                    output.write("<title>"+entry.title+"</title>"+"\n")
                    output.write("<description>"+entry.description+"</description>"+"\n")
                    output.write("</item>"+"\n")

                    output1.write(entry.title+"\n")
                    output1.write(entry.description+"\n")
                    output1.write("\n")



output.write("</sortie>")
output.close()
output1.close()

#commande shell pour exécuter treetagger 
subprocess.call("perl ~/Documents/tagger/token.pl -f ~/Documents/tagger/scriptpython.txt |~/Documents/tagger/cmd/tree-tagger-french > ~/Documents/tagger/output.txt", shell = True)

#conversion du fichier de Treetagger en XML
subprocess.call("perl ~/Documents/tagger/xml.pl ~/Documents/tagger/output.txt utf8", shell = True)

#exécution de Talismane
subprocess.call("java -Xmx1G -Dconfig.file=talismane-fr-5.2.0.conf -jar talismane-core-5.3.0.jar --analyse --sessionId=fr --encoding=UTF8 --inFile=/home/y/Documents/tagger/scriptpython.txt --outFile=/home/y/Documents/tagger/frTest.tal" , shell = True, cwd = "/home/y/Documents/talismane")

#conversion du fichier de Talismane en XML
subprocess.call("perl /home/y/Documents/talismanexml.pl /home/y/Documents/tagger/frTest.tal", shell= True)
