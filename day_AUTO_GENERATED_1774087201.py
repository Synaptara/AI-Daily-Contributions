def sort_dict_list(dict_list, key, reverse=False):
    try:
        return sorted(dict_list, key=lambda x: x[key], reverse=reverse)
    except KeyError:
        raise ValueError("The key does not exist in the dictionaries")

def sort_dict_list_attribute(dict_list, attr, reverse=False):
    return sorted(dict_list, key=lambda x: getattr(x, attr), reverse=reverse)

def sort_dict_list_item(dict_list, key, reverse=False):
    return sorted(dict_list, key=lambda x: x.get(key), reverse=reverse)

class DictionaryItem:
    def __init__(self, attr):
        self.attr = attr

dict_list = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 40}
]

dict_list_obj = [
    DictionaryItem(30),
    DictionaryItem(25),
    DictionaryItem(40)
]

print(sort_dict_list(dict_list, "age"))
print(sort_dict_list_attribute(dict_list_obj, "attr"))
print(sort_dict_list_item([{"a": 1}, {"a": 2}, {"b": 3}], "a"))