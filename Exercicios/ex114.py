import urllib
from urllib import request
try:
    urllib.request.urlopen("http://pudim.com.br/")
except:
    print('\033[1;31mNão consegui acessar o site D:')
else:
    print('\033[1;32mConsegui acessar o site :D')
