# ChineseHolidayCalendar
This project is used to generate Chinese adjusted rest holiday calendar information. Designed to be directly imported into the iOS system calendar App, no need for third-party calendar apps.



## Usage

1. cd **ChineseHolidayCalendar** directory
2. run ` python3 ./chineseholidaycalendar.py `, then a **ics** extension calendar file will be generated in the current directory
3.  Import the calendar file by email, you can see the chinese holiday information on the iOS Calendar App



## Customize

**holiday.csv** is the holiday data file, the format is: the first column is the name of the holiday, the second column is the date(yyyyMMdd) and the third column is the category('r' stands for rest, 'w' stands for work).

| First Column | Second Column | Third Column |
| :----------: | :-----------: | :----------: |
|     元旦     |   20210101    |      r       |
|    劳动节    |   20210425    |      w       |



