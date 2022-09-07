from flask import Flask, jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return "<p>Hello world</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)