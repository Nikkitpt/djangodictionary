from django.shortcuts import render
import requests

def diction(request):
    data = {}
    if word in request.GET:
        word = request.GET['word']
        key = "97008166-db2d-43bb-9e1b-703b806aa7f4"
        url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={key}"

        response = requests.get(url)
        data = response.json

        words = data[0]['meta']['id']
        shortdef = data[0]['shortdef']

    return render(request, 'dictionary_app/index.html', {

        # TODO: remove list brackets form shortdef, show all short def
        'shortdef': data[0]['shortdef'[0:]],
        'words': data[0]['meta']['id']
        })


####### first  original working view


from django.shortcuts import render
import requests


# Create your views here.

def index(request):
    """Homepage"""
    word = "bewildered"
    key = "97008166-db2d-43bb-9e1b-703b806aa7f4"

    response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={key}")
    data = response.json()


    return render(request, 'dictionary_app/index.html',{

        # TODO: remove list brackets form shortdef, show all short def
        'shortdef' : data[0]['shortdef'[0:]],
        'words' : data[0]['meta']['id']

        })


###anotherone

def index(request):
    """Homepage"""
    data= {}
    if 'wordsearch' in request.GET:

        wordsearch = request.GET['wordsearch']
        key = "97008166-db2d-43bb-9e1b-703b806aa7f4"

        response = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{wordsearch}?key={key}")
        data = response.json()


    return render(request, 'dictionary_app/index.html',{'data': data})
