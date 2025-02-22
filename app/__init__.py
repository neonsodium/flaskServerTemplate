from flask import Flask

from config import Config, DevelopmentConfig, ProductionConfig, TestingConfig

app = Flask(__name__)

# Load the configuration from Config class
if Config.ENV == "development":
    app.config.from_object(DevelopmentConfig)
elif Config.ENV == "production":
    app.config.from_object(ProductionConfig)
elif Config.ENV == "testing":
    app.config.from_object(TestingConfig)

from app.routes import main_routes

app.register_blueprint(main_routes, url_prefix="/")
