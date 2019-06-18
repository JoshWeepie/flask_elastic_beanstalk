from flask import Flask, render_template
import os

application = Flask(__name__)

@application.route("/")
def home():
    host = os.uname()[1]
    ip = (host[3:].replace("-", "."))
    return render_template("home.html", ip=ip)
    
if __name__ == "__main__":
    application.run(debug=True)
