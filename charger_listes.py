''' 
Ce script pour Python 3 récupèrtrois listes d'adresses IP a bannir sur les réseaux eer-to-Peer
Ces listes sont récupérées depuis le site ipblocklist.com
Comme le site les fournit compressées en GZip, ce script se charge de ladécompression.
Il se charge aussi d'assembler les trois listes, en les concaténant vers un fichier dans le répertoire courant
Ce script se lance sans argument, par exemple avec la commande suivante:
	$ python3 charger_listes.py
La sortie se situera dans le fichier liste_filtrage_bittorrent.txt du répertoire courant. Ce fichier 
sera écrasé s'il existe da au moment du lancement du programme. 
'''


from io import BytesIO
import gzip, codecs
from urllib.request import Request
from urllib.request import urlopen 


# Les chemins d'acces vers les trois listes a recuperer
chemin_bt_level_1 = r'http://list.iblocklist.com/?list=bt_level1&fileformat=p2p&archiveformat=gz'
chemin_bt_level_2 = r'http://list.iblocklist.com/?list=bt_level2&fileformat=p2p&archiveformat=gz'
chemin_bt_level_3 = r'http://list.iblocklist.com/?list=bt_level3&fileformat=p2p&archiveformat=gz'


'''
Une fonction qui se connecte au serveur, récupère la liste dont le chemin est passé en argument,
Décompresse la liste, et la renvoie sous la forme d'une chaine de caracteres
prete a etre affichee ou inseree dans un fichier
'''
def charger(chemin):
	request = Request(chemin)
	request.add_header('Accept-encoding', 'gzip')
	response = urlopen(request)
	print(response.info())
	info = response.info()
	buf = BytesIO( response.read())
	f = gzip.GzipFile(fileobj=buf)
	data = f.read()
	return data.decode(errors='ignore')



'''
Fonction principale du programme
Appelle trois fois la fonction charger() pour récupérer les trois listes
Ouvre un fichier en écriture ; ce fichier est écrasé s'il existe da
Replit le fichier avec la concaténation des trois listesrécupérées depuInternet
'''
def main():
	contenus = []
	adresses = [chemin_bt_level_1, chemin_bt_level_2, chemin_bt_level_3]

	for adresse in adresses:
		contenus.append(charger(adresse))

	with codecs.open('./liste_filtrage_bittorrent.txt', 'w', encoding='utf8', errors='ignore') as sortie:
		for contenu in contenus:
			sortie.write(contenu)



'''
Si ce fichier est le fichier passé en argument a l'interpréteuret non inclus en tant que modul
on lance la fonction principale
'''
if __name__ == '__main__':
	main()
