import random


class Card:
    def __init__(self, name, link, id, rareza):
        self.name = name
        self.link = link
        self.id = id
        self.rareza = rareza


cards = [
    Card(
        "Naki Guitar",
        "https://i.imgur.com/mebMzx5.jpg",
        1,
        5),
    Card(
        "Guitar",
        "https://i.imgur.com/ypVfoUE.jpg",
        2,
        1),
    Card(
        "Brofist",
        "https://i.imgur.com/PhPcDHS.png",
        3,
        1
    ),
    Card(
        "Carro de Max",
        "https://i.imgur.com/qZK7Fmf.jpg",
        4,
        3
    ),    
    Card(
        "Mau viendo el futuro",
        "https://i.imgur.com/P7JrHDX.jpg",
        5,
        3
    ),
    Card(
        "Hiram siendo hiram",
        "https://i.imgur.com/2NjunhD.jpg",
        6,
        2
    ),
    Card(
        "Mau GRRRRR",
        "https://i.imgur.com/KCn6bup.jpg",
        7,
        4
    ),
    Card(
        "Puro ANAHUAC",
        "https://i.imgur.com/U5K82MG.jpg",
        8,
        2
    ),
    Card(
        "Hiram siendo gay",
        "https://i.imgur.com/Nz8C1TN.png",
        9,
        4
    ),
    Card(
        "Pabel sexy",
        "https://i.imgur.com/gA0sMev.jpg",
        10,
        2
    ),
    Card(
        "Pasaporte de Tomas",
        "https://i.imgur.com/gEJWSwj.png",
        11,
        1
    ),
    Card(
        "guapeton haciendo brofist",
        "https://i.imgur.com/OSESWhb.png",
        12,
        3
    ),
    Card(
        "pabel brofist",
        "https://i.imgur.com/Hsj8joh.jpg",
        13,
        2
    ),
    Card(
        "Brofist maximus",
        "https://i.imgur.com/DybRG0i.jpg",
        14,
        5
    ),
    Card(
        "Inspector de chichis",
        "https://i.imgur.com/UwCyqrh.jpg",
        15,
        4
    ),
    Card(
        "THANOSINTHEBOX BEING A GOD",
        "https://media.discordapp.net/attachments/807399692303859732/807859220145504306/RobloxScreenShot20201225_232307832.png?width=860&height=484",
        16,
        5
    ),
    Card(
        "Los 3 mosqueteros",
        "https://media.discordapp.net/attachments/807409001964765194/808521062873694269/image0.jpg?width=645&height=484",
        17,
        3
    ),
    Card(
        "AngelLoLXD",
        "https://media.discordapp.net/attachments/807409001964765194/808521471579258880/image0.jpg?width=363&height=484",
        18,
        4
    ),
    Card(
        "Naki Tryhard",
        "https://media.discordapp.net/attachments/807409001964765194/808522672601825290/image0.jpg?width=363&height=484",
        19,
        4
    ),
    Card(
        "Vegeta Sus",
        "https://media.discordapp.net/attachments/807409001964765194/808523040618315786/image0.jpg?width=393&height=484",
        20,
        5
    ),
    Card(
        "Duo Dab",
        "https://media.discordapp.net/attachments/807409001964765194/808523807698452480/image0.jpg",
        21,
        4
    ),
    Card(
        "Duo Faze up",
        "https://media.discordapp.net/attachments/807409001964765194/808523807873826837/image1.jpg?width=272&height=484",
        22,
        5
    ),


  

]


def getRandomCard():
    index = random.randint(0, len(cards) - 1)
    return cards[index].name, cards[index].link, cards[index].id, cards[index].rareza
