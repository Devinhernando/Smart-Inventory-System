from flask import Flask, request, jsonify, render_template
import service

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(service.get_items())

@app.route('/api/items', methods=['POST'])
def create():
    data = request.get_json()
    item, err = service.create_item(
        data.get("name"),
        data.get("stock"),
        data.get("price")
    )
    if err:
        return jsonify({"error": err}), 400
    return jsonify(item), 201

@app.route('/api/items/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    item, err = service.update_item(id, data.get("stock"))
    if err:
        return jsonify({"error": err}), 400 if "Invalid" in err else 404
    return jsonify(item)

@app.route('/api/items/<int:id>', methods=['DELETE'])
def delete(id):
    ok, err = service.delete_item(id)
    if not ok:
        return jsonify({"error": err}), 404
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run(debug=True)