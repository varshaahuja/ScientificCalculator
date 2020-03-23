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

@staticmethod
def stdev(df):
  mean = sum(df) / len(df)
  sample_variance = sum((x - mean) ** 2 for x in df) / (len(df) - 1)

  samplestandard_deviation = sample_variance ** (0.5)
  return round(standard_deviation)

@staticmethod
def population_proportion_variance(num):
    for p in num:
      prop = p / sum(num)

    x = (prop * (1 - prop) / sum(num))

    variance_of_pop_prop = x ** (0.5)

    return variance_of_pop_prop




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

if choice == "2":
    print(calculate_median(l));

if choice == "14"
    print("The sample standard deviation of List is", stdev(df));

if choice == "5"
    print("The Variance of population proportion of list is", population_proportion_variance(num);
