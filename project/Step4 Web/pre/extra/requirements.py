from flask import Flask
app = Flask(__name__)


#只有post的时候用不了？
@app.route('/',methods=["POST","GET"])
def world():
    return "Hello"

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
