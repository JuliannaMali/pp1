winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}
sum=0
for x in winter_semester.values():
    sum+=x

print(f'The total number of hours in the winter semester is: {sum}')