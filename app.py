from flask import Flask, jsonify
from raw_data.import_sql import db
from apis.config import blue_print


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///hw_17.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['RESTX_JSON'] = {'ensure_ascii': False}


db.init_app(app)
app.app_context().push()
app.register_blueprint(blue_print)


@app.errorhandler(404)
def page_400_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return jsonify({"Error": 'Information Not Found'}), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
