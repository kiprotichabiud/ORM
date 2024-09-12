from persisting import session
from models import User, Comment
from sqlalchemy import select



statement = select(User).Where(User.username.in_(["paul","carol"]))

result = session.scalars(statement)

for user in result:
    print(user)