import logging
from flask import Flask
from loader.views import loader_blueprint
from main.views import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# регистрируем первый блюпринт с поиском по вхождению слов "/"
app.register_blueprint(main_blueprint)
# регистрируем второй блюпринт с добавлением постов
app.register_blueprint(loader_blueprint)

# добавляем логирование для проекта
logging.basicConfig(filename='basic.log', level=logging.INFO)

app.run()
