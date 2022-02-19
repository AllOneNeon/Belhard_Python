from unittest import TestCase
import os
from pathlib import Path

import pytest

path = '.\direct'
list_of_files = list(sorted(os.listdir(path)))
print(list_of_files)
for file in list_of_files:
    fold1 = (file.split('-')[0])
    fold2 = (file.split('-')[1])
    fl = (file.split('-')[2])
    Path(f'direct/{fold1}/{fold2}/').mkdir(parents=True, exist_ok=True)
    path1 = f'.\direct/{file}'
    path2 = f'.\direct{fold1}/{fold2}/{fl}'

    os.replace(path1, path2)

