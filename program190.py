# Create an outer function that accepts two parameters, a and b. Inside, 
# create an inner function that calculates the addition of a and b.
# The outer function should then add 5 to that sum and return the final result.
def outfunc(a,b):
    def infunc(a,b):
        sum=a+b
        return sum
    add=infunc(a,b)
    return add+5
print(outfunc(5,6))