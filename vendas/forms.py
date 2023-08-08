from django import forms

import pandas as pd

class VendasForm(forms.Form):
    access_token = forms.CharField()
    ids_situacoes = forms.CharField()
    start_date = forms.CharField(initial = (pd.Timestamp.now() - pd.Timedelta(hours = 7 * 24)))