from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, BooleanField, SelectField, DateField, DateTimeLocalField
from wtforms.validators import DataRequired, Length
from datetime import datetime as dt

# Список категорій, що використовується у випадаючому меню
CATEGORIES = [('tech', 'Tech'), ('science', 'Science'), ('lifestyle', 'Lifestyle')]


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2)])
    content = TextAreaField("Content", render_kw={"rows": 5, "cols": 40}, validators=[DataRequired()])
    is_active = BooleanField('Active Post')  # Чекбокс для відмітки активності поста
    publish_date = DateTimeLocalField('Publish Date', format="%Y-%m-%dT%H:%M", default=dt.now())                 # Поле для вибору дати публікації
    category = SelectField('Category', choices=CATEGORIES, validators=[DataRequired()]) 
    author_id = SelectField("Author", coerce=int)

    submit = SubmitField("Add Post")

    