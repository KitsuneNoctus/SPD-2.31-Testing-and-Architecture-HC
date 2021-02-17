# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace nested conditional with gaurd clases.
ADJ_FACTOR = 0.7
def get_adjusted_capital(capital, rate, duration, income):
    return (income / duration) * ADJ_FACTOR if capital > 0 and rate > 0 and duration > 0 else 0

adjusted_capital = get_adjusted_capital(50000, 4,10, 10000)
print(adjusted_capital) #700.0