# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def divide_path(full_path: str):
    def divide(abs_path: str, div: str) -> tuple:
        abs_path = abs_path.split(div)
        file_name, extension = abs_path[-1].split('.')
        path = div.join(abs_path[:-1])
        return path, file_name, extension

    return divide(full_path, '/') if '/' in full_path else divide(full_path, '\\')


print(divide_path('C:/WorkShop/Python/GB-Python-Tech/HomeWork #5/Task #1.py'))