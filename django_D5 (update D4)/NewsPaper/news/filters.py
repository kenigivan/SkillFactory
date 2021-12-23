from django_filters import FilterSet,  DateFromToRangeFilter
from .models import Post


# создаём фильтр
class NewsFilter(FilterSet):
    dateCreation = DateFromToRangeFilter()
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться)
    # информация о товарах
    class Meta:
        model = Post
        # # fields = {
        # #     'author__authorUser__username': ['icontains'],
        # #     'title': ['contains'],
        # #     'postCategory__name': ['icontains'],
        # # }
        fields = ('author', 'postCategory', 'dateCreation')
        # fields = {
        #     'author__authorUser__username' : ['icontains'],
        #     }
