from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=EMOn9iAgygx6r5mP3Q0M641BO1LMpwjIo6NOoqzo")
    data = u.read()
    nasa_dict = json.loads(data)
    return render_template("rest.html", image = nasa_dict["hdurl"], title = nasa_dict["title"], date = nasa_dict["date"], explanation = nasa_dict["explanation"], copy = nasa_dict["copyright"])

if __name__ == "__main__":
    app.debug = True
    app.run()
