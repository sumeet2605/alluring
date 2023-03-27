import os
from flask import Flask, session, render_template
from . import db, auth, blog, home, clients
from dotenv import load_dotenv

load_dotenv()


def create_app(test_config=None):
    # Create and configure the App
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECERT_KEY =os.getenv('SECERT_KEY'),
        DATABASE=os.path.join(app.instance_path, 'alluringlens.sqlite'),
    )
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello

    @app.route('/hello')
    def hello():
        return 'Hello World!'

    db.init_app(app)
    app.register_blueprint(home.bp)
    app.register_blueprint(clients.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404


    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('500.html'), 500


    return app

