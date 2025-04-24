import re
class emp:
    l=[]
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email

    def validaten(self):
        pattern = r"^[A-Z][a-z]+(?:[-'\s][A-Z][a-z]+)*$"
        while True:
            if re.match(pattern,self.name):
                break
            else:
                print("Invalid name. Please enter a valid employee name")
                self.name = input("1) Please enter employee name: ")
        return self.name
    
    def validatep(self):
        pattern = r'^\+91\d{10}$'

        while True:
            if re.match(pattern, self.phone):
                break
            else:
                print("Invalid phone number. Please enter a valid Indian phone number starting with +91 and 10 digits.")
                self.phone = input("1) Please enter your phone number: ")
        return self.phone
    
    def validatee(self):
        pattern = r'^[\w\.-]+@(?:gmail\.com|org\.in|hotmail\.com)$'

        while True:
            
            if re.match(pattern, self.email):
                break
            else:
                print("Invalid email. Please enter a valid email (gmail.com, org.in, or hotmail.com).")
                self.email = input("2) Please enter your email: ")
        return self.email
    
    def insert(self):
        k=[self.name,self.phone,self.email]
        emp.l.append(k)

    def display():
        print(emp.l)

    def add(self):
        self.name=self.validaten()
        self.phone=self.validatep()
        self.email=self.validatee()
        self.insert()




print("Hi, welcome to the employee details")
obj=emp("Vivek","+918332037033","sdfkb@gmail.com")
obj.add()
obj1=emp("Vinod","+918111037033","avfhkafqv@gmail.com")
obj1.add()
emp.display()
        




