############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code

        self.first_harvest = first_harvest

        self.color = color

        self.is_seedless = is_seedless

        self.is_bestseller = is_bestseller

        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType("cas", 2003, "orange", False, None, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", 1996, "green", True, None, "Crenshaw")
    crenshaw.add_pairing("prociutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon)
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    melon_types = make_melon_types()
    
    for melon in melon_types:
        print(f"{melon.name} pairs with")

        for pairing in melon.pairings: 
            print(f"- {pairing}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_types = make_melon_types()

    dictionary_melons = {}

    for melon in melon_types:
        if melon.code not in dictionary_melons:
            dictionary_melons[melon.code] = melon

    return dictionary_melons



############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(
        self, melon_type, shape_rating, color_rating, harvested_from, harvested_by
    ):
        """Initialize a melon."""

        self.melon_type = melon_type

        self.shape_rating = shape_rating

        self.color_rating = color_rating

        self.harvested_from = harvested_from

        self.harvested_by = harvested_by

    def is_sellable(self):
        """sellable if both its shape and color ratings > 5, and it did not come from field 3"""

        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    all_melon_types = []

    melons_by_id = make_melon_type_lookup(melon_types) # Not sure why they wanted us to do that


    melon_1= Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    all_melon_types.append(melon_1)

    melon_2= Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    all_melon_types.append(melon_2)

    melon_3= Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    all_melon_types.append(melon_3)

    melon_4= Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    all_melon_types.append(melon_4)

    melon_5= Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    all_melon_types.append(melon_5)

    melon_6= Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    all_melon_types.append(melon_6)

    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    all_melon_types.append(melon_7)

    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    all_melon_types.append(melon_8)

    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")
    all_melon_types.append(melon_9)

    return all_melon_types


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    melons = make_melons()

    for melon in melons:
        if melon.is_sellable() == True:
            print(f"Harvested by {melon.harvested_by} from Field {melon.harvested_from} CAN BE SOLD")
        else:
            print(f"Harvested by {melon.harvested_by} from Field {melon.harvested_from} NOT SELLABLE")