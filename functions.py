import json

def load_posts() -> list[dict]:
    """
    Функция загружает все посты из файла json и отдает list[dict]
    """
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_word(word: str) -> list[dict]:
    """
    Функция поиска постов по входящим словам отдает обратно list[dict]
    """
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post: dict) -> dict:
    """
    Функция принимает словарь {'pic':picture_path, 'content':content} и перезаписывает posts.json с добавлением
    нового поста
    :param post: {'pic':picture_path, 'content':content}
    :return: dict: {'pic':picture_path, 'content':content}
    """
    posts: list[dict] = load_posts()
    # добавляем в наши посты только что полученный пост
    posts.append(post)
    # полностью перезаписываем файл posts.json с новыми данными о постах
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
