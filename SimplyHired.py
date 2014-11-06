#!/usr/bin/env python2.7

import urllib2
from cookielib import CookieJar
from bs4 import BeautifulSoup as bs


class SearchSimplyHired():
  
  def __init__(self, keyword):
    self.cave_man_drawings = "qa=%s&qe=&qo=&qw=&t=&c=&lc=&ls=&lz=&mi=25&ws=100\
    &sb=&fdb=&fjt=&fex=&fed=&frl=&fsr=&fem=&fcz=&fcr=&name=&email=&clst=comboxp0" % keyword
    self.request_url = "http://www.simplyhired.com/a/jobs/search"
    referrer = "http://www.simplyhired.com/a/jobs/advanced-search"
    __cj = CookieJar()
    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(__cj))
    self.opener.addheaders = [("User-agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36")]
    self.opener.addheaders.append(("Referrer", referrer))
    
  def simplyResults(self):
    resp = self.opener.open(self.request_url, self.cave_man_drawings)
    soup = bs(resp.read())
    for span in soup.find_all("span"):
      try:
        if span['class'][0] == u"search_title":
	  self.count = span.string.split(" of ")[1]
	  self.count = self.count.replace(",", "")
	  self.count = float(self.count)/100
	  self.count = round(self.count)
	  print self.count
      except KeyError:
	continue
    f = open('test.html', 'wb')
    f.write(str(soup))
    
foo = SearchSimplyHired("NSA")
foo.simplyResults()
#print foo.opener.addheaders