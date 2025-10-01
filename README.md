# Secure User Authentication System

## About
This project implements a Secure User Authentication System aimed at providing secure and reliable user registration and login functionality for web applications. It is built using Python for backend logic and HTML for the front-end interface.

## Features
- User registration with securely hashed password storage
- User login with authentication and validation
- Simple and clean interface using HTML
- Emphasis on security best practices in user authentication

## Technologies Used
- Python (Backend logic and authentication)
- Flask (Web framework for routing and HTTP handling)
- bcrypt (Password hashing and security)
- MySQL (Relational database for user data)
- MongoDB (NoSQL database for logging and analytics)
- HTML (User interface and frontend)

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ChiragMenariyaCJ/Secure-User-Authentication-System.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Secure-User-Authentication-System
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\\Scripts\\activate
   ```
4. Install required dependencies:
   ```bash
   pip install flask flask-mysqldb pymongo bcrypt python-dotenv
   ```
5. Run the main Python application:
   ```bash
   python app.py
   ```

## Usage
- Open the application in your web browser.
- Register a new account.
- Log in with your registered credentials to access protected functionality.

## Contributing
Contributions are welcome! Feel free to fork the repo and submit pull requests for bug fixes, improvements, or new features.

## License
This project is licensed under the [MIT License](LICENSE).