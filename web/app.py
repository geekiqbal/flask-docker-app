from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def validate_inputs(reqData):
    status_code = None

    try:
        x = reqData["x"]
        y = reqData["y"]
        x = float(x)
        y = float(y)
        status_code = 200

    except:
        status_code = 301


    return status_code


class Add(Resource):
    def post(self):       
        resMap = status_code = z = None
        reqData = request.get_json()

        status_code = validate_inputs(reqData)
        
        if status_code == 200:
            x = float(reqData["x"])
            y = float(reqData["y"])
            z = x + y

            resMap = {
                "Message": z,
                "Status Code": status_code
            }

        else :
            resMap = {
                "Message": "Invalid Inputs",
                "Status Code": status_code
            }
    
        return jsonify(resMap)


class Subtract(Resource):
    def post(self):       
        resMap = status_code = z = None
        reqData = request.get_json()

        status_code = validate_inputs(reqData)
        
        if status_code == 200:
            x = float(reqData["x"])
            y = float(reqData["y"])
            z = x - y
            resMap = {
                "Message": z,
                "Status Code": status_code
            }

        else :
            resMap = {
                "Message": "Invalid Inputs",
                "Status Code": status_code
            }
    
        return jsonify(resMap)


class Multiply(Resource):
    def post(self):       
        resMap = status_code = z = None
        reqData = request.get_json()

        status_code = validate_inputs(reqData)
        
        if status_code == 200:

            x = float(reqData["x"])
            y = float(reqData["y"])
            z = x * y
            resMap = {
                "Message": z,
                "Status Code": status_code
            }

        else :
            resMap = {
                "Message": "Invalid Inputs",
                "Status Code": status_code
            }
    
        return jsonify(resMap)


class Divide(Resource):
    def post(self):       
        resMap = status_code = z = None
        reqData = request.get_json()

        status_code = validate_inputs(reqData)
        
        if status_code == 200 and reqData["y"] == 0:
            resMap = {
                "Message": "OOOPs Divde by Zero",
                "Status Code": 302
            }

        elif status_code == 200 :
            x = float(reqData["x"])
            y = float(reqData["y"])
            z = x / y
            resMap = {
                "Message": z,
                "Status Code": status_code
            }
        
        else:
            resMap = {
                "Message": "Invalid Inputs",
                "Status Code": status_code
            }
    
        return jsonify(resMap)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


if __name__ == "__main__":
    app.run(host="0.0.0.0")

