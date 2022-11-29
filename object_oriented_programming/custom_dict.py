import json


class CustomDict(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _getitem_(self, key, value):
        if key in self:
            raise KeyError(f"key{key} already exist")
        else:
            super().__setitem__(key, value)

            with open("classwork.list", mode="w+") as custom_diction:
                json.dumps(classwork, custom_diction)


classwork = CustomDict()
classwork = {"name": "Adeola",
             "age": 18,
             1: "Birthday",
             "hobby": ["playing", 'dancing', 'reading'],
             "bool": True}
