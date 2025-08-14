from backend.exporter import Exporter
from datetime import datetime
import json

def tui():
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    RESET = "\033[0m"
    CLS = "\033[2J"
    e = Exporter()
    time, last, old = e.get_2_last_records()
    dt = datetime.now()
    time = dt.strftime("%H:%M:%S")
    if time == -1: return
    print(CLS)
    print(time)
    print("-"*30)
    for index in range(0, len(last)):
        last_dict = last[index]
        old_dict = old[index]
        last_tprice = last_dict['tax_price']
        old_tprice = old_dict['tax_price']
        if last_tprice < old_tprice:
            print(f"{RED}▼{RESET} {last_tprice:.2f}/{old_tprice:.2f} | {last_dict['display_name']}")
        elif last_tprice > old_tprice:
            print(f"{GREEN}▲{RESET} {last_tprice:.2f}/{old_tprice:.2f} | {last_dict['display_name']}")
        else:
            print(f"  {last_tprice:.2f}/{old_tprice:.2f} | {last_dict['display_name']}")
