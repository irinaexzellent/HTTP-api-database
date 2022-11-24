from flask import Flask, jsonify, make_response


from API.GET_product_category_requests import blueprint as GET_product_category_blueprint
from API.GET_category_requests import blueprint as GET_category_blueprint
from API.GET_pairs import blueprint as GET_pairs_blueprint

app = Flask(__name__)

app.register_blueprint(GET_product_category_blueprint)
app.register_blueprint(GET_category_blueprint)
app.register_blueprint(GET_pairs_blueprint)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)