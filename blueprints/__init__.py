from blueprints import (CreateShortUrl, DeliteShortUrl,
                        GetUrlInfo, GoShortUrl) 

routers = [
    CreateShortUrl.router,
    DeliteShortUrl.router,
    GetUrlInfo.router,
    GoShortUrl.router,
]



