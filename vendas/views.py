from django.shortcuts import render

from .forms import *

import requests

# Create your views here.
def vendas(request):
    if request.method == 'GET':
        vendas_form = VendasForm()
        context = {'vendas_form': vendas_form}
    # 
    elif request.method == 'POST':
        # 
        button_value = request.POST.get('vendas_button')

        # 
        if button_value == 'chosen_filters':
            # 
            access_token = request.POST.get('access_token')
            ids_situacoes = request.POST.get('ids_situacoes')
            start_date = request.POST.get('start_date')

            # definição dos headers a serem utilizados nas requisições à API
            bling_headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}

            # definição da url comum às requisições da api
            server_url = 'https://www.bling.com.br/Api/v3'
            # 
            url_vendas_bling = f'{server_url}/pedidos/vendas?pagina=1&idsSituacoes[]=6'
            vendas_bling = requests.get(url_vendas_bling, headers = bling_headers)
            vendas_bling = vendas_bling.json()
            vendas_bling = vendas_bling['data']

            # 
            context = {'vendas_bling_dicts_list': vendas_bling}

    
    return render(request, 'vendas.html', context)