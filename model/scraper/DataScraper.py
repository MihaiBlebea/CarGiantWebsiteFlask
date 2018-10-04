import mechanicalsoup
from pandas import DataFrame


class DataScraper:

    def __init__(self, root_url, max_page_number):
        self.root_url = root_url
        self.max_page_number = max_page_number


    def get_data(self):
        data = []

        for i in range(1, self.max_pages):
            url = self.__get_next_url(root_url, i)
            data = data + self.__scrape_url(url)

        return DataFrame(data)


    def __scrape_url(self, url):
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(url)

        current_url = browser.get_url()

        links = browser.get_current_page().select('a.vehicle-cover ')

        car_array = []

        for link in links:
            complete_url = self.root_url + link.attrs['href']

            # Check if the request gives back 200 or error
            response = browser.get(complete_url)
            if response.status_code != 200:
                continue

            browser.open(complete_url)

            trs = browser.get_current_page().find_all('tr')
            car_details = browser.get_current_page().find('div', class_='car__main-details')
            car_price, car_details = self.__get_car_details(car_details)

            dict = {}
            dict['Car'] = car_name
            dict['Price'] = car_price

            for tr in trs:
                tds = tr.find_all('td')

                if len(tds) == 2:

                    # Remove white space from string
                    tds[0] = tds[0].text.strip()
                    tds[1] = tds[1].text.strip()

                    dict[tds[0]] = tds[1]

            car_array.append(dict)

        return car_array

    
    def __get_next_url(self):
        return self.root_url + '/page/' + str(self.page_cout)


    def __get_car_details(self, car_details):
        car_name = car_details.find('h1').text
        car_price = car_details.find('h2', class_='car__main-price').text
        return car_name, car_price
