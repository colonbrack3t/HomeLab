from django.shortcuts import render , redirect
from django.http import HttpResponse
import requests, json
from urllib.parse import urlencode
# Create your views here.
def get_access_token(request):
    print (request.GET.get('code'))
    
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Content-Type':'application/x-www-form-urlencoded',
    'Authorization' : 'Basic NjhlNzM5ZmY0MWNlNDRmMGI3MzBhNjhiNDlhZDUwYTU6N2JjZWZlNjBhMjVjNDM1ZWFiMmQ0Yjk2OWNmMzhhNzg=',}
    body = {'redirect_uri':'http://192.168.0.14:8000/spotify/access_token',
            'code' : request.GET.get('code'),
            'grant_type':"authorization_code"
    }
    x = requests.post(url, data = body, headers= headers)
    
    open('tokens','w').write(str(x.json()))
    return HttpResponse(x.text)
    
def change_device(request):
    refresh_token(request)
    access_token = json.loads(open('tokens','r').read().replace("'",'"'))['access_token']
    print(access_token)
    url = 'https://api.spotify.com/v1/me/player'
    headers = {'Content-Type': 'application/json', 
    'Authorization' : 'Bearer ' + access_token,'Accept': 'application/json'}
    body = {'device_ids': ["44770f601f1dd300a363792672f5d6679077c1f0"]}
    x = requests.put(url, json = body, headers= headers)

    return HttpResponse(x.text)

def login(request):
    url = 'https://accounts.spotify.com/authorize?'
    query = {'response_type' : 'code',
             'client_id':'68e739ff41ce44f0b730a68b49ad50a5',
             'redirect_uri':'http://192.168.0.14:8000/spotify/access_token',
             'scope':'user-modify-playback-state'
            }
    
    return redirect(url + urlencode(query))
def refresh_token(request):
    tokens = json.loads(open('tokens','r').read().replace("'",'"'))
    refresh_token = tokens['refresh_token']

    url = 'https://accounts.spotify.com/api/token'
    headers = {
               'Content-Type': 'application/x-www-form-urlencoded', 
               'Authorization' : 'Basic NjhlNzM5ZmY0MWNlNDRmMGI3MzBhNjhiNDlhZDUwYTU6N2JjZWZlNjBhMjVjNDM1ZWFiMmQ0Yjk2OWNmMzhhNzg=',
              'Accept': 'application/json'}
    body = {  'grant_type': 'refresh_token', 'refresh_token': refresh_token}
    x = requests.post(url, data = body, headers= headers)
    tokens['access_token'] = x.json()['access_token']
    open('tokens','w').write(str(tokens))
    return HttpResponse(tokens)
