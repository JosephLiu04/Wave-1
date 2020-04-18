Seconds = int(input("Input the total amount of seconds: "))
Days = int(Seconds / 86400)
Hours = int(Days / 3600)
Minutes = int(Hours / 60)
Days1 = Seconds // 86400
Hours1 = Days // 3600
Minutes1 = Hours // 60
Seconds1 = Seconds // Days // Hours // Minutes
print(Days , ":" , Hours , ":" , Minutes , ":" , Seconds1)