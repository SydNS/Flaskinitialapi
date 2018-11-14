from flask import Flask , request, jsonify
app= Flask(__name__)

pupils=[{'name':'Lano'},{'name':'Flutter'},{'name':'Toronto'},{'name':'CND'}]

@app.route("/",methods=['GET'])
def index():
	return jsonify({'message':'yo welcome'})

'''this endpoint displays the pupils list on line4'''
@app.route("/pupils",methods=['GET'])
def indx():
	return jsonify({'pupils':pupils}),200



'''this endpoint add the pupils to the list on line4'''
@app.route("/pupils",methods=['POST'])
def addin():
	n={'name': request.json['name']}
	return jsonify({'pupils added ':pupils}),200


if __name__ =='__main__':
	app.run(debug=True,port=3000)