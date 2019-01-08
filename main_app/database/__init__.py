from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from main_app.database.models import Post, Category
    db.drop_all()
    db.create_all()
