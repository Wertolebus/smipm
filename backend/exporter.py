from datetime import datetime
from backend.scraper import get_item_price, Item, Data
import json, pathlib



class Exporter():
    def __init__(self):
        self.items    = []
        self.path     = pathlib.Path().home() / "Desktop"
        self.filename = "test.json"

    def append_item(self, item : Item):
        self.items.append(item)

    def extend_item(self, item_list : list[Item]):
        self.items.extend(item_list)

    def get_data_from_list(self):
        data = []

        for item in self.items:
            data.append(get_item_price(item))

        return data

    def generate_iostream(self):
        pathlib.Path(self.path).mkdir(parents=True, exist_ok=True)
        if pathlib.Path(self.path / self.filename).is_file():
            return open(self.path / self.filename, 'r', encoding='utf8')
        else:
            f = open(self.path / self.filename, 'w', encoding='utf8')
            f.write("{}")
            f.close()
            f = open(self.path / self.filename, 'r', encoding='utf8')
            return f

    def load_json(self):
        iostream = self.generate_iostream()
        return json.load(iostream)

    def export(self):
        jdata = self.load_json()
        dt = datetime.now()
        time = dt.strftime("%H:%M:%S")
        items_data : list[Data]= self.get_data_from_list()
        if not time in jdata:
            jdata[time] = []
        for item in items_data:
            jdata[time].append(item.to_dict())
        if pathlib.Path(self.path / self.filename).is_file():
            f = open(self.path / self.filename, 'w', encoding='utf8')
            json.dump(jdata, f, ensure_ascii=False, indent=2)

    def import_json(self):
        if pathlib.Path(self.path / self.filename).is_file():
            return json.load(open(self.path / self.filename, 'r', encoding='utf8'))
    
    def get_2_last_records(self):
        data = self.load_json()

        return (list(data)[0], data[list(data)[-1]], data[list(data)[-2]]) if len(data) > 0 else (-1, -1, -1)