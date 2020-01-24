import unittest
from practice2 import Puppy, PUPPIES # Import almost anything from .py script

class TestPuppies(unittest.TestCase):

    def test_MakeUpper(self):

        # pup = random.choice(PUPPIES)
        pedro = Puppy('James', 3) # Pass in same number of arguements as __init__ from 
        self.assertEqual(pedro.make_upper(), 'JAMES') # Must know expected answer

if __name__ == "__main__":
    unittest.main()

# Run practice2_test.py in command-line