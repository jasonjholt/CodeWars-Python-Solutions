def pizza_rewards(customers, min_orders, min_price):
    r_customers = set()
    for customer in customers:
        print(customer, customers[customer])
        counting = [pizza for pizza in customers[customer] if pizza >= min_price]
        print(counting)
        if len(list(counting)) >= min_orders:
            r_customers.add(customer)
    return r_customers
