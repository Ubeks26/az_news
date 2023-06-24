from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorators import custom_login_required
from .models import New
import datetime



@custom_login_required
def home(request):
    news = New.objects.all().order_by('-id')
    a_week_ago = datetime.date.today() - datetime.timedelta(days=7)

    context = {
        "news" : news[2:6],
        'last_new': news.first(),
        "bottom_news" : news[1:4],
        'right_news': news[4:9],
        "weekly_top_news": news.filter(created_at__gte=a_week_ago).order_by('-seen_qty')[0:5],
        "wax_news" : news.order_by("seen_qty")
    }
    return render(request, 'index.html', context)



@custom_login_required
def category(request):
    news = New.objects.all()
    two_days_ago = datetime.date.today() - datetime.timedelta(days=2)
    # today = datetime.datetime.today()
    context = {
        "news" : news.filter(created_at__gte=two_days_ago)[:4],
        "first_news" : news[5:9],
        "middle_news" : news.order_by('seen_qty')[:4],
        "today_news" : news[::-1][:4]
    }
    return render(request, 'categori.html', context)



@custom_login_required
def blog(request):
    news = New.objects.all()

    context = {
        "news":news
    }
    return render(request, 'blog.html', context)



@custom_login_required
def about(request):
    news = New.objects.all()

    context = {
        "new":news[5]
    }
    return render(request, 'about.html', context)



@custom_login_required
def contact(request):
    news = New.objects.all()

    context = {
        "news":news[5]
    }
    return render(request, 'contact.html', context)



@custom_login_required
def detail(request):
    news = New.objects.all()

    context = {
        "news":news
    }
    return render(request, 'detail.html', context)



@custom_login_required
def elements(request):
    news = New.objects.all()

    context = {
        "news":news
    }
    return render(request, 'elements.html', context)



@custom_login_required
def latest_news(request):
    news = New.objects.all()

    context = {
        "news":news
    }
    return render(request, 'latest_news.html', context)



@custom_login_required
def single_block(request):
    news = New.objects.all()

    context = {
        "news":news
    }
    return render(request, 'single_blok.html', context)


