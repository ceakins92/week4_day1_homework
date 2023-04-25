# Write a function that accepts an array of 10 integers(between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# => returns "(123) 456-7890"
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

# Over-all: O(n)
def create_phone_number(n):
    phone = "".join([str(i) for i in n])  # O(n)
    return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"  # O(1)

#
#
#
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

# Over-all: O(N)


def check(seq, elem):
    if elem in seq:  # O(n)
        return True  # O(1)
    else:
        return False  # o(1)


# Given an array (arr) as an argument complete the function countSmileys that #should return the total number of smiling faces.
#
# Rules for a smiling face:
# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a #nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) #or D
# No additional characters are allowed except for those mentioned.
# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# THIS DIDN'T WORK, BUT I CAN'T FIGURE OUT WHY. IT DOESN'T CAPTURE ALL OCCURENCES
# def count_smileys(arr):
#    count = 0
#    if arr == None:
#        return '0'
#    faces = [':)', ':-)', ':~)', ';-)', ';~)', ';)',
#             ':D', ';D', ':~D', ':-D', ';-D', ';~D']
#    for face in faces:
#        if face in arr:
#            count += 1
#    return count

# I GOT THIS ONE TO WORK THO
# Overall  O(n^2)
def count_smileys(arr):
    faces = []  # O(1)
    for things in arr:  # O(n)
        if len(things) == 2 and things[0] in [":", ";"] and things[-1] in [")", "D"]:
            faces.append(things)  # O(n)
        elif len(things) > 2 and things[0] in [":", ";"] and things[1] in ["-", "~"] and things[-1] in [")", "D"]:
            faces.append(things)  # O(n)
    return len(faces)  # O(1)
# I know there's a shorter way to do this.
#
#
#
# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses #the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

# Overall O(n)


def is_pangram(string):
    alph_set = set(letter for letter in 'abcdefghijklmnopqrstuvwxyz')  # O(1)
    return len(alph_set.difference(set(string.lower()))) < 1  # O(n)
