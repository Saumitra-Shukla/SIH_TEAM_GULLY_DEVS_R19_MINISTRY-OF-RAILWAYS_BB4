from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name='rates'

urlpatterns = [
	        path('news_ratess/<int:pk>/', views.news_ratess, name="news_ratess"),
	        path('news_rates/', views.news_rates, name="news_rates"),
	        path('city_rates/', views.city_rates, name="city_rates"),
	        path('paper_rates/<int:pk>/', views.paper_rates, name="paper_rates"),
	        path('calc/', views.calc, name="calc"),
            
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
