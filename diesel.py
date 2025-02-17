from bs4 import BeautifulSoup

from Utils.fuel import Fuel

class Diesel(Fuel):
    def __init__(self, config: dict):
        super().__init__(config)
        self.url = config.get("diesel_url", None)
        self.price = self.get_prices()


def get_prices(self):
    html_text = self.get_html_from_website(self.url)
    soup = BeautifulSoup(html_text, features="html.parser")
    locations = soup.find_all("div", {"class": "location"})
    locations = [item.text for item in locations]
    prices = soup.find_all(id="box_pret")
    self.last_price = float(prices[0].text.split(" ")[0])
    prices = [float(item.text.split(" ")[0]) for item in prices]
    prices_dict = dict(zip(locations, prices))

    return prices_dict