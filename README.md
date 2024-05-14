## ✨ Learn Object Oriented Programming 💥

1. class
2. Instance object of class 
3. Attributs (Instance, class, and `__dect__` attributes)
4. Methods (Instance, class, and static)
5. Debugging Python Classes 
6. Specialized Classes From the Standard Library (data classes, Enumerations)
7. Inheritance and Class Hierarchies (Simple Inheritance, Multiple Inheritance )
8. Method Resolution Order
9. Extended vs Overridden Methods [link](https://realpython.com/python-classes/#extended-vs-overridden-methods)
10. Mixin Classes [source](https://realpython.com/python-classes/#mixin-classes)
11. Dependency Injection [source](https://realpython.com/python-classes/#dependency-injection)
12. Creating Abstract Base Classes (ABCs) and Interfaces [source](https://realpython.com/python-classes/#creating-abstract-base-classes-abcs-and-interfaces)

13. Polymorphism With Common Interfaces [source](https://realpython.com/python-classes/#unlocking-polymorphism-with-common-interfaces)


### Python classes :
- Python classes allow us to bundle data and behavior together in a single entity through attributes and methods, respectively.
-  We use the data to define the object’s current state and the methods to operate on that data or state.
- A method is just a function that we define inside a class. By defining it there, we make the relationship between the class and the method explicit and clear.
-Because they’re just functions, methods can take arguments and return values as functions do. 
- In a Python class, we can define three different types of methods:
1. Instance methods, which take the current instance, self, as their first argument
2. Class methods, which take the current class, cls, as their first argument
3. Static methods, which take neither the class nor the instance


### **Classes vs Instances** :

- **_Classes_** allow us to create **user-defined** **_data structures_**.
- _Classes defined functions_ is called **_methods_**, which identify the behaviors and actions that an object created from the class can perform with its data(attributes/variable).
- A `class` is a blueprint for how to define something. It doesn’t actually contain any data.
- While the _class_ is the _blueprint_, an **_instance_** is **_an object_** that’s built from a class and contains real data.
- we can create many instances from a single class.

---

### **Class Definition** :

> Python class names are written in CapitalizedWords notation by convention. Ex, Employee, IndianCars, TemplateView, ...

- All class definitions start with the `class` keyword, then add the name of the class and a colon. ex, `class Employee:`, `class IndianCows:`
- We define the properties that all class objects must have in a method called `__init__()`.
- Every time we create a new class object, `.__init__()` sets the initial state of the object by assigning the values of the object’s properties. That is, `.__init__()` initializes each new instance of the class.
- We can give `__init__()` any number of parameters, but the **_first parameter_** will always be a **_variable_** called `self`.
- When we create **_a new class instance_**, then Python automatically passes the instance to the `self` parameter in `__init__()` so that Python can define the new **_attributes_** on the object.

```py
class Employee:
  office_branch = "India"
  def __init__(self, name, age):
    self.name = name
    self.age = age
```

#### Attributes :
1. instance attributes:
2. class attributes:


##### 1. Instance attributes: 
- variables that we define inside a `.__init__()` method. 
- Their data is only available to that instance object and defines its state/data.
- From our above example, in the body of `__init__()` method, there are two statements using the `self` variable:
  1.  `self.name = name` creates an attribute called `name` and assigns the value of the name parameter to it.
  2.  `self.age = age` creates an attribute called `age` and assigns the value of the age parameter to it.
- Attributes created in `__init__()` method are called **_instance attributes_** (ex, `name` & `age`). An instance attribute’s value is specific to a particular instance of the target class.
- All Employee objects have a `name` and an `age`, but the **_values_** for the **_name_** and **_age attributes_** will vary depending on the **_Employee_** class instance.
- Unlike class attributes, we can’t access instance attributes through the class.
- If we try to do that, then we get an `AttributeError` exception.
- We need to access them through their containing instance.

```py 
  Employee.name
  Traceback (most recent call last):
      ...
  AttributeError: type object 'Employee' has no attribute 'name'

  emp_1 = Employee('Shyam', 32)
  emp_1.name
  # op: Shyam

```

> Note: Even though we can define instance attributes inside any instance method, it’s best to define all of them in the `.__init__()` method, which is the **instance initializer**. This ensures that all of the attributes have the correct values when we create a new instance. Additionally, it makes the code more organized and easier to debug.

> Note: Inside a class, we must access all instance attributes through the `self` argument. This argument holds a reference to the current instance, which is where the attributes belong and live. 

##### 2. class attributes:
- Variables that we define directly in the class body but outside of any method.
- we can access class attributes using either the class or one of its instances.
- **_class attributes_** are attributes that have the **_same value_** for **_all class instances_** (Ex, `office_branch` is `'India'` for all the instance objects of `Employee` class).

 
> **_class attributes_** vs **_instance attributes_**
> - Use **_class attributes_** to define properties that should have the same value for every class instance.
> -On the other hand, use **_instance attributes_** for properties thats values vary from one instance to another.

##### 3. The .__dict__ Attribute :
- In Python, both classes and instances have a special attribute called .`__dict__`. This attribute holds a dictionary containing the writable members of the underlying class or instance.
- In a class, `.__dict__` will contain class attributes and methods. In an instance, `.__dict__` will hold instance attributes.

```py
  emp_2 = Employee('Madhav', 40)
  print(emp_2.__dict__) #* OP: {'name': 'Madhev', 'age': 40}

  emp2.job = "Data Engineer"
  print(emp_2.__dict__) #* OP: {'name': 'Madhev', 'age': 40, 'job': 'Data Engineer'}
``` 

---

### **How Do we Instantiate a Class in Python?**

- Creating a new object from a class is called instantiating a class.
- We can create a new **_object_** by typing the name of the class, followed by opening and closing parentheses `Employee(arg1,arg2,...)`.
- To instantiate this Employee class, we need to provide values for name & age. If we don’t, then Python raises a TypeError:

```py
  class Employee:
    office_branch = "India"
    def __init__(self, name, age):
      self.name = name
      self.age = age

  Employee() # op: TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'.

  #To pass arguments to the name and age parameters, put values into the parentheses after the class name:
  raghav = Employee("Raghav Mohan", 25)
  shyam = Employee("Shyam Murti", 32)

  # After we create the Employee instances, we can access their 'instance attributes' using dot notation:
  print(raghav.name) #op: "Raghav Mohan"
  print(shyam.age) #op: 32

  # we can access 'class attributes' the same way:
  print(raghav.office_branch) #op: "India"
  print(shyam.office_branch) #op: "India"
```

- One of the biggest advantages of using **_classes_** to organize data is that instances are guaranteed to have the attributes we expect. All Empolyee instances have `.office_branch`, `.name`, and `.age` attributes, so we can use those attributes with confidence, knowing that they’ll always return a value.
- Although the attributes are guaranteed to exist, their values can change dynamically:

```py
  shyam.name = "Govind Damodar"
  print(shyam.name) #op: "Govind Damodar"
  raghav.age = 55
  print(raghav.age) #op: 55
  shyam.office_branch = "USA (Head Office)"
  print(shyam.office_branch) #op: "USA (Head Office)"

```

> The key takeaway here is that custom objects are **mutable** by default.
> An object is mutable if we can alter it dynamically. For example, lists and dictionaries are mutable, but strings and tuples are immutable.

---

### ⚙ methods of class :
1. Class Methods
2. Instance Methods
3. Static Methods
4. Special or Dunder Methods

#### 1. **Class Methods** with @classmethod :
- A class method is a method that takes the class object as its first argument instead of taking self. In this case, the argument should be called cls, which is also a strong convention in Python.
- we can create class methods using the `@classmethod` decorator. Providing our classes with multiple constructors is one of the most common use cases of class methods in Python.
```py
  class Employee:
    founded_year: int = 2010  
    def __init__(self, name: str, age: int, job: str, join: str):
      self.name : str = name
      self.age : int = age
      self.job : str = job
      self.joined : str = join
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
```

#### 2. **Instance Methods**
- In a class, an instance method is a function that takes the current instance as its first argument.
- **_Instance methods_** are **_functions_** that we define inside a class and can only call on an instance of that class.
- Just like `.__init__()`, an **_instance method_** always takes `self` as its first parameter.

```py
  class Employee:
    office_branch = "India branch"

    def __init__(self, name, age):
      self.name = name
      self.age = age

    # Instance method:
    def greeting(self):
      return f"Jay Jay Ram Krushna Hari dear {self.name}! Welcome to {self.office_branch} office."

    # Another Instance method:
    def naam_kirtan(self, naam):
      return f"{self.name} sings '{naam}.'"

  vithu = Employee("Vitthal Patil", "28 Yug")
  vithu.greeting()  # "Jay Jay Ram Krushna Hari dear Vitthal Patil! Welcome to India branch office."

  vithu.naam_kirtan("Shree Dnyanoba mauli Tukaram") # Vitthal Patil says 'Shree Dnyanoba mauli Tukaram.'

```

- This Employee class has two instance methods:
  1. `.greeting()` returns a string displaying the name and the office_branch of the employee.
  2. `.naam_kirtan()` has one parameter called `naam` and returns a string containing the employee’s name and the 'naam' that the employee sings.

```py
  print(vithu) # op: <__main__.Employee object at 0x00aeff70>
```

- When we print miles, we get a cryptic-looking message telling us that vithu is a Employee object at the memory address 0x00aeff70. This message isn’t very helpful.
- We can change what gets printed by defining a special instance method called `.__str(self)__`.

```py
  # when we change the name of the Employee class’s .greeting() method to .__str__():
  class Employee:
    office_branch = "India branch"
    # .....

    def __str__(self):
      return f"Jay Jay Ram Krushna Hari dear {self.name}! Welcome to {self.office_branch} office."

    # .....

  keerti = Employee("Keerti Pande", 30)
  print(keerti) # op: Jay Jay Ram Krushna Hari dear Keerti Pande! Welcome to India branch office.
```

#### 3. **Static Methods** with @staticmethod :
- These methods don’t take the instance or the class as an argument. So, they’re regular functions defined within a class. We could’ve also defined them outside the class as stand-alone function.
```py
  class Employee:
    # ....
    # ...
    @staticmethod
    def show_intro_msg(name:str):
      print(f"Hello {name}! This your own info.")
```

#### 4. Special Methods and Protocols or Dunder/magic methods:
- Python supports what it calls special methods, which are also known as dunder or magic methods. These methods are typically instance methods, and they’re a fundamental part of Python’s internal class mechanism. They have an important feature in common: Python calls them automatically in response to specific operations.
1. `.__init__()`: this method works as the instance initializer. Python automatically calls it when you call a class constructor.
2. `.__str__()` and `.__repr__()` methods provide string representations for our instance objects. 
- The `.__str__()` method provides what’s known as the informal string representation of an object. This method must return a string that represents the object in a user-friendly manner. You can access an object’s informal string representation using either `str()` or `print().`

---

### **How Do We Inherit From Another Class in Python?**
1. Simple Inheritance / single-base inheritance
2. 

- **Inheritance** is a powerful feature of **object-oriented programming**. 
- It consists of creating hierarchical relationships between classes, where **child classes** inherit **attributes** and **methods** from their **parent class**. 
- In Python, **one class** can have **multiple parents** or, more broadly, ancestors.
- This is called **implementation inheritance**, which allows us to reduce duplication & repetition by code reuse. It can also make your code **more modular**, **better organized**, and **more scalable**. 
- Inheritance is a great tool for **code reuse**. Subclasses will inherit and reuse functionality from their parent.
- Parent classes typically provide **generic and common functionality** that we can **reuse** throughout **multiple child classes**. 
- Child is the class that **inherits features and code** from Parent. 

> Note: 
> 1. Parent class == superclass == base class
> 2. child class == derived class == subclass

1. Simple Inheritance / single-base inheritance
- When we have a class that inherits from a single parent class, then we’re using **single-base inheritance** or just **simple inheritance**. 
- To make a Python class inherit from another, we need to list the parent class’s name in parentheses after the child class’s name in the definition.

```py
  class Parent:
    hair_color = "black"
    speak = ["Marathi"]

  class Child(Parent):
    speak = ["Marathi", "Hindi"] # Here, we have overridden the speak attribute, (Not a best practice...)

  print(parent.hair_color) # op: black
  print(child.hair_color) # op: black
  # Because child classes take on the attributes and methods of parent classes, Child.hair_color is also "black" without our explicitly defining that

  print(parent.speak)   # op : ["Marathi"]
  print(child.speak)  # op : ["Marathi", "Hindi"]
  # Because in Child class we overridden the speak attribute, (It is said to be bad practice ❌)
```

- Child classes can override or extend the attributes and methods of parent classes.
- In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.
- The built-in `super()` function allows we to access members in the superclass, as its name suggests.

```py
  class Parent:
    languages_speak = ["Marathi"]
    #......
    def speak(self, language):
      return f"I speak {languages_speak[0]}"

  class Child(Parent):
    languages_speak = ["Marathi", "Hindi", "English"]
    #.....
    def speak(self, language="Sanskrut")
      return super().speak(language)

  child = Child()
  print(Child.languages_speak) # op: ["Marathi", "Hindi", "English"]
  # Because child classes take on the attributes and methods of parent classes, Child.hair_color is also "black" without our explicitly defining that
```

> All objects created from a child class are instances of the parent class.

### 
