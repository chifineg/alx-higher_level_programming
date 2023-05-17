#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_new(new):
        return (new if new != search else replace)
    return list(map(s_new, my_list))
