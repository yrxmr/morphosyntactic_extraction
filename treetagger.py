#pour lancer le script, il faut le faire depuis un terminal bash
#écrire python3 le chemin du script puis le patron à trouver 

import argparse
import xml.etree.ElementTree as ET

output = open("patronstagger.txt","w+")

#sous-programme: parsing du patron avec argparse
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('patron', metavar='type', nargs='+', help='List of types to search for')
    return parser.parse_args()

#sous-programme: matching entre arguments et contenu du fichier
def matches(pattern, current_types):
    for pair in zip(pattern, current_types):
        if not pair[1].startswith(pair[0]):
            break
    else:
        return True

#programme principale
def main():
#on lance le premier sous-programme
    args = parse_arguments()
    patron = args.patron
    print(f'Searching for {patron}')

    current_types = [''] * len(patron)
    current_strings = [''] * len(patrtelon)

#parsing du fichier avec Element Tree
    tree = ET.parse('output.txt.xml')
#on parcourt l'arbre de sorte à  arriver jusqu'à  l'élément qui nous intéresse 
    document = tree.getroot()
    article = document.find('article')

#itération sur tous les éléments "element"
    for element in article.iter('element'):
        element_string = element.findtext("data[@type='string']")
        current_strings.append(element_string)
        current_strings.pop(0)

        element_type = element.findtext("data[@type='type']")
        current_types.append(element_type)
        current_types.pop(0)

#on regarde si le matching a eu lieu grÃ¢ce au second sous-programme
        if matches(patron, current_types):
            output.write(' '.join(current_strings)+"\n")
    else:
        print("Plus de patrons à trouver")


if __name__ == "__main__":
    main()
