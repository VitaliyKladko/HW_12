from flask import Blueprint, render_template, request

from functions import add_post
from loader.utils import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post/')
def post_page():
    """
    Функция отображает форму добавления поста
    """
    return render_template('post_form.html')


@loader_blueprint.route('/post/', methods=['POST'])
def add_post_page():
    """
    Функция вытягивает из post_form.html картинку и контент и записывает ее в posts.json и папку uploads
    """
    # в переменную picture кладем картинку, которую получаем из формы post_form.html
    picture = request.files.get('picture')
    # в переменную content кладем текст, который достаем из <form> в post_form.html
    content = request.form.get('content')

    # обработка на случай если ничего нет в picture или в content
    if not picture or not content:
        return 'Нет картинки или текста'

    # picture_path хранит в себе путь до сохраненной картинки (плюс функция сохранила картинку  uploads)
    picture_path: str = '/' + save_picture(picture)

    # post хранит в себе dict 'pic' - ссылка на путь картинки, 'content' - тот контент, который мы
    # получили из формы с помощью: request.form.get('content')
    post: dict = add_post({'pic': picture_path, 'content': content})

    # возвращаем render_template с post_uploaded.html
    return render_template('post_uploaded.html', post=post)
