import logging.config

import os
from flask import Flask, Blueprint, render_template
from main_app import settings
from main_app.api.movies.endpoints.posts import ns as blog_posts_namespace
from main_app.api.movies.endpoints.categories import ns as blog_categories_namespace
from main_app.api.movies.endpoints.list_movies import ns as blog_list_movies_namespace
from main_app.api.restplus import api
from main_app.database import db

app = Flask(__name__)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app) -> None:
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['MOVIEDB_API_KEY'] = settings.MOVIEDB_API_KEY


def initialize_app(flask_app) -> None:
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(blog_posts_namespace)
    api.add_namespace(blog_categories_namespace)
    api.add_namespace(blog_list_movies_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main() -> None:
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(host='0.0.0.0', debug=settings.FLASK_DEBUG)


@app.route('/', methods=['GET', 'POST'])
def render_frontend():
    """Render homepage"""

    return render_template('index.html')


if __name__ == "__main__":
    main()
