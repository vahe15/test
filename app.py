from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    user = {'username': 'Vahe'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

