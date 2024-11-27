from datetime import datetime as dt
from sqlalchemy.orm import backref
from app import db
from ..users.models import User


class Post(db.Model):
    __tablename__='posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=True)
    posted = db.Column(db.DateTime, default=dt.now())
    is_active =  db.Column(db.Boolean, default=True) # Поле для активності посту
    category = db.Column(db.String(20), nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    author = db.relationship('User', backref=backref("posts", lazy="dynamic"), lazy="joined")   #backref, який додає двосторонній доступ до пов'язаних даних між таблицями.

    def __repr__(self):
        return f"<Post(title={self.title})>"
    
    """
    The “dynamic” loader applies to collections only. It is not valid to use “dynamic” loaders 
    with many-to-one, one-to-one, or uselist=False relationships. 
    Newer versions of SQLAlchemy emit warnings or exceptions in these cases.
    """
