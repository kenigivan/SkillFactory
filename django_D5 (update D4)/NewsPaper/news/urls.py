from django.urls import path
from .views import NewsList, Search, about, NewDetailView, NewCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    # path('news/', news, name='news'),
    path('about/', about, name='about'),  # Ссылка о нас (о новостном портале)
    # path('news/<int:pk>/', detail, name='detail'),
    path('<int:pk>/', NewDetailView.as_view(), name='detail'),  # Ссылка на детали новости
    path('', NewsList.as_view(), name='news'),  # Главная страница - список новостей
    path('search/', Search.as_view(), name='search' ),  # Ссылка на поиск новости
    path('create/', NewCreateView.as_view(), name='create'),  # Ссылка на добавление новости
    path('update/<int:pk>', NewsUpdateView.as_view(), name='update'),  # Ссылка на редактирование новости
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='delete'),  # Ссылка на редактирование новости
]
