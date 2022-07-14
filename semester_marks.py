class Midterm:
    def midterm_marks(self):
        self.subjects = ['maths', 'chemistry', 'physics']
        #mid_marks = [ int(input("enter marks of " + subjects[i])) for i in subjects]
        i=0
        self.total_marks_mid=0
        while i<(len(self.subjects)):
            mid_marks_input=int(input("enter marks of " + self.subjects[i]))
            i+=1
            self.total_marks_mid+=mid_marks_input
         
        print(self.total_marks_mid)

class Semester(Midterm):
        def semester_marks(self):
             # subjects = ['maths', 'chemistry', 'physics']
            j=0
            self.marks_sem = 0
            while j<(len(self.subjects)):
                mid_marks_inputt=int(input("enter marks of " + self.subjects[j]))
                j+=1
                self.marks_sem+=mid_marks_inputt
            
            print(self.marks_sem)
        def semester_result(self):
            
            
            midterm_marks = (self.total_marks_mid*(100))/60
            semester_marks = (self.marks_sem*(100))/240
            total_marks = (self.total_marks_mid + self.marks_sem)/3
            print(total_marks)
            

#class Results_of_sem(semester):

p=Semester()
p.midterm_marks()
p.semester_marks()
p.semester_result()
