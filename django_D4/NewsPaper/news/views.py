from django.shortcuts import render
from .models import Post, Category
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .filters import NewsFilter
from .forms import NewForm


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    # queryset = Post.objects.all()
    # ordering = ['dateCreation']
    paginate_by = 3




def about(request):
    return render(request, 'about.html')


# def detail(request, pk):
#     pk = Post.objects.get(pk=pk)
#     return render(request, 'detail.html', context={'title': pk.title, 'text': pk.text, 'datatime': pk.dateCreation})

# дженерик для получения деталей о товаре
class NewDetailView(DetailView):
    template_name = 'detail.html'
    queryset = Post.objects.all()


class NewCreateView(CreateView):

    template_name = 'new_create.html'
    form_class = NewForm
    queryset = Post.objects.all()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        context['postCategory'] = Category.objects.all()
        context['form'] = NewForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()
        return super().get(request, *args, **kwargs)




class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_filter(self):
        return NewsFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
    # (привет, полиморфизм, мы скучали!!!)
    def get_context_data(self, *args, **kwargs):
        return {
            **super().get_context_data(*args, **kwargs),
            # вписываем наш фильтр в контекст
            'filter': self.get_filter()
        }
