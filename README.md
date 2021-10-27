


# short-url-api 

API позволяет сокращать любые ссылки (python, flask, SQLalchemy) 
------
API поддерживает только один MIME-тип: application/json
## Методы api

- /create [POST]
>Создаёт сокращённую ссылку
>Принимает на вход 1 параметр - url
>Возвращает исходный url, сокращённый url и ShortCode 

- /s/{ShortCode}/info [GET] 
>Возвращает нформацию о сокращённой ссылке
>(ShotCode, кол-во переходов, исходный URL) 

- /s/{ShortCode} [DELETE] 
>Удаляет скоращённую ссылку по её ШортКоду

- /s/{ShortCode} [GET] 
>Переход по сокращённой ссылке


