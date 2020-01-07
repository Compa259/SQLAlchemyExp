import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# Create engine to connect DB using MySQL Connector/Python
engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://root:123456@localhost:3306/sqlalchemy',
    echo=False
)

# Define and create table
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    age = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self):
        return "User: {0}, age: {1}".format(self.name, self.age)


class Company(Base):
    __tablename__ = 'companies'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=100))
    address = sqlalchemy.Column(sqlalchemy.String(length=300))

    def __repr__(self):
        return "Company: {0}, address: {1}".format(self.name, self.address)


Base.metadata.create_all(engine)

# Create session to query data
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

# ADD
# Add a user and company
user = User(name='Nguyen Minh Duc', age=24)
anonymous = User(name='Anonymous', age=24)
session.bulk_save_objects([user, anonymous])
company = Company(name='Tripi', address='PeakView Building')
session.add(company)
session.commit()

# READ
# Read users and companies, read by filter
users = session.query(User).all()
for user in users:
    print(user)
# person = session.query(User).filter_by(name='Nguyen Minh Duc').first()
# print('\nThe first one: ')
# print(person)


# UPDATE
session.query(User).filter(User.name == 'Anonymous').update({User.age: 25})

# DELETE
session.query(User).filter(User.name == 'Anonymous')\
    .delete(synchronize_session=False)

users = session.query(User).all()
for user in users:
    print(user)
session.commit()
session.close()