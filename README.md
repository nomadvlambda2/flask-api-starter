# Flask API Starter Demo

This mini-project demonstrates a simple Flask API with GET and POST endpoints for users.

## Description
- **app.py**: Flask app with /api/users endpoint.
- **requirements.txt**: Dependencies for Flask.

## Instructions
1. Install Flask: `pip install -r requirements.txt`.
2. Run: `python app.py`.
3. Test GET: curl http://localhost:5000/api/users
4. Test POST: curl -X POST -H "Content-Type: application/json" -d '{"name": "New User"}' http://localhost:5000/api/users

Extend this by adding database, authentication, or Dockerizing.