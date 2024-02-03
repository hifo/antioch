import app
from flask import jsonify

def test_get_root():
    result = app.get_root()
    assert result == 'Hello, Mortal! Try <a>http://127.0.0.1:5000/antioch/api/v1.0/spells</a>'

def test_get_version():
    result = app.get_version()
    assert result['version'] == '2023 Omnibus of the Realms'