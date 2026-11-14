import Pyro5.api


# The name server is running on the same computer.
Pyro5.config.NS_HOST = "localhost"
Pyro5.config.NS_PORT = 9090

# Find the remote object that the server registered as "stock".
stock = Pyro5.api.Proxy("PYRONAME:stock")

print("Connected to the stock server")
print("Commands: name <id>, quantity <id>, price <id> <quantity>, end")

while True:
    command = input("Command: ").strip().split()

    if not command:
        continue

    action = command[0].lower()

    try:
        if action == "name" and len(command) == 2:
            result = stock.get_name(int(command[1]))
            if result is None:
                print("Item not found")
            else:
                print("Item name:", result)

        elif action == "quantity" and len(command) == 2:
            result = stock.get_quantity(int(command[1]))
            if result is None:
                print("Item not found")
            else:
                print("Available quantity:", result)

        elif action == "price" and len(command) == 3:
            result = stock.get_price(int(command[1]), int(command[2]))
            if result is None:
                print("Item not found")
            else:
                print("Total price:", round(result, 2))

        elif action == "end":
            break

        else:
            print("Invalid command. Try: name <id>, quantity <id>, price <id> <quantity>, end")

    except ValueError:
        print("Please enter numeric IDs and quantities")

stock._pyroRelease()
print("Client stopped")
