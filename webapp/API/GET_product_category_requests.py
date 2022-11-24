from flask import Blueprint, jsonify, abort
from API.connect import connect

connection = connect()
blueprint = Blueprint('get_product_category', __name__)


@blueprint.route('/api/v1/category-products', methods=['GET'])
def get_processes(connection=connection):
    products = []
    category = []
    category_products = {}
    result = []
    # with closing(conn) as conn:
    with connection.cursor() as cursor:
        cursor.execute('SELECT products.product_name, categories.category_name\n'
                       ' FROM products\n'
                       ' LEFT JOIN products_categories\n'
                       ' ON products_categories.product_id=products.id\n'
                       ' LEFT JOIN categories\n'
                       ' ON categories.id=products_categories.category_id;')
        for row in cursor:
            products.append(row[0])
            category.append(row[1])
        
        for i in range(len(category)):
            if category[i] == None:
                category[i] = 'None'
        print(category)
        for i in range(0, len(category)):
            category_products[category[i]] = []
        for i in range(0, len(category)):
            if i in category_products.keys():
               category_products[category[i]].append(products[i])
            else:
               category_products[category[i]].append(products[i])
        result.append(category_products)

    return jsonify({'products': result})