#Make a class called Friend with the following conditions:
# - Name (string)
# - Age (integer)
# - Hobby (string either [Sport,Music,Reading,Computers])

# Make a class called Gift with the following conditions:
# - Name (string)
# - Category (string [Sport,Music,Reading,Computers])
# - Value (float)

# Now make a program that enters the number of friend N from the keyboard input
# and executes a loop to gather the information for all N friends
# then enters the max amount of money allowed to spend on gifts total_amount
# once the information is entered the program will assigned the perfect gift to
# every friend according with their hobby and the maximum amount of money to spend on all gift
# then prints the results on the screen
# Note: the list of gift with their information is hardcoded on the program you don't need
#  to enter it from the keyboard

name = ""
age = int 
hobby = ['Sport','Music','Reading','Computers']
value = float


class Friend:
    def __init__(self,name,age,hobby):
        self.name = name 
        self.age = age
        self.hobbie = hobby
        pass


class Gift:
    def __init__(self,name,category,value):
        self.name = name
        self.cetagory = category
        self.value = value
        pass


# move this method outside of the class by un-indenting back to the where this comment is 
# as is right now main is part of the gift class which is not a good idea since you have to create 
# a gift class to run it
    def main():
        freiend_n = int(input("number of friends: "))
        freiend_n = []
        for b in range(0, freiend_n):
            name = input("enter name: ")
            age = input("enter age: ")
            hobby, category = input("enter interest: ")
            value = input("value of gift")

Max_money =float(input("max money allowed to spend on gift : "))
print(Max_money)




