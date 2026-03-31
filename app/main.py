from flask import Flask
from flask_cors import CORS
from interfaces.api.routes import api

def create_app():
    app = Flask(__name__)
    CORS(app, resources={
        r"/*": {
            "origins": [
                "http://127.0.0.1:5500",
                "https://polimarket-u9d6.onrender.com",
                "https://entrega1-poli.vercel.app"
            ]
        }
    })

    app.register_blueprint(api)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
