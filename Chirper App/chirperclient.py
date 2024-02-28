chirperclient.py

import requests
import sys

BASE_URL = 'http://localhost'
PORT = ':5000'
GET_ENDPOINT = BASE_URL + PORT + '/get-chirps'
POST_ENDPOINT = BASE_URL + PORT + '/post-chirp'
LOGIN_ENDPOINT = BASE_URL + PORT + '/login'
SEARCH_ENDPOINT = BASE_URL + PORT + '/search-chirps'

def login():
   u = input('Enter username: ')
   r = requests.post(LOGIN_ENDPOINT, headers={'Username': u})
   if r.ok:
       print(u + ' logged in')
       return r.json()['token']
   else:
       print(r.text)
       sys.exit()

def get_chirps():
   r = requests.get(GET_ENDPOINT)
   if r.ok:
       print('-----chirps-----')
       for chirp in reversed(r.json()):
           print(chirp['userid'] + ' -> ' + chirp['text'])
       print('---------------')
   else:
       print('Error: ' + r.text)

def post_chirp(token):
   t = input('Enter your chirp: ')
   r = requests.post(POST_ENDPOINT, data={'text': t}, headers={'Token':token})
   if r.ok:
       print('Success: ' + r.text)
   else:
       print('Error: ' + r.text)

def search_chirps():
   search_term = input('Enter search term: ')
   r = requests.get(SEARCH_ENDPOINT, params={'q': search_term})
   if r.ok:
       chirps = r.json()
       if len(chirps) > 0:
           print('-----search results-----')
           for chirp in chirps:
               print(chirp['userid'] + ' -> ' + chirp['text'])
           print('------------------------')
       else:
           print('No results found')
   else:
       print('Error: ' + r.text)

print('Welcome to chirper!')
token = login()
while True:
   print('(0) quit')
   print('(1) read chirps')
   print('(2) post chirp')
   print('(3) search chirps')
   i = input('Enter command : ')
   if i == '0':
       break
   elif i == '1':
       get_chirps()
   elif i == '2':
       post_chirp(token)
   elif i == '3':
       search_chirps()
   else:
       print('Illegal command. Please try again.')