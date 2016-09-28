# Phyllis Torres
# Dictionary excerises

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Instructions:
# Create a dictionary named holidays that pairs the name of
# the holiday with the date it will occur this year, include at least four
# key-value pairs
# example: holiday = {'Independence Day':  'July 4'}
print color.BOLD + '\nChapter 11: Dictionary Exercises\n' + color.END
print('Phyllis Torres\n')
print('Due Date: October 13, 2016\n\n\n')
print color.BOLD + 'Task 1: Create and print a dictionary of holidays and the date it occurs in the year 2016.\n' + color.END
holidays = {'New Years Eve': 'January 1', 'Valentines Day': 'February 14', 'St. Patricks Day': 'March 17',
            'April Fools Day': 'April 1', 'Memorial Day': 'May 29', 'Indepenence Day': 'July 4', 'Labor Day': 'September 5',
            'Columbus Day': 'October 10', 'Halloween': 'October 31', 'All Saints Day': 'November 1',
            'Christmas Day': 'December 25'}

# print holiday -  does the order match what you put it in?
print color.YELLOW + str(holidays) + color.END

# Answer: No, the order does not match how it was entered into the dictionary
print('\nWhen printing a dictionary, the order in which it is printed out is unpredictable. The '
      'holidays dictionary was created in chronological order, but it prints out very differently.')

# run the len function on holiday - how does it calculate the results? ** print(len(holiday))
print("\n\n")
print color.BOLD + 'Task 2: Run the "len" function on the holidays dictionary created in Task 1.\n' + color.END
print('\nThe "len" function returns the number of key-value pairs of a dictionary and not the individual elements.')
print('The result of the "len" function on the holidays dictionary is: '),
print color.YELLOW + str(len(holidays)) + color.END

# Answer: The len function calculates the number of key-value pairs not the individual elements in the dictionary.

# Write the code to use the "in" function to find one of the keys in your dictionary. Make sure to surround the
# code with a print statement so that the result prints on screen
print("\n\n")
print color.BOLD + 'Task 3: Create code that uses the "in" function to find one of the keys in the holidays dictionary.' + color.END
print('\nThe key that will be used is: April Fools Day.')
print('The result of the "in" function is: '),
print color.YELLOW + str('April Fools Day' in holidays) + color.END

# now write the code to look for a key that is not in the dictionary. Make sure to surround the code
# with a print statement so the result prints on screen
print("\n\n")
print color.BOLD + 'Task 4: Create code that uses the "in" function to look for a key that will not be ' + color.END
print color.BOLD + 'found in the holidays dictionary.' + color.END
print('\nThe key that will be used is: Veterans Day.')
print('The result of the "in" function is when the key does not exist is: '),
print color.YELLOW + str('Veterans Day' in holidays) + color.END

# now write the code to find a value in your dictionary, use the print statement to show the results
print("\n\n")
print color.BOLD + 'Task 5: Create code to find a value in the holidays dictionary.' + color.END
print('\nThe value to be found in dictionary is: May 29.')
vals = holidays.values()
print('The result of using the "values" function and then the "in" function is: '),
print color.YELLOW + str('May 29' in vals) + color.END

# print all of the values in the dictionary
print("\n\n")
print color.BOLD + 'Task 6: Print all the values in the holidays dictionary.\n' + color.END
print color.YELLOW + str(vals) + color.END

# 11.2 Looping and Dictionaries
# Write the histogram code and test it by passing in a word that has at least two of one letter
# Print the result of running the histogram code
print("\n\n")
print color.BOLD + 'Task 7: Copy histogram code from section 11.2. The histogram function will create a ' + color.END
print color.BOLD + 'dictionary of the letters in the word passed to the function and will tally the ' + color.END
print color.BOLD + 'number of times each letter is found in the word.' + color.END
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

results = histogram('supercalifragilisticexpialidocius')
print('\nThe word used in this task is: supercalifragilisticexpialidocius\n')
print color.YELLOW + str(results) + color.END

# Exercise 11.2 Rewrite the histogram code using the get method, test with the same word, name the function histogram2
# hint assign the result of d.get(c,0) to a value then add one to the value of d[c]
print("\n\n")
print color.BOLD + 'Task 8: Rewrite the histogram code from section 11.2 using the "get" method, pass it the ' + color.END
print color.BOLD + 'same word used in Task 7, and print result of the function.\n' + color.END
def histogram2(x):
    d2 = dict()
    for c in x:
        d2[c] = d2.get(c, 0) + 1
    return d2

