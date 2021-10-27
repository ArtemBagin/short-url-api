from flask import redirect,Blueprint
from models import ShortUrls,db
import json

GoShortUrlRouter = Blueprint('GoShortUrl',__name__)


@GoShortUrlRouter.get('/s/<string:ShortCode>')
def GoShortUrl(ShortCode:str):
	url = ShortUrls.query.filter_by(ShortCode = ShortCode)
	if url.all():
		url.one().Transition += 1
		db.session.commit()
		return redirect(url.one().OriginalUrl)
	else:
		return json.dumps({"error":"Page not found"}),404

