from django.urls import path
from . import views

#todo: create base html for header

app_name= 'dictionary_app'
urlpatterns = [
    #homepage index
    path('',views.index, name='index',)

]