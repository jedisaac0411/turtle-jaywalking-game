import data
flag = True


def main():

    def resource_sufficient(user):
        for i in user:
            if data.resources[i] < user[i]:
                print(f'Not enough {i}')
                return False
        return True

    def process_coins():
        print("please insert coins:")
        quarter = int(input("how many quarters?: ")) * 0.25
        dimes = int(input("how many dimes?: ")) * 0.10
        nickles = int(input("how many nickles?: ")) * 0.05
        pennies = int(input("how many pennies?: ")) * 0.01
        total = quarter + dimes + nickles + pennies
        return total

    def make_coffee(user_drink):
        for i in data.MENU[user_drink]['ingredients']:
            data.resources[i] = data.resources[i] - data.MENU[user_drink]['ingredients'][i]
        print(f"Here is your {user_drink}, enjoy!")

    def check_transaction_successful(user_input_price, user_beverage):
        if user_input_price > data.MENU[user_beverage]['cost']:
            change = user_input_price - data.MENU[user_beverage]["cost"]
            print(f'Here is your change ${round(change, 2)}')
            data.profit += data.MENU[user_beverage]['cost']
            make_coffee(user_beverage)
        else:
            print('not enough money')

    user_input = input("what would you like? (espresso, latte, cappuccino): ")
    if user_input.lower() == 'off':
        global flag
        flag = False
    elif user_input.lower() == 'report':
        print(data.resources)
        print(f"Profit: {data.profit}")
    else:
        if resource_sufficient(data.MENU[user_input]['ingredients']):
            check_transaction_successful(process_coins(), user_input)


while flag:
    main()
