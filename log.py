from flask import Flask
from logging import FileHandler,WARNING

app = Flask(__name__) #instancia
if not app.debug:
    file_handler= FileHandler('errorlog.txt')
    file_handler.setLevel(WARNING)

    app.logger.addHandler(file_handler)

@app.route('/') #wrap (decorator)
def index():
    return 1 / 0

if __name__ == '__main__':
    app.run() #lunch server on port 5000"""
    
    
