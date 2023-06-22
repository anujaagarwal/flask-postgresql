

# Basic Server Documentation

This documentation provides an overview and usage instructions for the basic server implementation that includes a signup page, login functionality, and protected endpoints.

## Requirements

To run the server, ensure you have the following:

- Python 3.x installed on your machine
- Required Python packages installed: Flask, psycopg2, passlib

## Installation

1. Clone the repository or download the source code files.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required Python packages by running the following command:

```shell
pip install flask psycopg2 passlib
```

## Configuration

Before running the server, make sure to configure the PostgreSQL database connection details. Open the `server.py` file in a text editor and update the following lines with your specific configuration:

```python
# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_username",
    password="your_password"
)
```

## Usage

1. Start the server by running the following command in the terminal or command prompt:

```shell
python server.py
```

The server will start running on the default port `5000`.

2. Signup:

- Send a `POST` request to `http://localhost:5000/signup` with the following JSON payload:

```json
{
  "nickname": "your_nickname",
  "password": "your_password"
}
```

Replace `your_nickname` with the desired nickname and `your_password` with the desired password.

- If the signup is successful, you will receive a response with a status code of `201` and a JSON message: `{"message": "Signup successful."}`.

- If the nickname is already taken, you will receive a response with a status code of `400` and a JSON message: `{"message": "Nickname is already taken."}`.

3. Login:

- Send a `POST` request to `http://localhost:5000/login` with the following JSON payload:

```json
{
  "nickname": "your_nickname",
  "password": "your_password"
}
```

Replace `your_nickname` and `your_password` with the credentials you used during the signup.

- If the login is successful, you will receive a response with a status code of `200` and a JSON message: `{"message": "Login successful."}`.

- If the login fails (incorrect nickname or password), you will receive a response with a status code of `401` and a JSON message: `{"message": "Invalid nickname or password."}`.

4. Protected Endpoint:

- To access the protected endpoint, send a `GET` request to `http://localhost:5000/protected`.

- If the request is authenticated (successful login), you will receive a response with a status code of `200` and a JSON message: `{"message": "Protected endpoint accessed successfully."}`.

- If the request is not authenticated (no login or expired session), you will receive a response with a status code of `401` and a JSON message: `{"message": "Unauthorized access."}`.

## Conclusion

This documentation provides an overview of the basic server implementation and instructions for using the signup, login, and protected endpoints. Feel free to modify and extend the code to fit your specific requirements and add additional security measures as needed.
