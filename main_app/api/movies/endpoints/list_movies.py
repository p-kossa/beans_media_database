import logging

import requests
from flask import jsonify
from flask_restplus import Resource
from main_app.api.restplus import api
from main_app import settings

log = logging.getLogger(__name__)

ns = api.namespace('movies/list_movies', description='Testing MovieDB API')

api_key = settings.MOVIEDB_API_KEY

@ns.route('/')
class ListMovies(Resource):

    def get(self):
        """
        Returns a list of most popular rated R movies.
        """
        r = requests.get(
            'https://api.themoviedb.org/discover/movie/?certification_country=US&certification=R&sort_by=vote_average.desc?api_key={}'.format(api_key))

        return jsonify(r)
