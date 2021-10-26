from blueprints.CreateShortUrl import CreateShortUrlRouter
from blueprints.GoShortUrl import GoShortUrlRouter
from loader import app

app.register_blueprint(CreateShortUrlRouter)
app.register_blueprint(GoShortUrlRouter)


if __name__ == '__main__':
    app.run(debug = True)