"""Product controller handling product-related routes."""

from flask import Blueprint, render_template

product_bp = Blueprint('product', __name__)

@product_bp.route('/')
def index():
    # In a real app, fetch products from the model layer
    products = []
    return render_template('index.html', products=products)
