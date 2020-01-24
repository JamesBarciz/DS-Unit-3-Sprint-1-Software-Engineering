"""
1. Clone sprint file
2. Open text editor
3. mkdir (something) - cd (something) - type nul > filename.py on Windows / touch filename.py with Mac
    -create two files - unit test MUST HAVE ...._test.py in order to run test
4. DO NOT USE SEPARATE DIRECTORY FOR UNIT TEST FILE - Keep on same level/directory
    - eventually they will be in different directories for organizational purposes
5. Make class (class Stats:) etc...
6. To run an entire script in command-line terminal:
    if __name__ == '__main__':
****ASIDE: For sprint:
        A. Create class
        B. Instantiate class
        C. Use class
7. If you are trying to run a script, you run the script with `python run (filename.py)`
8. Import from a script - from (filename) import (class/module/variable) -
9. Create a class called TestSomething(unittest.TestCase):
    A. This class inherits from unittest.TestCase
10. Create a module:
    def test_method(self):
        # instantiate class with a variable
        self.assertSOMETHING(method, answer) # Know the answer ahead of time

    if __name__ == "__main__": # To run test on command-line
        unittest.main()

ITEMS NOT COVERED:
    A. Inheritance
    B. Super
    C. Loops for various items in class

"""