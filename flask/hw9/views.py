from . import app
from flask import Flask, render_template, request

like_count = 0

@app.route('/')
def index():
    return render_template('index.htm')


@app.route('/about', methods = ['POST', 'GET'])
def about():
    if request.method == 'POST':
        global like_count
        like_count += 1

    print(f'count is now {like_count}.')
    count = like_count

    return render_template('about_me.htm', new_count = count)


@app.route('/tabs', methods = ['POST'])
def tabs():
    if request.method == 'POST':
        return render_template('tabs.htm')
