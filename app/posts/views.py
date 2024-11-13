from . import post_bp
from flask import render_template, request, abort, flash, redirect, url_for
from .forms import PostForm
from .models import Post

from .utils import save_post, load_posts, get_post

@post_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        post_new = {"id": 1, "title": title, "content": content}
        save_post(post_new)
        flash(f'Post {title} added successfully!', 'success')
        return redirect(url_for('.add_post'))
    elif form.errors:
        flash(f"Enter the correct data in the form!", "danger")
   
    return render_template("add_post.html", form=form)


@post_bp.route('/') 
def get_posts():
    posts = load_posts()
    return render_template("posts.html", posts=posts)

@post_bp.route('/<int:id>') 
def detail_post(id):
    post = get_post(id)
    if post:
        return render_template("detail_post.html", post=post)
    return abort(404)