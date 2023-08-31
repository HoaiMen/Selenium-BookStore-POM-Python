from operator import itemgetter

# we can store test data in this module like users
users = [
    # {"name": "invalid_user", "email": "hoaimen@gmail.com", "password": "mentruong250"},
    {"name": "valid_user", "email": "hoaimen@gmail.com", "password": "mentruong250256"},
    # {"name": "valid_user", "email": "cucatim4@gmail.com", "password": "vanduc123"},
    # {"email": "admin@test.com", "password": "qwert1234"},
    # {"email": "admin@test.com", "password": "qwert1234"},
    # {"email": "admin@test.com", "password": "qwert1234"},
]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)
