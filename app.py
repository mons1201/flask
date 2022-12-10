from flask import Flask,make_response,render_template,jsonify,request,session
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

#ERASE 
@app.route("/erase/<reg>",methods=['DELETE'])
def deleting(reg):
    check=Bike.objects(regno=reg).first()
    check.delete()
    return jsonify(reg+"vehicle has deleted")

# update method
@app.route("/<reg>",methods=['GET','PUT'])
def getByRegno(reg):
    if request.method=="GET":
        one=Bike.objects(regno=reg).first()
        return jsonify(one)
    else:
        hai=request.json
        Bike.objects(regno=reg).update_one(set__brand=hai['brand'],set__model=hai['model'],set__cc=hai['cc'],set__price=hai['price'],set__year=hai['year'])
        return jsonify(Bike.objects(regno=reg))


@app.route("/budget/<int:cost>")
def getByPrice(cost):
    return jsonify(Bike.objects(price__lte=cost))

@app.route("/brand/<bnd>")
def getByBrand(bnd):
    return jsonify(Bike.objects(brand=bnd))



@app.route("/year/<int:yr>")
def getByYear(yr):
    return jsonify(Bike.objects(year__gte=yr))


# @app.route("/<reg>")
# def getByRegno(reg):
#     return jsonify(Bike.objects(regno=reg).first())




@app.route("/create",methods=['POST'])
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

