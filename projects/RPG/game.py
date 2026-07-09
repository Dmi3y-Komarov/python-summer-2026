import json
import random
import os
from player import Player
from src.text_manager import Text_manager

class Game:

    def __init__(self):
        self.player = None

        self.locations = self._load_json("data/locations.json")
        self.characters = self._load_json("data/classes.json")
        self.enemies = self._load_json("data/enemies.json")
        self.text_manager = Text_manager("ru")

    def _load_json(self, filename):
        full_path = os.path.join(os.path.dirname(__file__), filename)
        with open(full_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _t(self, choice, **kwargs):
        return self.text_manager.get(choice, **kwargs)

    def choose_character(self):
        print(self._t("character_selection.title"))

        for i, char in enumerate(self.characters, 1):
            print(self._t("character_selection.class_format", i = i, name = char["name"], description = char["description"]))
            print(self._t("character_selection.stats_format", hp = char["hp"], defense = char["defense"], attack = char["attack"]))

        while True:
            try:
                choice = int(input(self._t("character_selection.prompt")))
                if 1<=choice<=len(self.characters):
                    break
            except ValueError:
                print(self._t("errors.error_not_number"))

        player_name = input(self._t("character_selection.enter_name")).strip()
        if not player_name:
            player_name = self._t("character_selection.default_name")

        self.player = Player(self.characters[choice-1], player_name)
        self.text_manager.set_player(self.player)

        print(self._t("character_selection.welcome"))

    def get_current_location(self):
        for loc in self.locations:
            if loc["id"] == self.player.location:
                return loc
        return None

    def show_location(self):
        loc = self.get_current_location()
        print(f'\n{loc["name"]}')
        print(loc["description"])
        print(self._t("location.action_prompt"))
        for i, action in enumerate(loc["actions"], 1):
            action = "actions." + action
            print(self._t("location.action_format", i = i, action = self._t(action)))

    def handle_action(self, action):
        if action == 'rest' and self.player.location == 'cave':
            
            self.player.current_hp = 0
            self.text_manager.play_scene("death_sequences.death_from_bear_on_rest")
        elif action == 'rest':
            self.player.heal(30)
        elif action.startswith("go_to_"):
            new_location = action.replace("go_to_", "")
            self.player.location = new_location
            print(f'\nВы перешли в новую локацию')
            self.show_location()
        elif action.startswith("fight_"):
            enemy_id = action.replace("fight_", "")
            self._fight(enemy_id)
        elif action == "talk_grandfather":
            self._talk_grandfather()
        else:
            print(f'\nДействие {action} пока не реализовано!\n')

    def _fight(self, enemy_id):
        enemy_data = next((e for e in self.enemies if e["id"] == enemy_id), None)

        if not enemy_data:
            print("Враг не найден!")
            return False

        print(f'На тебя напал {enemy_data["name"]}! HP: {enemy_data["hp"]}')
        enemy_hp = enemy_data["hp"]

        while enemy_hp > 0 and self.player.is_alive():
            input("\n[Нажмите Enter для атаки]")

            damage = self.player.attack + random.randint(-3, 3)
            damage = max(1, damage)
            enemy_hp -= damage

            print(f'Ты нанес {damage} единиц урона!')

            if enemy_hp<0:
                break

            self.player.take_damage(enemy_data["attack"])

        if not self.player.is_alive():
            self.death_message = f'{self.player.name} погиб в бою!'
            return

        else:
            print(f'{enemy_data["name"]} повержен')

        if 'gold' in enemy_data and enemy_data["gold"]>0:
            gold_reward = enemy_data["gold"]
            self.player.gold += gold_reward
            print(f'Получено {gold_reward} золота!')

        if 'inventory' in enemy_data:
            print(f'Добыча с врага: ')

            for item_name, max_count in enemy_data["inventory"].items():
                drop_count = random.randint(0, max_count)
                if drop_count > 0:
                    self.player.add_item(item_name, drop_count)
                    print(f' • {item_name} : {drop_count} шт.')

        if 'soul' in enemy_data:
            soul_count = enemy_data["soul"]
            self.player.add_soul(soul_count)
            print(f'Получено {soul_count} душ')

    def _talk_grandfather(self):
        print("\nДед загадочно поглядываеь на вас и облизывается...\n- Хотите что-то купить?")
        print("1) Торговать")
        print("2) Напасть")
        print("3) Услуга?")
        print("0) Уйти")

        choice = input("Твой выбор: ").strip()
        if choice == "1":
            self._shop()
        elif choice == "2":
            self._fight("grandfather")
        elif choice == "3":
            print("Дед выпрыгиваеь из-за прилавка и идет в комнату. Но на входе он замирает, разворачивается к вам и манит руклй в кожаной перчатке за собой...")
            
            print("1) Пойти")
            print("0) Да ну его")

            second_choice = input("Выбор за Вами: ")

            if second_choice == "1":
                print("Только войдя в комнату вы получаете сильный удар чем-то тупым по голове и падаете без сознания...")
                print("Кто знает, что дед делал с Вами. Но Вы были обнаружены мертвым с сильнейшим анальным кровотечением...")
                self.player.current_hp = 0
                self.death_message = '\nВы оченб глупо погибли\n'
            else:
                print("Вы решили не связываться со странным стариком")
        else:
            print("Вы решили не связываться со странным стариком")

    def _shop(self):
        print("\nЛавка деда: ")
        print("Пока тут пусто. Приходи позже!")

    def game_over(self):
        print(self.player.death_message)
        print(f'{self.player.name} отправился в мир иной...')
        print(f'Небольшие итоги его жизни: ')
        print(f" • Класс: {self.player.character_class}")
        print(f" • Золото: {self.player.gold}")
        print(f" • Душ собрано: {self.player.souls}")
        print(f" • Предметов в инвентаре: {sum(self.player.inventory.values())}")

        while True:
            print("\n1) Начать заново")
            print("0) Выйти из игры")

            choice = input('Твой выбор: ').strip()

            if choice == '1':
                print("\nНачинаем новую игру!")
                self.__init__()
                self.choose_character()
                return True
            elif choice == '0':
                print("\nСпасибо за игру!")
                return False
            else:
                print("Неверный ввод")

    def check_player_alive(self):
        if not self.player.is_alive():
            self.game_over()
        return True
