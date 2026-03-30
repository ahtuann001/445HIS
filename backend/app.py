<<<<<<< HEAD
from flask import Flask, render_template
from router import router               # Import các API
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(router)          # Đăng ký router chứa API


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
=======
from flask import Flask, render_template
from router import router               # Import các API
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(router)          # Đăng ký router chứa API


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
>>>>>>> e917c657e71d9020a74df9d03c7e8f974a51a9be
    )