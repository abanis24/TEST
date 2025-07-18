from dateutil import parser

date = 'Jun 23 2024 07:31PM'

converted_date = parser.parse(date)
print(converted_date)
print(type(converted_date))