class Person():
    def __init__ (self, fname, lname):
        self.fname = fname
        self.lname = lname
        return
    
    def printFullName(self):
        return

class Student(Person):
    def __init__ (self, fname, lname, studID, hg):
        super().__init__(fname, lname)
        self.studID = studID
        self.hg = hg
        self.subject = []
        return

    def enrolClass(self):
        s1 = subject()
        s1.subjectName = subjectName
        s1.StudentID = studID
        subjects.append(s1)

    def showClasses(self):
        for sub in subjects:

class Subject():
    def