results2 = histogram2('supercalifragilisticexpialidocius\n')
print color.YELLOW + str(results2) + color.END

# Looping and Dictionaries
# use a for statement to print your holiday dictionary
# What prints? The keys or the values?
print("\n\n")
print color.BOLD + 'Task 9: Use a "for" statement to print the holidays dictionary.\n' + color.END
def print_d(h):
    for k in h:
        print color.YELLOW + str(k) + color.END

print_d(holidays)
print('\nIf the key is in the print statment, the results of using the "for" statement is to print out only the dictionary keys.')
print('The value could also be included in the print statement to display both the keys and the values. Note, once again,')
print('the display of the dictionary contents is unpredictable.')
# Answer: It depends on what is specified. If the keys are in the print statement, only the keys are printed out. The
# values could be added to the print statement to print out at the same time.

print ("\n\n")  # leave this code so that there are blank lines before the next exercise
# now write code that prints all of the keys and all of their values in the holiday dictionary
# if you use the print statement then values separated by commas they appear on the same line
print color.BOLD + 'Task 10: Modify code from Task 9 to print the keys and the values of the holidays ' + color.END
print color.BOLD + 'dictionary.\n' + color.END
def print_d2(h):
    for k in h:
        print color.YELLOW + str(k) + ', ' + str(h[k]) + color.END

print_d2(holidays)

print ("\n\n")  # leave this code so that there are blank lines before the next exercise
# Reverse Lookup
# Type the code for the Reverse Lookup from 11.3 below
print color.BOLD + 'Task 11: Type the code for a reverse lookup function from section 11.3, test the code by calling it with' + color.END
print color.BOLD + 'the holidays dictionary and one of the values in the dictionary, and print the result.' + color.END
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value not found in dictionary')

# Test the code by calling it with the holiday dictionary and one of your values (print the result)
result3 = reverse_lookup(holidays, 'October 31')
print('\nThe value passed to the reverse lookup function is: October 31.')
print('\nThe result of calling the reverse lookup function is: '),
print color.YELLOW + str(result3) + color.END

# Call the code a second time with a value that doesn't exist, run the program
print ("\n\n")
print color.BOLD + 'Task 12: Call the reverse lookup function a second time with a value that does not' + color.END
print color.BOLD + 'exist in the dictionary. The value used was January 24. The result was an error message.' + color.END
print color.BOLD + 'The error returned was a LookupError with the added message: value not found in dictionary. ' + color.END
print color.BOLD + 'This code was commented out in order to continue with the remaining exercises.' + color.END

# the following code was run to look up a value that does not exist in the dictionary
# result4 = reverse_lookup(holidays, 'January 24')
# print(result4)

# Copy and paste the error code here, add # as needed to make the error a comment

# Traceback (most recent call last):
#  File "C:/Users/mrspa_000/Desktop/PRG105/dictionaries-1.py", line 106, in <module>
#    result4 = reverse_lookup(holidays, 'January 24')
#  File "C:/Users/mrspa_000/Desktop/PRG105/dictionaries-1.py", line 99, in reverse_lookup
#    raise LookupError('value not found in dictionary')
# LookupError: value not found in dictionary

# leave the line of code that caused the error, but put a # in front of it to make it a comment
# see above

# 11.4 Dictionaries and lists
# Type in the code to invert a dictionary
# Call the invert_dict function with the holiday dictionary
# print the results
print ("\n\n")
print color.BOLD + 'Task 13: Type the code to create a function to invert a dictionary from section 11.4, ' + color.END
print color.BOLD + 'call that function with the holidays dictionary, and print the results.\n' + color.END
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

print('The results of calling the function to invert the dictionary are: \n')
inverse_results = invert_dict(holidays)
print color.YELLOW + str(inverse_results) + color.END

# Exercise 11.5 Exercise 11.5. Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict. Solution: http://thinkpython.com/code/invert_dict. py .
print ("\n\n")
print color.BOLD + 'Task 14: Rewrite the invert dictionary function using the "setdefault" method and print the results.\n' + color.END
def invert_dict2(d):
    inverse2 = dict()
    for key in d:
        val = d[key]
        inverse2.setdefault(val, []).append(key)
    return inverse2
print('The results of calling the function to invert the dictionary that uses a setdefault method are: \n')
inverse_results2 = invert_dict2(holidays)
print color.YELLOW + str(inverse_results2) + color.END
