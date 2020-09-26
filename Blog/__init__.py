import os
from flask import Flask


def create_app(test_config=None):
    # Create the application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # Access password
        SECRET_KEY='DEV',
        # Creates a database in the current dir
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
    )
    # Tells the app where to get it's configurations
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello world'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app