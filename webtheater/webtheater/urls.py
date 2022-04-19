from django.contrib import admin
from django.urls import path

from webtheater import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('drama/<str:url>', views.exibir_drama, name='exibir_drama'),
    path('filme/<str:url>', views.exibir_filme, name='exibir_filme'),
    path('musica/<str:url>', views.exibir_musica, name='exibir_musica')
]
