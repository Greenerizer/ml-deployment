from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def home():
   return render_template('index.html')

@app.route('/', methods = ["GET", "POST"])
def image():
   imagefile = request.files['imagefile']
   image_path = './images/' + imagefile.filename
   imagefile.save(image_path)

   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True, port=3000)