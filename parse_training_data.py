
class_names = ["person", "empty"]

for class_name in class_names:
    cnt = 0
    contents = ""
    for line in open("{0}.txt".format(class_name)):
        line = line.strip("\n")
        
        if line == "-- Image start --":
            # One sample is ready.
            f = open("data/{0}.{1}.csv".format(class_name, cnt), "w")

            # Header
            header = ""
            for i in range(768):
                header += "ir{0},".format(i)
            header = header.rstrip(",")
            f.write(header)
            f.write("\n")
            # Data
            contents = contents.rstrip(",")
            f.write(contents)

            f.close()
            
            contents = ""
            cnt+=1
        else:
            contents += line
