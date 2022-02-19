from pathlib import *
from random import randint


Path('direct').mkdir(exist_ok=True)
for i in range (10):
    Path( f'direct/'
          f'{randint(2020, 2022)}-'
          f'{randint(1, 12)}-'
          f'{randint(1, 31)}.txt'
    ).touch()