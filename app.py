from flask import Flask, render_template

app = Flask(__name__)

# Sample data
products = {
    'clothing': [
        {'id': 1, 'name': 'Jacket', 'price': 99.99, 'description': 'A warm jacket.'},
        {'id': 2, 'name': 'T-shirt', 'price': 19.99, 'description': 'A cool t-shirt.'}
    ],
    'shoes': [
        {'id': 3, 'name': 'Sneakers', 'price': 49.99, 'description': 'Comfortable sneakers.'}
    ]
}

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/category/<category_name>')
def category(category_name):
    if category_name in products:
        return render_template('category.html', category_name=category_name.capitalize(), products=products[category_name])
    else:
        return "Category not found", 404

@app.route('/product/<int:product_id>')
def product(product_id):
    for category in products.values():
        for product in category:
            if product['id'] == product_id:
                return render_template('product.html', product=product)
    return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)
