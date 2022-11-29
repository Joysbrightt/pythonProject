entries = []


def create_entry():
    # using zip to create a list

    date, title = input('date'), input('title')
    key = ['date', 'title', 'body']
    value = [date, title, input(f'{date}\n{title}\n\n dear diary \n')]
    each_entry = dict(zip(key, value))
    return each_entry
    # each_entry = [{'date': },{'tltle': }, {'body': }]


def diary(password):
    val = input({password})
    if password == val:
        entries = []
        to_continue = input("'y' to continue 'n' to [y/n]").lower()

        while to_continue == 'y':
            entries.append(create_entry())
            to_continue = input(" 'y' to continue 'n' to stop [y/n]").lower()
        return entries


def find_by_title(title):
    return [entry for entry in entries if entries['title'] == title]


def delete_entry_of(title):
    entries.pop(find_by_title(title).index())

    print(diary())
