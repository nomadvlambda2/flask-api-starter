from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
  {"id": 1, "name": "Alice"},
  {"id": 2, "name": "Bob"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
  return jsonify(users)

@app.route('/api/users', methods=['POST'])
def add_user():
  new_user = {"id": len(users) + 1, "name": request.json["name"]}
  users.append(new_user)
  return jsonify(new_user), 201

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)