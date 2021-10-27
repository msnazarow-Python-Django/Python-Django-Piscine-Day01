#!/usr/bin/env python3
def var_to_dict(array_of_tuples):
    my_dict = {}
    for my_tuple in array_of_tuples:
        my_dict[my_tuple[1]] = my_tuple[0]
    return  my_dict


def main():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    my_dict = var_to_dict(d)
    print('\n'.join(f"'{key}': '{value}'" for key, value in my_dict.items()))


if __name__ == '__main__':
    main()
