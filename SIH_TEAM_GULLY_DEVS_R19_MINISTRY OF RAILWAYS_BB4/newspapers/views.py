from django.shortcuts import render
from .models import Preference,Newspaper_name,News
# Create your views here.
from django.views.generic import View,TemplateView,ListView,DetailView
import csv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


class NewsListView(ListView):
	model = News
	context_object_name = 'news'
	#template_name = 'newspaper/newspaper_detail.html
	def get_queryset(self):
		now = timezone.now()
		upcoming = News.objects.filter(date__gte=now).order_by('date')
		passed = News.objects.filter(date__lte=now).order_by('-date')
		return list(upcoming) + list(passed)

class NewsDetailView(DetailView):
	model = News
	context_object_name = 'news_detail'
	template_name = 'newspapers/news.html'


# class NewsDetailView2(DetailView):
# 	model = News
# 	context_object_name = 'news_detail'
# 	template_name = 'newspapers/newspaper_detail.html'


class NewspaperListView(ListView):
	model = Newspaper_name
	context_object_name = 'newspaper'

# class NewspaperDetailView(DetailView):
# 	model = Newspaper_name

# 	context_object_name = 'newspaper_detail'
# 	template_name = 'newspapers/newspaper_detail.html'
# 	# def get_queryset(self):
# 	# 	news=News.objects.filter(newspaper_name=newspaper_detail.name)
# 	# 	return list(news)
# 	def get_context_data(self,**kwargs):
# 		context=super().get_context_data(**kwargs)
# 		context['news']=' News.objects.filter(newspaper_name=str(Newspaper_name_name))'
# 		return context

def news_detail_view(request, pk):

	newspaper= Newspaper_name.objects.filter(pk=pk)
	print(newspaper)
	# news = newspaper.related_news.all
	news=list(News.objects.filter(newspaper_name_id=int(pk)))
	print(news)
	return render(request, 'newspapers/newspaper_detail.html',{'news': news,'newspaper':newspaper,'names':Newspaper_name.objects.all().order_by('-id')})

def vader_sentiment(request):
	news_new=[]
	index=[]
	senti_comp=[]
	final_index=[]
	read = News.objects.all()
	i=1
	for x in read:
		news_new.append(x.article)
		sentence =x.article
		my_dict=analyser.polarity_scores(sentence)
		senti_comp.append(my_dict['compound'])
		# print(senti_comp)
		index.append(i)
		i+=1
	senti_comp, index = zip(*sorted(zip(senti_comp,index)))
	print(senti_comp)
	print(index)
	j= -0.5000
	k=0
	final_index=[]

	for i in senti_comp:
		if i<=j:
			final_index.append(index[k])
		k+=1
	# print(final_index)
	j= 0.5000
	k=0
	# final_index=[]

	for i in senti_comp:
		if i>j:
			final_index.append(index[k])
		k+=1
	# print(final_index)
	j= -0.5000
	k=0
	# final_index2=[]

	for i in senti_comp:
		if i <0 and i > j:
			final_index.append(index[k])
		k+=1
	# print(final_index2)
	j= 0.5000
	k=0
	# final_index3=[]

	for i in senti_comp:
		if i >0 and i< j:
			final_index.append(index[k])
		k+=1
	# print(final_index3)
	j=0.0
	k=0
	# final_index4=[]

	for i in senti_comp:
		if i == j:
			final_index.append(index[k])
		k+=1
	# print(final_index4)
	print(final_index)
	news_new_final=[]
	for i in final_index:
		news_new_final.append(news_new[i-1])
	return render(request, 'newspapers/preriority.html',{'news': news_new_final})


def train_delay(request):
	from bs4 import BeautifulSoup
	from urllib.request import urlopen

	url = 'https://runningstatus.in'


	source = urlopen(url)
	html_data = BeautifulSoup(source,'html.parser')

	data = str(html_data.find('table', class_='table table-sm m-0'))
	d=data[123:]
	return render(request,'newspapers/train_delay.html',context={'data':d})


def latest_news(request):
	news=News.objects.all()
	return render(request,'newspapers/latest.html',context={'news':news})

def train_delay_stat(request):
	from bs4 import BeautifulSoup
	from urllib.request import urlopen

	url = 'https://runningstatus.in'

	source = urlopen(url)
	html_data = BeautifulSoup(source).find('div',class_='main-content').find('div',class_='row gutters')
	data = html_data.find('div',class_='col-xl-9 col-lg-9 col-md-9 col-sm-9').find_all('div',class_='row gutters')[2]
	da=str(data)[3912:28790]

	return render(request,'newspapers/train_delay_stat.html',context={'data':da})
