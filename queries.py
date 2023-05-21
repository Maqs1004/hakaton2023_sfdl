def options(color_label='black',
            size_label='18',
            y_ticks_color='black',
            y_font_size='18',
            x_ticks_color='black',
            x_font_size='18',
            step_size='1000'):
    """Функция для создания объекта опций графика.

        Аргументы:
        - color_label (строка): Цвет меток легенды. По умолчанию: 'blue'.
        - size_label (строка): Размер шрифта меток легенды. По умолчанию: '18'.
        - y_ticks_color (строка): Цвет делений по оси Y. По умолчанию: 'green'.
        - y_font_size (строка): Размер шрифта по оси Y. По умолчанию: '18'.
        - x_ticks_color (строка): Цвет делений по оси X. По умолчанию: 'green'.
        - x_font_size (строка): Размер шрифта по оси X. По умолчанию: '18'.
        - step_size (строка): Шаг делений. По умолчанию: '1'.

        Возвращает:
        Строка, представляющая объект опций графика в формате JSON.
        """
    return "options: {\
            plugins: {\
              legend: {\
                labels: {\
                  color: '" + color_label + "',\
                  font: { \
                    size: " + size_label + "\
                  }\
                }\
              }\
            },\
        scales: { \
            y: { \
                ticks: { \
                color: '" + y_ticks_color + "', \
                font: {\
                    size: " + y_font_size + ", \
                },\
                stepSize: " + step_size + ",\
                beginAtZero: true\
                }\
            },\
            x: { \
                ticks: {\
                    color: '" + x_ticks_color + "',\
                    font: {\
                        size: " + x_font_size + "\
                            },\
                    stepSize: " + step_size + ",\
                    beginAtZero: true\
                        }\
                    }\
                }\
                }\
            }"


def direction_list():
    """
    запрос списка доступных направлений
    :return: список
    """
    return ["Москва - Сочи", "Сочи - Москва", "Москва - Астрахань", "Астрахань – Москва"]


def get_profile_flight(query):
    # Тестовые данные
    labels_bar = "['Africa', 'Asia', 'Europe', 'Latin America', 'North America']"
    data = "[2478, 5267, 734, 784, 433]"

    # Тут делаем запрос в метод , который сделает Влад с Софьей

    # Полученные данные передаем для построения графика
    data = bar(labels_bar, data, "profile_flight_table")
    return data


def get_profile_saled(query):
    # Тестовые данные
    labels_bar = "['Africa', 'Asia', 'Europe', 'Latin America', 'North America']"
    data = "[2478, 5267, 734, 784, 433]"

    # Тут делаем запрос в метод , который сделает Влад с Софьей

    # Полученные данные передаем для построения графика
    data = bar(labels_bar, data, "profile_saled_table")
    return data


def get_seasons(query):
    # Тестовые данные
    labels_bar = "['Africa', 'Asia', 'Europe', 'Latin America', 'North America']"
    data = "[2478, 5267, 734, 784, 433]"

    # Тут делаем запрос в метод , который сделает Влад с Софьей

    # Полученные данные передаем для построения графика
    data = bar(labels_bar, data, "seasons_table")
    return data


def get_dynamics(query):
    # Тестовые данные
    labels_bar = "['Africa', 'Asia', 'Europe', 'Latin America', 'North America']"
    data = "[2478, 5267, 734, 784, 433]"

    # Тут делаем запрос в метод , который сделает Влад с Софьей

    # Полученные данные передаем для построения графика
    data = bar(labels_bar, data, "dynamics_table")
    return data


def line_bar(labels_bar, data_bar, lables_line, data_line, element_id):
    """Функция для создания комбинированной диаграммы.

    Аргументы:
    - labels_bar (строка): Метки для столбцов диаграммы.
    - data_bar (строка): Данные для столбцов диаграммы.
    - labels_line (строка): Метки для линейной диаграммы.
    - data_line (строка): Данные для линейной диаграммы.
    - element_id (строка): Идентификатор элемента, куда будет отображаться диаграмма.

    Возвращает:
    Строка с JavaScript-кодом для создания комбинированной диаграммы с использованием библиотеки Chart.js.
    """

    # Тестовые данные
    # labels_bar = "['Red', 'Blue', 'Yellow', 'Green', 'Purple']"
    # data_bar = "[12, 19, 3, 5, 2]"
    # lables_line = "Dataset 2"
    # data_line = "[12, 19, 3, 5, 2]"
    return "const ctx = new Chart(document.getElementById('" + element_id + "'), {\
                type: 'bar',\
                data: {\
                    labels: " + labels_bar + ",\
                    datasets: [{\
                        label: '# of Votes',\
                        data: " + data_bar + ",\
                        borderWidth: 1,\
                        backgroundColor: ['blue'],\
                        order: 1\
                    },\
                        {label: '" + lables_line + "',\
                        data: " + data_line + ",\
                        borderColor: ['red'],\
                        type: 'line',\
                        order: 0}]\
                        },\
            " + options() + ");"


def bar(labels_bar, data, element_id):
    """Функция для создания столбчатой диаграммы.

    Аргументы:
    - labels_bar (строка): Название для столбцов диаграммы.
    - data (строка): Данные для столбцов диаграммы.
    - element_id (строка): ID элемента в HTML
    Возвращает:
    Строка с JavaScript-кодом для создания столбчатой диаграммы с использованием библиотеки Chart.js.
    """

    return "const myBarChart =  new Chart(document.getElementById('" + element_id + "').getContext('2d'), {\
        type: 'bar',\
        data: {\
            labels: " + labels_bar + ",\
            datasets: [\
                {\
                    label: 'Population (millions)',\
                    backgroundColor: ['#3e95cd', '#8e5ea2', '#3cba9f', '#e8c3b9', '#c45850'],\
                    data: " + data + "\
                }\
            ]\
        },\
        " + options() + ");"
