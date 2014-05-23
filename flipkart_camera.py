import urlparse
import urllib
import BeautifulSoup
from BeautifulSoup import BeautifulSoup

url = "http://www.flipkart.com/panasonic-lumix-dmc-tz25-point-shoot/p/itmdnzjmmqvf65g5?pid=CAMDNZJVNSRUJSGW&srno=b_9&ref=edd7966e-8bd4-430b-8917-cd641aad97e4"
fo = open("cam22.txt", "a+")

htmltext = urllib.urlopen(url).read()
soup = BeautifulSoup(htmltext)
#print len(urls)
table = soup.findAll('table')
for k in range(6,26):
    rows = table[k].findAll('tr')
    h = table[k].findAll('th')
    fo.write('\n')
    fo.write(h[0].string)
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
            text = td.find(text=True) + ';'
            fo.write(text)
        fo.write('\n')
fo.close()
print "End"
