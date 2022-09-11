from flask import Blueprint, render_template, request
from functions import get_posts_by_word, load_posts

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    """
    Вьюшка передает представление на 'index.html' (страница для поиска)
    """
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    """
    Во вьюшку передается какое-то слово для поиска по постам и на выходе отдаются найденные посты
    """
    # в переменную кладется слово для поиска по средствам request.args.get по ключу 's'
    search_query = request.args.get('s', '')
    # в переменную posts передается список словарей постов

    posts = get_posts_by_word(search_query)
    return render_template('post_list.html', query=search_query, posts=posts)