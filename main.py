from flask import Flask, render_template, request, redirect
import os
import random
import time
from flask_sock import Sock

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(random.randrange(4096))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.get_json().get("render") == "reset":
            f = open("templates/index.html", "w")
            f.write(open("templates/template.html", "r").read())
            f.close()
        else:
            f = open("templates/index.html", "w")
            f.write(request.get_json().get("render"))
            f.close()

    return render_template('index.html', template="template.html")


if __name__ == '__main__':
    # print(socket.gethostbyname(socket.gethostname()))
    # Development
    app.run(debug=True, host="0.0.0.0", port=25565, threaded=True, ssl_context='adhoc')
