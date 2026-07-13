import uuid
from src.text_manager import Text_manager

class ItemTemplate:

    def __init__(self, item_id, data):
        self.id = item_id
        self.type = data["type"]
        self.subtype = data.get("subtype", "generic")
        self.base_stats = data.get("base_stats", {})
        self.text_id = data.get("text_id", item_id)
        
        self.max_durability = data.get("max_durability", 100)
        self.durability = data.get("durability", self.max_durability)

        self.base_hits = data.get("base_hits", {})
        self.holding_blade_hits = data.get("holding_blade_hits", {})

    def get_hit_damage(self, hit_type, holding_blade = False):
            hits_dict = self.holding_blade_hits else self.base_hits
            return hits_dict.get(hit_type, 0)

    def get_stat(self, stat_name):
            return self.base_stats.get(state_name, 0)

class Item:

    def __init__(self, template: ItemTemplate, lang="ru"):
        self.text_manager = Text_manager(lang, "items_text.json")
        self.template = template
        self.unique_id = str(uuid.uuid4())[:8]

        self.current_durability template.durability
        self.is_equipped = False

        self.modifiers = {
                "thrust" : 0,
                "cutting_blow" : 0,
                "chopping_blow" : 0,
                "strike_guard" : 0,
                "defense" : 0,
                "heal_amount" : 0
                }

        self.player_skills = {}
        self.player_stats = {}

    def get_name(self):
        
    def get_description(self, text_manager):
