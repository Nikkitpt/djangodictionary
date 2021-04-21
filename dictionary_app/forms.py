from django import forms
from django.conf import settings
import requests


class DictionaryForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        key = "97008166-db2d-43bb-9e1b-703b806aa7f4"
        response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={key}")
        if response.status_code == 200:
            print('connected')
            result = response.json()



        else:
            result = "api unavailable"
        return result


