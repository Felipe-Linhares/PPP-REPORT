from flask_frozen import Freezer
from app import app
from src.constants import SQUADS
from datetime import datetime

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def index():
    yield {}

if __name__ == '__main__':
    freezer.freeze()