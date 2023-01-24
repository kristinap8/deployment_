import pickle

from flask import Flask, render_template,request
from flask_cors import CORS,cross_origin

app = Flask(__name__)

@app.route("/")
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route("/description",methods=["GET"])
@cross_origin()
def description():
    return render_template("description.html")

@app.route("/description/profile")
@cross_origin()
def profile():
    return render_template("profile.html")

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            product_id = request.form['product_id']
            type = request.form['type']
            process_temperature = int(request.form['process_temperature'])
            rotational_speed = int(request.form['rotational_speed'])
            torque = int(request.form['torque'])
            tool_wear = int(request.form['tool_wear'])
            machine_failure = int(request.form['machine_failure'])
            TWF = int(request.form['TWF'])
            HDF = int(request.form['HDF'])
            PWF = int(request.form['PWF'])
            OSF = int(request.form['OSF'])
            RNF = int(request.form['RNF'])
            filename = 'linear_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict([product_id,type,process_temperature,rotational_speed,torque,tool_wear,machine_failure,TWF,HDF,PWF,OSF,RNF])
            return render_template('results.html',prediction = prediction[0])
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
