from flask import Flask, jsonify, request
from datastructures import Family

app = Flask(__name__)

# Instancia de la familia
jackson_family = Family("Jackson")

@app.route('/')
def home():
    return jsonify({"message": "API de Familia funcionando"}), 200

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(jackson_family.get_all_members()), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"error": "Miembro no encontrado"}), 404

@app.route('/member', methods=['POST'])
def add_member():
    member_data = request.get_json()
    jackson_family.add_member(member_data)
    return jsonify({"message": "Miembro agregado"}), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({"done": True}), 200
    return jsonify({"error": "Miembro no encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
