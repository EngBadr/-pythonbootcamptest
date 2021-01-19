#import the package numpy and make the shortcut "np" for it.
import numpy as np

#Write the code that will produce the requested output or action as you see on the following cell
print ('Hello, Badr Alharbi!')

#define a numpy array [1, 2, 3, 4, 5] and assign it to variable x

x=np.array([1,2,3,4,5])
#Print x
print ('define a numpy array [1, 2, 3, 4, 5] and assign it to variable x')
print(x)

#Print the mean of x using numpy
print ('Print the mean of x using numpy')
print(np.mean(x))

#Print the maximum number in array x
print('Print the maximum number in array x')
print(x.max())

#Generate a random number between 35 and 40

print('Generate a random number between 35 and 40')
print(np.random.randint(35,40))

#generate a list (N) of 1000 numbers with random values between 100 and 150
arra_list=100 + np.random.randint(50,size=1000)

print('A list of 1000 numbers with random values between 100 and 150')
print(arra_list)

# get the mean, median, std, and variance of the list N
print('Mean of N')
print(np.mean(arra_list))
print('median of N')
print(np.median(arra_list))
print('std of N')
print(np.std(arra_list))
print('variance of N')
print(np.var(arra_list))

# generate a 2D array of size 3 x 4 of random numbers between 18-65
tow_d_Arr=np.random.randint(18,65,size=12).reshape(3,4)
print('generate a 2D array of size 3 x 4 of random numbers between 18-65')
print(tow_d_Arr)


#Get the mean for every columns N

print('Get the mean for every columns N')
print(np.mean(tow_d_Arr,0))



#Get the mean for every row of N
print('Get the mean for every row of N')

print(np.mean(tow_d_Arr,1).reshape(3,1))

#Create the following 2D array (S) of students grade in a classroom
print ('Create the following 2D array (S) of students grade in a classroom')
grades = np.array([[20, 15, 40],[25, 24, 35],[21, 15, 25]])

print(grades)

print('Get the sums of student grades in S')
print(np.sum(grades,1).reshape(3,1))

#Get the means of student grades in every activity (coursework, midterm exam,final exam) in S

print('Get the means of student grades in every activity (coursework, midterm exam,final exam) in S')
print(np.mean(grades,1).reshape(3,1))

#reshape S in a way that make the colums represent the students and rowsrepresent the activity, as follow
print('reshape S in a way that make the colums represent the students and rowsrepresent the activity, as follow')
print(np.transpose(grades))
