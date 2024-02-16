calculus=eval(input('Enter your Marks (Applied Calculus): '))
ict=eval(input('Enter your Marks (I.C.T): '))
islamiyat=eval(input('Enter your Marks (Islamiyat): '))
programming=eval(input('Enter your Marks (Programmming Fundamentals): '))
english=eval(input('Enter your Marks (English): '))
a=(calculus,ict,islamiyat)
b=(programming,english)
c=sum(a)
d=sum(b)
grade={
    80:'A+ Grade',
    70:'A Grade',
    60:'B Grade',
    50:'C Grade',
    40:'Fail'
}
total_marks = (c+d)
if total_marks>=80:
    print('Marks: ',total_marks)
    print('Grade: ',grade[80])
elif total_marks>=70:
    print('Marks: ',total_marks)
    print('Grade: ',grade[70])
elif total_marks>=60:
    print('Marks: ',total_marks)
    print('Grade: ',grade[60])
elif total_marks>=50:
    print('Marks: ',total_marks)
    print('Grade: ',grade[50])
else:
    print('Marks: ',total_marks)
    print("Grade: D Fail :)")