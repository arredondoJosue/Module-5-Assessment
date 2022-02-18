# from tkinter.tix import INTEGER

# from numpy import integer


# this line creates a variables that references the data inside the text file 'um-server-01' 
log_file = open("um-server-01.txt")

# this function goes line by line in the text file and extracts the data 1-4 if the day is Tuesday or if the row is labeled as "Tue", then prints that line
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


sales_reports(log_file)

#extra credit function
def ten(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        qty = int(line[16:18])
        # if day == "Tue":
        #     print(line)
        #     # print(int(qty))
        if qty > 10:
            print(line)

ten(log_file)