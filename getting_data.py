from queries import bar


def get_profile_flight(query):
    """
    Профиль спроса. Вылетевшие рейсы
    :param query: данные из формы
    :return:
    """
    # Тестовые данные, удалить при добавлении метода
    labels_bar = "['Africa', 'Asia', 'Europe', 'Latin America', 'North America']"
    data = "[2478, 5267, 734, 784, 433]"

    # Тут делаем запрос в метод , который сделает Влад с Софьей

    # Полученные данные передаем для построения графика
    data = bar(labels_bar, data, "profile_flight_table")
    return data


def get_profile_saled(query):
    """
    Профиль спроса. Проданные рейсы
    :param query: данные из формы
    :return:
    """
    # Тестовые данные, удалить при добавлении метода
    labels_bar = "['Africa', 'Asia', 'Europe', 'Latin America', 'North America']"
    data = "[2478, 5267, 734, 784, 433]"

    # Тут делаем запрос в метод , который сделает Влад с Софьей

    # Полученные данные передаем для построения графика
    data = bar(labels_bar, data, "profile_saled_table")
    return data


def get_seasons(query):
    """
    Сезоны
    :param query: данные из формы
    :return:
    """
    # Тестовые данные, удалить при добавлении метода
    labels_bar = "['Africa', 'North America']"
    data = "[2478, 5267, 734, 784, 433]"

    # Тут делаем запрос в метод , который сделает Влад с Софьей

    # Полученные данные передаем для построения графика
    data = bar(labels_bar, data, "seasons_table")
    return data


def get_dynamics(query):
    """
    Динамика бронирования
    :param query: данные из формы
    :return:
    """
    # Тестовые данные, удалить при добавлении метода
    labels_bar = "['Paper', 'Salt', 'Cucumber']"
    data = "[2478, 5267, 734, 784, 433]"

    # Тут делаем запрос в метод , который сделает Влад с Софьей

    # Полученные данные передаем для построения графика
    data = bar(labels_bar, data, "dynamics_table")
    return data