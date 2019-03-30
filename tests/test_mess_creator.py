import os

from mess_creator import MessCreator


class TestMessCreator:

    def setup_method(self, method):
        self.MessCreator = MessCreator()

    def test_mess_creator_can_get_home_dir(self):
        home = os.path.expanduser('~')
        assert self.MessCreator.home == home
