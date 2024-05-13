class Calculator:
  def __init__(self, version: float):
    self.version = version
  
  def description(self) -> str:
    ur_version_info = f'You are using version: {self.version}'
    print(ur_version_info)
    return ur_version_info

  @staticmethod
  def add_numbers(*numbers: float) -> float:
    # print(numbers)
    result: float = 0
    if numbers:
      for num in numbers :
        result += num

    return result


c1 = Calculator.add_numbers(20,3.0,5.2,5.8)
print(c1)