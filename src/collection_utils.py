def dict_min_key_value(dictionary: dict):
    """
    Given a dict, returns the key which has the minimum value, along with the value.
    It assumes the values are comparable objects eg integers, strings, objects that implement __cmp__
    :param dictionary: A dictionary to be searched upon
    
    :return: A pair of min key and the corresponding value
    """
    min_key = min(dictionary, key=dictionary.get)
    min_value = dictionary.get(min_key)
    return min_key, min_value


def dict_max_key_value(dictionary: dict):
    """
    Given a dict, returns the key which has the maximum value, along with the value.
    It assumes the values are comparable objects eg integers, strings, objects that implement __cmp__
    :param dictionary: A dictionary to be searched upon
    :return: A pair of max key and the corresponding value
    """
    min_key = max(dictionary, key=dictionary.get)
    min_value = dictionary.get(min_key)
    return min_key, min_value


def list_min_index_value(values_list: list):
    """
        Given a list, returns the index which has the minimum value, along with the value.
        It assumes the values are comparable objects eg integers, strings, objects that implement __cmp__
        :param values_list: A list to be searched upon
        :return: A list of index(es) that have the minimum value and the corresponding value
    """
    min_value = min(values_list)
    how_many = values_list.count(min_value)
    c = 0
    index_list = []
    for idx, value in enumerate(values_list):
        if value == min_value:
            index_list.append(idx)

        print(c)
        if c > how_many:
            break

        c += 1

    return index_list, min_value


def list_max_index_value(values_list: list):
    """
        Given a list, returns the index which has the maximum value, along with the value.
        It assumes the values are comparable objects eg integers, strings, objects that implement __cmp__
        :param values_list: A list to be searched upon
        :return: A list of index(es) that have the maximum value and the corresponding value
    """
    min_value = min(values_list)
    how_many = values_list.count(min_value)
    c = 0
    index_list = []
    for idx, value in enumerate(values_list):
        if value == min_value:
            index_list.append(idx)

        if c >= how_many:
            break

        c += 1

    return index_list, min_value
