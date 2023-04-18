"""
Implement a class Address. An address has a house number, a street, an optional apartment number, a
city, a state, and a postal code. Define the constructor such that an object can be created in one of two
ways: with an apartment number or without. Supply a print method that prints the address with the street
and house number (and maybe apartment number) on one line and the city, state, and postal code on the
next line. Supply a method def comesBefore (self, other) that tests whether this address comes before
other when compared by postal code.
"""


class Address:
    def __init__(self, street, house_nr, city, state, post, apart_nr=None):
        self.house_nr = house_nr
        self.street = street
        self.apartment_nr = apart_nr or ''
        self.city = city
        self.state = state
        self.post = post

    def comes_before(self, other):
        return self.post < other.post

    def __str__(self):
        header = "| %-25s | %-10s | %-15s | %-20s | %-10s | %-10s |" \
                 % ('Street', 'House Nr', 'Apartment Nr', 'City', 'State', 'Post')
        separator = "\n" + "+" + "-" * 27 + "+" + "-" * 12 + "+" + "-" * 17 + "+" + "-" * 22 + "+" + "-" * 12 + "+" + "-" * 12 + "+\n"
        row = "| %-25s | %-10d | %-15s | %-20s | %-10s | %-10s |" \
              % (self.street, self.house_nr, self.apartment_nr, self.city, self.state, self.post)
        return separator + header + separator + row + separator


address = Address("123 Main St", 42, "Apt 4", "New York", "NY", "10001")
address2 = Address("456 Elm St", 99, "Apt 2", "L.A", "CA", "90001")

if address.comes_before(address2):
    print(f"{address} comes before {address2}")
else:
    print(f"{address} comes after {address2}")



