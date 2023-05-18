from flask import Flask, render_template
from post import posts_dict
import requests

app = Flask(__name__)


@app.route('/')
def show_blogs():
    return render_template('index.html', posts_dict=posts_dict)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts_dict:
        if list(posts_dict).index(blog_post)+1 == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, posts_dict=posts_dict)


if __name__ == "__main__":
    app.run(debug=True)
