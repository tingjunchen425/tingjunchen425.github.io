import asyncio
import aiohttp
import os

urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/WebCrawlerArchitecture.svg/220px-WebCrawlerArchitecture.svg.png",
    "https://www.cloudflare.com/resources/images/slt3lc6tev37/7G1pGDcm2zBHK11Y8frz3m/34d9963332f3cd59abc02cf665b34730/what-is-web-crawler-spider-bot.png",
    "https://i.imgur.com/A8hQuVY.png",
    "https://i.imgur.com/ubBkkM4.png",
    "https://i.imgur.com/ubBkkM4.png"
]

async def getPicture(url,name,path):
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            picture = await resp.content.read()
            tasks.append(asyncio.create_task(output(picture,name,path)))
            await asyncio.wait(tasks)

async def output(picture,name,path):
    with open(f"{path}/{name}", mode="wb") as f:
        f.write(picture)
        print(f"{name} output success")

async def main(urls):
    path = "./pictures"
    if not os.path.exists(path):
        os.makedirs(path)
    tasks = []
    for url in urls:
        name = url.split('/')[-1]
        tasks.append(asyncio.create_task(getPicture(url,name,path)))
    await asyncio.wait(tasks)

asyncio.run(main(urls=urls))