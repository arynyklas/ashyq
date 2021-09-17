from ashyq import Ashyq


# Init class and set phone number
phone_number = input('Input phone number: ')
ashyq = Ashyq(phone_number)

# SMS (login) request
ashyq.new_install()

# Join by received SMS
code = input('Input SMS code: ')
print(ashyq.connect(code))

# User info (cached)
print(ashyq.user)
