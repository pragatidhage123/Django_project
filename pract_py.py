'''def user_info(*args,name,**kwargs):
    total = 0
    for i in args:
        total += i
    print(f"the total of a numbers is =",total)
    #print(f"my name is {name}")
    
    for key,value in kwargs.items():
        print(f"my name is {name} and my {key} = {value}")
   
user_info(1,5,7,8,name="sia",age=20)'''

def add(num):
    def extra_info(*args):
        print('''this is add function''')
        num(*args)
    return extra_info
@add
def add(*args):
    total = 0
    for i in args:
        total += i
    print(f"the total of a numbers is =",total)
    
    
add(1,5,7,8)




