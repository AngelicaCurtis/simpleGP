from django.urls import path

from aniversarios.views import aniversarios

urlpatterns = [
    path('calendario/', aniversarios, name='calendario'),

]
