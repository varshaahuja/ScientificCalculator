import csv
class scientificCalculator:

    #Population Mean
    @staticmethod
    def populationMean(data):
        n= len(data)
        sum=0
        for i in range(0,n): sum= sum +data[i]


        input = csv.reader(open("populationMean.csv"))
        next(input)
        for row in input:
            print(row[0:10])

        return sum/n ;

    #Population Standard Deviation
    @staticmethod
    def populationStandardDeviation(data):
        n= len(data);
        dev=0
        mean = scientificCalculator.populationMean(data);
        for i in range(0, n):
            dev= dev+ (data[i]-mean)**(2)
        stdev = (dev/n)**(1/2)
        return stdev

    @staticmethod
    def populationVariance(data):
        stdev = scientificCalculator.populationStandardDeviation(data)
        variance = (stdev)**(2)
        return (variance)

    @staticmethod
    def standardizedScore(data, i):
        stdev = scientificCalculator.populationStandardDeviation(data);
        mean = scientificCalculator.populationMean(data)
        standardizedScore = (data[i]-mean)/stdev
        return standardizedScore

    @staticmethod
    def sampleMean(data,m):
        sum=0
        for i in range(0,m): sum= sum +data[i]
        return float(sum/m);


if __name__ == '__main__':
        choice = ""

        data = [61.30144938,47.60287892,49.68059683,46.78598215,31.56768015,55.43093392,52.31036665,65.32512215,42.86435468,59.75510375]
        while choice != "16":
            print("Select the operation:")
            print("1. Population Mean")
            print("2. Median")
            print("3. Mode")
            print("4. Population Standard Deviation")
            print("5. Variance of population proportion")
            print("6. Z-Score")
            print("7. Standardized score")
            print("8. Population Correlation Coefficient")
            print("9. Confidence Interval")
            print("10. Population Variance")
            print("11. P Value")
            print("12. Proportion")
            print("13. Sample Mean")
            print("14. Sample Standard Deviation")
            print("15. Variance of sample proportion")
            print("16. Quit")

            choice = input("Enter Choice: ")

            if choice == "1":
                print( scientificCalculator.populationMean(data));
            elif choice == "4":
                print(scientificCalculator.populationStandardDeviation(data));

            elif choice == "7":
                print(scientificCalculator.standardizedScore(data,4));

            elif choice == "10":
                print(scientificCalculator.populationVariance(data));

            elif choice == "13":
                print(scientificCalculator.sampleMean(data,6));
