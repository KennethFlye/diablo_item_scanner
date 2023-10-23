import Gear


class Weaponry(Gear):

    def __init__(self, rarity, is_legendary, affix_list, item_power, item_type, damage_range):
        super().__init__(rarity, is_legendary, affix_list, item_power, item_type)
        self.damage_range = damage_range
        