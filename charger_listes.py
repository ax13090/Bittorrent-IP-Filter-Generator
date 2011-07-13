from io import BytesIO
import gzip, codecs
from urllib.request import Request
from urllib.request import urlopen 

chemin_bt_level_1 = r'http://list.iblocklist.com/?list=bt_level1&fileformat=p2p&archiveformat=gz'
chemin_bt_level_2 = r'http://list.iblocklist.com/?list=bt_level2&fileformat=p2p&archiveformat=gz'
chemin_bt_level_3 = r'http://list.iblocklist.com/?list=bt_level3&fileformat=p2p&archiveformat=gz'

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

def main():
	contenus = []
#	adresses = [chemin_bt_level_1, chemin_bt_level_2, chemin_bt_level_3]
	adresses = [
'file:/Users/axel/Downloads/bt_level1.gz', 
'file:/Users/axel/Downloads/bt_level2.gz', 
'file:/Users/axel/Downloads/bt_level3.txt']

	for adresse in adresses:
		contenus.append(charger(adresse))

	with codecs.open('./liste_filtrage_bittorrent.txt', 'w', encoding='utf8', errors='ignore') as sortie:
		for contenu in contenus:
			sortie.write(contenu)


if __name__ == '__main__':
	main()
