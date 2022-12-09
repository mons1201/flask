from flask import Flask,make_response,render_template,jsonify,request
from flask_mongoengine import MongoEngine


app=Flask(__name__)

#database configuration
app.config['MONGODB_HOST']="mongodb+srv://mohan:mohan@cluster0.traigro.mongodb.net/kutty?retryWrites=true&w=majority"

# object document mapping config


mydb=MongoEngine()
mydb.init_app(app)


class Bike(mydb.Document):
    regno=mydb.StringField()
    model=mydb.StringField()
    brand=mydb.StringField()
    year=mydb.IntField()
    cc=mydb.FloatField()
    price=mydb.IntField()
    
@app.route("/<reg>")
def getByRegno(reg):
    return jsonify(Bike.objects(regno=reg).first())



@app.route("/",methods=['POST'])
def addnew():
    hai=request.json
    bike=Bike()
    bike.brand=hai['brand']
    bike.regno=hai['regno']
    bike.model=hai['model']
    bike.price=hai['price']
    bike.cc=hai['cc']
    bike.year=hai['year']

    bike.save()
    return jsonify(bike)


    
@app.route("/",methods=['GET'])
def showall():
    return jsonify(Bike.objects.all())

#@app.route("/fresh")
# def adding():
#     bike=Bike()
#     bike.regno="TN4M231"
#     bike.model="Pulsar"
#     bike.brand="TVS"
#     bike.year=2020
#     bike.cc=200
#     bike.price=90000

#     bike.save()
#     return jsonify(bike)



@app.route("/Hi")
def hello():
    return make_response("<h1>Happy to see you</h1>")
    
@app.route("/free")
def come():
    return render_template('connect.html')

@app.route("/passing",methods=['GET'])
def read():
    return render_template('page.html',mohana="Document verification")

@app.route("/mine/<int:dt>")
def write(dt):
    access=dt*4
    return render_template('page.html',mohana=access)

if __name__=="__main__":
    app.run(debug=True,port=5643)

