import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')

except urllib.error.URLError:
    print('Acesso Inválido')


#except:
    #print('Acesso Inválido')

else:
    print('Acesso Válido')
    # print(site.read()) pega conteudo HTML