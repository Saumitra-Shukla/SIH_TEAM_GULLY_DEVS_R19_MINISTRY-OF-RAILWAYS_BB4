from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import time
import csv
import re


def full_news(url):

	source = urlopen(url)
	bsob = BeautifulSoup(source, 'lxml')
	data=[]
	html= bsob.find('div', class_="wrapper clearfix article-content-wrapper")
	data.append(html.find('div', class_='main-content').find('div',class_='Normal').text)
	try:
		d = html.find('div',class_='main-content').find('section',class_='highlight clearfix').find('img').attrs['src']
		data.append(d)
	except (AttributeError, TypeError):
		data.append('NULL')
	return data

def scrape(url, driver):


	source = urlopen(url)

	bsob = BeautifulSoup(source, 'lxml')

	data = bsob.find_all('li',{'class': 'article','itemprop': 'itemListElement', 'itemscope': 'itemscope'})


	with open('/home/abhishek/Desktop/sir_dekhiye/scraped_data/toi_data.csv','a') as file:

		# csv_reader = csv.reader(file)
		csv_writer = csv.writer(file)
		# csv_writer.writerow(['head','time','para','img'])
		prev = datetime.datetime.today() - datetime.timedelta(days=1)
		prev = time.strptime(str(prev)[0:10], '%Y-%m-%d')
		j=1

		for s in data:

			content = s.find('div', class_='content')
			head =  content.find('span', class_='title').text

			# head = s.find('a', class_='story-card75x1-text').text
			site = content.find('a', {'target':'_blank'})["href"]
			tim = content.find('span', class_='meta').text
			date = time.strptime(tim[0:10], '%Y-%m-%d')
			if date < prev:
				break
			para = full_news("https://timesofindia.indiatimes.com/"+site)
			print(para[1])
			j+=1

			csv_writer.writerow([head,tim,para[0],para[1]])#Reminder:::extract image link
			# print(1)

def my_scheduled_job():
    options = Options()
    options.headless = True

    print('starting driver')

    driver = webdriver.Firefox(options=options, executable_path=r'/home/abhishek/Desktop/geckodriver')

    print('opening site')

    driver.get("https://timesofindia.indiatimes.com/")

    print('searching keyword')

    time.sleep(10)

    driver.find_element_by_xpath("//div[@class='bottom-area']//div[@class='search-form']//div[@class='wrapper']//span[@class='sports-sprite search-btn jSearchLens']").click()

    driver.find_element_by_xpath("//input[@id='query'][@class='textbox jAutoSuggestorInput']").send_keys("railway"+Keys.ENTER)

    time.sleep(15)

    driver.find_element_by_xpath("//div[@id='search-band'][@class='news_tab clearfix']//a[@id='news']").click()

    time.sleep(5)

    # driver.find_element_by_xpath("//div[@class='inner']//span[@id='current-filter']").click()

    # time.sleep(10)

    # driver.find_element_by_xpath("//div[@class='inner']//ul[@style='display: block;']//li[@id='24hrs']").click()

    with open('/home/abhishek/Desktop/sir_dekhiye/scraped_data/toi_data.csv','w') as file:
    	csv_writer = csv.writer(file)
    	csv_writer.writerow(['head','time','para','img'])

    url = driver.current_url

    print('starting scraping')

    scrape(url, driver)

    print('scraping finished')

    driver.close()


def full_news_hindu(url):

	source = urlopen(url)
	bsob = BeautifulSoup(source, 'lxml')
	data=[]
	data.append( bsob.find('div', {'id' : re.compile(r"^(content-body-)\d{8}-\d{8}")}))
	try:
		d = bsob.find('img', class_='lead-img adaptive placeholder')
		data.append(d['src'])
	except (AttributeError, TypeError) :
		data.append('NULL')

	return data


def scrape_hindu(url, driver):

	source = urlopen(url)
	bsob = BeautifulSoup(source, 'lxml')

	# head = bsob.find_all('a' , class_='story-card75x1-text')
	# for s in head:
	# 	print(s.text)

	data = bsob.find_all('div', class_='story-card-news')

	with open('/home/abhishek/Desktop/sir_dekhiye/scraped_data/hindu_data.csv','a') as file:

		# csv_reader = csv.reader(file)
		csv_writer = csv.writer(file)
		# csv_writer.writerow(['head','time','para','img'])
		j=0

		for s in data:

			head = s.find('a', class_='story-card75x1-text').text

			# head = s.find('a', class_='story-card75x1-text').text
			site = s.find('a', class_='story-card75x1-text')["href"]
			tim = s.find('span', class_='dateline').text
			para = full_news_hindu(site)
			j+=1
			print(j)
			csv_writer.writerow([head,tim,para[0],para[1]])#Reminder:::extract image link


	print('next page')

	try:
		driver.find_element_by_xpath("//li[@class='next page-item']//a[@class='page-link']").click()
		time.sleep(8)
		url = driver.current_url
		scrape_hindu(url,driver)

	except NoSuchElementException:
		pass

