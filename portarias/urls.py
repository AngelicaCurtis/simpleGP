from django.urls import path

from portarias.views import PortariaCreate, portarias_list

urlpatterns = [

    path('portaria_form/', PortariaCreate.as_view(), name="portaria-form"),
    path('lista-portarias/', portarias_list, name="lista-portarias"),

]
