def simpleparse():
    my_string = "|:re-tag:||:this:|"  # weird tag to be replaced
    my_string.replace("|:", "<")
    my_string.replace(":|", ">")
    print(my_string)

    the_words = my_string.split(":|")
    for word in the_words:
        # word = "<" + word + ">"
        print(word)


def findsub():
    import re

    bigstring = "oatmilk/cherry/Q274876"
    the_split = re.split(r'\/', bigstring)
    print(the_split.pop())
