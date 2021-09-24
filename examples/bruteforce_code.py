from ashyq import Ashyq, drivers, exceptions


# OR you can use AsyncDriver: drivers.a_sync.AsyncDriver
driver = drivers.sync.SyncDriver()


# Init class and set phone number
phone_number = input('Input phone number: ')
ashyq = Ashyq(driver, phone_number)


# SMS (login) request
ashyq.new_install()


i = 1

while i <= 9999:
    code = '{:04}'.format(i)

    try:
        # Join by received SMS
        ashyq.connect(code)

        # On succesfully logged_on
        break

    except exceptions.AshyqException:
        print('Passed:', code)
        i += 1


if ashyq.logged_on:
    print('Logged on with code {}!'.format(code))

    print()

    print('Device ID:', ashyq.device_id)
    print('Access token:', ashyq.access_token)
    print('Refresh token:', ashyq.refresh_token)
    print('User info:', ashyq.user)

else:
    print('Code not found')
    print('Too many account logins were detected')


ashyq.close()
