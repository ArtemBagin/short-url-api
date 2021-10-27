# short-url-api

- API позволяет сокращать любые ссылки

- API поддерживает только один MIME-тип: application/json
## Методы api

- /create [POST]
>Создаёт сокращённую ссылку
>Принимает на вход 1 параметр - `url`

>Возвращает исходный url, сокращённый url и ShortCode 

- /s/{ShortCode}/info [GET] 
>Возвращает информацию о сокращённой ссылке
>(ShotCode, кол-во переходов, исходный URL) 

- /s/{ShortCode} [DELETE] 
>Удаляет скоращённую ссылку по её ШортКоду

- /s/{ShortCode} [GET] 
>Переход по сокращённой ссылке

## База данных 
Я использовал SQLite3 в связке с SQLalchemy, но SQLAlchemy позволяет работать с такими базами данных как MySQL, MS-SQL, PostgreSQL, Oracle и другими

## config.py 

`host` - URL-адрес для вызова методов API

`sqlite_path` - в моем случае, путь до базы данных
