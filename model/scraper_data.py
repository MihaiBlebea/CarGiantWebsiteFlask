import mechanicalsoup
import pandas as pd


def retrive_data(root_url, max_pages):
    data = []

    for i in range(1, max_pages):
        print('Started scraping page nr: ' + str(i))
        url = next_url(root_url, i)
        data = data + scrape(url)

    for car in data:
        car = remove_money_sign(car)
        car = remove_asterix(car)
        car = remove_comma(car)

    return pd.DataFrame(data)


def next_url(root_url, page_cout):
    return root_url + '/page/' + str(page_cout)


def scrape(url):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)

    current_url = browser.get_url()

    links = browser.get_current_page().select('a.vehicle-cover ')

    car_array = []

    for link in links:
        complete_url = 'https://www.cargiant.co.uk' + link.attrs['href']

        # Check if the request gives back 200 or error
        response = browser.get(complete_url)
        if response.status_code != 200:
            continue

        browser.open(complete_url)

        trs = browser.get_current_page().find_all('tr')
        car_details = browser.get_current_page().find('div', class_='car__main-details')
        car_name = car_details.find('h1').text
        car_price = car_details.find('h2', class_='car__main-price').text

        dict = {}
        dict['Car'] = car_name
        dict['Price'] = car_price

        print('Scraping car: ' + car_name)

        for tr in trs:
            tds = tr.find_all('td')

            if len(tds) == 2:

                # Remove white space from string
                tds[0] = tds[0].text.strip()
                tds[1] = tds[1].text.strip()

                dict[tds[0]] = tds[1]

        car_array.append(dict)

    return car_array


def remove_money_sign(car):
    for column in car:
        if '£' in car[column]:
            car[column] = car[column].replace('£', '')
    return car


def remove_asterix(car):
    for column in car:
        if '*' in car[column]:
            car[column] = car[column].replace('*', '').strip()
    return car


def remove_comma(car):
    for column in car:
        if ',' in car[column]:
            car[column] = car[column].replace(',', '')
    return car
