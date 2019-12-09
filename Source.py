from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    trenutni_cas = datetime.datetime.now()
    return f"<h1>Moja prva spletna stran</h1><h3>Nov naslov</h3>{trenutni_cas}<li>List</li>"

@app.route("/about")
def on_about():
    #with open("index.html") as html_datoteka:
        #vsebina = html_datoteka.read()
        #return vsebina
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

print("Hello world")