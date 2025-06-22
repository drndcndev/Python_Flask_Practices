from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print(f"[LOGGED] Name : {data.get('name')} | \
        Email : {data.get('email')} | \
        Msg: {data.get('message')}")
    return jsonify({"status": "received"}), 200 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)