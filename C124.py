from flask import Flask,jsonify,request


app=Flask(__name__)
tasks=[
    {
        "id":1,
        "title":"Buy Vegetables",
        "description":"Buy Brocoli, carrot, etc",
        "done":False
    },
        {
        "id":2,
        "title":"Go to park",
        "description":"walk 2km",
        "done":False
    }
]
@app.route("/")
def helloworld():
    return "hello world"
@app.route("/add-data",methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the task detials"
        },400)
    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":success,
        "message":"task added successfuly"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if (__name__=="__main__"):
    app.run(debug=True)