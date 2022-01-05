# import webbrowser
# try:
#     webbrowser.open('http://pudim.com.br/')
# except:
#     print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
# else:
#     print('\033[1;33mConsegui acessar o Site Pudim\033[m')

# Guanabara
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[1;33mConsegui acessar o Site Pudim\033[m')
    print(site.read()) #impressão do HTML
