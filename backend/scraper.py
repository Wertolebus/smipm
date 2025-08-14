import logging
import requests

class Item():
    def __init__(self, display_name, item_id):
        self.display_name = display_name
        self.item_id = item_id

    def get_tuple(self): return (self.display_name, self.item_id)

class Data():
    def __init__(self, display_name, price):
        self.display_name = display_name
        self.price = price
        self.tax_price = float("%.2f" % (price / 1.15))
    
    def to_dict(self):
        return {
            "display_name": self.display_name,
            "price": self.price,
            "tax_price": self.tax_price,
        }

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_item_price(item : Item):
    item_name, item_id = item.get_tuple()
    url = f'https://steamcommunity.com/market/itemordershistogram?country=RU&language=english&currency=18&item_nameid={item_id}'
    # logging.info(f"`{item_name}` - fetching")
    try:
        jsond = requests.get(url).json()
    except KeyError:
        logging.error(f"failed to fetch `{item_name}`")
        return Data(item_name, -1)
    price = float("%.2f" % ((int(jsond['highest_buy_order']) * .01)))
    # logging.info(f"`{item_name}` - done")
    return Data(item_name, price)
