"""
Definition of urls for Kursov.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('MZakaz/', views.MZakaz, name='MZakaz'),
    path('zakaz/', views.zakaz, name='zakaz'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('pool/', views.pool, name='pool'),
    path('blog/', views.blog, name='blog'),
    path('pizza/', views.pizza, name='pizza'),
    path('sup/', views.sup, name='sup'),
    path('roll/', views.roll, name='roll'),
    path('parametr/<int:parametr>/', views.blogpost, name='blogpost'),
    path('parametr2/<int:parametr2>/', views.pizzapost, name='pizzapost'),
    path('parametr3/<int:parametr3>/', views.suppost, name='suppost'),
    path('parametr4/<int:parametr4>/', views.rollpost, name='rollpost'),
    path('links/', views.links, name='links'),
    path('newpost/', views.newpost, name='newpost'),
    path('newzakaz/', views.newzakaz, name='newzakaz'),
    path('videopost/', views.videopost, name='videopost'),
    path('registration/', views.registration, name='registration'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
