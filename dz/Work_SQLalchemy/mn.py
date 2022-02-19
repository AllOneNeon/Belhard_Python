from httpx import Limits
from sqlalchemy import insert,select,and_, or_, not_,delete,update,desc
from db import Base,engine,execute
from models import User, Address
from heapq import nlargest

Base.metadata.create_all(engine)

users_data = [
    {'name':'Malkolm', 'fullname': 'Malkolm Ralph','gender':'male','age':33},
    {'name':'Roman', 'fullname': 'Roman Pierce','gender':'male','age':32},
    {'name':'Andrei', 'fullname': 'Andrei Mironov','gender':'male','age':34},
    {'name':'Johny', 'fullname': 'Johny Depp','gender':'male','age':35},
    {'name':'Tati', 'fullname': 'Tati Mura','gender':'female','age':34},
    {'name':'Vyacheslav', 'fullname': 'Vyacheslav Bub','gender':'male','age':34},
]
def insert_many_users():
    query = insert(User)
    execute (query,users_data) 
insert_many_users()    

def select_users():    
    query = ( 
    select(User.name).order_by(User.age.desc()).limit(3)
        # .join(Address)
        .where(
            (User.gender=='male') &
            ((User.name.like ('J%')) |
            (User.name.like('A%')))
            )
            )           
                          
    with engine.connect() as conn:
        cursor = conn.execute(query)
        users = list(cursor)
    for i in users:
        print (dict(i))
        
select_users()
    
     
def delete_duplicate_user():
    query = delete (User).where(User.id==2)
    execute(query)
# delete_duplicate_user()


def insert_adress():
    execute(insert(Address)
            .values (email_address='all_neo@mail.ru',user_id=6))
# insert_adress()
    

def update_age():
    query = (update(User)
        .where(User.name=='Tati')
        .values(age=32))
    execute(query)
# update_age()