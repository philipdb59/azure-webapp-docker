from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello from a simplified Flask app!"

if __name__ == "__main__":
    # Important: Bind to '0.0.0.0' and use port 7000
    app.run(host="0.0.0.0", port=7000)
