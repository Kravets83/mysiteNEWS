from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('',  HomeNews.as_view(), name='home'),
    # path('', cache_page(60)(HomeNews.as_view()), name='home'),cache on 60 sec
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
    path('/login/', user_login, name='login'),
    path('/logout/', user_logout, name='logout'),
    path('/register/', register, name='register'),
    path('/contact/', contact, name='contact'),

]
