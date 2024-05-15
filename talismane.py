#pour lancer le script, il faut le faire depuis un terminal bash
#écrire python3 le chemin du script puis le patron à trouver 

import argparse
import xml.etree.ElementTree as ET

output = open("/patronstalismane.txt","w+")

#Sous-programme: parsing des arguments du patron avec argparse
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('patron', metavar='type', nargs='+', help='List of types to search for')
    return parser.parse_args()

#Sous-programme: vérification du matching entre le patron et le contenu du fichier
def matches(pattern, current_types):
    for pair in zip(pattern, current_types):
        if not pair[1].startswith(pair[0]):
            break
    else:
        return True


#programme principal 
def main():
#on lance le sous-programme pour parser les arguments du patron
    args = parse_arguments()
    patron = args.patron
    print(f'Searching for {patron}')

    current_types = [''] * len(patron)
    current_strings = [''] * len(patron)

#parsing du fichier avec Element Tree
    tree = ET.parse('/frTest.tal.xml')
#on accède au root de l'arbre pour ensuite pouvoir le parcourir
    basetalismane = tree.getroot()
    
#itération sur chaque élément P, puis sur chaque élément item
    for p in basetalismane.findall("p"):
        for item in p.findall("item"):
            item_string = item.findtext("a[2]")
            current_strings.append(item_string)
            current_strings.pop(0)

            item_type = item.findtext("a[4]")
            current_types.append(item_type)
            current_types.pop(0)
            
#on vérifie si le matching a eu lieu grâce au sous-programme
            if matches(patron, current_types):
                output.write(' '.join(current_strings)+"\n")
            else:
                print("Plus de patrons à trouver")


if __name__ == "__main__":
    main()
