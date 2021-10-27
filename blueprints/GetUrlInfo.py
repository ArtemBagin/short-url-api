from flask import Blueprint
from models import ShortUrls
import json

router = Blueprint('GetUrlInfo',__name__)


@router.get('/s/<string:ShortCode>/info')
def GetUrlInfo(ShortCode:str):
	url = ShortUrls.query.filter_by(ShortCode = ShortCode)
	if url.all():
		UrlInfo = url.one().__dict__
		UrlInfo.pop('_sa_instance_state')
		return json.dumps(UrlInfo),200
	else:
		return json.dumps({"error":"Page not found"}),404

