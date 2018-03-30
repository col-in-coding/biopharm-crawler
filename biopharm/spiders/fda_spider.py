import scrapy
from biopharm.items import BiopharmItem

class FdaSpider(scrapy.Spider):
	name = "fda"

	def start_requests(self):
		urls = [
			'https://www.biopharmcatalyst.com/calendars/fda-calendar'
		]
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		items = response.xpath('//table[@class="list-table"]/tbody/tr')
		
		for item in items:
			ticker = item.css("td.js-td--drug strong.drug::text").extract_first()
			price = item.css("td.js-td--price div.price::text").extract_first()
			drug = item.css("td.js-td--drug strong.drug::text").extract_first()
			stage = item.css("td.js-td--stage::text").extract_first()
			catalyst = item.css("td.js-td--catalyst time.catalyst-date::text").extract_first()
			note = item.css("td.js-td--catalyst div.catalyst-note::text").extract_first()

						

			yield BiopharmItem(
				ticker = ticker.strip(),
				price = price.strip().replace("$",""),
				drug = drug.strip(),
				stage = stage.strip(),
				catalyst = catalyst.strip(),
				note = "" if note is None else note.strip()+";",
				)
