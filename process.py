# this line creates a variables that references the data inside the text file 'um-server-01' 
log_file = open("um-server-01.txt")

# this function goes line by line in the text file and extracts the data 1-4 if the day is Tuesday or if the row is labeled as "Tue", then prints that line
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)
