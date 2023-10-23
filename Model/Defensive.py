import Gear


class Defensive(Gear):

    def __init__(self, rarity, is_legendary, affix_list, item_power, item_type, armor_amount):
        super().__init__(self, rarity, is_legendary, affix_list, item_power, item_type)
        self.armor_amount = armor_amount


