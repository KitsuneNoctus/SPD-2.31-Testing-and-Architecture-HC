
# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
def get_price():
    return self.get_base_price() * self.get_discount_factor()

def get_base_price():
    return quantity * item_price

def get_discount_factor():
    return 0.95 if get_base_price() > 1000 else 0.98
