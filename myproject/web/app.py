from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def index():
    resp = requests.get(
        url='http://127.0.0.1:9080/crawl.json?spider_name=coronavirus&url=https://www.worldometers.info/coronavirus'
    ).json()

    data = resp.get('items')

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)