from flask import Flask, request, jsonify, render_template
from service import create_item, get_items, update_item, delete_item

app = Flask(__name__)

# ✅ HOME
@app.route("/")
def home():
    return render_template("index.html")


# ✅ CREATE
@app.route("/items", methods=["POST"])
def create():
    data = request.get_json()

    name = data.get("name")
    stock = data.get("stock")
    price = data.get("price")

    item, err = create_item(name, stock, price)  # ✅ FIX

    if err:
        return jsonify({"error": err}), 400

    return jsonify(item), 201


# ✅ GET ALL
@app.route("/items", methods=["GET"])
def get_all():
    items = get_items()
    return jsonify(items), 200


# ✅ UPDATE
@app.route("/items/<int:id>", methods=["PUT"])
def update(id):
    data = request.get_json()

    item, err = update_item(id, data.get("stock"))

    if err == "Not found":
        return jsonify({"error": err}), 404

    if err:
        return jsonify({"error": err}), 400

    return jsonify(item), 200


# ✅ DELETE
@app.route("/items/<int:id>", methods=["DELETE"])
def delete(id):
    success, err = delete_item(id)

    if not success:
        return jsonify({"error": err}), 404

    return jsonify({"message": "Deleted"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)