from app import app  # Import the Flask app instance from __init__.py
from app import routes  # Import routes to register them

if __name__ == '__main__':
    app.run(debug=True)