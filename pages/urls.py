from django.urls import path
from .views import HomePageView, AboutPageView, ServicesPageView, ContactPageView, BlogPageView, PortfolioPageView

urlpatterns = [
    path('portfolio/', PortfolioPageView.as_view(), name='portfolio'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]