book = dict()

book["apple"] = 1
book["milk"] = 2
book["avocado"] = 3
book["edibles"] = 4

print(book)

print(book["avocado"])

# building a phone book using hash functions
# todo HASHES ARE USED FOR
# Modelling relationships from one thing to another thing
# filtering out duplicates
# hash tables are used for lookups on a much larger scale..
#  hash tables are also used to map web address to an IP address -> The process is called DNS resolution..

# Todo Big O Notation of hashing:
# SEARCH: average_case(O(1), worst_case(O(n)
# INSERT: average_case(O(1), worst_case(O(n)
# DELETE: average_case(O(1), worst_case(O(n)

phone_book = dict()
phone_book = {}

phone_book["jenny"] = 12345
phone_book["emergency"] = 911

print(phone_book["jenny"])

# using hash function to check if a person has voted

voted = {}


def check_voter(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
    print("let them vote!")


# application  and websites uses hash table as a cache: which stores a user activity against when next they will make
# the same web calls
cache = {}


def get_data_from_server(url):
    return cache[url]


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

# TODO:-> Exercise 5.4-5.7

def __main__():
    print(check_voter("tom"))
    print(check_voter("tom"))
