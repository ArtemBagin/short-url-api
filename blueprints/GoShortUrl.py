from flask import redirect,Blueprint
from models import ShortUrls
import json

GoShortUrlRouter = Blueprint('GoShortUrl',__name__)


@GoShortUrlRouter.get('/s/<string:ShotCode>')
def GoShortUrl(ShotCode:str):
	url = ShortUrls.query.filter_by(ShotCode = ShotCode)
	if url.all():
		return redirect(url.one().OriginalUrl)
	else:
		return json.dumps({"error":"Page not found"}),404

