from flask import Flask, request, jsonify, render_template
from Mainfile import llm




app=Flask(__name__)

@app.route('/',methods=['POST'])
def predict():
    data=request.get_json()
    reviews=data.get('text')
    response=llm(reviews)

    return jsonify({"response":response})
    

if __name__ == "__main__":
    app.run(debug=True)







