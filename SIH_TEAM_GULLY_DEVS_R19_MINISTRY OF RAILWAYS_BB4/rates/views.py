from django.shortcuts import render
from .models import *
from newspapers.models import Newspaper_name
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse ,HttpResponseRedirect

# Create your views here.

# class ViewListView(ListView):
# 	model = News_rates
# 	context_object_name = 'news_rates'

# class ViewDetailView(DetailView):
# 	model = News_rates
# 	context_object_name = 'news_rates_detail'
# 	template_name = 'newspapers/news_rates_detail.html'

def news_rates(request):
	if request.method == 'POST':
		quote = request.POST.get('name')
		if not(quote):
			p=News_rates.objects.all()
			page = request.GET.get('page', 1)
			paginator = Paginator(p, 1)
			try:
				rrates = paginator.page(page)
			except PageNotAnInteger:
				rrates = paginator.page(1)
			except EmptyPage:
				rrates = paginator.page(paginator.num_pages)
			context ={
			'newspapers':Newspaper_name.objects.all(),
			'news_rates':rrates
			}
		else:
			# quote=Newspaper_name.objects.filter(name=quote1)
			p=list(News_rates.objects.filter(newspaper_name_id=int(quote[-1])))
			#print(p.rate_text)
			page = request.GET.get('page', 1)
			paginator = Paginator(p, 1)
			try:
				rrates = paginator.page(page)
			except PageNotAnInteger:
				rrates = paginator.page(1)
			except EmptyPage:
				rrates = paginator.page(paginator.num_pages)
			context ={
			'newspapers':Newspaper_name.objects.all(),
			'news_rates':rrates
			}
	else:
		p=News_rates.objects.all()
		#print(p.rate_text)
		page = request.GET.get('page', 1)
		paginator = Paginator(p, 1)
		try:
			rrates = paginator.page(page)
		except PageNotAnInteger:
			rrates = paginator.page(1)
		except EmptyPage:
			rrates = paginator.page(paginator.num_pages)
		context ={
		'newspapers':Newspaper_name.objects.all(),
		'news_rates':rrates
		}

	# context={
	# 'newspapers':Newspaper_name.objects.all()
	# }

	return render(request, 'rates/news_rate_detail.html', context=context )

def news_ratess(request,pk):
	context ={
		'newspapers':Newspaper_name.objects.all(),
		'news_rates':list(News_rates.objects.filter(newspaper_name_id=int(pk)))
	}
	return render(request, 'rates/news_rate_detail.html', context=context )


def paper_rates(request,pk):

	name=str(City.objects.get(pk=pk).city_text)
	print(name)

	from bs4 import BeautifulSoup
	from urllib.request import urlopen

	url ='https://www.bhavesads.com/'+name+'-newspaper/display-ad-rates'

	source = urlopen(url)
	html_data = BeautifulSoup(source).find('div',class_='tab-content').find('div',{'id': 'Categorys'}).find_all('div', class_='col-sm-12')
	paper=[]
	for data in html_data:
		try:
			paper1 = data.find('p',class_='special-text').text[:-10]
			paper.append(paper1)
		except AttributeError:
			pass

	names=[]
	for p in paper:
		names.append(Newspaper_name.objects.get(name=p))

	return render(request, 'rates/paper-list.html',{'city':names})


def city_rates(request):
	return render(request, 'rates/city-list.html',{'city':City.objects.all()})

def calc(request):

	return render(request, 'rates/calculater.html', {})
