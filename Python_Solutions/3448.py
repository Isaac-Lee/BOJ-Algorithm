count = 0
total = 0
unknown = 0
T = int(input())
while count < T:
    line = input()
    if line == "":
        count += 1
        effi = ((total - unknown) / total) * 100
        effi = round(effi, 1)
        if effi == int(effi):
            print("Efficiency ratio is "+f'{int(effi)}'+"%.")
        else:
            print("Efficiency ratio is " + f'{effi}' + "%.")
        total = 0
        unknown = 0
    total += len(line)
    unknown += line.count("#")

