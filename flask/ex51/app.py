from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def index():
    name_var = input('Type your name > ').capitalize()
    return render_template('index.html', user_name = name_var)

if __name__ == '__main__':
    app.run(debug = True)
