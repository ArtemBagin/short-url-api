from loader import db

class ShortUrls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    OriginalUrl = db.Column(db.String(300))
    ShortUrl = db.Column(db.String(120), unique=True)
    ShortCode = db.Column(db.String(120), unique=True)
    Transition = db.Column(db.Integer, default = 0)

    def __init__(self,OriginalUrl,ShortUrl,ShortCode):
        self.OriginalUrl = OriginalUrl
        self.ShortUrl = ShortUrl
        self.ShortCode = ShortCode

# db.create_all()
