from urllib.request import urlopen, Request
import urllib.error
from bs4 import BeautifulSoup
import re

url=input("Enter the page you want to check. Enter the full URL:")
keyword=input("Enter your SEO keyword that you want to search for:")
keyword=keyword.casefold()

try:
    req = Request(url, headers={'User-Agent':'Mozilla/6.0'})
    html=urlopen(req)
except urllib.error.HTTPError as e:
    print(e)

data=BeautifulSoup(html, "html.parser")

def seo_title_found(keyword,data):
    if data.title:
        if keyword in data.title.text.casefold():
            status="Keyword Found"
        else:
            status="Keyword Not Found"
    else:
        status="No Title found on the page."
    return status


def seo_title_stop_words(data):
    words = 0
    list_words = []
    if data.title:
        with open('stopwords.txt', 'r') as f:
            for line in f:
                if re.search(r'\b' + line.rstrip('\n') + r'\b', data.title.text.casefold()):
                    words+=1
                    list_words.append(line.rstrip('\n'))
        if words>0:
            stop_words="We found {} stop words in your title. The words are {}".format(words,list_words)
        else:
            stop_words=("Great! We did not find any stop words in your title.")
    else:
        stop_words=" Sorry we could not find a title."
    return stop_words


def seo_title_length(data):
    if data.title:
        if len(data.title.text)>60:
            length="The title length is more than the recommended number of charecters. Your title is {} charecters long.".format(len(data.title.text))
        else:
            length="The title is well under the recommended number of charecters. Your title is {} charecters long.".format(len(data.title.text))

    else:
        length="We did not find any title on the page."
    return length

def seo_url_keyword(url):
    if url:
        if keyword in url:
            slug = "Your keyword was found in the url."
        else:
            slug = "The keyword was not found in your url, it is recommended to add for a better optimization."
    else:
        slug = "No url was entered"
    return slug

def seo_url_length(url):
    if url:
        if len(url)>100:
            url_length = "Your URL is {} charecters long which is more than the recommended maximum length.".format(len(url))
        else:
            url_length = "Great! Your URL is under the recommended maximum charecter limit of 100."
    else:
        url_length = "URL Not found."
    return url_length

def seo_h1_keyword(keyword, data):
    total_h1 = 0
    total_h1_keyword = 0
    if data.h1:
        all_tags = data.find_all('h1')
        for tag in all_tags:
            total_h1 += 1
            tag = str(tag.string)
            if keyword in tag.casefold():
                total_h1_keyword += 1
                h1_tag = "Found a keyword in H1 tag. You have a total of {} H1 tags and {} keywords".format(total_h1,total_h1_keyword)
            else:
                h1_tag = "Did not find any keyword in H1 tag. You have a total of {} H1 tags".format(total_h1)
    else:
        h1_tag = "No H1 tags found on the page."
    return h1_tag

def seo_h2_keyword(keyword, data):
    total_h2 = 0
    total_h2_keyword = 0
    if data.h2:
        all_tags = data.find_all('h2')
        for tag in all_tags:
            total_h2 += 1
            tag = str(tag.string)
            if keyword in tag.casefold():
                total_h2_keyword += 1
                h2_tag = "Found a keyword in H2 tag. You have a total of {} H2 tags and {} keywords".format(total_h2,total_h2_keyword)
            else:
                h2_tag = "Did not find any keyword in H2 tag. You should have atleast one H2 tag with the keyword in it. You have a total of {} H1 tags".format(total_h2)
    else:
        h2_tag = "No H2 tags found on the page."
    return h2_tag


print(seo_title_found(keyword,data))
print(seo_title_stop_words(data))
print(seo_title_length(data))
print(seo_url_keyword(url))
print(seo_url_length(url))
print(seo_h1_keyword(keyword,data))
print(seo_h2_keyword(keyword,data))