from decimal import Decimal 
from decimal import getcontext

number = Decimal(input("Число: "))
getcontext().prec = 4              
print(number.quantize(Decimal('1.000')))



# соответственно меняем точность на 3 и меняем в принте десимал 1.00 и так далее ( пока так разобрался)