#dictionaries {}

user = input("Search for a customer: ")
customer = {
    "Shiba Smallball":"""
    age: 3
    is_verified: True
    Occupation: CEO of Shiba Land
    
    """,

    "Duckie Mini": """
    age: 1
    is_verified: True
    Occupation: Actress
    
    """

}

#retrieve info of customer from the dictionaries


#however, it comes with limitations
# as it showed error when Name or NAME is searched
# so .get() method is used, to show none instead

print(f"Here is the info you required: {customer.get(user)}")


