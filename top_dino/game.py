from top_dino.deck import *


def play() -> None:
    # 1 Gerar baralho
    dino_deck = generate_dino_deck()

    # (EXEMPLO-1) print dino_card para cada dino_card no dino_deck
    # for dino_card in dino_deck:
    #     print(dino_card)

    #  list comprenhension
    # (EXEMPLO-2) print dino_card para cada dino_card no dino_deck
    # [print(dino_card)for dino_card in dino_deck]

    # 2 embaralhar as cartas
    p1_deck, p2_deck = split_deck(dino_deck)

    # print(p1_deck)
    # print()
    # print(p2_deck)

    # 3 gerar o relatório de batalhas
    # print(get_random_attr(p1_deck[0]))

    p1_score = 0
    p2_score = 2

    # percorrendo o p1_deck ed retornando o numero do index e o card..
    for index, p1_card in enumerate(p1_deck):
        p2_card = p2_deck[index]
        attr_to_compare = get_random_attr(p1_deck[index])

        print(f"p1_card -> {p1_card}")
        print(f"p2_card -> {p2_card}")
        print(f"attr_to_compare -> {attr_to_compare}")


        if p1_card[attr_to_compare] > p2_card[attr_to_compare]:
            p1_score += 1
            print(f'{p1_card["name"]} WINS')

        elif p1_card[attr_to_compare] < p2_card[attr_to_compare]:
            p1_score += 1
            print(f'{p2_card["name"]} WINS')

        else:
            print(f"DRAW")
        print()

        if p1_score > p2_score:
            print(f"PLAYER 1 WINS")

        elif p1_score < p2_score:
            print(f"PLAYER 2 WINS")
        
        else:
            print(f"DRAW")
        