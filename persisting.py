from sqlalchemy.orm import Session
from models import User, Comment
from connect import engine 

session = Session(bind=engine)

user1 = User(
    username='abiud',
    email_address='abiud@gmail.com',
    comments=[Comment(text="Hello World"), Comment(text="Please Subscribe")]
)

paul = User(
    username='paul',
    email_address="paulmukuru@gmail.com",
    comments=[Comment(text="Whats app"), Comment(text="Please Subscribe")]
)

carol = User(
    username="carol",
    email_address="carol@gmail.com"
)


session.add_all([user1, paul, carol])

session.commit()
