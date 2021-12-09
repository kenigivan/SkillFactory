from django.urls import path
from .views import news, detail, about

urlpatterns = [
    path('news/', news, name='news'),
    path('about/', about, name='about'),
    path('news/<int:pk>', detail, name='detail')
]