from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/enrollTuition', methods=['POST'])
def submit():
    data = request.get_json()
    
    
    unit_enrolled = data.get('unitEnrolled')
    cost_per_unit = data.get('costPerUnit')

    total_tuition = float(unit_enrolled) * float(cost_per_unit)

    discounted_tuition = total_tuition * 0.25
    total_tuition = total_tuition - discounted_tuition
        
    print(f"[LOGGED] Name: {data.get('name')} | \
        Units Enrolled: {unit_enrolled} | \
        Cost Per Unit: {cost_per_unit} | \
        Total Tuition: {total_tuition} | \
        Discounted Tuition: {discounted_tuition}")
        
    return jsonify({"discountedTuition": total_tuition}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)