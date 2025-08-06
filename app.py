from flask import Flask
from routes.auth_routes import auth_api
from routes.complaint_routes import complaint_api
from routes.admin_routes import admin_api
from utils.database import init_db

app = Flask(__name__)
app.config.from_object('config')

# Register Blueprints
app.register_blueprint(auth_api, url_prefix="/auth")
app.register_blueprint(complaint_api, url_prefix="/complaints")
app.register_blueprint(admin_api, url_prefix="/admin")

# Initialize DB
init_db()

if __name__ == "__main__":
    app.run(debug=True)
