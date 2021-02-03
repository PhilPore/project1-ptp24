import os 
import flask

from flask import Flask, render_template
from dotenv import load_dotenv, find_dotenv
import requests
import random


#load_dotenv(find_dotenv())
load_dotenv(find_dotenv())
auth_url = 'https://accounts.spotify.com/api/token'
clientid = os.getenv("CLI_ID")
client_secret = os.getenv("CLI_SEC")
Auth_Req = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': clientid,
    'client_secret': client_secret,
})
auth_tok = Auth_Req.json()['access_token']
#print(auth_tok)

header = {
   'Authorization': "Bearer {}".format(auth_tok)
}

url="https://api.spotify.com/v1/browse/new-releases"




app = Flask(__name__)
@app.route('/')
def init_main():
    print("Killroy was here")
    header = {
       'Authorization': "Bearer {}".format(auth_tok)
    }
    
    url="https://api.spotify.com/v1/browse/new-releases"
    
    parameters = {'limit': 10}
    
    response = requests.get(url, headers = header, params = parameters)
    
    data = response.json()
    resources = []
    for i in range(10):
        resources.append(data['albums']['items'][i]['artists'][0]['id'])
    artist_id = resources[random.randint(0,len(resources)-1)]
    return render_template("index.html",resources=resources,art_id = artist_id) #will have to pass data in here.

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )