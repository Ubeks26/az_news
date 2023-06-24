from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/', category, name='category'),
    path('blog/', blog, name='blog'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('detail/', detail, name='detail'),
    path('elements/', elements, name='elements'),
    path('latest_news/', latest_news, name='latest_news'),
    path('single_block/', single_block, name='single_block'),
]
