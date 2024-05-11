import csv
with open("test1.csv","w",newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["symbol", "data", "close"])
    writer.writerow(["rb2101", "20200907", "3736"])
    writer.writerow(["rb2101", "20200908", "3737"])
    writer.writerow(["rb2101", "20200909", "3738"])
    writer.writerow(["rb2101", "20200906", "3739"])

f.close()