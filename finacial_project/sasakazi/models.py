from django.db import models

# Create your models here.

# Need #1
# We need model classes - customer, account and card
# The customer may have many bank accounts, hence a relationship
# exists between the customer and the account(s). 
# Have a foreign key in the account class to link the 
# database - user/customer_id used. 






#  the accounts should/could be debit or credit accounts. 
# hence the account class should have a model with 
# specificity on what type the card is. 
# Have a balance, interest rate, etc information




# the card class considers - a client can have more than
# more than one card number - take a number for each card
# have a foreign key linking the accounts and card models
# having each card reflect an amount linked to the account. 