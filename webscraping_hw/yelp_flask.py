#!/usr/bin/env python

from flask import Flask, render_template
import json
from yelp_scrap import yelp_scrap_50
import pandas as pd

app = Flask(__name__)

# Declaring global variable to store scraped data


# decorator with home end point
@app.route("/")
def home():
    
    return "Welcome to the app where we scrap yelp.com for top restaurants!"


@app.route("/scrape")
def scrape():
    df = yelp_scrap_50(63017)
    yelp_top_50 = pd.DataFrame.to_dict(df)
    with open('yelp_50.json', 'w') as fp:
        json.dump(yelp_top_50, fp)
    return "Data is ready!\n Go to /all endpoint to view results"
    
@app.route("/all")
def all():
    with open('yelp_50.json', 'r') as fp:
        data = json.load(fp)
        yelp_df = pd.DataFrame(data)
    return yelp_df.to_html(header="true", table_id="table")

if __name__ == "__main__":
    app.run(debug=True)