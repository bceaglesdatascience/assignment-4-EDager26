customer_names= []
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
    updated_costs = []
    for item_cost in item_costs:
        updated_cost = item_cost +  item_cost * sales_tax
        updated_costs.append(updated_cost)
    return updated_costs

new_costs = add_tax(item_costs, sales_tax)

customer_info = {}

purchase_number = 1

while purchase_number<=num_of_purchases:
    customer = customer_names[purchase_number-1]
    cost_plus_tax = new_costs[purchase_number-1]
    if customer in customer_info:
        customer_info[customer] += cost_plus_tax
    else:
        customer_info[customer] = cost_plus_tax

    purchase_number+=1

print(customer_info)

