class Node:
    def __int__(self, data):
        self.data = data
        self.next_element = None


class Linked_list:
    def __init__(self):
        self.head_element = None

    def get_head(self):
        return self.head_element

    def is_empty(self):
        if self.head_element is None:
            return True
        else:
            return False


lst = Linked_list()
print(lst.get_head())
empty = Linked_list()
print(empty.is_empty())

# todo get_head()
# todo insert_at_tail(data)
# todo insert_at_head(data)
# todo delete()
# todo delete_at_head()
# todo search()
# todo is_empty()
