"""simpleGP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from django.urls import path, include
from django.views.generic import TemplateView

from home import urls as home_urls
from user import urls as user_urls
from progressoes import urls as progressoes_urls
from portarias import urls as portarias_urls
from estagioProbatorio import urls as estagios_urls
from servidores import urls as servidores_urls
from aniversarios import urls as aniversarios_urls
from servidores.views import home

urlpatterns = [

                  path('accounts/', include('django.contrib.auth.urls')),
                  path('admin/', admin.site.urls),
                  path('login/', auth_views.LoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='sair'),
                  path('home/', home),
                  path('estagios/', include(estagios_urls)),
                  path('', include(home_urls)),
                  path('user', include(user_urls)),
                  path('aniversarios/', include(aniversarios_urls)),
                  path('progressoes/', include(progressoes_urls)),
                  path('portarias/', include(portarias_urls)),
                  path('servidores/', include(servidores_urls)),
                  path('index/', TemplateView.as_view(template_name='index.html')),  # usando TemplateView
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # usado somente em desenvolvimento
