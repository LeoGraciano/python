import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("Site Pudim não esta acessível no momento.")
else:
    print("Consegui Acessar o Site Pudim com sucesso")
