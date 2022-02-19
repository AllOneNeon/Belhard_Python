import pickle

class Person:
    name = 'Noname'
    def greet(self):
            print('Get out of here, ' + self.name + '!')

bob = Person()
bob.name = 'Bob'
bob.greet()
s = pickle.dumps (bob.greet)
print (s)
