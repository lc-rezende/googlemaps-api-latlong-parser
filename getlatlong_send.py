# coding: utf-8
import urllib2
import json

GOOGLE_KEY = ''
ADDRESS = 'Avenida das Américas 3443 Barra da Tijuca, Rio de Janeiro, RJ'
ADDRESS = ADDRESS.replace(' ', '+')
URL = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (ADDRESS, GOOGLE_KEY)

googleresponse = urllib2.urlopen(URL)
jsonresponse = json.loads(googleresponse.read())

print jsonresponse['results'][0]['geometry']['location']
