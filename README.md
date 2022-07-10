[![](https://img.shields.io/pypi/v/asyncgur.svg)](https://pypi.org/project/asyncgur/) [![](https://img.shields.io/pypi/dm/asyncgur.svg?style=plastic)](https://pypi.org/project/asyncgur/) [![](https://img.shields.io/github/license/Dyleee/asyncgur.svg?style=plastic)](https://pypi.org/project/asyncgur/) [![](https://img.shields.io/github/stars/Dyleee/asyncgur.svg?style=plastic)](https://pypi.org/project/asyncgur/)

# asyncgur

> An Asynchronous Imgur Wrapper for Python


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
```

> See misc/examples for more usecases.