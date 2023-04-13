from flask import Flask, request, jsonify
from flask_cors import CORS
from img_proc import changeColor

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/', methods=['GET'])
def index():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the request JSON data
    data = request.get_json()


    # Extract the input parameters from the request data
    input_param1 = data['url']
    input_param2 = data['color']
    print(input_param1)
    print(input_param2)
    color = hex_to_rgb(input_param2)
    def hex_to_rgb(hex_code):
        # remove the # symbol, if present
        hex_code = hex_code.lstrip('#')
    
        # convert the hex code to RGB values
        red = int(hex_code[0:2], 16)
        green = int(hex_code[2:4], 16)
        blue = int(hex_code[4:6], 16)
    
        return (red, green, blue)

    # changeColor(input_param1, (300, 100), [color.red, color.green, color.blue], None)
    
    # Create a JSON response with the output
    response = {
        'processedpath': './public/edited/img.jpg',
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=8000)