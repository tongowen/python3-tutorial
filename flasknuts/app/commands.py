import click
from app.model import User, Book, Photo
from app import db, app


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    
    db.create_all()
    click.echo('Initialized database.') 


@app.cli.command()
def forge():
    """Generate fake data."""
    db.create_all()
    
    # 全局的两个变量移动到这个函数内
    name = 'tong owen'
    photos = [
        {'photo': 'My Neighbor Totoro', 'date': '1988'},
        {'photo': 'Dead Poets Society', 'date': '1989'},
        {'photo': 'A Perfect World', 'date': '1993'},
        {'photo': 'Leon', 'date': '1994'},
        {'photo': 'Mahjong', 'date': '1996'},
        {'photo': 'Swallowtail Butterfly', 'date': '1996'},
        {'photo': 'King of Comedy', 'date': '1999'},
        {'photo': 'Devils on the Doorstep', 'date': '1999'},
        {'photo': 'WALL-E', 'date': '2008'},
        {'photo': 'The Pork of Music', 'date': '2012'},
    ]
    
    user = User(name=name, pwd='123456')
    db.session.add(user)

    book = Book(book="语文书", date='今天')
    db.session.add(book)

    for m in photos:
        pho = Photo(photo=m['photo'], date=m['date'])
        db.session.add(pho)
    
    db.session.commit()
    
    click.echo('Done.')
