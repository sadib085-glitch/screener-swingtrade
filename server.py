
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/screener', methods=['POST'])
def screener():
    data = request.get_json()
    ticker = data.get('ticker', 'BBCA')

    # Dummy response simulating technical analysis
    result = {
        "ticker": ticker,
        "entry": 8500,
        "take_profit": 9000,
        "stop_loss": 8300,
        "strategy": "Swing Trade",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
