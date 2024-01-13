class Data:

    def __init__(self, data, ip_destination):
        self.data = data
        self.ip = ip_destination  # ip of destination


class Server:
    __number_of_servers = 0

    def __init__(self):
        Server.__number_of_servers += 1
        self.ip = Server.__number_of_servers
        self.buffer = []
        self.main_router: Router = None

    def send_data(self, data: Data):
        self.main_router.buffer.append(data)

    def get_data(self):
        buffer_before_cleaning = self.buffer.copy()
        self.buffer.clear()
        return buffer_before_cleaning

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.servers = dict()
        self.buffer = []

    def link(self, server):
        if server.ip not in self.servers:
            self.servers[server.ip] = server
            server.main_router = self

    def unlink(self, server):
        val = self.servers.pop(server.ip, False)
        if val:
            val.router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
            else:
                pass  # here we should raise error destination unreachable
        self.buffer.clear()