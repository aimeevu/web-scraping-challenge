from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars
import json
from bson import json_util

app = Flask(__name__)

# Databasae Connection with PyMongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsDataDB"
mongo = PyMongo(app)

@app.route("/")
def index():
    marsData = mongo.db.marsData.find_one()
    # return json.loads(json_util.dumps(marsData))
    return render_template("index.html", mars=marsData)

@app.route("/scrape")
def scrape():
    # Databse Reference
    marsTable = mongo.db.marsData

    # Drops table if it exists
    mongo.db.marsData.drop()

    # Calls script to scrap data
    marsData = scrape_mars.scrape_all()

    # Loads dictionary into MongoDB
    marsTable.insert_one(marsData)

    # Returns data
    return redirect("/")

if __name__ == "__main__":
    app.run()
