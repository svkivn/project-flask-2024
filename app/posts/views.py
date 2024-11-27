from . import post_bp
from flask import render_template, request, abort, flash, redirect, url_for
from .forms import PostForm
from .models import Post
from app.users.models import User
from app import db

from .utils import save_post, load_posts, get_post

@post_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    
    # Отримання списку авторів із бази даних
    authors = User.query.all()
    form.author_id.choices = [(author.id, author.username) for author in authors]

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        is_active = form.is_active.data
        category = form.category.data
        content = form.content.data
        publish_date = form.publish_date.data
        post_new = Post(title=title, content=content, 
                        is_active=is_active, category=category,
                        posted = publish_date, user_id = form.author_id.data )
        db.session.add(post_new)
        db.session.commit()
        flash(f'Post {title} added successfully!', 'success')
        return redirect(url_for('.add_post'))
    elif form.errors:
        flash(f"Enter the correct data in the form!", "danger")
   
    return render_template("add_post.html", form=form)


@post_bp.route('/') 
def get_posts():
    stmt = db.select(Post).order_by(Post.posted.desc())
    posts =  db.session.scalars(stmt).all()
    return render_template("posts.html", posts=posts)

@post_bp.route('/<int:id>') 
def detail_post(id):
    post = db.get_or_404(Post, id)
    return render_template("detail_post.html", post=post)


@post_bp.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(Post, post_id) # Якщо об'єкт не знайдено, автоматично повертається помилка 404
    form = PostForm(obj=post)          # Ініціалізує форму PostForm, заповнюючи її полями об'єкта post
    form.publish_date.data = post.posted
    if form.validate_on_submit():
        #Оновлення полів title та content, оновлення у БД
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated successfully!')
        return redirect(url_for('.detail_post', id=post.id))
    return render_template('add_post.html', form=form)

from flask import request

@post_bp.route('/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = db.get_or_404(Post, post_id)  # Отримуємо пост або 404
    #db.session.delete(post)  # Видаляємо пост
    #db.session.commit()  # Зберігаємо зміни в базі даних
    flash(f'Post {post.id} deleted successfully!', 'success')  # Відображаємо повідомлення
    return redirect(url_for('.get_posts'))  # Перенаправляємо на список постів


