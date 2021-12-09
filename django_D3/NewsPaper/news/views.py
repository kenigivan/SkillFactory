from django.shortcuts import render
from .models import Post
from django.utils import timezone


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def about(request):
    return render(request, 'about.html')


def news(request):
    posts = Post.objects.filter(dateCreation__lte=timezone.now()).order_by('-dateCreation')
    # posts = Post.objects.all()
    return render(request, 'news.html', context={'posts': posts})


def detail(request, pk):
    pk = Post.objects.get(pk=pk)
    # text = pk.text
    return render(request, 'detail_post.html', context={'title': pk.title, 'text': pk.text, 'datatime': pk.dateCreation})


def filter_message(message: str):
    variants = ['mat',  'мат', 'премат' 'блбл']  # непристойные выражения
    ln = len(variants)
    filtred_message = ''
    string = ''
    pattern = '*'  # чем заменять непристойные выражения
    for i in message:
        string += i
        string2 = string.lower()
        flag = 0
        for j in variants:
            if not string2 in j:
                flag += 1
            if string2 == j:
                filtred_message += pattern * len(string)
                flag -= 1
                string = ''
        if flag == ln:
            filtred_message += string
            string = ''
    if string2 != '' and string2 not in variants:
        filtred_message += string
    elif string2 != '':
        filtred_message += pattern * len(string)
    return filtred_message

