from flask import Flask
from flask_cors import CORS


import controllers.frontcontroller as fc

app = Flask(__name__)
cors = CORS
app.config['CORS_HEADERS'] = 'CONTENT TYPE'

fc.route(app)

if __name__ == '__main__':
    app.run()
