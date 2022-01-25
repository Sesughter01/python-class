s1 = "Ault"
s2 = "Kelly"
s3 = s1[:2]
s4 = s1[2:]
s5 = s3 + s2 + s4
# my_list = s3.split()
# print(s5)

# Output all the occurences of USA 
str1 = "Welcome to USA. usa awesome,isn;t it?"
str2 = str1.lower()
# str2 = str1.split()
# usa_strs = str2[2:4]
str3 = str2.count("awesome")
# print(str3)

# Given: a string write a programme to find the position of a substring emma in the given sting
str6 = "Emma is a data scientist who knows Python. Emma works at google."
str7 = str6.rindex("Emma")
# print("last occurrence of Emma starts at index %s" % (str7))

# Turn the given string with dashes to one without dashes
str8 = "Emma-is-a-data-scientist"
str9 = str8.replace("-"," ")
# print(str9)

# Remove all special characters from string 

new_str = "/*Jon is @developer & musician"
new_str2 = new_str.replace("/"," ").replace("*"," ").replace("@"," ").replace("&"," ")
# print(new_str2)
