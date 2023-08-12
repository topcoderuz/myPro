from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView
from news.views import NewsPageView
urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('news/', NewsPageView.as_view(), name='news'),

]
