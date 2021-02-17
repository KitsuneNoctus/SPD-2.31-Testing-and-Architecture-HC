
# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

def send_hiring_email(email):
    print("email sent to: ", email)

def show_movies_played(movies):
    print('Movies Played: ', end='')
    for m in movies[i]:
        print(m, end=', ')

def check_age(index):
    return birth_year[index] > 1985

for i, value in enumerate(emails):
    if check_age(i):
        print(first_names[i], last_names[i])
        show_movies_played(movies)
        print()
        send_hiring_email(value)