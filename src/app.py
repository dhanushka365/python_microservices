import socket
from unicodedata import name
from flask import Flask, jsonify, render_template

app=Flask(__name__)

#Function to fetch hostname and Ip
def fetchDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Hostname:",host_name)
    print("Ip:",host_ip)
    return str(host_name), str(host_ip)

@app.route('/')
def home():
    return "<p>Hello world</p>"

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )
    
@app.route("/details")
def details():
    host_name, host_ip = fetchDetails()
    return render_template('index.html',host_name=host_name,host_ip=host_ip)
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)