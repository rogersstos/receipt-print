# create a product and price for three items
p1_name, p1_price="Oranges", 5.97
p2_name, p2_price="Shampoo", 3.75
p3_name, p3_price="Olive Oil", 9.53

# create a company name and information
company_name="Sweet Farm"
company_address="10 King St."
company_city="Ingersoll, ON"

# declare ending message
message="Thanks for shopping with us today!"

# create a top border
print("*" * 50)

# print company information first, using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

# print a line between sections
print("=" * 50)

# print out header for section of items
print("\tProduct Name\tProduct Price")

# create a print statement for each product
print("\t{}\t\t${}".format(p1_name.title(), p1_price))
print("\t{}\t\t${}".format(p2_name.title(), p2_price))
print("\t{}\t${}".format(p3_name.title(), p3_price))

# print a line between sections
print("=" * 50)

# print out header for section of total
print("\t\t\tTotal")

# calculate total price and print out
total = p1_price + p2_price + p3_price
print("\t\t\t${}".format(total))

# print a line between sections
print("=" * 50)

# output thank you message
print("\n\t{}\n".format(message))

# create a bottom border
print("*" * 50 )