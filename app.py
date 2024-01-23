from flask import Flask, jsonify, abort
import data

app = Flask(__name__)

caveats = data.caveats
spells = data.spells

@app.route('/antioch/api/v1.0/spells', methods=['GET'])
def get_all_spells():
    return jsonify({'spells': spells})

@app.route('/antioch/api/v1.0/caveats', methods=['GET'])
def get_all_caveats():
    return jsonify({'caveats': caveats})

@app.route('/antioch/api/v1.0/spell/<string:spell_name>', methods=['GET'])
def get_spells_by_circle(spell_name):
    spell = [spell for spell in spells if spell['name'] == spell_name]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': spell[0]})

@app.route('/antioch/api/v1.0/spell_by_circle/<int:circle>', methods=['GET'])
def get_spell(circle):
    spell = [spell for spell in spells if spell['circle'] == circle]
    if len(spell) == 0:
        abort(404)
    return jsonify({'spells': spell[0]})

if __name__ == '__main__':
    app.run(port=os.getenv("PORT", default=5000, host='0.0.0.0'))