from datetime import date

class ShreeOm():
  def __init__(self, name:str, age:int) -> None:
    self.name = name
    self.age = age
  
  @classmethod
  def age_from_year(cls, name:str, birth_year:int) :
    current_year: int = date.today().year
    age: int = current_year - birth_year
    return ShreeOm(name, age)

class Child(ShreeOm):
  def __init__(self, name:str, age:int, job) -> None:
    super().__init__(name, age)
    self.job = job
    self.is_manager = False



p1 = ShreeOm('Shyam', 32)
print(p1.__dict__)

c1 = Child('Pradumn', 21, 'Data Scientist')
print(c1.__dict__)