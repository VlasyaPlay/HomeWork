#1
immutable_var=(1,4,'String',True)
print(immutable_var)
#immutable_var [4] = 100
#print(immutable_var) #картеж относится к неизменяемым типам данных

#2
mutable_list=[5,9,'String',False]
print(mutable_list)
mutable_list[0] = 10
mutable_list[1] = 'apple'
mutable_list[2] = 23
mutable_list[3] = True
print(mutable_list)