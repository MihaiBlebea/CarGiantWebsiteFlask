from scraper.DataScraper import DataScraper
from scraper.DataFormater import DataFormater, RemoveMoneySign, RemoveAsterix, RemoveComma


class ScraperFacade:

    def __init__(self, root_url, max_page):
        self.data_scraper = DataScraper(root_url, max_page)
        self.data = self.data_scraper.get_data()


    def get_formated_data(self):

        data_formater = DataFormater(self.data)
        data_formater.add( RemoveMoneySign() )
        data_formater.add( RemoveAsterix() )
        data_formater.add( RemoveComma() )
        return data_formater.run()
