from flask import Blueprint
from models import ShortUrls,db
import json

router = Blueprint('DeliteShortUrl',__name__)


@router.delete('/s/<string:ShortCode>')
def DeliteShortUrl(ShortCode:str):
	url = ShortUrls.query.filter_by(ShortCode = ShortCode)
	if url.all():
		url.delete()
		db.session.commit()
		return json.dumps({"message":"link has been deleted"}),200
	return json.dumps({"error":"Page not found"}),404



