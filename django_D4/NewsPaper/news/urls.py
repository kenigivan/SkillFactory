from django.urls import path
from .views import NewsList, Search, about, NewDetailView, NewCreateView

urlpatterns = [
    # path('news/', news, name='news'),
    path('about/', about, name='about'),  # Ссылка о нас (о новостном портале)
    # path('news/<int:pk>/', detail, name='detail'),
    path('news/<int:pk>/', NewDetailView.as_view(), name='detail'),  # Ссылка на детали новости
    path('news/', NewsList.as_view(), name='news'),  # Главная страница - список новостей
    path('news/search/', Search.as_view(), name='search' ),  # Ссылка на поиск новости
    path('news/create/', NewCreateView.as_view(), name='create'),  # Ссылка на добавление новости
]
