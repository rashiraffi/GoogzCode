import re

str = "The rain in Spain"
#Regular expression search
x = re.search("(\w+\s*\w+)\s", str)

print("The second white-space character is located in position:", x.start()) 
