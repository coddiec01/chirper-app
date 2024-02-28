import json
import time
import secrets
import flask
import basicdb

DATABASE = 'chirper.json'

app = flask.Flask(__name__)
basicdb.load_db(DATABASE)

logins = {}

for row in basicdb.db_from('logins'):
   logins[row['userid']] = row['password']

sessions = {..>@app.route('/login', methods=['POST'])
def login():
   username = flask.request.headers['Username']
   token = secrets.token_hex()
   sessions[token] = username
   return json.dumps({'token': t..>@app.route('/get-chirps')
def get_chirps():
   chirps = basicdb.orderby(basicdb.db_from('chirps'), 'time')[-5:]
   return j..>@app.route('/post-chirp', methods=['POST'])
def post_chirp():
   token = flask.request.headers['Token']
   if token not in sessions:
       return 'Invalid token', 401
   chirp = {'userid': sessions[token], 'time': str(time.time()), 'text': flask.request.form['text']}
   if len(chirp['text']) > 100:
       return 'chirp too long', 403
   basicdb.insert('chirps', chirp)
   return 'chirp p..>@app.route('/search-chirps')
def search_chirps():
   query = flask.request.args.get('query')
   if query:
       chirps = basicdb.orderby(basicdb.db_from('chirps'), 'time')
       result = []
       for chirp in chirps:
           if query.lower() in chirp['text'].lower():
               result.append(chirp)
               if len(result) == 5:
                   break
       return json.dumps(result)
   else:
       return 'No search query specified', 400

app.run(host='0.0.0.0')
