'''
List operations qiuestions
 



'''

string  = ['English' , 'Hindi' , 'Mathematics', 'Physics', 'Chemistry']

new_string_dict = {i : int(input( i +" marks : ")) for i in string}

#for i in string:
    
#    marks_input = input('Enter marks of subject  ' + i + " ")
#    s = {i : int(marks_input)}

print(new_string_dict)
