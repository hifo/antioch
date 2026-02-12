"""
The main app.py for Antioch Spell API
"""

import os
from flask import Flask, jsonify, abort
import spells_a_through_c
import spells_d_through_f
import spells_g_through_l
import spells_m_through_p
import spells_r_through_z
import caveats

app = Flask(__name__)

caveats = caveats.caveats
# concatonates all spells from various files
spells = spells_a_through_c.spells + spells_d_through_f.spells + \
      spells_g_through_l.spells + spells_m_through_p.spells + spells_r_through_z.spells

@app.route('/')
def get_root():
    """Return the root endpoint with a status"""
    return 'Hello, Mortal! Try <a>http://127.0.0.1:5000/antioch/api/v1.0/spells</a>'

@app.route('/antioch/api/v1.0/version', methods=['GET'])
def get_version():
    """Gets the current version of the Realms Omnibus supported"""
    return {'version': '2025 Omnibus of the Realms'}

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
    spell = [spell for spell in spells if spell['name'] == spell_name]
    if len(spell) == 0:
        abort(404, 'Invalid name')
    return jsonify({'spells': spell[0]})

@app.route('/antioch/api/v1.0/spells_by_circle/<int:circle>', methods=['GET'])
def get_spell_by_circle(circle):
    """
    Returns all spells by circle
    circle - integer
    """
    spell = [spell for spell in spells if spell['circle'] == circle]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': spell})

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
    spell = [spell for spell in spells if spell['name'] == spell_name]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': spell[0]["caveats"]})

if __name__ == '__main__':
    app.run(port=os.getenv("PORT"), host='0.0.0.0')
    