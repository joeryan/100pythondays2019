NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    name_set = []
    for name in names:
        if name.title() not in name_set:
            # first_name, last_name = name.split()
            # case_name = "{} {}".format(first_name.)
            name_set.append(name.title())
    return name_set


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    split_names = [(name.split()) for name in names]
    split_names.sort(key=lambda name: name[1], reverse=True)
    return [' '.join(name) for name in split_names]

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    split_names = [name.split() for name in names]
    split_names.sort(key=lambda name: len(name[0]))
    return split_names[0][0]