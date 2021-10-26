from flask_restful import Resource,reqparse
from random import choice,randint
from models import db,ShortUrls
from flask import Blueprint
from config import host
import string
import json

CreateShortUrlRouter = Blueprint('CreateShortUrl',__name__)



def CreateCode():
    ShotCode = ''
    while ShortUrls.query.filter_by(ShotCode = ShotCode).all() or ShotCode == '':
        ShotCode = "".join(choice(string.ascii_letters) for _ in range(randint(1,6)))
    return ShotCode


@CreateShortUrlRouter.post('/create')
def CreateShortUrl():
    parser = reqparse.RequestParser()
    parser.add_argument("url",type = str)
    params = parser.parse_args()

    if not params["url"]:
        return json.dumps({"error":"Not found param 'url'"}),500

    ShortCode = CreateCode()
    ShortUrl = f"{host}/s/{ShortCode}"

    new_url = ShortUrls(params["url"],ShortUrl,ShortCode)
    db.session.add(new_url)
    db.session.commit()

    return json.dumps({"ShortUrl":ShortUrl}),200

