#make software for students 
#1)register students
#2)show all students detail
#3)student by id 
#4)find topper
#5)find failed student >33
#6)exit
class student:
    def __init__(self,id,name,number,marks):
        self.id=id
        self.name=name
        self.number=number
        self.marks=marks
    def show(self):
        print('id =',self.id,'name =',self.name,'number =',self.number,'marks =',self.marks)
    def fail(self):
        if self.marks<=33:
            print(self.name,'is fail','   marks=',self.marks)
print('enter 1 to register students')
print('enter 2 to fetch all students')
print('enter 3 to find student by id')
print('enter 4 to find topper student')
print('enter 5 to find fail students')
print('enter 6 to exit')
n=0
students=[]
try:
    while n!=6:
        c=0
        n=int(input('enter your choice:-'))
        if n>6 or n<0:
            print('invalid input')
            n=6
        if n==1:
            students.append(student(int(input('enter student id:-')),input('enter the name:-'),int(input('enter student number:-')),int(input('enter student marks:-'))))
        if n==2:
            for i in students:
                i.show()
        if n==3:
        #getting error because of the student[i] the value we need we are not getting it 
            find=int(input('enter student id:-'))
            for j in students:
                if find==j.id:
                    j.show()
                    c=1
            if c==0:
                print('no student with this roll number')
        if n==4:
            topper=students[0]
            for i in range(0,len(students)):
                if topper.marks<students[i].marks:
                    topper=students[i]
            topper.show()
        if n==5:
            for i in range(0,len(students)):
                if c==0:
                    students[i].fail()
                    c=1
            if c==1:
                print('every student is pass')

except ValueError:
    print('only enter numbers')
