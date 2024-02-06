#Function to check the intersection of chordes
def doesIntersect(result_chordes):
    # Extracting the end character of each key
    end_characters = [key[-1] for key in result_chordes.keys()]

    if end_characters[0]==end_characters[2] and end_characters[1]==end_characters[3]:
        return True
    else:
        return False


# Example 1:
#radian_list = [0.9, 1.3, 1.70, 2.92]
#chord_identifiers = ["s_1", "e_1", "s_2", "e_2"]
    
# Example 2: 
#radian_list = [0.78, 1.47, 1.77, 3.92]
#chord_identifiers = ["s_1", "s_2", "e_1", "e_2"]

#Example 3: 
radian_list = [0.78, 1.47, 1.77, 3.92, 2.25, 4.68, 5.34, 6.81, 0.95, 2.72]
chord_identifiers = ["s_1", "s_2", "e_1", "e_2", "s_3", "e_3", "s_4", "e_4", "s_5", "e_5"]

# Creating a dictionary using zip
result_dict = dict(zip(chord_identifiers, radian_list))

# Printing the resulting dictionary
#print(result_dict)

# Sorting the dictionary by keys
sorted_dict_by_keys = dict(sorted(result_dict.items()))
#print(len(sorted_dict_by_keys))

# Creating lists for keys and values
iden_list = list(sorted_dict_by_keys.keys())
rad_list = list(sorted_dict_by_keys.values())

# Defining length for parse 
n2 = int(len(iden_list)/2)

# Initialize intersections
intersect =0

for i in range(0, n2 - 1 ):
    for j in range(i+1, n2):
        chordes_i  = [iden_list[i], iden_list[i+n2], iden_list[j], iden_list[j+n2]]
        chordes_r  = [rad_list[i], rad_list[i+n2], rad_list[j], rad_list[j+n2]]
        result_chordes = dict(zip(chordes_i, chordes_r))
        result_chordes = sorted_dict_by_values = dict(sorted(result_chordes.items(), key=lambda item: item[1]))

        if doesIntersect(result_chordes)==True:
            intersect = intersect + 1
        result_chordes= []

#Prints the total intersections
print("Total inserctions: ", intersect)

