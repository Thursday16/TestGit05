import re

def check_coursecode(course_code):
   regex = r'\b[A-Z][A-Z][A-Z]+[0-9][0-9][0-9][0-9]\b'

   if (re.fullmatch(regex, course_code)):
      print("true")
# process
   else:
      print("false")


def check(email):

   regex = r'\b[A-Za-z0-9.%_$+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
   #{2,7} refers to the boundaries that the .com could only have 2-7 letters

   if (re.fullmatch(regex, email)):
      print("Valid Email")  # process

   else:
      print("Invalid Email")


# quit


def run():
   #check_coursecode(course_code="DEX2111")
   check(email="Percy2545@gmail.com")

