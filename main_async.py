import asyncio
import time
from functions_async import *


async def main():
    # Chamadas assíncronas das funções
    address = await getBrazilAddress('38407754')
    print(address)

    pokemon_info = await getPokemonInfo('pikachu')
    print(pokemon_info)

    holidays = await getHolidays('API_KEY', 'US', '2023', '06', '09') # NEED API KEY
    print(holidays)

    currency_price = await getCurrencyPrice('USD', 'BRL')
    print(currency_price)

    chuck_norris_joke = await getChuckNorrisJoke()
    print(chuck_norris_joke)

    globo_main_page = await globoMainPage()
    print(globo_main_page)

    cnn_main_page = await cnnBrasilMainPage()
    print(cnn_main_page)

    uol_main_page = await uolMainPage()
    print(uol_main_page)

    estadao_main_page = await estadaoMainPage()
    print(estadao_main_page)

    r7_main_page = await r7MainPage()
    print(r7_main_page)

# ASYNC
start_time = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

end_time = time.time()
execution_time = end_time - start_time
print(f"Total ASYNC execution time: {execution_time} seconds.")