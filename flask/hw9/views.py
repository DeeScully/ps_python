from . import app
from flask import Flask, render_template, request
import string

like_count = 0

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.form['msg_to_encrypt']
        key = int(request.form['key'])
        ltr_map = string.ascii_lowercase
        encrypted_str = ''

        for i in msg:
            if i == ' ':
                encrypted_str += ' '
            else:
                ltr_location = ltr_map.find(i)
                new_location = (ltr_location + key) % 26
                encrypted_str += ltr_map[new_location]

        encrypted_str = f'{encrypted_str}'
        print(encrypted_str)
        return render_template('index.htm', encrypted_str = encrypted_str)

    else: return render_template('index.htm')


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
