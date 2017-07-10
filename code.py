import feedparser
import smtplib
from email.mime.text import MIMEText

'''
Listado de bases de datos para empezar:
Springer
Busquedas por Autor, Titulo, Usuario
'''

url = 'http://feeds.weblogssl.com/xatakamx'

feed = feedparser.parse(url)
print(feed['items'][0]['title'])
print(feed['items'][0]['datex'])
#print(feed['items'])
