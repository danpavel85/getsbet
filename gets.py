import requests
from lxml.html import fromstring

# r = requests.get('https://www.getsbet.ro/eveniment/2414/')
r = requests.get('https://www.getsbet.ro/oferta/sport-fotbal')
root = fromstring(r.text)

urls = root.xpath("//table[@class='games']//td[3]//a[@href][1]/@href")
# print(urls)
for url in urls:
  r = requests.get(url)
  root = fromstring(r.text)

  game = root.xpath("//div[@id='tab-toate-pariurile']//div[normalize-space(text())='Final']//ancestor::div[@class='box']//tbody//td[3]/text()")[0].strip()
  f1 = root.xpath("//div[@id='tab-toate-pariurile']//div[normalize-space(text())='Final']//ancestor::div[@class='box']//tbody//td[4]/text()")[0].strip()
  fx = root.xpath("//div[@id='tab-toate-pariurile']//div[normalize-space(text())='Final']//ancestor::div[@class='box']//tbody//td[5]/text()")[0].strip()
  f2 = root.xpath("//div[@id='tab-toate-pariurile']//div[normalize-space(text())='Final']//ancestor::div[@class='box']//tbody//td[6]/text()")[0].strip()
  under = root.xpath("//div[@id='tab-toate-pariurile']//div[normalize-space(text())='Total Goluri']//ancestor::div[@class='box']//td[normalize-space(text())='S2.5']//ancestor::div[@id='derivatesContent']//tbody//td[5]/text()")[0].strip()
  over = root.xpath("//div[@id='tab-toate-pariurile']//div[normalize-space(text())='Total Goluri']//ancestor::div[@class='box']//td[normalize-space(text())='P2.5']//ancestor::div[@id='derivatesContent']//tbody//td[4]/text()")[0].strip()
  final = game + ' ' + f1 + ' ' + fx + ' ' + f2 + ' ' + under + ' ' + over
  print(final)