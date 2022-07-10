import base64
from typing import Union

class PayloadData:

    def __init__(self, *args, **kwargs) -> None:
        kwargs['image'] = ImageData(kwargs['image']).content
        self.payload : dict = kwargs

class ImageData:

    def __init__(self, content : Union[str, bytes]) -> None:
        self.content = content
        if type(content) == bytes:
            self.content = base64.b64encode(content)
            self.content = self.content.decode('utf-8')
        self.type = type(content)