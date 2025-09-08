import os


class FileCommon:
    def __init__(self, filepath):
        self.path = filepath
        self.data = {'name': None, 'size': None, 'creation_date': None, 'owner': None}

    def get_info(self):
        'геттер - получает информацию о файле из файла и заполняет словарь'
        file = open(self.path, 'r', encoding='UTF8')
        line = file.read()
        val_gen = (x for x in line.split(' '))  # генератор создает строковые переменные из строчки файла
        for i in self.data:  # заполняем словарь с данными
            self.data[i] = next(val_gen)
        file.close()
        return self.data

    def create(self):
        'создает файл соответствующего типа'
        pass

    def delete(self):
        'удаляет файл по пути self.path'
        os.remove(self.path)


class Photo(FileCommon):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.data.update({'resolution': None, 'dpi': None, 'color_bpi': None})

    def create(self):
        file = open(self, 'w', encoding='UTF')
        file.write('создан пустой файл фото')
        file.close()


class Music(FileCommon):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.data.update({'type': None, 'bitrate_kbps': None})

    def create(self):
        file = open(self, 'w', encoding='UTF')
        file.write('создан пустой файл музыки')
        file.close()


class Video(FileCommon):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.data.update({'resolution': None, 'bitrate_kbps': None})

    def create(self):
        file = open(self, 'w', encoding='UTF')
        file.write('создан пустой файл видео')
        file.close()


def file_info(file: FileCommon):  # универсальный интерфейс получения данных файлов разных типов
    print(file.get_info())


def file_create(new_name, type):  # интерфейс создания файла соответствующего типа
    if type == 'фото':
        Photo.create(new_name)
    elif type == 'музыка':
        Music.create(new_name)
    elif type == 'видео':
        Video.create(new_name)


def file_delete(name):  # удаление файла
    file = FileCommon(name)
    file.delete()

# file1=Music('music.py') # проверяем получение данных
# file_info(file1)

# file_create('video_new.py', 'видео') # проверяем создание файла

# file_delete('video_new.py') # проверяем удаление файла
