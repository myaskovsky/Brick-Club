from flask import Flask


app = Flask(__name__)


from app.main.routes import main
app.register_blueprint(main)

