import requests
import aiohttp
import asyncio


baseUrl = "http://3.1.5.108:3004"
# baseUrl = "https://api.winwwin68.com"
# baseUrl = "http://localhost:3004"


async def fetch_url(session, url):
    async with session.get(url, ssl=False) as response:
        if response.status == 200:
            return await response.json()
        else:
            return ''
    

async def get_user_data(from_date, end_date, user_code, user_name):
    url = f'{baseUrl}/report?startDate={from_date}&endDate={end_date}&userCode={user_code}&userName={user_name}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if (len(response) == 0):
            return '***'
        return response['profit']
        # print(response)

