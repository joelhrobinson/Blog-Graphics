# simple function call
# Declare a variable and initialize it
# change variable inside subfunction 
f = 101
print ("GLOBAL Value of f is ",f )
# Global vs. local variables in functions
def subFunction():
# global f
    f = 'Python'
    print ( "Subfunction value of f is ", f)

#-------------------------------------------------
subFunction()       # invoke the function
#print ("Main function the Value of f is ",f )