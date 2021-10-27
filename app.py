from blueprints.DeliteShortUrl import DeliteShortUrlRouter
from blueprints.CreateShortUrl import CreateShortUrlRouter
from blueprints.GoShortUrl import GoShortUrlRouter
from loader import app

app.register_blueprint(CreateShortUrlRouter)
app.register_blueprint(GoShortUrlRouter)
app.register_blueprint(DeliteShortUrlRouter)



if __name__ == '__main__':
    app.run(debug = True)