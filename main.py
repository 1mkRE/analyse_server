from flask import Flask
import waitress as wt
import socket
import os

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    hostname = socket.gethostname()
    print('Analyse software server')
    s = wt.create_server(app, host="0.0.0.0", port=5000)
    try:
        # run app in debug mode on port 5000
        # app.run(debug=False, port=5000, host='0.0.0.0')#from waitress import server
        print("Server starting on Port 5000")
        print(os.system('ipconfig'))
        s.run()
    except KeyboardInterrupt:
        print("Server closing")
        s.close()
