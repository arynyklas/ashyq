from ashyq import Ashyq


# Init class and set phone number
phone_number = input('Input phone number: ')
ashyq = Ashyq(phone_number)

# SMS (login) request
ashyq.new_install()

# Join by received SMS
code = input('Input SMS code: ')
print(ashyq.connect(int(code)))

# User's PCR info
print(ashyq.user_pcr())

# Any person's PCR info (work only if user is security manager)
print(ashyq.pcr('YYMMDDXXXXXX'))
