from simpleCalculator import simpleCalculator as calculator
import pytest
import unittest
import csv
from scientificCalculator import scientificCalculator as scientificCalculator


class test_PythonSimpleCalc(unittest.TestCase):

    def test_calc(self):
        assert calculator

    def test_calc_add(self):
        num1 = []
        num2 = []
        res = []
        i = 0
        with open('Unit Test Addition.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV)
            for row in readCSV:
                num1.append(row[0])
                num2.append(row[1])
                res.append(row[2])
            while (i != len(num1)):
                assert calculator.add(int(num1[i]), int(num2[i])) == int(res[i])
                i = i + 1;

    def test_calc_subtract(self):
        num1 = []
        num2 = []
        res = []
        i = 0
        with open('Unit Test Subtraction.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV)
            for row in readCSV:
                num1.append(row[0])
                num2.append(row[1])
                res.append(row[2])
            while (i != len(num1)):
                assert calculator.subtraction(int(num2[i]), int(num1[i])) == int(res[i])
                i = i + 1;

    def test_calc_multiply(self):
        num1 = []
        num2 = []
        res = []
        i = 0
        with open('Unit Test Multiplication.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV)
            for row in readCSV:
                num1.append(row[0])
                num2.append(row[1])
                res.append(row[2])
            while (i != len(num1)):
                assert calculator.multiply(int(num2[i]), int(num1[i])) == int(res[i])
                i = i + 1;

    def test_calc_divide(self):
        num1 = []
        num2 = []
        res = []
        i = 0
        with open('Unit Test Division.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV)
            for row in readCSV:
                num1.append(row[0])
                num2.append(row[1])
                res.append(row[2])
            while (i != len(num1)):
                assert round(calculator.divide(float(num2[i]), float(num1[i])), 9) == float(res[i])
                i = i + 1;

    def test_calc_square(self):
        num1 = []
        res = []
        i = 0
        with open('Unit Test Square.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV)
            for row in readCSV:
                num1.append(row[0])
                res.append(row[1])
            while (i != len(num1)):
                assert calculator.square(int(num1[i])) == int(res[i])
                i = i + 1;

    def test_calc_squareroot(self):
        num1 = []
        res = []
        i = 0
        with open('Unit Test Square Root.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV)
            for row in readCSV:
                num1.append(row[0])
                res.append(row[1])
            while (i != len(num1)):
                assert round(calculator.squareRoot(float(num1[i])), 8) == round(float(res[i]), 8)
                i = i + 1;

    def test_calc_populationMean(self):

        input = csv.reader(open("populationMean.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert float(scientificCalculator.populationMean((list_of_floats))) == float(row[10])

    def test_calc_populationStandardDeviation(self):
        input = csv.reader(open("populationStandardDeviation.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert float(scientificCalculator.populationStandardDeviation((list_of_floats))) == float(row[10])

    def test_calc_standardizedScore(self):
        input = csv.reader(open("standardizedScore.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert  float(scientificCalculator.standardizedScore((list_of_floats), int(row[11]))) == float(row[10])

    def test_calc_populationVariance(self):
        input = csv.reader(open("populationVariance.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert float(scientificCalculator.populationVariance((list_of_floats))) == float(row[10])

    def test_calc_samplmean(self):
        input = csv.reader(open("sampleMean.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert float(scientificCalculator.sampleMean(list_of_floats, int(row[11]))) == float(row[10])

    def test_calc_ZScore(self):
        input = csv.reader(open("Unit_Test_ZScore.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert  float((scientificCalculator.zscore((list_of_floats), int(row[11]))) == float(row[10]))

    def test_calc_Proportion(self):
        input = csv.reader(open("Unit_Test_Proportion.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert  float((scientificCalculator.zscore((list_of_floats), int(row[11]))) == float(row[10]))

    def test_calc_Mode(self):
        input = csv.reader(open("Unit_Test_Mode.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert scientificCalculator.mode(list_of_floats) == float(row[10])

    def test_calc_Var(self):
        input = csv.reader(open("Unit_Test_Var.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert scientificCalculator.var(list_of_floats) == float(row[10])

    def test_calc_CI(self):
        input = csv.reader(open("Unit_Test_CI.csv"))
        next(input)
        for row in input:
            list_of_floats = []
            output_floats = []
            for item2 in row[10:14]:
                output_floats.append(float(item2))
            for item in row[0:10]:
                list_of_floats.append(float(item))
            assert scientificCalculator.confidence_interval((list_of_floats), float(row[14])) == output_floats