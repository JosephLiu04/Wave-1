Total = int(input('Please enter the amount of cents:'))
print(Total // 200 , "toonies")
Toonies = Total % 200
print(Toonies // 100 , "loonies")
Loonies = Toonies % 100
print(Loonies // 25 , "quarters")
Quarters = Loonies % 25
print(Quarters // 10  , "dimes")
Dimes = Quarters % 10
print(Dimes // 5 , "nickles")
Nickles = Quarters % 5
print(Nickles // 1 , "pennies")


