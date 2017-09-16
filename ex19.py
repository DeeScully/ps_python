def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """
    str > none
    input 2 str and call print w/str formatting to print input strings
    """
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print str
print("We can just give the function numbers directly:")

# call function and pass in 20, 30
cheese_and_crackers(20, 30)


# print str
print("OR, we can use variables from our script:")

# assign int to var
amount_of_cheese = 10

# assign int to var
amount_of_crackers = 50

# call func and pass in vars line 22, 25
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print str
print("We can even do math inside too:")

# call func and pass expression, expression
cheese_and_crackers(10 + 20, 5 + 6)


# print str
print("And we can combine the two, variables and math:")

# call func and pass in expression, expression
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
