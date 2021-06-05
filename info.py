from flask import Flask, Response
import sys
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__) #instancia



@app.route('/', methods=['GET'])
def home_page ():
    print('Hello word - normal')
    print('Hello word - sys.stderr', file=sys.stderr)
    app.logger.info('Hello word - app.logger.info')
    return Response('test', status=200, mimetype='text/html')


if __name__ == '__main__':
    app.run(port=5000)