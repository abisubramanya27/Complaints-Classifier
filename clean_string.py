import string
import re

def clean_string(s) :
    return re.sub('[^a-zA-Z]+',' ',str(s)).lower()
