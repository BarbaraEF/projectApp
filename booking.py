from functools import reduce


class Booking:
    def __init__(self, numero, name, age, service, guests, amount):
        self.numero = int(numero)
        self.name = name.strip()
        self.age = int(age)
        self.service = int(service)
        self.guests = int(guests)
        self.amount = int(amount)
        self.about_service = {
            "0": "hall",
            "1": "hall and party",
            "2": "hall, party and food",
            "3": "hall, party, food and surprise"
        }

    def get_numero(self):
        return self.numero

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_service(self):
        return self.service

    def get_guests(self):
        return self.guests

    def get_amount(self):
        return self.amount


    def _str_(self):
        return "{},{},{},{},{},{}".format(self.numero, self.name, self.age, self.service, self.guests, self.amount)

    def _screen_(self):
        return "ID: {} | Name: {} | Age: {} | Service: {} | Guests: {} | Amount: {}".format(self.numero, self.name,self.age, self.about_service[str(self.service)],self.guests, self.amount)


# open the file
# load the info
def file_to_bookings():
    array_bookings = list()
    with open('booking.csv', 'r') as file:
        for line in file:
            data = line.split(',')
            booking = Booking(data[0],data[1],data[2],data[3],data[4],data[5])
            array_bookings.append(booking)
    return array_bookings


# noinspection PyProtectedMember
def show_bookings(list_booking):
    for booking in list_booking:
        # noinspection PyProtectedMember
        print(booking._screen_())

#for each service returns the max amount and which service repeats more
def sumServices(array_bookings, service):
    vector = list()
    for booking in array_bookings:
        if booking.get_service() == service:
            vector.append(booking.get_amount())
    return reduce((lambda x,y:x+y),vector) if vector else 0

def sumAmountServices(array_bookings):
    dicSum = dict()
    for i in range(len(array_bookings[0].about_service)):
        dicSum[i]=sumServices(array_bookings,i)
    print(dicSum)
    print(max(dicSum))


array = file_to_bookings()
show_bookings(array)
sumAmountServices(array)
