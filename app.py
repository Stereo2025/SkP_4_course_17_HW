from flask import jsonify, current_app
from raw_data.import_sql import db
from apis.config import api

app = current_app


@app.errorhandler(404)
def page_400_error(error):
    """ Обработчик ошибок на стороне сервера"""

    return jsonify({"Error": 'Information Not Found'}), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
