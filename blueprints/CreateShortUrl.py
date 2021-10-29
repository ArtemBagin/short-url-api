from flask_restful import reqparse
from random import choice,randint
from models import db,ShortUrls
from flask import Blueprint
from config import host
import string
import json
import re

router = Blueprint('CreateShortUrl',__name__)


def CreateCode():
    ShortCode = ''
    while ShortUrls.query.filter_by(ShortCode = ShortCode).all() or ShortCode == '':
        ShortCode = "".join(choice(string.ascii_letters) for _ in range(randint(1,6)))
    return ShortCode


@router.post('/create')
def CreateShortUrl():
    parser = reqparse.RequestParser()
    parser.add_argument("url",type = str)
    params = parser.parse_args()

    if not params["url"]:
        return json.dumps({"error":"Not found argument 'url'"}),500

    if not re.match(r'^(ftp|http|https):\/\/[^ "]+$',params["url"]):
        return json.dumps({"error":"incorrect link format"}),500
    
    ShortCode = CreateCode()
    ShortUrl = f"{host}/{ShortCode}"

    NewUrl = ShortUrls(params["url"],ShortUrl,ShortCode)
    db.session.add(NewUrl)
    db.session.commit()

    return json.dumps({"ShortUrl":ShortUrl}),200



