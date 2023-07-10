import requests
from bs4 import BeautifulSoup

def get_brazil_address(cep):
    url = f'http://viacep.com.br/ws/{str(cep)}/json/'
    try:
        response = requests.get(url)
        data = response.json()
        logradouro = data['logradouro']
        bairro = data['bairro']
        cidade = data['localidade']
        estado = data['uf']
        phrase = f'O cep "{cep}" corresponde a {logradouro}, do bairro {bairro}, em {cidade}/{estado}.'
    except:
        phrase = 'CEP inválido ou inexistente.[get_brazil_address]'

    print (phrase)
    return phrase

def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.glitch.me/v1/pokemon/{str(pokemon_name)}'
    try:
        response = requests.get(url)
        data = response.json()
        poketype = data[0]['types']
        poketype_phrase = ", ".join(poketype)
        abilities_data = data[0]['abilities']
        abilities_list = [f'{abilities[0]}({ability_type})' for ability_type, abilities in abilities_data.items()]
        abilities_phrase = ", ".join(abilities_list)
        evolution_line = data[0]['family']['evolutionLine']
        evolution_line_phrase = ", ".join(evolution_line)
        phrase = f'{pokemon_name.capitalize()} is {poketype_phrase} type and these are its abilities: {abilities_phrase}. The evolutions of this Pokemon are respectively: {evolution_line_phrase}.'
    except:
        phrase = 'Invalid Input[get_pokemon_info]'

    print (phrase)
    return phrase

def get_holidays(api_key, country, year, month, day):
    url = f'https://holidays.abstractapi.com/v1/?api_key={api_key}&country={country}&year={year}&month={month}&day={day}'
    try:
        response = requests.get(url)
        data = response.json()
        holiday_type = data[0]['type']
        name = data[0]['name']
        location = data[0]['location']
        phrase = f'In the chosen country({country}) it is a {holiday_type} and its name is {name} and it is a holiday in the following states: {location}'
    except:
        phrase = 'Invalid Input.[get_holidays]'

    print (phrase)
    return phrase

def get_currency_price(currency1, currency2):
    currencys = currency1 + '-' + currency2
    url = f'https://economia.awesomeapi.com.br/last/{currencys}'
    try:
        response = requests.get(url)
        data = response.json()
        bid = data[currency1 + currency2]['bid']
        phrase = f'{currency1} price is: {bid} {currency2}'
    except:
        phrase = 'Invalid Input[get_currency_price]'

    print (phrase)
    return phrase

def get_chuck_norris_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    try:
        response = requests.get(url)
        data = response.json()
        joke = data['value']
        phrase = f"Here's a random Chuck Norris joke: {joke}"
    except:
        phrase = 'Invalid Input[get_chuck_norris_joke]'
        
    print (phrase)
    return phrase

def globo_main_page():
    url = "https://www.globo.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(class_="post__title").get_text()
    title = title.strip()
    title = (f'The main GLOBO NEWS is: {title}')
    print (title)

    return title

def cnnbrasil_main_page():
    url = "https://www.cnnbrasil.com.br/"
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    title = soup.find('h2', attrs={'class': 'home__title headline__primary_title'}).get_text()
    title = title.strip()
    title = (f'The main CNN BRASIL NEWS is: {title}')
    print (title)

    return title

def uol_main_page():
    url = "https://noticias.uol.com.br/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find('h2').get_text()
    title = title.strip()
    title = (f'The main UOL NEWS is: {title}')
    print (title)

    return title

def estadao_main_page():
    url = "https://www.estadao.com.br/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find('h2', attrs={'class': 'headline'}).get_text()
    title = title.strip()
    title = (f'The main ESTADAO NEWS is: {title}')
    print (title)

    return title

def r7_main_page():
    url = "https://www.r7.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    title_element = soup.find('a', attrs={'class': 'r7-flex-title-h1__link'}).get_text()
    title = title_element.strip()
    title = (f'The main R7 NEWS is: {title}')
    print (title)

    return title

