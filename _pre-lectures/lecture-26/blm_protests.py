from CSE8ACSV import *

blm_data = get_blm_data("blm_state.csv")

#print(blm_data)

##count = 0
##for row in blm_data:
##    print(row)
##    count += 1
##    if count == 3:
##        break

def get_num_protests(state):
    for row in blm_data:
        if row["State"] == state:
            return row["TotalProtests"]

# Assume blm_data is a list of dictionaries
def mystery(num_protests):
    states = []
    for item in blm_data:
        if item["TotalProtests"] >= num_protests:
            states.append(item["State"])
    return states



def get_states_with_atleast_num_protests(num_protests):
    #Homework
    return None

def get_states_with_atmost_num_protests(num_protests):
    #Homework
    return None

