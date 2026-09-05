"""
The main app.py for Antioch Spell API
"""

import json
import os
import re
from pathlib import Path

from flask import Flask, abort, jsonify

import caveats as caveats_module

app = Flask(__name__)

caveats = caveats_module.caveats


def load_spells_from_json():
    """Load spells from the generated JSON file and normalize them for the API."""
    data_dir = Path(__file__).resolve().parent
    json_path = data_dir / 'spells.json'

    if not json_path.exists():
        return []

    with json_path.open('r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    normalized = []
    for spell in data.get('spells', []):
        item = dict(spell)
        metadata = item.pop('metadata', {})
        if isinstance(metadata, dict):
            item.update(metadata)

        circle_value = item.get('circle')
        if isinstance(circle_value, str):
            match = re.search(r'(\d+)', circle_value)
            if match:
                item['circle'] = int(match.group(1))

        normalized.append(item)

    return normalized


spells = load_spells_from_json()

@app.route('/')
def get_root():
    """Return the root endpoint with a status"""
    return 'Hello, Mortal! Try <a>http://127.0.0.1:5000/antioch/api/v1.0/spells</a>'

@app.route('/antioch/api/v1.0/version', methods=['GET'])
def get_version():
    """Gets the current version of the Realms Omnibus supported"""
    return {'version': '2026 Omnibus of the Realms'}

@app.route('/antioch/api/v1.0/spells', methods=['GET'])
def get_all_spells():
    """Gets all spells"""
    return jsonify({'spells': spells})

@app.route('/antioch/api/v1.0/spell/<string:spell_name>', methods=['GET'])
def get_spells_by_name(spell_name):
    """
    Gets a spell by name
    spell_name - string
    """
    if spell_name == '':
        abort(404, 'No name provided')
    spell = [spell for spell in spells if spell['name'].lower() == spell_name.lower()]
    if len(spell) == 0:
        abort(404, 'Invalid name')
    return jsonify({'spells': spell[0]})

@app.route('/antioch/api/v1.0/spells_by_circle/<int:circle>', methods=['GET'])
def get_spell_by_circle(circle):
    """
    Returns all spell names by circle
    circle - integer
    """
    spell = [spell for spell in spells if spell.get('circle') == circle]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': [s['name'] for s in spell]})

@app.route('/antioch/api/v1.0/caveats', methods=['GET'])
def get_all_caveats():
    """Returns all spell caveats"""
    return jsonify({'caveats': caveats})

@app.route('/antioch/api/v1.0/caveat_by_name/<string:caveat_name>', methods=['GET'])
def get_caveat_by_name(caveat_name):
    """
    Searches for a spell caveat by name
    caveat_name - string
    """
    spell = [caveat for caveat in caveats if caveat['name'] == caveat_name]
    if len(spell) == 0:
        abort(404)
    return jsonify({'caveats': spell[0]})

@app.route('/antioch/api/v1.0/spell_caveats/<string:spell_name>', methods=['GET'])
def get_caveats_for_spell(spell_name):
    """
    Looks up the caveats for a particular spell
    spell_name - string
    """
    spell = [spell for spell in spells if spell['name'].lower() == spell_name.lower()]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': spell[0]["caveats"]})

if __name__ == '__main__':
    port = int(os.getenv("PORT", "5000"))
    app.run(port=port, host='0.0.0.0')
    