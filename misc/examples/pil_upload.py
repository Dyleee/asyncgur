from io import BytesIO
from asyncgur import Imgur
from PIL import Image

import numpy
import asyncio

imgur_app = Imgur(CLIENT_ID)

async def main():
    imarray = numpy.random.rand(100,100,3) * 255
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA') # Generate a random image
    image_bytes = BytesIO()
    im.save(image_bytes, 'PNG') # Save the image to a BytesIO object
    x =  image_bytes.getvalue() # Get the bytes of the image
    image, response = await imgur_app.upload_image(image=x)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())