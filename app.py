from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Example data structures
fuel_prices = {
    'Regular': 2.59,
    'Mid-Grade': 2.89,
    'Premium': 3.09,
    'Diesel': 3.19
}

# Simple loyalty program data
loyalty_members = {
    '12345': {'name': 'John Doe', 'points': 120},
    '67890': {'name': 'Jane Doe', 'points': 200}
}

@app.route('/')
def home():
    return render_template('index.html', fuel_prices=fuel_prices)

@app.route('/update_fuel_price', methods=['POST'])
def update_fuel_price():
    fuel_type = request.form.get('fuel_type')
    new_price = request.form.get('new_price')
    
    if fuel_type in fuel_prices:
        fuel_prices[fuel_type] = float(new_price)
        return jsonify({'message': 'Fuel price updated successfully!'}), 200
    else:
        return jsonify({'message': 'Fuel type not found'}), 404

@app.route('/loyalty_points/<member_id>', methods=['GET'])
def get_loyalty_points(member_id):
    member = loyalty_members.get(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({'message': 'Member not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
