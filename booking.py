import csv
from functools import reduce

about_services = {
        "0": "hall",
        "1": "hall and party",
        "2": "hall, party and food",
        "3": "hall, party, food and surprise"
}
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
class BookingManager():
    def file_to_bookings(self):
        array_bookings = list()
        with open('booking.csv', 'r') as file:
            for line in file:
                data = line.split(',')
                booking = Booking(data[0],data[1],data[2],data[3],data[4],data[5])
                array_bookings.append(booking)
        return array_bookings


    # noinspection PyProtectedMember
    def show_bookings(self, list_booking):
        for booking in list_booking:
            # noinspection PyProtectedMember
            print(booking._screen_())

    #for each service returns the max amount and which service repeats more
    def sumServices(self, array_bookings, service):
        vector = list()
        for booking in array_bookings:
            if booking.get_service() == service:
                vector.append(booking.get_amount())
        return reduce((lambda x,y:x+y),vector) if vector else 0

    def sumAmountServices(self, array_bookings):
        dicSums = dict()
        for i in range(len(array_bookings[0].about_service)):
            result = self.sumServices(array_bookings, i)
            dicSums[i]=result
            print("Service {}:{} has a total amount ${}".format(i, about_services[str(i)],result))


        max_key =max(zip(dicSums.values(), dicSums.keys()))[1]
        print("Service most required is", about_services[str(max_key)])

    def vector_creation(self, atr, condition, array):
        new_array = list()
        for booking in array:
            print(booking.__dict__[atr])
            if booking.__dict__[atr] > condition:
                new_array.append(booking)
        return new_array

    def filter_vector (self, dicc_filter, array):
        for filter in dicc_filter:
            array = self.vector_creation(filter,dicc_filter[filter],array)

        self.show_bookings(array)
        return array

    def agregar_reserva(self, array_bookings):
        # Ingreso id reserva
        numero = input("Enter the booking code: ")

        # Solicitar el nombre de reserva, edad, servicio etc
        name = input("Name: ")
        age = input("Age: ")
        about_service = input("Service: ")
        guests = input("Guest: ")
        amount = input("Amount: ")

        num_exist = [booking.numero for booking in array_bookings]
        while numero in num_exist:
            print("Number must be unique.")
            numero = input("Enter the correct number: ")
        new_booking = Booking(numero, name, age, about_service,guests, amount)
        array_bookings.append(new_booking)
        with open('booking.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([numero, name, age, about_service,guests, amount])

        print("Reserva agregada con éxito!")
        return array_bookings

bookManager = BookingManager()
dicc_filter = {
    "age": 5,
    "guests": 10
}

array = bookManager.file_to_bookings()
bookManager.show_bookings(array)
#bookManager.sumAmountServices(array)
#bookManager.vector_creation("age", 10, array)

print("-------------")
#bookManager.filter_vector(dicc_filter, array)
bookManager.agregar_reserva(array)
bookManager.show_bookings(array)
