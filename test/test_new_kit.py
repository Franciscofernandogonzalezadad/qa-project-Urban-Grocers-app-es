import unittest
import configuration
import data


class test_new_kit(unittest.TestCase):
    def test_new_kit(self, status_code=201):
        current_kit_body = data.kit_body1
        current_KITS_PATH = configuration.KITS_PATH
        new_kit = ('kit_body1' + 'KITS_PATH')
        assert status_code == 201

        print(status_code)





