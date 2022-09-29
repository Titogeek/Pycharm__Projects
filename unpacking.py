my_siblings=['Mercy','Kelly','Esparanza','Kenan']
_1st,_2nd,_3rd,_4th = my_siblings
print(_1st)
print(_2nd)
print(_3rd)
print(_4th)

print(_1st + _2nd + _3rd + _4th)
print(_3rd,_4th)

def myfunct():
    global x
    x= " Is a Beast Brother"
myfunct()

print(_4th + x)

my_data = 5.4
print(type(my_data))

test_data = {"name": "The Great", "age": 36}
print(type(test_data))

tes_data2 = True
print(type(tes_data2))

test_data_3 = " What is your name dawg? "
print(len(test_data_3))
x = test_data_3.strip()
print(len(x))


test_data_4 = ['Mango' , 'Orange' ,'Pineapple' ,'Passion']
if "Mango" in test_data_4:
    print("Yes, Mango Is A fruit")
