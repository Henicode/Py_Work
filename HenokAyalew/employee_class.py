# Employee Information 

from typing import Iterable


class employee:

    Salary = float()

    def __init__(self,Name,Sin_Number,Role,Salary,Date_of_Birth,Address):
        self.Name = Name
        self.Sin_Number = Sin_Number
        self.Role = Role
        self.Salary = Salary
        self.Date_of_Birth = Date_of_Birth
        self.Address = Address

    def increaseSalary(self):
        self.Salary = self.Salary(*1.7)

    def decreaseSalary(self):
        self.Salary = self.Salary(*0.5)

    def changeRole(self,newRole):
        self.Role = newRole

    def changeAddress(self, newAdress):
        self.address = newAdress

    def chageSalary(self, newSalary):
        self.Salary = newSalary



Henok = employee("Henok Ayalew", "938-845-824", "Student", "178,900.0", "12 Jan 1999", "1723 Westpoint SW")

print("Emplouee card:{}",Henok.Sin_Number)
print("Name: ",Henok.Name)
print("Salary: USD",Henok.Salary)
print("Role:",Henok.Role)
print("Date of Birth:",Henok.Date_of_Birth)
print("Address:",Henok.Address)


Henok.increaseSalary()
print("Salary increased by 17%: USD {}",Henok.Salary)

Henok.decreaseSalary()
print("Salary decreased by 5%: USD {}",Henok.Salary)

Henok.chageSalary(900000)
print("Salary change: USD",Henok.Salary)


Henok.changeRole("Instructor")
print("New Role:",Henok.Role)

Henok.changeAddress("183 spin SE")
print("New Address:",Henok.address)



