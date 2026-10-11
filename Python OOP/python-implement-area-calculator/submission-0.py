import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, a, b=None):
        if b==None:
            return round((math.pi * a**2), 2)
        else:
            return (a * b)
        
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
