# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, ChartPageView


#urlpatterns = [
#	path('chartjs/', ChartView.as_view(), name='chart'),
#]

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
	
	path('chart/', ChartPageView.as_view(), name='chart'),

	path('', HomePageView.as_view(), name='home'),
]