from typing import List, Optional
from pydantic import BaseModel

class Child (BaseModel):
    name: str
    age: int

class Person (BaseModel):
    name: str
    age: int
    children: Optional [List[Child]] = None
    married: bool
    city: None

@property
def of_legal_age (self):
    return self.age >= 18

data = {
    'age': 45,
    'name': 'Potter',
    'children': [
        {'age': 3,
        'name': 'Anna'
        }
    ],
    'married': True,
    'city': None   
    }

p = Person (**data)
print (p.json())