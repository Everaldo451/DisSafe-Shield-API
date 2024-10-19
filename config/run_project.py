from os import path, getenv
from dotenv import load_dotenv
from config.json_handler import load_config


def run_project(app):
    check_config_file = path.exists('.env')
    if not check_config_file:
        raise FileNotFoundError('.env file not found')
    check_config_file = path.exists('config/config.json')
    if not check_config_file:
        raise FileExistsError('config/config.json file not found')

    load_dotenv()
    config = load_config()
    status = config['status']
    if not status:
        raise ValueError('Not have status in config.json')

    if status == 'development':
        PORT = getenv('DEVELOPMENT')
    if status == 'production':
        PORT = getenv('PRODUCTION')
    DEBUG = getenv('FLASK_DEBUG')
    HOST= getenv('FLASK_HOST')
    if not PORT or not DEBUG or not HOST:
        raise ValueError('Port, host or debug value not set in .env')

    app.run(host=HOST, debug=DEBUG, port=PORT)
