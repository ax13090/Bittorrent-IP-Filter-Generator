from io import BytesIO
import gzip
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
	print('Content-Encoding', response.info().get('Content-Encoding') )
	info = response.info()
	buf = BytesIO( response.read())
	f = gzip.GzipFile(fileobj=buf)
	data = f.read()
	return data.decode(errors='ignore')


if __name__ == '__main__':
	print (charger(r'file:/Users/axel/Downloads/bt_level3.txt'))
