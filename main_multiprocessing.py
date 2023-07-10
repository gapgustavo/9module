import multiprocessing
import time
from functions_multiprocessing import *

if __name__ == '__main__':
    start_time = time.time()

    processes = [
        multiprocessing.Process(target=get_brazil_address, args=('38407754',)),
        multiprocessing.Process(target=get_pokemon_info, args=('pikachu',)),
        multiprocessing.Process(target=get_holidays, args=("api_key", "US", "2023", "12", "25")),
        multiprocessing.Process(target=get_currency_price, args=("USD", "BRL")),
        multiprocessing.Process(target=get_chuck_norris_joke),
        multiprocessing.Process(target=globo_main_page),
        multiprocessing.Process(target=cnnbrasil_main_page),
        multiprocessing.Process(target=uol_main_page),
        multiprocessing.Process(target=estadao_main_page),
        multiprocessing.Process(target=r7_main_page)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total MULTIPROCESSING execution time: {execution_time} seconds.")
