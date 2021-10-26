from loader import db

class ShortUrls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    OriginalUrl = db.Column(db.String(300))
    ShotUrl = db.Column(db.String(120), unique=True)
    ShotCode = db.Column(db.String(120), unique=True)

    def __init__(self,OriginalUrl,ShotUrl,ShotCode):
        self.OriginalUrl = OriginalUrl
        self.ShotUrl = ShotUrl
        self.ShotCode = ShotCode


