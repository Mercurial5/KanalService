from flask import Flask, render_template
from sqlalchemy.orm import Session
from dotenv import load_dotenv

load_dotenv()

from models import Orders, engine

app = Flask(__name__)


@app.route('/')
def main():
    with Session(engine) as session:
        orders = session.query(Orders).all()
        return render_template('index.html', orders=orders)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1235', debug=True)
