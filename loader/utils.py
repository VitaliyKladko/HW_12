def save_picture(picture) -> str:
    """
    Данная функция сохраняет картинку из form
    :param picture: получаем ее по средствам: picture = request.files.get('picture') в loader.views
    :return: path: str
    """
    # найдем имя этой картинки picture - это объект Flask и мы можем исп. его методы
    filename = picture.filename
    # выносим путь сохранения в отдельную переменную для удобства
    path = f'./uploads/images/{filename}'
    # cохраняем картинку с помощью метода (напомню, picture - это объект Flask)
    picture.save(path)
    return path

