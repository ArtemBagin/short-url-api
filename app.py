from blueprints.DeliteShortUrl import DeliteShortUrlRouter
from blueprints.CreateShortUrl import CreateShortUrlRouter
from blueprints.GetUrlInfo import GetUrlInfoRouter
from blueprints.GoShortUrl import GoShortUrlRouter
from loader import app

app.register_blueprint(CreateShortUrlRouter)
app.register_blueprint(GoShortUrlRouter)
app.register_blueprint(DeliteShortUrlRouter)
app.register_blueprint(GetUrlInfoRouter)




if __name__ == '__main__':
    app.run(debug = True)