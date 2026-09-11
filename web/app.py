import os

from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

mongo_uri  = os.environ.get("MONGO_URI")
db_name    = os.environ.get("DB_NAME")

client = MongoClient(mongo_uri)
db = client[db_name]
routers = db["routers"]
interface_status = db["interface_status"]

@app.route("/")
def main():
    data = list(routers.find())
    return render_template("index.html", data=data)

@app.route("/add", methods=["POST"])
def add_router():
    ip = request.form.get("ip")
    username = request.form.get("username")
    password = request.form.get("password")

    if ip and username and password:
        routers.insert_one({
            "ip": ip,
            "username": username,
            "password": password
        })
    return redirect(url_for("main"))

@app.route("/delete/<id>", methods=["POST"])
def delete_router(id):
    try:
        routers.delete_one({"_id": ObjectId(id)})
    except Exception:
        pass
    return redirect(url_for("main"))

@app.route("/router/<ip>")
def router_detail(ip):
    records = list(interface_status.find({"router_ip": ip}).sort("timestamp", -1).limit(3))
    return render_template("router_detail.html", ip=ip, records=records)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)