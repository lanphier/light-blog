#!/usr/bin/env python
import os

from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

def make_shell_context():
    return dict(app=app, db=db)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
3