from django.urls import path
from chat import views
from metricas import views as metricas_views


urlpatterns = [

    path('', metricas_views.cad_vendedor, name='cadastrar_vendedor'),
    path('chat/', views.chat, name="chat"),
    path('api/chat/', views.chat_api, name="chat_api"),
    

]