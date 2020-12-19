[![](https://img.shields.io/pypi/v/asyncgur.svg)](https://pypi.org/project/asyncgur/)

# asyncgur

> An Asynchronous Imgur Wrapper to upload or get an image for Python


*Example Usage:*
```python
from asyncgur import Imgur
client_id = 'YOUR_IMGUR_CLIENT_ID'
imgur_app = Imgur(client_id)

async def main():
    image, response = await imgur_app.upload_image(image='some_image_url_or_bytes')
    assert response.success == True and response.status == 200
    print(image)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
