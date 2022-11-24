from flask import Blueprint, jsonify, abort
from API.connect import connect

connection = connect()
blueprint = Blueprint('get_pairs', __name__)


@blueprint.route('/api/v1/pairs', methods=['GET'])
def get_processes(connection=connection):
    products = []
    # with closing(conn) as conn:
    with connection.cursor() as cursor:
        cursor.execute('SELECT products.product_name, categories.category_name\n'
                       ' FROM products\n'
                       ' LEFT JOIN products_categories\n'
                       ' ON products_categories.product_id=products.id\n'
                       ' LEFT JOIN categories\n'
                       ' ON categories.id=products_categories.category_id;')
        for row in cursor:
            products.append([str(row[0])+ '---'+ str(row[1])])

    return jsonify({'products': products})