import os
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")

def homepage():
    return render_template("homepage.html")

@app.route("/get_words")
def get_words():
    #defining words array from the mongodb collection words
    words = list(mongo.db.words.find())
    #words in blue is what the template will call the cluster of data from words in white
    return render_template("dictionary.html", words=words)

@app.route("/add_slang", methods=["GET","POST"])
def add_slang():
    if request.method == "POST":
        words = {
            "words_name": request.form.get("words_name"),
            "meaning": request.form.get("meaning"),
            "language_category": request.form.get("language_category")
        }
        mongo.db.words.insert_one(words)
        flash("Slang successfully added! Thank you for your contribution.")
        return redirect(url_for("get_words"))

    categories = mongo.db.language.find().sort("language_category",1)
    return render_template("add_slang.html", categories=categories)


@app.route("/edit_word/<word_id>", methods=["GET","POST"])
def edit_word(word_id):
    word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    
    categories = mongo.db.language.find().sort("language_category",1)
    return render_template("edit_slang.html", word=word, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)   