from flask import Flask, render_template, jsonify
from backend.exporter import Exporter
from datetime import datetime

app = Flask(__name__)
e = Exporter()

@app.route('/')
def root():
    return render_template('root.html', page_title="Root")

@app.route('/get_data')
def get_data():
    data = e.import_json()
    date = datetime.now().strftime("%d.%m.%Y")
    if date not in data:
        return jsonify({"times": [], "cases": {}})

    date_data = data[date]
    times = list(date_data.keys())
    cases = {}
    for t, items in date_data.items():
        for item in items:
            name = item["display_name"]
            if name not in cases:
                cases[name] = []
            cases[name].append({"time": t, "price": item["price"]})
    return jsonify({"times": times, "cases": cases})

def web_run():
    app.run(host='0.0.0.0', port=6969, debug=False)
