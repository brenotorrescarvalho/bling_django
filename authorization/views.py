from django.shortcuts import render, redirect

from django.http import HttpRequest, HttpResponse

from .forms import *

import base64
import requests

# Create your views here.

def authorization(request: HttpRequest) -> HttpResponse:
    
    # ao requisitar o get, retorna o primeiro formulário para coleta do client_id
    if request.method == 'GET':
        get_authorization_form = GetAuthorizationForm()
    
        # definição do dicionário context
        context = {'get_authorization_form': get_authorization_form}


    
    # 
    if request.method == 'POST':
        # 
        button_value = request.POST.get('authorization_button')
        # se for o post que retorna o authorization_code
        if button_value == "get_authorization_form":

            # coleta do client_id
            client_id = request.POST.get('client_id')

            # 
            authorization_base_url = "https://www.bling.com.br/Api/v3/oauth/authorize"
            redirect_uri = "https://oauth.pstmn.io/v1/browser-callback"
            state = 'e2036c1019652e66a05adc8efc130e62'
            scope = '98309+98310+98313+507943+575904+106168710+182224097+199272829+220621674+318257556+318257568+318257570+318257583+363921589+363921590+363921591+363921592+791588404'
            # 
            authorization_final_url = f'{authorization_base_url}?response_type=code&client_id={client_id}&state={state}'

            print(authorization_final_url)

            # 
            get_token_form = GetTokenForm()

            # 
            context = {'client_id': client_id, 'authorization_final_url': authorization_final_url, 'get_token_form': get_token_form}

        elif button_value == 'get_token_form':

            token_url = "https://www.bling.com.br/Api/v3/oauth/token"

            # 
            client_id = request.POST.get('client_id')
            authorization_code = request.POST.get('authorization_code')
            client_secret = request.POST.get('client_secret')

            # 
            credenciais_do_client_app = f'{client_id}:{client_secret}'
            credenciais_do_client_app_bytes = credenciais_do_client_app.encode('utf-8')
            credenciais_do_client_app_bytes_base64 = base64.b64encode(credenciais_do_client_app_bytes)
            base64_das_credenciais_do_client_app = credenciais_do_client_app_bytes_base64.decode('utf-8')


            token = requests.post(f'{token_url}', headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': '1.0', 'Authorization': f'Basic {base64_das_credenciais_do_client_app}'}, data = {'grant_type': 'authorization_code', 'code': authorization_code})

            token_response = token.json()
            # acess_token de fato
            access_token = token_response['access_token']

            # 
            context = {'show_token': access_token}
            

            
            
            
    # retorno da view de autorização / autenticação do bling
    return render(request, 'authorization.html', context)

