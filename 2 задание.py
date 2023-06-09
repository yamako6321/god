import math
v_g = float(input()) #in gallons
v_l = v_g*3.78541 #in liters
n_brrls_of_oil = math.ceil(v_g/19.5) #rounding up
v_CO2 = v_g*20 #in pounds
BTU1 = 115000 #1 gallon of gasoline contains 115,000 BTUs of energy
BTU_g = v_g*BTU1
BTU2 = 75700 #1 gallon of ethanol contains 75,700 BTUs of energy
v_e = BTU_g/BTU2 #1 gallon ethanol
price = v_g*3 #in dollars USA
print(f'volume of gasoline in liters: {v_l}, \n'
      f'barrels of oil: {n_brrls_of_oil}, \n'
      f'volume of carbon dioxide: {v_CO2}, \n'
      f'equivalent volume of ethanol (gallons): {v_e}, \n'
      f'price: {price}')
