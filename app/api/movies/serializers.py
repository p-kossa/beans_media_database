from flask_restplus import fields
from app.api.restplus import api

movie_post = api.model('Movie post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a movie'),
    'title': fields.String(required=True, description='Movie title'),
    'body': fields.String(required=True, description='Article content'),
    'pub_date': fields.DateTime,
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.name'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_movie_posts = api.inherit('Page of movies', pagination, {
    'items': fields.List(fields.Nested(movie_post))
})

category = api.model('Movie category', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a movie category'),
    'name': fields.String(required=True, description='Category name'),
})

category_with_posts = api.inherit('Blog category with posts', category, {
    'posts': fields.List(fields.Nested(movie_post))
})
