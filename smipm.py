import asyncio
from backend.exporter import Exporter
from backend.scraper import Item
from ui.web.app import web_run
import threading

items = [
    Item("Fracture Case", 176185874),
    Item("Fever Case", 176506126),
    Item("Kilowatt Case", 176413986),
    Item("Recoil Case", 176321160),
    Item("Revolution Case", 176358765),
    Item("Dreams & Nightmares Case", 176288467),
    Item("Gallery Case", 176460428),
]

e = Exporter()
e.extend_item(items)

async def periodic_scrape():
    while True:
        e.export()
        await asyncio.sleep(5)

async def main():
    t = threading.Thread(target=web_run, daemon=True)
    t.start()
    await periodic_scrape()

asyncio.run(main())
