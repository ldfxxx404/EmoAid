from random import choice

pictures_url = [
    "https://img1.akspic.ru/crops/5/7/0/7/47075/47075-lavanda-video-purpur-pole-tsvetok-2560x1440.jpg",
    "https://img.freepik.com/free-photo/sunset-water_23-2151989512.jpg",
    "https://img.freepik.com/free-photo/violet-sunset_1361-153.jpg",
    "https://wallpapers.com/images/hd/lime-green-aesthetic-2880-x-1800-oigtaysh0gk0bjer.jpg",
]


def choice_rand_picture():
    return choice(pictures_url)
