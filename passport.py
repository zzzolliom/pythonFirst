
vises=["1 week","1 month","6 months","1 yeahr","2 yeahrs","4 yeahrs"]
class Pasport():
    def __init__(self,name,sname,year_of_birth,country,number):
        self.name= name
        self.sname=sname
        self.year_of_birth=year_of_birth
        self.country=country
        self.number=number

    def print_info(self,obj):
        print(obj.__dict__)


class ForgeinPassport(Pasport):
    def __init__(self,name,sname,year_of_birth,country,number,visa=1):
        self.name = name
        self.sname = sname
        self.year_of_birth = year_of_birth
        self.country = country
        self.number = number
        self.visa=visa
    def print_info(self,obj):
        print(obj.__dict__)

p=Pasport("ОLYA","ZUB","1986","RUS",111111)
p.print_info(p)

f=ForgeinPassport("ОLYA","ZUB","1986","RUS",111111,vises[0])
f.print_info(f)