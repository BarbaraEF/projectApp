
class Booking:
    def __init__(self, IDnum, name, age, services, guests, amount):
        self.IDnum  = IDnum
        self.name = name
        self.age = age
        self.services = services
        self.guests = guests
        self.amount = amount

    def get_IDnum(self):
        return self.IDnum
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_services(self):
        return self.services
    def get_guests(self):
        return self.guests
    def get_amount(self):
        return self.amount

    def __str__(self):
        return "{},{},{},{},{},{}".format(self.IDnum, self.name, self.age, self.services, self.guests, self.amount)

    def __screen__(self):
        return "ID {} | Name {} | Age {} | Service {} | Guests {} | Amount {}".format(self.IDnum, self.name, self.age, self.services, self.guests, self.amount)

