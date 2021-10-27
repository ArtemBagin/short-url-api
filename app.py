from blueprints import routers
from loader import app

for router in routers:
    app.register_blueprint(router)

if __name__ == '__main__':
    app.run(debug = True)
