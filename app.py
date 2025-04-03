from flask import Flask,jsonify
app=Flask(__name__)
from routes.routes import routes_blueprint
@app.route("/",methods=["GET"])
def home():
    return {"message": "Hello, World!"}, 200
app.register_blueprint(routes_blueprint)
if __name__=='__main__':
    print("server started...")
    app.run(debug=True,port=8080)