def who_never found_out():
    people = {
        'Megan': 'forgot_to_buy_deodorant',
        'Jessica': 'owner_of_deodorant'
    }

    for person, action in people.items():
        if action == 'forgot_to_buy_deodorant':
            return person

print(who_never_found_out())  # This should print 'Megan'