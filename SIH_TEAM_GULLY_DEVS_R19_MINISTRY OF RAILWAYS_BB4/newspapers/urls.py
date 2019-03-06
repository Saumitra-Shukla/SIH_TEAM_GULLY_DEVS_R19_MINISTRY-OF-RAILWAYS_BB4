from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='newspapers'

urlpatterns = [

			path('news/',views.NewsListView.as_view(),name='news_list'),
			path('news/<int:pk>/',views.NewsDetailView.as_view(),name='news_detail'),
			path('newspaper/', views.NewspaperListView.as_view(), name="newspaper_list"),
			path('newspaper/<int:pk>/', views.news_detail_view, name="newspaper_detail"),
			path('news/preriority',views.vader_sentiment,name='vader_sentiment'),
			path('train_delay/', views.train_delay, name="train_delay"),
			path('news/latest',views.latest_news,name='latest'),
			path('train_delay_stat/', views.train_delay_stat, name="train_delay_stat"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
