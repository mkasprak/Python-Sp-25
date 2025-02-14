'''
    Exploring list operations
'''

# List of delinquent account numbers
# delinquent_accounts = [1056, 2008, 3278, 4189]
# if 2008.0 in delinquent_accounts:
#     print("The account number 2008 is delinquent.")
# else:
#     print("The account number 2008 is not delinquent.")

# Find the index of 2008 in the list
# for i in range(len(delinquent_accounts)):
#     if delinquent_accounts[i] == 2008:
#         print(f"The account number 2008 is at index {i}")

# List of items to buy
needed_list = ["Apples", "Lettuce", "Bread", "Milk", "Peanut Butter"]

# Loop to manage shopping list
got_it = "ice cream"  # flag
while got_it != "done":
    for item in needed_list:
        print(item)

    got_it = input("\nPlease enter the item you have gotten from the list: ")

    if got_it in needed_list:
        needed_list.remove(got_it)

    if len(needed_list) == 0:
        print("You are done!")
        got_it = "done"
