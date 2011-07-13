from io import BytesIO
import gzip
from urllib.request import Request
from urllib.request import urlopen 

chemin_bt_level_1 = r'http://list.iblocklist.com/?list=bt_level1&fileformat=p2p&archiveformat=gz'
chemin_bt_level_3 = r'http://list.iblocklist.com/?list=bt_level3&fileformat=p2p&archiveformat=gz'

def charger(chemin):

	request = Request(chemin)
	request.add_header('Accept-encoding', 'gzip')
	response = urlopen(request)
	print(response.info())
	print('Content-Encoding', response.info().get('Content-Encoding') )
	info = response.info()
	if True or info.get('Content-Encoding') == 'gzip' or info.get('Content-Type') == 'application/x-gzip':		
		print('if')
		buf = BytesIO( response.read())
		f = gzip.GzipFile(fileobj=buf)
		data = f.read()
		print(data)
	else:
		print('else')
		print(response.read())
	pass;


if __name__ == '__main__':
	charger(chemin_bt_level_3)
