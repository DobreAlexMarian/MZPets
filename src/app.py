"""Flask application entry point for MZPets MVC demo."""

from flask import Flask
from .controllers.product_controller import product_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(product_bp, url_prefix='/products')

@app.route('/')
def home():
    # Simple home page redirect to product index
    return "<h1>Welcome to MZPets Demo</h1><p>Visit <a href='/products/'>Products</a></p>"

if __name__ == '__main__':
    # Run in debug mode for demo purposes
    app.run(debug=True)
