from django.contrib import admin
from django.urls import include, path
#from cadastro.views import home  # Certifique-se de importar a view corretamente

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('cadastro/', include('cadastro.urls')),
    #path('', home, name='home'),  # Adiciona esta linha
]
