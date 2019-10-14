from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_application
from db import db

app = create_application()

# Migrate object for db migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
	manager.run()
