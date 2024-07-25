import asyncio

import segno
from urllib.request import urlopen


async def regular(data: str):
    qrcode = segno.make_qr(data)
    qrcode.save(
        f"{data}.png",
        scale=10,
        border=1,
    )
    return f"C:/Users/Asus/PycharmProjects/qr_code_maker_bot/{data}.png"


async def animated(data: str) -> str:
    slts_qrcode = segno.make_qr(data)
    nirvana_url = urlopen("https://giphy.com/gifs/3oEdv1GbekAakxXO8g")
    slts_qrcode.to_artistic(
        background=nirvana_url,
        target=f"{data}.gif",
        scale=10,
    )
    return f"C:/Users/Asus/PycharmProjects/qr_code_maker_bot/{data}.gif"
