import unittest
from practice import Stats, INPUT

class TestPractice(unittest.TestCase):
    
    def test_meanz(self):
        ed = Stats(INPUT)
        self.assertEqual(ed.meanz(), 3.0)

if __name__ == "__main__":
    unittest.main()
