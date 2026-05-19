import lxml.etree as et
import json

root_tag = et.Element('events')

with open('DATA/meteorite_events.json', errors="replace") as meteors_in:
    raw_data = json.load(meteors_in)
    for row in raw_data:
        event_tag = et.SubElement(root_tag, "event", id=row["id"])
        name_tag = et.SubElement(event_tag, "name")
        name_tag.text = row['name']
        et.SubElement(event_tag, "mass").text = row.get('mass', "NO MASS")

encoded_xml_data = et.tostring(root_tag, pretty_print=True)
xml_data = encoded_xml_data.decode()
print(xml_data)