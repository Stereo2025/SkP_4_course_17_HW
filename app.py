from flask import Flask, jsonify
from raw_data.import_sql import db
from data_management.create_db import create_dbase
from apis.config import blue_print


app = Flask(__name__)
app.register_blueprint(blue_print)


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///hw_17_dbase.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['RESTX_JSON'] = {'ensure_ascii': False}


db.init_app(app)
app.app_context().push()
create_dbase()


@app.errorhandler(404)
def page_400_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return jsonify({"Error": 'Information Not Found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
