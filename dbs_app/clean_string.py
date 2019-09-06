# =====================================================================================================
""" Cleans a given string by removing the Punctuation Marks and other non-alphabetic characters  """
# =====================================================================================================

import string
import re

def clean(s) :
   print("Initiated String cleaning...")
   #Converts all the alphabets to lowercase as well before returning
   print('\n')
   return re.sub('[^a-zA-Z]+',' ',str(s)).lower()

# =====================================================================================================