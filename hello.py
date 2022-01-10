from flask import Flask

app = Flask(__name__)
# print(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/12ELmx0C4EFKcE/giphy.gif" width=200>'


def make_bold(function):
    def wrapper():
        return f'<strong>{function()}</strong>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper


# Different route using app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"


# Creating variable paths and converting the path to a specified type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, You are {number} yrs old!"

if __name__ == "__main__":
    # Run app in debug mode to auto-reload
    app.run(debug=True)

