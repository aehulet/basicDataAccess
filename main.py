# This is a sample Python script.
import dbFuncts
import xmlPractice
import spql, parse
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings

# parse.findsub()
# result_dict = spql.get_query(spql.LOAD_BASE)
# print(spql.load_base(spql.get_wd_query(spql.LOAD_BASE)))
result_dict = spql.get_wd_query(spql.query_item_detail("Q116341990"))
print(spql.load_item_detail(result_dict))
# print(spql.get_wd_query(spql.query_item_detail("Q116341990")))

# xmlPractice.get_attribute()
# xmlPractice.write_values()
# xmlPractice.remove_element()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
