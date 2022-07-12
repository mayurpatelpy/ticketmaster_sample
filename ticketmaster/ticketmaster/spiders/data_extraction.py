import datetime
import json

import requests
import scrapy
import pandas as pd
from scrapy.http import HtmlResponse


class DataExtractionSpider(scrapy.Spider):
    name = 'data_extraction'
    allowed_domains = ['']
    def __init__(self):
        self.output_list = []

    start_urls = ['www.example.com']



    def parse(self, response):
        input_df = pd.read_excel('Ticketmaster_Input.xlsx')

        for i in range(len(input_df)):
            # this code will be collect home page data

            url = input_df['Input'][i]
            headers = {
                'accept': '*/*',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,gu;q=0.7',
                'cache-control': 'max-age=0',
                'cookie': 'LANGUAGE=en-us; SID=edzAfyt603SAXnwzG7JUrBK99JLvpnvk01YAeEwFHvuKrerl6gu1vCKs0M3nZBhNzIWM5Fd0zwJg0eTS; lightstep_guid%2Fco2.sdk=49138c2a161e7f89; lightstep_session_id=1f773c8223ea97aa; mt.v=2.1717198810.1657643175685; lightstep_guid%2Fedp.app=0a39c65956c69019; TMUO=west_QOu2Bi1xCft6EjLHXcc8WjKfNM3OHx/XrRHQn6uc5n4=; _gcl_au=1.1.656262640.1657643202; TMSPON=48b26025-4941-413b-9803-9ea6aa7035a7; _rdt_uuid=1657643216887.b8b481eb-1451-4235-ad46-c0fea07ab1c4; _scid=ecd4cba6-5199-48b6-930c-834d6bf141b7; _fbp=fb.1.1657643225193.1404470753; _pin_unauth=dWlkPU5HVXpNMk5oWkdFdE5tTTBNUzAwWlRneExXSmhNalV0TldOaE1tTmpNREk0TjJVMg; _gid=GA1.2.1610056890.1657643237; _cs_c=0; TM_PIXEL={"_dvs":"0:l5idzmma:ZTH2FV7M8Zj29mA8cWRdME5YSOr7~Z0O","_dvp":"0:l5idzmma:HkW3eWLbmjmjHYAsCwoiFfJdenA_nIaM"}; _dvs=0:l5idzmma:ZTH2FV7M8Zj29mA8cWRdME5YSOr7~Z0O; _dvp=0:l5idzmma:HkW3eWLbmjmjHYAsCwoiFfJdenA_nIaM; seerses=e; seerid=c78eb1ff-8445-4b3e-97d0-79445fa8c83b; __qca=P0-1828335516-1657643251436; reese84=3:Op3zOOUxVeLBdr/V4VK25w==:EN0EEqVhlhStI+Y5jjb4+FLcmI7YiJ3ORH8C8C51FAPazLDKUQG5DgenkHjzqyXo4PxVZt9D85yU0F608ytt+SgRlHU5umu85u6xQtVCJ6vEyU807dNpTv9TkqG+wDznZIt6xAT45Ff+i3rXsWkYXSS23ebXXn3c82Nh22LQAIMK/ZKDNbauvtDHyCUvd/MOFtD9unKYkVTKBCBYa5mA5A5nWeYusTgWnSl6L8iNz8c4AtqfW+VJKYAd4F8AA8q/hRWlg+LJgPLNbd/lYliyXQ/aRGxq0fMwANI4e352KnK1HeNzA8hT24M16ej4XcOeSOLLo6DBvoK40+IcHCi74TO06G0Ywz4bGH0Y9EL4HYqnjjUxy5YItMb5/S6z1GhzigO/c7Jm9DHCe9c16IRUtKEldRFYcVErbhgm9ulY6ehUMe5MpHU5rQvqOR0E6hP12iCUGTyQJIwSPQpSRbPFPSZiGZwieblCjs2s1g3IiD5bYk592mDFcRnjOazjROwT:d0JP5auSmO6+TiAupEqu5vmZnwCs3ABosVDvkgUhK2U=; BID=SHUQFydoYZXfaji_3NT1fYSlUAiO-CWCR0P8WaKfpJMlGg1peSFdPIYIFZMBa1cQjjxMxjhlXKmIBSxS; VENUE=180306; ARTIST=806007; BRANDTEXTCOLOR=#FFFFFF; BRAND=2478; eps_sid=b3a5a70b1261401c8643e070309b7cd3; mt.pc=2.2; _dc_gtm_UA-60025178-1=1; _uetsid=82dacd2001ff11ed97db4998a7f662c4; _uetvid=82db38e001ff11ed8a5fdf8c84392c5b; _cs_cvars=%7B%221%22%3A%5B%22Page%20Name%22%2C%22TM_US%3A%20CCP%20EDP%3A%20RS%3A%20Onsale%22%5D%2C%222%22%3A%5B%22Page%20Type%22%2C%22CCP%20EDP%3A%20Onsale%22%5D%2C%225%22%3A%5B%22EDP%20Type%22%2C%22CCP%20EDP%3A%20SIM%22%5D%2C%228%22%3A%5B%22Primary%20Page%20Categor%22%2C%22Sports%22%5D%2C%229%22%3A%5B%22Page%20Sub%20Category%22%2C%22Football%22%5D%2C%2210%22%3A%5B%22Event%20Type%22%2C%22STANDARD%22%5D%2C%2211%22%3A%5B%22Artist%20Name%22%2C%22Pittsburgh%20Steelers%22%5D%7D; _cs_id=4dc4cc0f-3b81-a49f-afbe-296a099dda2c.1657643243.1.1657645002.1657643243.1.1691807243541; _cs_s=2.5.0.1657646802528; __pdst=d4bb63ad37fb49258c40e82691dc1a38; _ga_Y9KJECPJMY=GS1.1.1657643243.1.1.1657645002.60; AMCV_F75C3025512D2C1D0A490D44%40AdobeOrg=T; _ga=GA1.2.468220794.1657643237',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
            }
            res = requests.get(url, headers=headers)
            if res.status_code != 200:
                break
            print(url)
            response = HtmlResponse(url='', body=res.content, encoding='utf-8')
            js_data = response.xpath('//*[@data-bdd="eventSchema"]//text()').get()
            if js_data != None:
                json_data = json.loads(js_data)
                try:
                    date_slug = json_data['startDate'].split('T')[0]
                    event_date = datetime.datetime.strptime(date_slug, '%Y-%m-%d').strftime('%Y/%m/%d')
                except Exception as e:
                    print('You Have Error in Event Date..', e)
                    event_date = ''
            else:
                event_date = ''
            title = response.xpath('//*[@class="event-header__event-name"]/span/text()').get('').strip()
            venue = response.xpath(
                '//*[@class="event-header__event-location event-header__event-location-link"]/span/text()').get('').strip()

            event_link = response.xpath('//*[@property="og:url"]/@content').get('').strip()

            # this code will be collect ticket data

            try:
                ticket_headers = {
                    'accept': '*/*',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'cookie': headers['cookie'],
                    'origin': 'https://www.ticketmaster.com',
                    'referer': 'https://www.ticketmaster.com/',
                    'tmps-correlation-id': '7a697339-8164-4a73-af81-36107a9ebddb',
                    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
                }
                event_id = url.split('event/')[-1]
                ticket_url = f'https://offeradapter.ticketmaster.com/api/ismds/event/{event_id}/quickpicks?show=places+maxQuantity+sections&mode=primary:ppsectionrow+resale:ga_areas+platinum:all&qty=000000000001%3A2&q=not(%27accessible%27)&includeStandard=true&includeResale=true&includePlatinumInventoryType=false&ticketTypes=000000000001&embed=area&embed=offer&embed=description&apikey=b462oi7fic6pehcdkzony5bxhe&apisecret=pquzpfrfz7zd2ylvtz3w5dtyse&resaleChannelId=internal.ecommerce.consumer.desktop.web.browser.ticketmaster.us&limit=100&offset=0&sort=listprice'
                get_ticket_response = requests.get(ticket_url, headers=ticket_headers)
                if get_ticket_response.status_code != 200:
                    break
                ticket_data = get_ticket_response.json()
                available_ticket = ticket_data['total']
                item = {}
                item['EventUrl'] = event_link
                item['EventName'] = title
                item['EventDate'] = event_date
                item['EventVenue'] = venue
                item['AllAvailableTickets'] = available_ticket
                self.output_list.append(item)
            except Exception as e:
                print(e)

    def close(spider, reason):
        output_df = pd.DataFrame(spider.output_list)
        output_df.to_csv('ticketmaster_sample.csv', index=False)

