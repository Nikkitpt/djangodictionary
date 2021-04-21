from django.shortcuts import render
from .forms import DictionaryForm

def index(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            print('valid like salad')
            search_result = form.search()
            deff = search_result[0]['shortdef']


    else:
        form = DictionaryForm()
    return render(request, 'dictionary_app/index.html', {'search_result':search_result, 'form':form})