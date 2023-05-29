# biblioteca builtin....
import random

# DINO_NAMES -> É CAIXA ALTA = CONST, QUE VAI SER UMA TUPLA.
DINO_NAMES = (
    "Tyrannosaurus rex",
    "Velociraptor",
    "Stegosaurus",
    "Triceratops",
    "Brachiosaurus",
    "Allosaurus",
    "Ankylosaurus",
    "Spinosaurus",
    "Diplodocus",
    "Pteranodon",
    "Parasaurolophus",
    "Archaeopteryx",
    "Apatosaurus",
    "Iguanodon",
    "Gallimimus",
    "Microraptor",
    "Deinonychus",
    "Pachycephalosaurus",
    "Coelophysis",
    "Carnotaurus",
)


def generate_dino_deck() -> list[dict]:
    dino_cards = []

    # Pra cada nome no DINO_NAMES crie um dino_card que vai ser um dicionario contendo, name, strenght, agility, height...
    for dino_name in DINO_NAMES:
        dino_card = {
            "name": dino_name,
            "strenght": random.randint(1, 10),
            "agility": round(random.uniform(0, 10),1),
            "height": round(random.uniform(0, 10),2),
        }
        dino_cards.append(dino_card)

    return dino_cards





# embaralhar os cards..
def split_deck(deck: list[dict]) -> tuple[list[dict],list[dict]]:

    # embaralha o deck inteiro..
    random.shuffle(deck)
    
    # recebendo a lista de dict, pegando o tamanho e dividindo por 2. que retorna float com /...
    # para retornar inteiro //
    half_deck = len(deck) // 2
    # print(half_deck)

    # vai do inicio até o indice 3 que é half_deck.(dividir o deck)
    p1_deck = deck [:half_deck]

    # vai do indice 3 até o final( pegar a metade do deck dividir pra cada um)
    p2_deck = deck[half_deck:]

    # for card in p1_deck:
    #     print(f"p1_deck -> {card}")

    # comprenheinson..
    print()
    # [print(f"p2_deck -> {card}") for card in p2_deck]

    return p1_deck, p2_deck





def get_random_attr(card: dict) -> str:
    # para cada key dentro de card keys,
    # se a key for diferente de name atribuir nesse key aqui.
    card_keys = [key for key in card.keys() if key !="name"]

    # choice escolhe entre um dos elelementos de uma lista..
    return random.choice(card_keys)