"""TEST_CHANGE_ENV.py"""

import os


path = os.getenv('PATH')
print(f'path:{path}')

path_ = path.split(';')
print(f'path_:{path_}')

