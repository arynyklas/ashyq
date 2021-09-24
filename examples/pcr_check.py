from ashyq import Ashyq, drivers


# OR you can use AsyncDriver: drivers.a_sync.AsyncDriver
driver = drivers.sync.SyncDriver()


# Init class and set phone number
phone_number = input('Input phone number: ')
ashyq = Ashyq(driver, phone_number)


# SMS (login) request
ashyq.new_install()

# Join by received SMS
code = input('Input SMS code: ')
print(ashyq.connect(code))

# User's PCR info
print(ashyq.user_pcr())

# Any person's PCR info by IIN (work only if user is security manager)
print(ashyq.pcr('YYMMDDXXXXXX'))
