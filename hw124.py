from flask import Flask , jsonify , request
import pandas as pd

app = Flask(__name__)

contacts=[
    {
        "contact": "9987644456",
        "name":"raju",
        "done":False,
        "id":1
    },
    {
        "contact": "9987623956",
        "name":"shamu",
        "done":False,
        "id":1
    }


]

@app.route("/add-data" ,  methods = ["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message": "please provide the data!"
        },404)

    contact = {
        'id': contacts[-1]["id"]+1,
        'name': request.json['name'],
        'contact': request.json.get('contact' , ""),
        'done': False
    }

    contacts.append(contact)
    return jsonify({
        'status':"success",
        'message':'contact added succesfully!'
    })

@app.route("/get-data")
def get_contact():
    return jsonify({
        'data':contacts
    })

if (__name__ == '__main__'):
    app.run(debug = True)