def my_scheduled_job_hindu():
    options = Options()
    options.headless = True

    print('starting driver')

    driver = webdriver.Firefox(options=options, executable_path=r'/home/abhishek/Desktop/geckodriver')
    driver.get("https://www.thehindu.com")

    print('entering search element')

    driver.find_element_by_name('q').send_keys("railway"+Keys.ENTER)

    time.sleep(5)

    print('appplying filter')

    driver.find_element_by_xpath("//a[@class='searchFilter '][@data-value='yesterday']").click()

    driver.find_element_by_xpath("//a[@class='searchFilter '][@data-value='text']").click()

    url = driver.current_url

    with open('/home/abhishek/Desktop/sir_dekhiye/scraped_data/hindu_data.csv','w') as file:
    	csv_writer = csv.writer(file)
    	csv_writer.writerow(['head','time','para','img'])

    print('scraping started')

    scrape_hindu(url, driver)

    print('scraping finished')
    driver.close()


def full_news_express(url):

	source = urlopen(url)
	bsob = BeautifulSoup(source, 'lxml')
	data=[]
	html= bsob.find_all(class_="o-story-content")#.next_sibling().find('div', class_="o-story-content")
	data.append(html[1].find_all('p'))
	try:
		data.append( html[1].find('figure',class_='wp-caption alignnone').find('img').attrs['src'])
	except AttributeError as e:
		data.append('NULL')
	return data
	# print(data[0])


def scrape_express(url, driver):

	source = urlopen(url)
	bsob = BeautifulSoup(source, 'lxml')
	# html = bsob.find('div', class_= "l-grid l-grid--y50")
	data = bsob.find_all('div', class_="l-grid__item l-grid__item--divided")

	prev = datetime.datetime.today() - datetime.timedelta(days=1)
	prev = time.strptime(str(prev)[0:10], '%Y-%m-%d')

	# for s in data:
	# 	print(s.find('a', class_='m-block-link__anchor').text)
	# 	print('\n')


	with open('/home/abhishek/Desktop/sir_dekhiye/scraped_data/express_data.csv','a') as file:

		csv_writer = csv.writer(file)
		j=0
		for s in data:

			head =  s.find('a', class_='m-block-link__anchor').text
			site = s.find('a', class_='m-block-link__anchor')["href"]
			tim = s.find('time', class_='m-article-landing__date')['datetime']
			date = time.strptime(tim[0:10], '%Y-%m-%d')
			if date < prev:
				break
			para = full_news_express(site)
			j+=1
			print(j)

			csv_writer.writerow([head,tim,para[0],para[1]])#Reminder:::extract image link
			# print(1)

def my_scheduled_job_express():
    options = Options()
    options.headless = True

    print('starting driver')

    driver = webdriver.Firefox(options=options, executable_path=r'/home/abhishek/Desktop/geckodriver')
    driver.get("https://indianexpress.com/")

    print('opening site')

    time.sleep(15)

    print('searching keyword')

    driver.find_element_by_xpath("//span[@class='s-search__off']").click()

    driver.find_element_by_xpath("//input[@class='m-search-field__input']").send_keys("railway"+Keys.ENTER)

    # time.sleep(15)

    # driver.find_element_by_xpath("//div[@class='inner']//span[@id='current-filter']").click()

    # time.sleep(5)

    # driver.find_element_by_xpath("//div[@class='inner']//ul[@style='display: block;']//li[@id='24hrs']").click()

    time.sleep(10)

    print('starting scraper')

    with open('/home/abhishek/Desktop/sir_dekhiye/scraped_data/express_data.csv','w') as file:
    	csv_writer = csv.writer(file)
    	csv_writer.writerow(['head','time','para','img'])

    url = driver.current_url

    scrape_express(url, driver)

    print('scraping finished')

    driver.close()
