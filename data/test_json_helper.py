import json
import unittest 
import pickle
import os
from json_helper import read_all_json_files, read_json, write_pickle, load_pickle


class TestJsonHelper(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'data.super_smash_bros'
        self.test_json_file = os.path.join(self.test_dir, 'mario.json')
        self.test_pickle_file = os.path.join(self.test_dir, 'super_smash_characters.pickle')

    
    def test_read_json_files(self):
        data = read_json(self.test_json_file)
        expected = {
            "name": "Mario",
            "neutral_special": "Fireball",
            "side_special": "Cape",
            "up_special": "Super Jump Punch",
            "down_special": "F.L.U.D.D.",
            "final_smash": "Mario Finale"
        }
        self.assertEqual(data, expected)

    def test_read_all_json_files(self):
        data = read_all_json_files(self.test_dir)
        expected = [
            {
                "name": "Mario",
                "neutral_special": "Fireball",
                "side_special": "Cape",
                "up_special": "Super Jump Punch",
                "down_special": "F.L.U.D.D.",
                "final_smash": "Mario Finale"
            },{
                "name": "Link",
                "neutral_special": "Bow and Arrows",
                "side_special": " Boomerang",
                "up_special": " Spin Attack",
                "down_special": "Remote Bomb",
                "final_smash": "Ancient Bow and Arrow"
            }
        ]
        self.assertEqual(data, expected)

    def test_write_pickle(self):
        data_to_pickle = [
            {
                "name": "Mario",
                "neutral_special": "Fireball",
                "side_special": "Cape",
                "up_special": "Super Jump Punch",
                "down_special": "F.L.U.D.D.",
                "final_smash": "Mario Finale"
            },{
                "name": "Link",
                "neutral_special": "Bow and Arrows",
                "side_special": " Boomerang",
                "up_special": " Spin Attack",
                "down_special": "Remote Bomb",
                "final_smash": "Ancient Bow and Arrow"
            }
        ]
        write_pickle(self.test_dir, data_to_pickle)
        self.assertTrue(os.path.exists(self.test_pickle_file))

        with open(self.test_pickle_file, 'rb') as file:
            pickle.dump(data_to_pickle, file)

        data = load_pickle(self.test_pickle_file)
        self.assertEqual(data, data_to_pickle)


    if __name__ == '__main__':
        unittest.main()