from flask import Flask, render_template, request

app = Flask('__name__')

@app.route('/hello', methods = ['post', 'get'])
def index():
    greeting = 'Hello World'

    if request.method.lower() == 'post':
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet} {name}'
        print(f'the greeting is now {greeting} and the len is {len(greeting)}')
        return render_template('index.html', greeting = greeting)
    else: return render_template('hello_form.html')

    # name = request.args.get('name', 'Nobody')
    #
    # if name:
    #     greeting = f'Hello, {name}'
    # else: greeting = 'hello world'

if __name__ == '__main__':
    app.run(debug = True)
