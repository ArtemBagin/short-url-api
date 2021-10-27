from blueprints import CreateShortUrl
from blueprints import DeliteShortUrl
from blueprints import GetUrlInfo
from blueprints import GoShortUrl

routers = [
    CreateShortUrl.router,
    DeliteShortUrl.router,
    GetUrlInfo.router,
    GoShortUrl.router,
]



