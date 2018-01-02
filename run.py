# -*- coding: utf-8 -*-
from project.server import app

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        debug=app.config['DEBUG']
    )
