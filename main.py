n_days = int(input())
n_second = n_days * 60 * 60
v_hour = 38241 #miles per hour
v_second = v_hour/3600 #miles per second
length = v_second * n_second #in miles
print(f'in miles: {length}, in kilometers: {length * 1.609344}, in astronomical units: {length * 1.609344 * 149597870.7}')

