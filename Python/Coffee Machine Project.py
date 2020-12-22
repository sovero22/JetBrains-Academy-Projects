class CoffeeMachine:

    def __init__(self):
        self.resources = [400, 540, 120, 9, 550]
        self.res_names = ['water', 'milk',
                          'coffee beans', 'disposable cups', 'money']

    def remaining(self):
        print('The coffee machine has:')
        counter = 0
        for counter in range(len(self.resources)):
            if counter == 4:
                print('$', self.resources[counter],
                      'of', self.res_names[counter])
            else:
                print(self.resources[counter],
                      'of', self.res_names[counter])

    def buy(self):
        option = input('''What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:''')
        if option == '1':
            consumption = [-250, 0, -16, -1, 4]

        elif option == '2':
            consumption = [-350, -75, -20, -1, 7]

        elif option == '3':
            consumption = [-200, -100, -12, -1, 6]

        elif option == 'back':
            pass

        if option in ('1', '2', '3'):
            i = 0
            for i in range(len(self.resources)):
                if (self.resources[i] < abs(consumption[i])) and (i < len(self.resources) - 1):
                    print('Sorry, not enough', self.res_names[i], '!')
                    break
                else:
                    self.resources[i] = self.resources[i] + consumption[i]
                    if i == len(self.resources) - 1:
                        print('I have enough resources, making you a coffee!')

    def fill(self):
        water_add = int(input("Write how many ml of water do you want to add:"))
        milk_add = int(input("Write how many ml of milk do you want to add:"))
        beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
        disp_cups_add = int(input('Write how many disposable cups of coffee do you want to add:'))
        fill_r = [water_add, milk_add, beans_add, disp_cups_add, 0]
        i = 0
        for i in range(len(self.resources)):
            self.resources[i] = self.resources[i] + fill_r[i]

    def take(self):
        print('I gave you $', str(self.resources[4]))
        self.resources[4] = 0


machine = CoffeeMachine()
action = ''
while action != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit):')

    if action == 'buy':
        machine.buy()
    elif action == 'fill':
        machine.fill()
    elif action == 'take':
        machine.take()
    elif action == 'remaining':
        machine.remaining()
