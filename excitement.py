# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    
    message = "I am super excited for this course!"

    array = [message] * 5

    return array[0] + " " + array[1] + " " + array[2] + " " + array[3] + " " + array[4]

print(show_excitement())

