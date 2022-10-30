from flask import Flask, jsonify, render_template, request
from model_cereal.utils import CerealRating
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Flask")
    # return "Ajay is good person."
    
    return render_template("index.html")

# @app.route('/rating')
# def predicte_rating():

#     data =request.form
#     print("Data-->",data)

#     mfr = data['mfr']
#     types = data['types']
#     calories = eval(data['calories'])
#     protein = eval(data['protein'])
#     fat = eval(data['fat'])
#     sodium = eval(data['sodium'])
#     fiber = eval(data['fiber'])
#     carbo = eval(data['carbo'])
#     sugars = eval(data['sugars'])
#     potass = eval(data['potass'])
#     shelf = eval(data['shelf'])
#     cups = eval(data['cups'])
#     name = data['name']


        
#     cr = CerealRating(mfr,type,calories,protein,fat,sodium,fiber,carbo,sugars,potass,shelf,cups,name)
#     rating = cr.get_predicted_rating()
#     return jsonify({"Result": f"predicted cereal rating is {rating} %"})



@app.route('/predict_rating',methods = ["POST","GET"])
def get_predict_charges():
    if request.method == "GET":
        print("we are using GET method")
    

        data = request.form
        print("Data-->",data)

        mfr = request.args.get("mfr")
        types = request.args.get("types")
        calories = eval(request.args.get("calories"))
        protein = eval(request.args.get("protein"))
        fat = eval(request.args.get("fat"))
        sodium = request.args.get("sodium")
        fiber = eval(request.args.get("fiber"))
        carbo = eval(request.args.get("carbo"))
        sugars = eval(request.args.get("sugars"))
        potass = eval(request.args.get("potass"))
        shelf = eval(request.args.get("shelf"))
        cups = eval(request.args.get("cups"))
        name = request.args.get("name")

        print("mfr,types,calories,protein,fat,sodium,fiber,carbo,sugars,potass,shelf,cups,name",mfr,types,calories,protein,fat,sodium,fiber,carbo,sugars,potass,shelf,cups,name)

        
        cr = CerealRating(mfr,types,calories,protein,fat,sodium,fiber,carbo,sugars,potass,shelf,cups,name)
        rating = cr.get_predicted_rating()
        # return jsonify({"Result": f"predicted cereal rating is {rating} %"})
        return render_template("index.html", prediction = rating)

    else:
        print("we are using POST method")

        mfr = request.form.get("mfr")
        types = request.form.get("types")
        calories = eval(request.form.get("calories"))
        protein = eval(request.form.get("protein"))
        fat = eval(request.form.get("fat"))
        sodium = request.form.get("sodium")
        fiber = eval(request.form.get("fiber"))
        carbo = eval(request.form.get("carbo"))
        sugars = eval(request.form.get("sugars"))
        potass = eval(request.form.get("potass"))
        shelf = eval(request.form.get("shelf"))
        cups = eval(request.form.get("cups"))
        name = request.form.get("name")

        print("mfr,types,calories,protein,fat,sodium,fiber,carbo,sugars,potass,shelf,cups,name",mfr,types,calories,protein,fat,sodium,fiber,carbo,sugars,potass,shelf,cups,name)
        
        cr = CerealRating(mfr,types,calories,protein,fat,sodium,fiber,carbo,sugars,potass,shelf,cups,name)
        rating = cr.get_predicted_rating()
        # return jsonify({"Result": f"predicted cereal rating is {rating} %"})
        return render_template("index.html", prediction = rating)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = config.PORT_NUMBER, debug = True)
    # app.run(host = '0.0.0.0',port = 5000, debug = True)