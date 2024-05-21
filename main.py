from flask import Flask
from config import config
from scr.route import route_Tienda_productos

app = Flask(__name__)

if __name__ == '__main__':
   # app.config.from_object(config['development'])
    app.secret_key = 'Qwerty2023*'

    # Blueprint
    app.register_blueprint(route_Tienda_productos.main, url_prefix='/')

    app.run(host='0.0.0.0' , port=50100, debug=True)
