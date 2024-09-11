def divide_numbers(numerator,denominator):
    
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        return "Error:Division by zero is not allowed."
    else:
        return f"The result is {result}"

numerator = 10
denominator = 0
print(divide_numbers(numerator,denominator))















































"""

class Grt_cmn_dsr():
    def __init__(self):
        pass
    def gcd(self,val1,val2):
        if val1 == 0:
            return val2
        elif val2 == 0:
            return val1
        else:
            return self.gcd(val2 , val1 % val2)

my_gcd = Grt_cmn_dsr()
val1 ,val2 = 30,15
print(f"The Greatest Common Divisor of {val1} and {val2} is:"
      ,my_gcd.gcd(val1,val2))
"""
