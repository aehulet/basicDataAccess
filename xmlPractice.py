import xml.etree.ElementTree as et


def get_attribute():
    tree = et.parse('country_data.xml')
    root = tree.getroot()
    a = root.attrib
    print(a)

    for child in root:
        print(child.tag, child.attrib)

    for country in root.findall('country'):
        rank = country.find('rank').text
        name = country.get("name")
        print(name, rank)


def write_values() -> object:
    tree = et.parse('country_data.xml')
    root = tree.getroot()
    for rank in root.iter('rank'):
        new_rank = int(rank.text) + 1
        rank.text = str(new_rank)
        rank.set('updated', 'yes')
    tree.write('output.xml')


def remove_element() -> object:
    tree = et.parse('country_data.xml')
    root = tree.getroot()
    for country in root.findall('country'):
        rank = int(country.find('rank').text)
        if rank > 50:
            root.remove(country)

    tree.write('output2.xml')


def use_sub_elements():
    et.Element('ant')
    et.SubElement(ant, 'b')
