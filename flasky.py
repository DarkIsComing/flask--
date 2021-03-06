import os
from flask_migrate import Migrate,MigrateCommand
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment
from flask_script import Manager,Shell
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager=Manager(app)


def make_shell_context():
    return dict(db=db, User=User,Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)
manager.add_command('db',MigrateCommand)
manager.add_command('shell',Shell(make_context=make_shell_context))

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__=="__main__":
    #manager.run()
    app.run()