from django.shortcuts import render
from .models import Post, Category
from django.utils import timezone
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .filters import NewsFilter
from .forms import NewForm


class NewsList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    # user = 'author'
    # queryset = Post.objects.all()
    ordering = ['-dateCreation']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context


def detail(request, pk):
    pk = Post.objects.get(pk=pk)
    return render(request, 'detail.html', context={'title': pk.title, 'text': pk.text, 'datatime': pk.dateCreation})

# дженерик для получения деталей о новости
class NewDetailView(DetailView):
    template_name = 'news/detail.html'
    queryset = Post.objects.all()


class NewCreateView(CreateView):
    template_name = 'news/news_create.html'
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
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новую новость
            form.save()
        return super().get(request, *args, **kwargs)


class Search(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 10

    # def get_filter(self):
    #     return NewsFilter(self.request.GET, queryset=super().get_queryset())
    #
    # def get_queryset(self):
    #     return self.get_filter().qs
    #
    # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
    # (привет, полиморфизм, мы скучали!!!)
    # def get_context_data(self, *args, **kwargs):
    #     return {
    #         **super().get_context_data(*args, **kwargs),
    #         # вписываем наш фильтр в контекст
    #         'filter': self.get_filter()
    #     }
    # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # вписываем наш фильтр в контекст
        context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
        return context

    # def postCategory_detail(request, post_pk):
    #     post = Post.objects.get(pk=post_pk)
    #     category = post.postCategory.all()
    #     return category


# дженерик для редактирования объекта
class NewsUpdateView(UpdateView):
    template_name = 'news/news_update.html'
    form_class = NewForm
    queryset = Post.objects.all()

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте,
    # который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления объекта
class NewsDeleteView(DeleteView):
    template_name = 'news/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


def about(request):
    return render(request, 'news/about.html')