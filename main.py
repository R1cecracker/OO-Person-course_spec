class Person():
    def __init__ (self, fname, lname):
        self.fname = fname
        self.lname = lname
        return
    
    def printFullName(self):
        print(f"{self.fname} {self.lname}")

class Student(Person):
    def __init__ (self, fname, lname, studID, hg):
        super().__init__(fname, lname)
        self.studID = studID
        self.hg = hg
        self.subject = []
        return
    
    def enrolClass(self, subjectName, studID):
        s1 = Subject(subjectName, studID)
        self.subject.append(s1)

    def ShowClasses(self):
        for i in range(len(self.subject)):
            print("Student ID: ", self.subject[i].studentID)
            print("Subject Name: ", self.subject[i].subjectName)
            print()
        return

class Parent(Person):
    def __init__(self, fname, lname, occupation, alumni):
        super().__init__(fname, lname)
        self.occupation = occupation
        self.alumni = alumni

class Subject():
    def __init__ (self, subjectName, studentID):
        self.subjectName = subjectName
        self.studentID = studentID

    def printStudentList(self):
        print(f"Student ID: {self.studentID}, Subject: {self.subjectName}")

#main
s1 = Student("Troy", "Harcoan", 12345, "heber")
s1.printFullName()
s1.enrolClass("Math Advanced", 12345)
s1.enrolClass("English Advanced", 12345)
s1.enrolClass("Physics", 12345)
s1.enrolClass("Ancient History", 12345)
s1.enrolClass("Music", 12345)
s1.enrolClass("Software Engineering", 12345)
s1.ShowClasses()