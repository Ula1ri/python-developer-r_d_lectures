import logging
from flask import Flask

app = Flask(__name__)

# Налаштування логування
logging.basicConfig(filename='flask.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

# Ендпоінт "hello"
@app.route('/hello')
def hello():
    app.logger.info('Hello endpoint was reached')
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()