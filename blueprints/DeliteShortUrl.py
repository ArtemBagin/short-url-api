from flask import Blueprint
from models import ShortUrls,db
import json

DeliteShortUrlRouter = Blueprint('DeliteShortUrl',__name__)


@DeliteShortUrlRouter.delete('/s/<string:ShortCode>')
def DeliteShortUrl(ShortCode:str):
	url = ShortUrls.query.filter_by(ShortCode = ShortCode)
	if url.all():
		url.delete()
		db.session.commit()
		return json.dumps({"message":"link has been deleted"}),404
	else:
		return json.dumps({"error":"Page not found"}),404

