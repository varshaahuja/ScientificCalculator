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


l = [1]
print(calculate_median(l))

l = [3, 1, 2]
print(calculate_median(l))

l = [1, 2, 3, 4]
print(calculate_median(l))

# calculate Variance

def population_variance(num):
  sumOfNumbers = 0
  for t in num:
    sumOfNumbers = sumOfNumbers + t

  avg = sumOfNumbers / len(num)

  var = sum((t - avg) ** 2 for t in num) / len(num)
  return var


print("The variance of List is", population_variance([19, 21, 46, 11, 18]))

@staticmethod
def stdev(df):
  mean = sum(df) / len(df)
  sample_variance = sum((x - mean) ** 2 for x in df) / (len(df) - 1)

  standard_deviation = sample_variance ** (0.5)
  return round(standard_deviation)

  print("The sample standard deviation of List is", stdev([19, 21, 46, 11, 18]))


@staticmethod
def populatuin_proportion_variance(num):
    for p in num:
      prop = p / sum(num)

    x = (prop * (1 - prop) / sum(num))

    variance_of_pop_prop = x ** (0.5)

    return variance_of_pop_prop

@staticmethod
def correlationCoefficient(X, Y, n):
  sum_X = 0
  sum_Y = 0
  sum_XY = 0
  squareSum_X = 0
  squareSum_Y = 0

  i = 0
  while i < n:
    sum_X = sum_X + X[i]

    sum_Y = sum_Y + Y[i]

    sum_XY = sum_XY + X[i] * Y[i]

    squareSum_X = squareSum_X + X[i] * X[i]
    squareSum_Y = squareSum_Y + Y[i] * Y[i]

    i = i + 1

  # use formula for calculating correlation
  # coefficient.
  corr = (n * sum_XY - sum_X * sum_Y) / (math.sqrt((n * squareSum_X - sum_X * sum_X) * (n * squareSum_Y - sum_Y * sum_Y)))

  return corr








