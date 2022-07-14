#Student result ...,.
class Students():
    def __init__(self , no_of_subjects):
            
            self.no_of_subjects = no_of_subjects
            self.marks_input = [int(input("Enter the Marks of Subject No : " + str(i)+ " ")) for i in range(1, no_of_subjects+1) ]
           # self.total_marks = sum(self.marks_input)
           # self.result = self.total_marks/no_of_subjects


                                                                        #for i in range(1,no_of_subjects+1):
                                                                          #  self.marks_input = int(input("Enter the Marks of Subject No " + str(i)))
                                                                        
                                                                      #  self.marks+= str(self.marks)
    def results(self):
        #totalmarks
        #totalmarks+= self.marks
        self.total_marks = sum(self.marks_input)
        self.result = self.total_marks/self.no_of_subjects
        print(str(self.result) + "%")
        self.division()
    def division(self):
        if self.result>=80:
            print("Your are first division pass")
        if self.result<80 and self.result>=60:
            print("Your are second division passs")
        if self.result<60 and self.result>=40:
            print("you are third division pass")
        if self.result<40:        
            print("You are fail")

subjects = int(input("Enter no of subjects : "))

p = Students(subjects)
p.results()





        
