import random


class Card:
    def __init__(self, name, link, id, rareza):
        self.name = name
        self.link = link
        self.id = id
        self.rareza = rareza


cards = [
    Card(
        "ÃÒœŋ±ĶŅŰłģė×´ñµĭðĸŲŪªŒÞŀū½åŻĕÊŕēôź·ŎöùĒûüÓľĈÀőŢċĞď",
        "https://i.pinimg.com/736x/d0/b2/00/d0b200be256c685f13e4caa83d365e9e.jpg",
        1,
        6
    ),
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
    Card(
        "Evan dab",
        "https://cdn.discordapp.com/attachments/810942575154036776/810942819220062218/WIN_20201104_10_20_03_Pro.jpg",
        23,
        3
    ),
    Card(
        "God",
        "https://scontent.ftij2-1.fna.fbcdn.net/v/t1.15752-9/147494538_250123623397533_4694279337264144857_n.jpg?_nc_cat=101&ccb=3&_nc_sid=ae9488&_nc_eui2=AeGzFpm2Rc3kps4qQ0cmVZ-49autxOD_PiT1q63E4P8-JCSGxwcxi7zPoy7LF4984O9HVbTXwTk4C0EXIiXrWTdl&_nc_ohc=IDy-DXPZ5-UAX-vCCK3&_nc_ht=scontent.ftij2-1.fna&oh=b480ff52513015c407e4eb3b89d331e6&oe=604EEC65",
        24,
        5
    ),
    Card(
        "Armando Fase 1",
        "https://scontent.ftij2-1.fna.fbcdn.net/v/t1.15752-9/147494538_250123623397533_4694279337264144857_n.jpg?_nc_cat=101&ccb=3&_nc_sid=ae9488&_nc_eui2=AeGzFpm2Rc3kps4qQ0cmVZ-49autxOD_PiT1q63E4P8-JCSGxwcxi7zPoy7LF4984O9HVbTXwTk4C0EXIiXrWTdl&_nc_ohc=IDy-DXPZ5-UAX-vCCK3&_nc_ht=scontent.ftij2-1.fna&oh=b480ff52513015c407e4eb3b89d331e6&oe=604EEC65",
        25,
        2
    ),
    Card(
        "Armando Fase 2",
        "https://scontent.ftij2-1.fna.fbcdn.net/v/t1.15752-9/147338454_175999727244015_5145030684428162932_n.jpg?_nc_cat=104&ccb=3&_nc_sid=ae9488&_nc_eui2=AeFOvd4dgGTBCRbDQkMJDm1bkYbVRrBOgJqRhtVGsE6AmnQCajL7D-OZCjrM3LT9CR6Yau-QdaVhAD0Q4k-WGHDK&_nc_ohc=Lh2M3IgLWH0AX9uCcCT&_nc_ht=scontent.ftij2-1.fna&oh=7bd3d14e6b37074378640109368add39&oe=605215A8",
        26,
        2
    ),
    Card(
        "Armando Cool",
        "https://scontent.ftij2-1.fna.fbcdn.net/v/t1.15752-9/147813331_240811704309972_466427288274722927_n.jpg?_nc_cat=101&ccb=3&_nc_sid=ae9488&_nc_eui2=AeFb3neHjoL9IosLwLtFfW6zg4xPHbi5X1WDjE8duLlfVRW9MLySwY1QsD7tPYKmxjIquaeFjlxBXOWTdM6yMria&_nc_ohc=TG9tea-GOHwAX_K4bl2&_nc_ht=scontent.ftij2-1.fna&oh=9d2919ce48073b7bc6e15d731c54f962&oe=604F0F33",
        27,
        1
    ),
    Card(
        "Armando Fase Maxima",
        "https://scontent.ftij2-1.fna.fbcdn.net/v/t1.15752-9/147272616_891303798299611_5985287083702272256_n.jpg?_nc_cat=103&ccb=3&_nc_sid=ae9488&_nc_eui2=AeHtneHd4cbf_QJYl1u4Ziehm71copc2YOCbvVyilzZg4N21z2tfIC5YOFNFyAhnON-ge60Q8PM9zZD2SHvAlDvI&_nc_ohc=DR0Ml6FO4f8AX-VXlF8&_nc_ht=scontent.ftij2-1.fna&oh=fd61350e5fa53376f78636de8b2311cd&oe=60518859",
        28,
        4
    ),
    Card(
        "I am Paris",
        "https://media.discordapp.net/attachments/807408559235137536/809572589415563274/image.png?width=400&height=484",
        29,
        1
    ),
    Card(
        "One Piece",
        "https://media.discordapp.net/attachments/807414009338527774/808223769092948008/image0.jpg?width=660&height=484",
        30,
        1
    ),
    Card(
        "Shot on Mi 9 Triple AI Camera",
        "https://media.discordapp.net/attachments/807397347566551070/809895217674190878/IMG-20210210-WA0016.jpg?width=860&height=484",
        31,
        3
    ),
    Card(
        "Buki Galletas",
        "https://media.discordapp.net/attachments/807397347566551070/809895272024768512/IMG_20210210_225830361.jpg?width=363&height=484",
        32,
        1
    ),
    Card(
        "Gay Temple",
        "https://media.discordapp.net/attachments/807401302627582002/807413723488321536/gaytemple.png?width=484&height=484",
        33,
        5
    ),
    Card(
        "Jose",
        "https://media.discordapp.net/attachments/810942575154036776/811662867966722098/149449228_3628706870573292_5698232597926803450_n.png?width=284&height=505",
        34,
        3
    ),
    Card(
        "Hans Guapeton",
        "https://media.discordapp.net/attachments/809606599064420433/811672165095178250/image0.png?width=284&height=505",
        35,
        4
    ),
    Card(
        "Hans dormido",
        "https://media.discordapp.net/attachments/809606599064420433/811672536106532874/image0.jpg?width=379&height=505",
        36,
        4
    ),
    Card(
        "Pabel calvo",
        "https://media.discordapp.net/attachments/809606599064420433/811672709742067763/image0.jpg?width=478&height=505",
        37,
        5
    ),
    Card(
        "Jose cocainomano   ",
        "https://media.discordapp.net/attachments/809606599064420433/811673143953195078/image0.jpg",
        38,
        2
    ),
    Card(
        "Naki Guitar",
        "https://i.imgur.com/mebMzx5.jpg",
        39,
        5
    ),







  

]


def getRandomCard():
    index = random.randint(0, len(cards) - 1)
    return cards[index].name, cards[index].link, cards[index].id, cards[index].rareza
