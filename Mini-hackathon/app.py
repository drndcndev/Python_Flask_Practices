from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/greet')
def greet():
    name = request.args.get('name', 'Stranger')
    return jsonify({"Greeting": f"Hello {name}!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# docker build -t mini-hackathon .
# docker run -d -p 5000:5000 mini-hackathon