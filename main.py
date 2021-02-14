import os

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



gen_auth = os.getenv("Acc_Tok")
gen_id = os.getenv("Gen_ID")
gen_sec = os.getenv("Gen_Sec")


app = Flask(__name__)
@app.route('/')
def init_main():
    print("Killroy was here")
    header = {
       'Authorization': "Bearer {}".format(auth_tok)
    }
    
    url="https://api.spotify.com/v1/browse/new-releases"
    
    parameters = {'limit': 20}
    
    response = requests.get(url, headers = header, params = parameters)
    
    data = response.json()
    resources = [] 
    #grab an artists id. Will be used to get a random top track and its data.
    for i in range(20):
        resources.append([ data['albums']['items'][i]['artists'][0]['id'],
        data['albums']['items'][i]['artists'][0]['name'],
        data['albums']['items'][i]['available_markets'] ])
    
    artist_id = resources[random.randint(0,len(resources)-1)]
    
    track_url = "https://api.spotify.com/v1/artists/{id}/top-tracks".format(id=artist_id[0])
    
    path_param = {
        'market': 'US'
    }
    
    track_rep = requests.get(track_url,headers= header, params = path_param)
    
    track_data = track_rep.json()
    
    track = track_data['tracks'][random.randint(0,len(track_data['tracks'])-1)]
    
    spot_resources = [track['name'],track['preview_url'],track['album']['images'][0]['url']]
    song = track['name'].split("(feat")
    search_template ={ 'q': song[0] + ", " + artist_id[1] }
    #search_template ={ 'q': artist_id[1] + " " + spot_resources[0] }#set up the genius api
    geni_header = { 'Authorization': "Bearer {}".format(gen_auth)} #header for genius api
    geni_url= "https://api.genius.com/search" #search feature needed.
    
    geni = requests.get(geni_url, headers=geni_header,params=search_template)
    
    geni_data = geni.json()
    
    if len(geni_data['response']['hits']) == 0 or geni_data == None or geni_data['meta'] != 200: #either song doesnt exist yet or theres a cache miss.
        geni_data = None
    else:
       geni_data = geni_data['response']['hits'][0]['result']['url']
    
    return render_template("index.html",resources=resources,
    art_id = artist_id,
    track_res = spot_resources,
    genius_link = geni_data
    ) #will have to pass data in here. Might be a good idea to look at the html and grab the resources on your own. I want to make it nice

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )