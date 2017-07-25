"""
A first simple Cloud Foundry Flask app

"""
from flask import Flask
import os

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))
home = str(os.getenv('HOME'))

@app.route('/')
def hello_world():    
    msg = ' *** Hello World! I am instance ' + str(os.getenv("CF_INSTANCE_INDEX", 0))
    env = str(os.getenv('APP_ENV', 'unknown'))
    return home + ' - ' + env + ' - ' + msg

@app.route('/list')
def listing():
    return str(os.listdir(os.environ['HOME']))

@app.route('/file')
def file_processing():
    myfile = open(os.getenv('FILE_LOCATION', home) + '/readme.md')
    sf = str(myfile)
    print sf
    return sf

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
