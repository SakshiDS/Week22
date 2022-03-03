#!/usr/bin/env python

from flask import Flask, render_template
from yelp_scrap import yelp_search
import pandas as pd

app = Flask(__name__)

# decorator with home end point
@app.route("/")
def home():
    text = "This is the home page. Use the endpoint /scrape to scrape restaurants from Yelp. Use scrape/all to see results!"
    caution = "Please be patient. These pages take a long time to load!"
    return render_template('index.html', home_text=text, caution_text=caution)


@app.route("/scrape")
def scrape():
    df = yelp_search()
    df_dict = pd.DataFrame.to_dict(df)
    return render_template('index.html', data=df_dict)
    

@app.route("/scrape/all")
def all():
    df = yelp_search() 
    return df.to_html(header="true", table_id="table")

if __name__ == "__main__":
    app.run(debug=True)