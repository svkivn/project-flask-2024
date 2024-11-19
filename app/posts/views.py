from . import post_bp
from flask import render_template, request, abort, flash, redirect, url_for
from .forms import PostForm
from .models import Post
from app import db

from .utils import save_post, load_posts, get_post

@post_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        is_active = form.is_active.data
        category = form.category.data
        content = form.content.data
        publish_date = form.publish_date.data
        post_new = Post(title=title, content=content, 
                        is_active=is_active, category=category,
                        posted = publish_date)
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
    post = get_post(id)
    if post:
        return render_template("detail_post.html", post=post)
    return abort(404)


@post_bp.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(Post, post_id) # Якщо об'єкт не знайдено, автоматично повертається помилка 404
    form = PostForm(obj=post)          # Ініціалізує форму PostForm, заповнюючи її полями об'єкта post
    if form.validate_on_submit():
        #Оновлення полів title та content, оновлення у БД
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post updated successfully!')
        return redirect(url_for('.get_posts'))
    return render_template('add_post.html', form=form)



