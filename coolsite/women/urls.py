from django.urls import path, re_path
from django.urls import include
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path("", WomenHome.as_view(), name="home"),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(),name='register')

]

