customer_names = []
item_costs = []

num_of_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

purchase_number = 1

while purchase_number <= num_of_purchases:
    customer_name = str(input("Customer: "))
    item_cost = float(input("Cost: "))
    customer_names.append(customer_name)
    item_costs.append(item_cost)
    purchase_number+=1

def add_tax(item_costs, sales_tax):
    for index, item_cost in enumerate(item_costs):
        item_costs[index] += item_cost * sales_tax
       
    return item_costs

new_costs = add_tax(item_costs, sales_tax)

print(new_costs)
