# Objectives:
#
# make sure that the team class' .full_name method behaves as desired
# make sure that we can initialize or instantiate the team class

import unittest

from app.class_from_class import Team
# from app.team import Team

class TestTeams(unittest.TestCase):

    def test_full_name(self):
        team = Team('New York', 'Giants', [])
        self.assertEqual(team.full_name, 'New York Giants')

if __name__ == "__main__":
    unittest.main()
