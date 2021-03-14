import sys
import csv
import uuid

icalendar_header = '''
BEGIN:VCALENDAR
VERSION:2.0
PRODID:icalendar-python
CALSCALE:GREGORIAN
X-WR-CALNAME:中国节假日
X-APPLE-LANGUAGE:zh
X-APPLE-REGION:CN
'''

icalendar_footer = 'END:VCALENDAR'

def generate_calendar_file():
    with open('holiday.csv', 'r') as f:
        icalendar_data = icalendar_header
        reader = csv.reader(f)
        for item in reader:
            event_body = assemble_event(item)
            icalendar_data = icalendar_data + event_body
        icalendar_data = icalendar_data + icalendar_footer
        with open('2021_chinese_holiday_calendar.ics', 'wb') as ics_file:
            ics_file.write(icalendar_data.encode('utf-8'))

        

def assemble_event(event):
    name = event[0]
    date = event[1]
    category = event[2]
    begin = 'BEGIN:VEVENT' + '\n'
    dtstamp = 'DTSTAMP:' + date + 'T000000Z' + '\n'
    uid = 'UID:' + str(uuid.uuid1()) + '\n'
    dtstart = 'DTSTART;VALUE=DATE:' + date + '\n'
    classCategory = 'CLASS:PUBLIC' + '\n'
    title = '上班'
    if category == 'r':
        title = name + '·' + '休息'
    summary = 'SUMMARY;LANGUAGE=zh_CN:' + title + '\n'
    transp = 'TRANSP:TRANSPARENT' + '\n'
    categories = 'CATEGORIES:chineseholiday' + '\n'
    end = 'END:VEVENT' + '\n'
    body = begin + dtstamp + uid + dtstart + classCategory + summary + transp + categories + end
    return body


if __name__ == '__main__':
    generate_calendar_file()



