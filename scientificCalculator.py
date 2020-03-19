class scientificCalculator:

    #Population Mean
    @staticmethod
    def populationMean(data):
        n= len(data)
        sum=0
        for i in range(0,n): sum= sum +data[i]
        return sum/n ;



if __name__ == '__main__':
        choice = ""

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
                data=[1,2,3,4,5,6,7,8,9,11]
                print( scientificCalculator.populationMean(data));
