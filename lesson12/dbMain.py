from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

HOST = "localhost"
PORT = 5432
LOGIN = "postgres"
PASSWORD = "root"
DB_NAME = "core111122"
engine = create_engine(f'postgresql://{LOGIN}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}', echo=True)

# metadata = MetaData()
# authors_table = Table('authors',
#                       metadata,
#                       Column('id', Integer, primary_key=True),
#                       Column('name', String))
# books_table = Table('books',
#                     metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('title', String),
#                     Column('description', String),
#                     Column('author_id', ForeignKey('authors.id')))
# #
# # if __name__ == "__main__":
# #     metadata.create_all(engine)
# from sqlalchemy.orm import mapper, relation
# from sqlalchemy.orm import relationship, backref
#
#
# class Author(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return self.name
#
#
# class Book(object):
#     def __init__(self, title, description, author):
#         self.title = title
#         self.description = description
#         self.author = author
#
#     def __repr__(self):
#         return self.title
#
# mapper(Book, books_table)
# mapper(Author, authors_table, properties = { 'books': relation(Book, backref='author')})

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship(Author, backref=backref('books', order_by=title))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

    def __repr__(self):
        return f"<{self.id}; {self.title}; {self.description}>"
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # author_1 = Author(name='Richard Dawkins')
    # author_2 = Author('Matt Ridley')
    # book_1 = Book(title='The Red Queen', description='A popular science book', author=author_2)
    # book_2 = Book('The Selfish Gene', 'A popular science book', author_1)
    # book_3 = Book('The Blind Watchmaker', 'The theory of evolutio', author_1)
    # session.add(author_1)
    # session.add(author_2)
    # session.add(book_1)
    # session.add(book_2)
    # session.add(book_3)
    # print(book_2)
    # session.commit()
    # print(book_2)
    q = session.query(Book).order_by(Book.id).all()
    print(q)
    q = session.query(Book).filter(Book.title == 'The Selfish Gene').order_by(Book.id).all()
    print(q)



