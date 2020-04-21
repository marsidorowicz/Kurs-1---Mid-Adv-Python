workDays = [19, 21, 22, 21, 20, 22]

print(workDays)
print(workDays[2])
enumerateDays = list(enumerate(workDays))
print(enumerateDays)

for pos, value in enumerateDays:
    print("Pozycja", pos, "Wartość", value)

months = ["I", "II", "III", "IV", "V"]

monthsDays = list(zip(months, workDays))
print(monthsDays)

for m, d in monthsDays:
    print("Month", m, "Days", d)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print("Pozycja", pos, "Miesiąc", m, "Dzień", d)