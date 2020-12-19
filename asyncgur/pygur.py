import json
import asyncio
from typing import Any
from dataclasses import dataclass

import dacite
import aiohttp

@dataclass
class Image_info:
    id: str
    name: Any
    description: Any
    datetime: Any
    type: Any
    animated: Any
    width: Any
    height: Any
    size: Any
    views: Any
    bandwidth: Any
    vote: Any
    favorite: Any
    nsfw: Any
    section: Any
    account_url: Any
    account_id: Any
    is_ad: Any
    in_most_viral: Any
    has_sound: Any
    tags: Any
    ad_type: Any
    ad_url: Any
    edited: Any
    in_gallery: Any
    deletehash: Any
    name: Any
    link: Any


@dataclass
class Response:
    success: Any
    status: Any
    data: dict


class Imgur:
    def __init__(self, client_id):
        self.client_id = client_id
        self.headers = {
            'Authorization' : f'Client-ID {self.client_id}'
        }

    async def get_request(self, url, payload=None):
        async with aiohttp.request('get', url, headers=self.headers, data=payload) as resp:
            resp.raise_for_status
            return json.loads(await resp.text())

    async def post_request(self, url, payload):
        async with aiohttp.request('post', url, headers=self.headers, data=payload) as resp:
            resp.raise_for_status
            return json.loads(await resp.text())

    async def get_image(self, image_hash):
        response = await self.get_request(f'https://api.imgur.com/3/image/{image_hash}')
        return response

    async def upload_image(self, title=None, description=None, name=None, image=None, video=None):
        payload = {
            'title': title,
            'description': description,
            'name': name,
            'image': image,
            'video': video
        }

        response = await self.post_request(f'https://api.imgur.com/3/image', payload)
        image_data = dacite.from_dict(data_class=Image_info, data=response['data'])
        api_response = dacite.from_dict(data_class=Response, data=response)
        return image_data, api_response
