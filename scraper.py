import os
from bs4 import BeautifulSoup
# Python 3.x
from urllib.request import urlopen, urlretrieve

URL = 'https://oshpd.ca.gov/data-and-reports/cost-transparency/hospital-chargemasters/latest-chargemasters/'
OUTPUT_DIR = './xlsxFiles'  # path to output folder, '.' or '' uses current folder

u = urlopen(URL)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html, "html.parser")
for link in soup.select('a[href^="https://"]'):
    print(link)

    href = link.get('href')
    if not any(href.endswith(x) for x in ['.csv', '.xls', '.xlsx']) and 'CDM' not in href:
        continue
    hospName = ''
    date = ''
    postLink = link.find_parent("td").find_parent('tr')
    print(postLink)
    if (link.find_parent("td").find_parent('tr')):
        date = '#' + link.find_parent("td").find_parent(
            'tr').select_one('tr > td.column-1').text + '#'
        print(date)
        hospName = '$' + link.find_parent("td").find_parent(
            'tr').select_one('tr > td.column-2').text + '$'
    outPutLink = date + hospName + str(href.rsplit('/', 1)[-1])
    filename = os.path.join(
        OUTPUT_DIR, outPutLink)

    # We need a https:// URL for this site
    href = href.replace('http://', 'https://')

    print("Downloading %s to %s..." % (href, filename))
    urlretrieve(href, filename)
    print("Done.")
