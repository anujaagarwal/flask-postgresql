from app import app
import controllers

app.add_url_rule('/signup', 'signup', controllers.signup, methods=['POST'])
app.add_url_rule('/login', 'login', controllers.login, methods=['POST'])
app.add_url_rule('/protected', 'protected', controllers.protected, methods=['GET'])


