from flask import Flask, render_template
from req_func import get_random_data
import json

app = Flask(__name__)


@app.route('/')
def hello():
    result = get_random_data()
    if result.status_code == 404:
        print(result.text)
        return "", 500
    else:
        data = json.loads(result.text)
        return render_template("user/user.html", data=data)
    
if __name__ == "__main__":
    app.run(host ='0.0.0.0')