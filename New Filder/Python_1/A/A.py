import xml.etree.ElementTree as ET

# Sample XML data
xml_data = """<?xml version="1.0"?>
<root>
    <item id="1">
        <name>Item 1</name>
        <value>10</value>
    </item>
    <item id="2">
        <name>Item 2</name>
        <value>20</value>
    </item>
</root>
"""

# Parse the XML data
root = ET.fromstring(xml_data)

# Iterate through items
for item in root.findall('item'):
    item_id = item.get('id')  # Get attribute 'id'
    name = item.find('name').text  # Get name text
    value = item.find('value').text  # Get value text

    print(f"ID: {item_id}, Name: {name}, Value: {value}")