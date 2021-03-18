#what is the score?
score = int(input("What is your test score?"))

#determine the grade
if score >= 90:
    print('Your grade is an A')
else:
    if score >= 80:
        print('Your grade is a B')
    else:
        if score >= 70:
            print('Your grade is a C')
        else:
            if score < 70:
                print('Retake this test')
                