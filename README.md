# pygur

> An Asyncio Imgur Wrapper to upload or get an image for Python


*Example Usage:*
`
from pygur import Imgur
client_id = 'YOUR_IMGUR_CLIENT_ID'
app = Imgur(client_id)

async def main():
    image, response = await app.upload_image(image='http://images.mewbot.me/Lychee/uploads/big/e787c2213fd640ea8515b4493f5fc9c4.png')
    assert response.success == True and response.status == 200
    print(image)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())`
