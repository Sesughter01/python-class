# 
# set_universal = set_english.union(set_french)
total_english = 9
list_english = [1,2,3,4,5,6,7,8,9]
total_french = 9
list_french = [10,1,2,3,11,21,55,6,8]

conv_list_en = set(list_english)
conv_list_fren = set(list_french)
total_num = conv_list_en.symmetric_difference(conv_list_fren)
total_num2 = conv_list_en.union(conv_list_fren)
total = len(total_num2)
print(total)

#### If 
