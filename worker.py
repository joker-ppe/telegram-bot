import requests
import aiohttp
import asyncio
from cloudscraper import CloudScraper
from bs4 import BeautifulSoup

from style import get_style

baseUrl = "http://3.1.5.108"


# baseUrl = "https://api.winwwin68.com"
# baseUrl = "http://localhost:3004"


async def fetch_url(session, url):
    print(url)
    async with session.get(url, ssl=False) as response:
        if response.status == 200:
            return await response.json()
        else:
            return ''


async def get_user(from_date, end_date, yesterday, user_name):
    url = f'{baseUrl}/report/user?startDate={from_date}&endDate={end_date}&yesterday={yesterday}&userName={user_name}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_user_tet(user_name):
    url = f'{baseUrl}/report/user/tet?userName={user_name}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_user_last_week(user_name):
    url = f'{baseUrl}/report/userLastWeek?userName={user_name}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_report_super(end_date, nick_name, is_last_week):
    url = f'{baseUrl}/report/nickName?endDate={end_date}&nickName={nick_name.lower()}&isLastWeek={is_last_week}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_report_super_tet(end_date, nick_name):
    url = f'{baseUrl}/report/nickName/tet?endDate={end_date}&nickName={nick_name.lower()}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_list_report_info(end_date):
    url = f'{baseUrl}/report/listReportInfo?endDate={end_date}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_user_data(from_date, end_date, user_name, filter='profit'):
    url = f'{baseUrl}/report?startDate={from_date}&endDate={end_date}&userName={user_name}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response[filter]
        # print(response)


async def get_report_number(end_date):
    url = f'{baseUrl}/report/numbers?endDate={end_date}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_user_os_bet(end_date, user_name):
    url = f'{baseUrl}/report/user/os_bet?endDate={end_date}&userName={user_name}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def check_user_os_bet(end_date, data):
    url = f'{baseUrl}/report/user/check_os_bet?endDate={end_date}&numbers={data.numbers}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_user_os_number(end_date, user_name):
    url = f'{baseUrl}/report/user/os_number?endDate={end_date}&userName={user_name}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        if len(response) == 0:
            return '***'
        return response


async def get_user_profit(from_date, end_date, user_name):
    response = await get_user_data(from_date, end_date, user_name, filter='profit')
    return response


async def get_user_os(from_date, end_date, user_name):
    response = await get_user_data(from_date, end_date, user_name, filter='outstanding')
    return response


async def get_report_xsmb():
    url = 'https://xoso.com.vn/'
    scraper = CloudScraper()
    response = scraper.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    table = soup.find_all(attrs={'class': 'table-result table-xsmb'})[0]

    table_loto = soup.find_all(attrs={'class': 'table-loto'})[0]

    html_table = "<html><body>"
    html_table += get_style()
    html_table += table.prettify()
    html_table += table_loto.prettify()
    html_table += "</body></html>"
    return html_table


async def get_user_outside_bid(from_date, end_date):
    url = f'{baseUrl}/report/bidOutside?startDate={from_date}&endDate={end_date}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        # print(response)
        if len(response) == 0:
            return '***'
        return int(response['outsideBid']) * (-1)


async def get_supers(from_date, end_date):
    url = f'{baseUrl}/report/supers?startDate={from_date}&endDate={end_date}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        # print(response)
        if len(response) == 0:
            return '***'
        return response


async def get_masters(from_date, end_date):
    url = f'{baseUrl}/report/masters?startDate={from_date}&endDate={end_date}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        # print(response)
        if len(response) == 0:
            return '***'
        return response


async def get_agents(from_date, end_date):
    url = f'{baseUrl}/report/agents?startDate={from_date}&endDate={end_date}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        # print(response)
        if len(response) == 0:
            return '***'
        return response


async def get_members(from_date, end_date):
    url = f'{baseUrl}/report/members?startDate={from_date}&endDate={end_date}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        # print(response)
        if len(response) == 0:
            return '***'
        return response


async def get_members_inactive(from_date, end_date):
    url = f'{baseUrl}/report/membersInactive?startDate={from_date}&endDate={end_date}'
    async with aiohttp.ClientSession() as session:
        response = await fetch_url(session, url)
        # print(response)
        if len(response) == 0:
            return '***'
        return response
