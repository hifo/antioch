from flask import Flask, jsonify, abort
import os
import data

app = Flask(__name__)

caveats = data.caveats
spells = data.spells

@app.route('/')
def get_root():
    return 'Hello, Mortal! Try <a>http://127.0.0.1:5000/antioch/api/v1.0/spells</a>'

@app.route('/antioch/api/v1.0/version', methods=['GET'])
def get_version():
    return {'version': '2023 Omnibus of the Realms'}

@app.route('/antioch/api/v1.0/spells', methods=['GET'])
def get_all_spells():
    return jsonify({'spells': spells})

@app.route('/antioch/api/v1.0/caveats', methods=['GET'])
def get_all_caveats():
    return jsonify({'caveats': caveats})

@app.route('/antioch/api/v1.0/spell/<string:spell_name>', methods=['GET'])
def get_spells_by_name(spell_name):
    spell = [spell for spell in spells if spell['name'] == spell_name]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': spell[0]})

@app.route('/antioch/api/v1.0/spell_caveats/<string:spell_name>', methods=['GET'])
def get_caveats_for_spell(spell_name):
    spell = [spell for spell in spells if spell['name'] == spell_name]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': spell[0]["caveats"]})

@app.route('/antioch/api/v1.0/spells_by_circle/<int:circle>', methods=['GET'])
def get_spell_by_circle(circle):
    spell = [spell for spell in spells if spell['circle'] == circle]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': spell})

if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000), host='0.0.0.0')