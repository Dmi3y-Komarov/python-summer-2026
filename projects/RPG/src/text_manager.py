import os
import json
from player import Player

class Text_manager:

    def __init__(self, lang="ru"):

        self.file_name = "texts.json"
        self.lang = lang
        self.context = {}
        self.texts = {}
        self.player = None

        self.cache = {}
        self.old_name = self.file_name

        self._load_texts()

    def set_player(self, player):
        self.player = player
        self.context_update()

    def context_update(self):
        self.context = vars(self.player).copy()

        aliases = {
                "hp" : "current_hp",
                "class" : "character_class"
                }
        for alias, real_name in aliases.items():
            self.context[alias] = self.context[real_name]

    def _load_texts(self):
        texts_path = os.path.join(os.path.dirname(__file__), "..", "data/", self.file_name)

        texts_path = os.path.normpath(texts_path)

        with open(texts_path, 'r', encoding='utf-8') as f:
            all_texts = json.load(f)

        if self.lang in all_texts:
            self.texts = all_texts[self.lang]
        else:
            raise ValueError(f"Язык {self.lang} не найден!")

    def get(self, key, **kwargs):

        keys = key.split('.')

        value = self.texts
        for k in keys:
            if k in value:
                value = value[k]
            else:
                return f"\n£\nОшибка: не существующий ключ {k}!"

        if self.player:
            self.context_update()

        all_args = {**self.context}

        all_args.update(**kwargs)
        if isinstance(value, str):

            try:
                return value.format(**all_args)
            except KeyError as e:
                return f"\n£\nОшибка: переменная {e} не найдена в {key}"

        return value

    def play_scene(self, choice, **kwargs):
        scene = self.get(choice, **kwargs)

        for container in scene:
            message = container["text"]
            print(message)

    def _clear_cache(self):
        self.cache = {}

    def _swap_cache(self):
        texts = self.texts
        self.texts = self.cache
        self.cache = texts

    def get_file_name(self):
        return self.file_name

    def set_file_name(self, new_name):
        old_name = get_file_name()
        if old_name != new_name:
            self.file_name = new_name
            self.cache = self.texts
            self._load_texts()
        elif self.old_name == new_name:
            self._swap_cache()
        return old_name
