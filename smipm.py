import asyncio
from argparse import ArgumentParser
from ui.tui import tui
from backend.exporter import Exporter
from backend.scraper import Item

p = ArgumentParser()
t = p.add_mutually_exclusive_group(required=True)
t.add_argument("-web", action="store_true")
t.add_argument("-tui", action="store_true")
args = p.parse_args()

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

async def periodic_function():
    while True:
        e.export()
        await asyncio.sleep(5)

async def console_display():
    while True:
        tui()
        await asyncio.sleep(1)

async def main():
    if args.tui:
        await asyncio.gather(
            periodic_function(),
            console_display()
        )

    if args.web:
        gui()

asyncio.run(main())
