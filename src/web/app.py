import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parent.parent.parent))
from datetime import datetime
from flask import Flask, render_template, request, jsonify
from src.utils import generate_report
from src.constants import SQUADS

app = Flask(__name__)

@app.route('/')
def index():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html', current_date=current_date, squads=SQUADS)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    report = generate_report(
        data['date'],
        data['squad'],
        data['sprint'],
        data['progressos'].split('\n'),
        data['planos'].split('\n'),
        data['problemas'].split('\n')
    )
    return jsonify({'report': report})

if __name__ == '__main__':
    # Use production config when running with gunicorn
    app.run(host='0.0.0.0', port=10000)