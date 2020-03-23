class scientificCalculator:

@staticmethod
def calculate_median(l):
    l = sorted(l)
    l_len = len(l)
    if l_len < 1:
        return None
    if l_len % 2 == 0:
        return (l[(l_len - 1) // 2] + l[(l_len + 1) // 2]) // 2.0
    else:
        return l[(l_len - 1) // 2]


if __name__ == '__main__':
        choice = ""

        while choice != "7":
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
    print(calculate_median(l));