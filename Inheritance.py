##'''
##Inheritance :
##                there are some basic type of inheritance those are listed bellow
##                single inheritance
##                multilevel inheritance 
##                multiple inheritance
##                hierarchical inhertance
##                hybrid inhertance
##'''

#single inheritance

class Input:
    def __init__(a):
        a.num1 = 56
class Output(Input):
    def __init__(a):
        a.num2 =45
        super().__init__()
        print('This is single inhertance')
        print(a.num1+a.num2)
        

p=Output()

#------------------------------------------------------------------------------------
#multilevel inheritance
class Input1:
    def __init__(a):
        a.num1 = 56

class Input2(Input1):
    def __init__(a):
        Input1.__init__(a)
        a.num2 = 65
        
class Output(Input2):
    def __init__(a):
#there are two ways to0 access information about the parent classess 
#..........
        #one is this one below 
        #Input1.__init__(a)
        #Input2.__init__(a)
#.........
        #second is the call constructor in father to grandfather and 
        #call super() in the most child class.
        super().__init__()
        print('this is multilevel inhertance')
        print(a.num1+a.num2)

p=Output()

#------------------------------------------------------------------------------------
#multiple inheritance

class Input1:
    def __init__(a):
        a.num1 = 56

class Input2:
    def __init__(a):
        a.num2 = 65
        
class Output(Input1,Input2):
    def __init__(a):
        Input1.__init__(a)
        Input2.__init__(a)
        #a.num2 =45
        print('This is multiple inhertance')
        print(a.num1+a.num2)

p=Output()

#------------------------------------------------------------------------------------
#hierarchical inhertance

class Input1:
    def __init__(a):
        a.num1 = 56

class Output1(Input1):
    def __init__(a):
        #Input1.__init__(a) or
        super().__init__()
        num2 = 65
        print('Because this is hierarchical inhertance hereis 2 outputs ')
        print(a.num1+num2)
        
class Output2(Input1):
    def __init__(a):
        #Input1.__init__(a) or
        super().__init__()
        num2=66
        
        print(a.num1+num2)

p=Output1()
q=Output2()

#----------------------------------------------------------------------------------
#hybrid inheritance

class Input1:
    def __init__(a):
        a.num1 = 56

class Output1(Input1):
    def __init__(a):
        #Input1.__init__(a) or
        super().__init__()
        a.num2 = 65
        a.sum_out1= a.num1+a.num2
        print('Because this is hybrid inhertance here is 1 parent then two chid the 1 child ')
        print(a.num1+a.num2 )
       # print('Output 1')
        
class Output2(Input1):
    def __init__(a):
        #Input1.__init__(a) or
        super().__init__()
        a.num2=66
        a.sum_out2=a.num1+a.num2
        print(a.num1+a.num2)
       # print(end=' '+ 'Output2')

class MostchildClass(Output1,Output2):
    def __init__(a):
        Output1.__init__(a)
        Output2.__init__(a)
        last_child_sum = a.sum_out1+a.sum_out2
        print(last_child_sum)
        print('most child class')

#p=Output1()
#q=Output2()
r=MostchildClass()
