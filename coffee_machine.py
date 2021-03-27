class CoffeeMachine:
    n_machines = 0
    machines_state = {1: "Choosing an action", 2: "Choosing a type of coffee", 3: 'Filling', 4: "Taking", 0: 'Off'}
    espresso_norm = {'water': 250, 'coffee_beans': 16, 'disposable cups': 1, "money": 4}
    latte_norm = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'disposable cups': 1, "money": 7}
    cappuccino_norm = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'disposable cups': 1, "money": 6}

    def __new__(cls):            # Ограничение количества экземпляров кофемашин
        if cls.n_machines == 0:
            cls.n_machines += 1
            return object.__new__(cls)
        else:
            return None

    def __init__(self):          # Создание экземпляра с начальными параметрами
        self.machine_has = {'water': 400, 'milk': 540, 'coffee_beans': 120, 'disposable cups': 9, 'money': 550}
        self.state = 1
        self.on_state = True

    def active_state(self):     # Проверка действующего статуса машины и вызов соответствующей функции
        if CoffeeMachine.machines_state[self.state] == "Choosing an action":
            self.make_action()
        elif CoffeeMachine.machines_state[self.state] == "Choosing a type of coffee":
            self.choosing_coffee()
        elif CoffeeMachine.machines_state[self.state] == 'Filling':
            self.fill()
        elif CoffeeMachine.machines_state[self.state] == "Taking":
            self.take()
        elif CoffeeMachine.machines_state[self.state] == "Off":
            self.on_state = False

    def make_action(self):
        action = input('Write action (buy, fill, take, remaining, exit): ')
        if action == "buy":
            self.state = 2
        elif action == 'fill':
            self.state = 3
        elif action == "take":
            self.state = 4
        elif action == 'remaining':
            self.remaining()
            self.state = 1
        elif action == "exit":
            self.state = 0
        else:
            print('Invalid action!')
        print()

    def choosing_coffee(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if choice == '1':
            self.checking_resources(self.espresso_norm)
        elif choice == '2':
            self.checking_resources(self.latte_norm)
        elif choice == '3':
            self.checking_resources(self.cappuccino_norm)
        elif choice == 'back':
            self.state = 1
            return
        else:
            print('Invalid choice!')
        self.state = 1

    def checking_resources(self, norm):
        result = 'ok'
        for key in norm.keys():
            if key != 'money':
                if self.machine_has[key] < norm[key]:
                    result = key
                    break
        if result == 'ok':
            for key in norm.keys():
                if key != 'money':
                    self.machine_has[key] -= norm[key]
                else:
                    self.machine_has[key] += norm[key]
            else:
                print('I have enough resources, making you a coffee!')
        else:
            print('Sorry, not enough ' + result + ' !')

    def fill(self):
        print()
        self.machine_has['water'] += int(input('Write how many ml of water do you want to add: '))
        self.machine_has['milk'] += int(input('Write how many ml of milk do you want to add: '))
        self.machine_has['coffee_beans'] += int(input('Write how many grams of coffee beans do you want to add: '))
        self.machine_has['disposable cups'] \
            += int(input('Write how many disposable cups of coffee do you want to add: '))
        self.state = 1

    def take(self):
        print()
        print("I gave you ", self.machine_has["money"])
        self.machine_has['money'] = 0
        self.state = 1

    def remaining(self):
        print()
        print('The coffee machine has:')
        print(self.machine_has["water"], 'of water')
        print(self.machine_has['milk'], 'of milk')
        print(self.machine_has["coffee_beans"], 'of coffee beans')
        print(self.machine_has['disposable cups'], 'of disposable cups')
        print(self.machine_has['money'], 'of money')


coffee_machine = CoffeeMachine()
while coffee_machine.on_state:
    coffee_machine.active_state()
