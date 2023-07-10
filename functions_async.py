import aiohttp
from bs4 import BeautifulSoup
import requests

async def getBrazilAddress(cep):
    url = f'http://viacep.com.br/ws/{str(cep)}/json/'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                logradouro = data['logradouro']
                bairro = data['bairro']
                cidade = data['localidade']
                estado = data['uf']
                frase = f'O cep "{cep}" corresponde a {logradouro}, do bairro {bairro}, em {cidade}/{estado}.'
    except:
        frase = 'CEP inválido ou inexistente.'

    return frase

async def getPokemonInfo(pokemon_name):
    url = f'https://pokeapi.glitch.me/v1/pokemon/{pokemon_name}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                poketype = data[0]['types']
                poketype_phrase = ", ".join(poketype)
                abilities_data = data[0]['abilities']
                abilities_list = [f'{abilities[0]}({ability_type})' for ability_type, abilities in abilities_data.items()]
                abilities_phrase = ", ".join(abilities_list)
                evolution_line = data[0]['family']['evolutionLine']
                evolution_line_phrase = ", ".join(evolution_line)
                phrase = f'{pokemon_name.capitalize()} is {poketype_phrase} type and these are its abilities: {abilities_phrase}. The evolutions of this Pokemon are respectively: {evolution_line_phrase}.'
    except:
        phrase = 'Invalid Input'
    return phrase

async def getHolidays(api_key, country, year, month, day):
    url = f'https://holidays.abstractapi.com/v1/?api_key={api_key}&country={country}&year={year}&month={month}&day={day}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                holiday_type = data[0]['type']
                name = data[0]['name']
                location = data[0]['location']
                phrase = f'In the chosen country({country}) it is a {holiday_type} and its name is {name} and it is a holiday in the following states: {location}'
    except:
        phrase = 'Invalid Input'
    return phrase

async def getCurrencyPrice(currency1, currency2):
    currencys = currency1 + '-' + currency2
    url = f'https://economia.awesomeapi.com.br/last/{currencys}'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                bid = data[currency1 + currency2]['bid']
                phrase = f'{currency1} price is: {bid} {currency2}'
    except:
        phrase = 'Invalid Input'
    return phrase

async def getChuckNorrisJoke():
    url = 'https://api.chucknorris.io/jokes/random'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                joke = data['value']
                phrase = f"Here's a random Chuck Norris joke: {joke}"
    except:
        phrase = 'Invalid Input'
    return phrase

async def globoMainPage():
    url = "https://www.globo.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(class_="post__title").get_text()
    title = title.strip()
    title = (f'The main GLOBO NEWS is: {title}')
    print (title)

    return title

async def cnnBrasilMainPage():
    url = "https://www.cnnbrasil.com.br/"
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    title = soup.find('h2', attrs={'class': 'home__title headline__primary_title'}).get_text()
    title = title.strip()
    title = (f'The main CNN BRASIL NEWS is: {title}')
    print (title)

    return title

async def uolMainPage():
    url = "https://noticias.uol.com.br/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find('h2').get_text()
    title = title.strip()
    title = (f'The main UOL NEWS is: {title}')
    print (title)

    return title

async def estadaoMainPage():
    url = "https://www.estadao.com.br/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find('h2', attrs={'class': 'headline'}).get_text()
    title = title.strip()
    title = (f'The main ESTADAO NEWS is: {title}')
    print (title)

    return title

async def r7MainPage():
    url = "https://www.r7.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    title_element = soup.find('a', attrs={'class': 'r7-flex-title-h1__link'}).get_text()
    title = title_element.strip()
    title = (f'The main R7 NEWS is: {title}')
    print (title)

    return title