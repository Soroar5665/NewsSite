from django.http import HttpResponse
from django.shortcuts import render
import requests



def index(request):
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=178a7d90e43b4fbe9c4c3b1271c1ca0c"
    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []
    cont = []
    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        cont.append(f['url'])
        img.append(f['urlToImage'])
    mylist = zip(title, desc, img, cont)
    context = {'mylist':mylist}
    return render(request, 'index.html', context)


def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
def aboutus(request):
    return render(request, 'aboutus.html')
