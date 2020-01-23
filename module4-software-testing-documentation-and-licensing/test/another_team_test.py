# to be recognized by pytest the file must be something '_test.py'

from app.class_from_class import Team

def test_example():
    team = Team('New York', 'Giants', [])
    assert team.full_name == 'New York Giants'
    