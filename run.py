from flask import Flask,json
from flask import request, abort
import datetime
import pymongo
client = pymongo.MongoClient(host="127.0.0.1", port=27017)
db = client.blacklist
collection = db.phones

app = Flask(__name__)
@app.route('/')
def index():
    if request.remote_addr != '127.0.01':
        abort(403)
@app.route('/v1/check', methods = ['POST'])
def check():
    post_param = request.get_data().decode()
    jsonrequest = json.loads(post_param)    
    real_callee = jsonrequest['callee'][-11:]
    if(collection.find_one({'phone':real_callee})):
        callId = jsonrequest['callId']
        res_str = '{"callId":%d,"forbid":1,"transactionId":"910821-128385"}'%callId
        db.logs.insert_one({'callTime':datetime.datetime.now(),'callee':real_callee, 'type':1})
        return res_str
    else:
        callId = jsonrequest['callId']
        res_str ='{"callId":%d}'%callId
        return res_str


if __name__ == '__main__':
    # app.run(host="0.0.0.0",port=5000)
    app.run(debug=True)
