__author__ = 'taylor'
# module to get info from site and parse into text

import requests
from bs4 import BeautifulSoup
from collections import Counter
import sys
from string import punctuation
import re
from urllib.request import urlopen
import urllib

words = []
if len(sys.argv) != 3:
    print("ERROR: Wrong number of arguments")
    sys.exit(1)
else:
    with open(sys.argv[2], 'r') as f:
        contents = f.readlines()
        for i in range(len(contents)):
            words.extend(contents[i].split())
        url = sys.argv[1]

def get_articles(url):
    source_code = requests.get(url)
    #plain_text = source_code.text
    soup = BeautifulSoup(source_code.content, "html.parser")
    text = (soup.findAll(text=True))
    c = Counter([x.lower() for y in text for x in y.split()])
    for w in words:
        del c[w]
    l = []
    p = ['=', '.', "/", ":", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    l = list(c.elements())
    for word in l:
        for letter in word:
            if letter in p:
                del c[word]

    l3 = [x for x in c.most_common() if x not in words]
    i = 1
    for x in range(10):
        print(i, l3[x])
        i+=1
get_articles(url)
input("")
