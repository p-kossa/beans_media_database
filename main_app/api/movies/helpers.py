from main_app.database import db
from main_app.database.models import Post, Category


def create_movie(data) -> None:
    title = data.get('title')
    body = data.get('body')
    category_id = data.get('category_id')
    category = Category.query.filter(Category.id == category_id).one()
    post = Post(title, body, category)
    db.session.add(post)
    db.session.commit()


def update_movie(post_id, data) -> None:
    post = Post.query.filter(Post.id == post_id).one()
    post.title = data.get('title')
    post.body = data.get('body')
    category_id = data.get('category_id')
    post.category = Category.query.filter(Category.id == category_id).one()
    db.session.add(post)
    db.session.commit()


def delete_movie(post_id) -> None:
    post = Post.query.filter(Post.id == post_id).one()
    db.session.delete(post)
    db.session.commit()


def create_category(data) -> None:
    name = data.get('name')
    category_id = data.get('id')

    category = Category(name)
    if category_id:
        category.id = category_id

    db.session.add(category)
    db.session.commit()


def update_category(category_id, data) -> None:
    category = Category.query.filter(Category.id == category_id).one()
    category.name = data.get('name')
    db.session.add(category)
    db.session.commit()


def delete_category(category_id) -> None:
    category = Category.query.filter(Category.id == category_id).one()
    db.session.delete(category)
    db.session.commit()
