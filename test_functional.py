"""
E2E Regressions for Antioch
"""

import requests

BASE_URL = 'https://antioch-production.up.railway.app/'

def test_get_root():
    """
    Tests get root
    """

    res = requests.get(BASE_URL, timeout=10000)
    assert res.status_code == 200
    assert res.text == 'Hello, Mortal! Try <a>http://127.0.0.1:5000/antioch/api/v1.0/spells</a>'

def test_get_version():
    """
    Tests get version
    """
    res = requests.get(BASE_URL + 'antioch/api/v1.0/version', timeout=10000)
    assert res.status_code == 200
    data = res.json()
    assert data['version'] == '2025 Omnibus of the Realms'

def test_spells_by_name():
    """
    Tests get version
    """
    res = requests.get(BASE_URL + 'antioch/api/v1.0/spell/cry%20of%20life', timeout=10000)
    assert res.status_code == 200
    data = res.json()
    spell = data["spells"]
    assert spell['name'] == 'cry of life'
    assert spell['circle'] == 6
    assert spell['uses'] == '1'
    assert spell['caveats'] is None
    assert spell['material'] is None
    assert spell['active'] is None
    assert spell['verbal'] == 'All in the sound of my voice, rise and fight'
    cry_desc = (
                "This spell instantly raises all dead characters whose players hear the "
                "verbal. The spell affects all who hear it, including NPCs and "
                "characters fighting against the spellcaster."
            )
    assert spell['description'] == cry_desc

def test_get_spell_no_name_provided():
    """
    Tests the get spell by name route when no name is provided
    """
    res = requests.get(BASE_URL + 'antioch/api/v1.0/spell/', timeout=10000)
    assert res.status_code == 404

def test_get_spell_invalid_name():
    """
    Tests the get spell by name route with an invalid name
    """
    res = requests.get(BASE_URL + 'antioch/api/v1.0/spell/test', timeout=10000)
    assert res.status_code == 404


def test_get_all_spells():
    """
    Tests the all spells route
    """
    res = requests.get(BASE_URL + '/antioch/api/v1.0/spells', timeout=10000)
    assert res.status_code == 200
    data = res.json()
    assert 'spells' in data
    