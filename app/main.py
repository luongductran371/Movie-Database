from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
  return f"<p>Hello, World!</p>"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8000)
