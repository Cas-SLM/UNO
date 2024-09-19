
colors = ["RED", "BLUE", "YELLOW", "GREEN", "ALL"]
types = ["NUMBER", "DRAW", "REVERSE", "SKIP", "WILD", "WILD DRAW"]

def get_deck():
    card_list = []
    for card_type in types:
        match card_type:
            case "NUMBER":
                [card_list.append(card) for card in get_number_cards()]
                # card_list.append(get_number_cards())
            case "DRAW":
                [card_list.append(card) for card in get_draw2_cards()]
                # card_list.append(get_draw2_cards())
            case "REVERSE":
                [card_list.append(card) for card in get_reverse_cards()]
                # card_list.append(get_reverse_cards())
            case "SKIP":
                [card_list.append(card) for card in get_skip_cards()]
                # card_list.append(get_skip_cards())
            case "WILD":
                [card_list.append(card) for card in get_wild_cards()]
                # card_list.append(get_wild_cards())
            case "WILD DRAW":
                [card_list.append(card) for card in get_wild_draw_cards()]
                # card_list.append(get_wild_draw_cards())
    return card_list


def get_draw2_cards():
    card_list = []
    for color in colors:
        if color == "ALL":
            continue
        for i in range(2):
            card = Card(color, 2, "DRAW")
            card_list.append(card)
    return card_list

def get_reverse_cards():
    card_list = []
    for color in colors:
        if color == "ALL":
            continue
        for i in range(2):
            card = Card(color, -1, "REVERSE")
            card_list.append(card)
    return card_list

def get_skip_cards():
    card_list = []
    for color in colors:
        if color == "ALL":
            continue
        for i in range(2):
            card = Card(color, 1, "SKIP")
            card_list.append(card)
    return card_list

def get_wild_cards():
    card_list = []
    for i in range(4):
        card = Card("ALL", 0, "WILD")
        card_list.append(card)
    return card_list

def get_wild_draw_cards():
    card_list = []
    for i in range(4):
        card = Card("ALL", 4, "WILD DRAW")
        card_list.append(card)
    return card_list

def get_number_cards():
    card_list = []
    for num in range(20):
        if num == 10: continue
        card_num = num - 10 if num > 10 else num
        for color in colors:
            if color == "ALL":
                continue
            card = Card(color, card_num, "NUMBER")
            card_list.append(card)

    return card_list


class Card:
    color = str
    number = int
    card_type = str
    def __init__(self, color : str, number : int, card_type : str):
        self.color = color
        self.number = number
        self.card_type = card_type

    def __str__(self):
        if self.card_type == "NUMBER":
            return f"{self.color} {self.number}"
        elif self.card_type == "DRAW":
            return f"{self.color} {self.card_type} {self.number}"
        elif self.card_type in ["REVERSE", "SKIP"]:
            return f"{self.color} {self.card_type}"
        elif self.card_type == "WILD DRAW":
            return f"{self.card_type} {self.number}"
        elif self.card_type == "WILD":
            return f"{self.card_type}"
        else:
            return f"{self.card_type} {self.color} {self.number}"


