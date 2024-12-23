# login.py

def login(username, password):
    # Simple hardcoded credentials for demonstration
    correct_username = "user"
    correct_password = "pass"

    if username == correct_username and password == correct_password:
        return "Login successful!"
    return "Invalid username or password."
