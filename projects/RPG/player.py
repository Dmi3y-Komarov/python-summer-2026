class Player:

    def __init__(self, character_data, player_name):
        self.id = character_data["id"]
        self.name = player_name
        self.character_class = character_data["name"]

        self.death_message = "ВЫ ПОГИБЛИ"
        self.base_death_message = "ВЫ ПОГИБЛИ"

        self.max_hp = character_data["hp"]
        self.current_hp = character_data["hp"]
        self.attack = character_data["attack"]
        self.defense = character_data["defense"]

        self.location = character_data["start_location"]
        self.gold = 50

        self.inventory = {}
        self.souls = 0

    def is_alive(self):
        return self.current_hp > 0
    
    def take_damage(self, damage):
        real_damage = max(1, damage - self.defense)
        self.current_hp -= real_damage
        print(f'{self.name} получил {real_damage} урона. НР: {self.current_hp}/{self.max_hp}')

    def heal(self, amount):
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        print(f"{self.name} восстановил {amount} единиц здоровья. НР: {self.current_hp}/{self.max_hp}")

    def add_item(self, item_name, count):
        self.inventory[item_name] = self.inventory.get(item_name, 0) + count
        print(f'В инвентарь добавлено {count} штук {item_name}')

    def remove_item(self, item_name, count):
        if item_name not in self.inventory:
            return False

        current_count = self.inventory[item_name]

        if current_count - count < 0:
            return False

        new_count = max(current_count - count, 0)
        if new_count == 0:
            del self.inventory[item_name]
        else:
            self.inventory[item_name] = new_count
        return True

    def add_soul(self, count):
        self.souls += count
        print(f'{self.name} получил {count} душ. У Вас {self.souls} единиц')

    def show_stats(self):
        print(f'{self.name} [{self.character_class}]')
        print(f'HP:{self.current_hp}/{self.max_hp}')
        print(f'Атака: {self.attack} | Защита: {self.defense}')
        print(f'Золото: {self.gold}')
        print(f'Локация: {self.location}')
        print(f'Инвентарь: {self.inventory if self.inventory else "Пусто"}')
        print(f'Души: {self.souls}')
