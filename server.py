import Pyro5.api
import Pyro5.server

from stock import Stock


@Pyro5.api.expose
class StockServer:
    def __init__(self):
        self.stock = Stock("data.csv")

    def get_name(self, id):
        return self.stock.get_name(id)

    def get_quantity(self, id):
        return self.stock.get_quantity(id)

    def get_price(self, id, quantity):
        return self.stock.get_price(id, quantity)


# Create the Pyro server and register the remote object with the name server.
daemon = Pyro5.server.Daemon()
uri = daemon.register(StockServer())
name_server = Pyro5.api.locate_ns()
name_server.register("stock", uri)

print("Stock server is ready")
daemon.requestLoop()
