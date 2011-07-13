from urllib.request import urlopen
chemin_bt_level_1 = r'http://list.iblocklist.com/?list=bt_level1&fileformat=p2p&archiveformat=gz'


def charger(chemin):
	with urlopen(chemin) as f:
		print(f.get('Content-Encoding'))
		#print(f.read())
	pass;


if __name__ == '__main__':
	charger(chemin_bt_level_1)
