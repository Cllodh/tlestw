import os
from flask import Flask

def create_app():
    app = Flask(__name__, static_folder=os.path.abspath('static'))
    app.secret_key = 'your_secret_key_please_change'  # 請改成安全的隨機字串
    from .routes import main_bp
    from .api import api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app 