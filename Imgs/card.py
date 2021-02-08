import random


class Card:
    def __init__(self, name, link, id):
        self.name = name
        self.link = link
        self.id = id


cards = [
    Card(
        "Naki Guitar",
        "https://i.imgur.com/mebMzx5.jpg",
        1),
    Card(
        "Guitar",
        "https://i.imgur.com/ypVfoUE.jpg",
        2),
    Card(
        "Brofist",
        "https://i.imgur.com/PhPcDHS.png",
        3
    ),
    Card(
        "Carro de Max",
        "https://i.imgur.com/qZK7Fmf.jpg",
        4
    ),    
    Card(
        "Mau viendo el futuro",
        "https://i.imgur.com/P7JrHDX.jpg",
        5
    ),
    Card(
        "Hiram siendo hiram",
        "https://i.imgur.com/2NjunhD.jpg",
        6
    ),
    Card(
        "Mau GRRRRR",
        "https://i.imgur.com/KCn6bup.jpg",
        7
    ),
    Card(
        "Puro ANAHUAC",
        "https://i.imgur.com/U5K82MG.jpg",
        8
    ),
    Card(
        "Hiram siendo gay",
        "https://i.imgur.com/Nz8C1TN.png",
        9
    ),
    Card(
        "Pabel sexy",
        "https://i.imgur.com/gA0sMev.jpg",
        10
    ),
    Card(
        "Pasaporte de Tomas",
        "https://i.imgur.com/gEJWSwj.png",
        11
    ),
    Card(
        "guapeton haciendo brofist",
        "https://i.imgur.com/OSESWhb.png",
        12
    ),
    Card(
        "pabel brofist",
        "https://i.imgur.com/Hsj8joh.jpg",
        13
    ),
    Card(
        "Brofist maximus",
        "https://i.imgur.com/DybRG0i.jpg",
        14
    ),
    Card(
        "Inspector de chichis",
        "https://i.imgur.com/UwCyqrh.jpg",
        15
    ),
    Card(
      "THANOSINTHEBOX BEING A GOD",
      "https://media.discordapp.net/attachments/807399692303859732/807859220145504306/RobloxScreenShot20201225_232307832.png?width=860&height=484",
      16
    )
  

]


def getRandomCard():
    index = random.randint(0, len(cards) - 1)
    return cards[index].name, cards[index].link, cards[index].id
