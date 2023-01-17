from datetime import date
start_date = input("Enter start date, (Format: 27,09,2018)\n>>>")
start_date = [int(x) for x in start_date.split(",")]
end_date = input("Enter end date, (Format: 16,12,2020)\n>>>")
end_date = [int(x) for x in end_date.split(",")]
print(start_date,end_date)
delta = date(end_date[2],end_date[1],end_date[0]) - date(start_date[2],start_date[1],start_date[0])
print("Number of days is",delta.days,"days")
