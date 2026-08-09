#average by using class and objects 
class Student:
    def __init__(self,name,markslist):
        self.name=name
        self.marks=markslist
    def average(self):
        sum=0
        length=len(self.marks)
        for marks in self.marks:
            sum=marks+sum
        average=sum/length
        print("average is ",average)

student1=Student("bhuvnesh",[79,65,87,78,97])
student1.average()