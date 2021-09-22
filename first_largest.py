"""
Python program to find the largest element and its location.
"""
def largest_element(a, loc=False):
    """ Return the largest element of a sequence a.
    """
    Largest_value = a[0]
    location = 0
    for i in range(1,len(a)):
        if a[i] > Largest_value:
            Largest_value = a[i]
            location = i
    if loc == True:
        return Largest_value,location
    else:
        return Largest_value


if __name__ == "__main__":

    a = [1,2,3,5,1]
    print("Largest element is {:}".format(largest_element(a)))
