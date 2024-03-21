from  flask import Flask


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from authors_app.extension import db,migrate
from authors_app.models.user import User
from authors_app.controllers.auth.auth_controller import auth



def create_app():
    app =Flask(__name__)
    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    
    from authors_app.models.company import Company
    from authors_app.models.user import User
    from authors_app.models.book import Book 
    
    @app.route('/')
    def home():
        return"hello World"
    
    
    app.register_blueprint(auth,url_prefix="/api/v1/auth")
    
    return app


if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)