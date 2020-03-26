from simpleCalculator import simpleCalculator as calculator
import pytest
import unittest
import csv
from scientificCalculator import scientificCalculator as scientificCalculator



class test_PythonSimpleCalc(unittest.TestCase):

 def test_calc(self):
        assert calculator

def test_calc_add(self):
        num1=[]
        num2 = []
        res = []
        i=0
        with open('Unit Test Addition.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV)
            for row in readCSV:
                num1.append(row[0])
                num2.append(row[1])
                res.append(row[2])
            while(i!=len(num1)):
               assert calculator.add(int(num1[i]), int(num2[i])) == int(res[i])
               i=i+1;


def test_calc_subtract(self):
        num1=[]
        num2 = []
        res = []
        i=0
        with open('Unit Test Subtraction.csv') as csvfile:
            readCSV = csv.reader(csvfile)
            next(readCSV)
            for row in readCSV:
                num1.append(row[0])
                num2.append(row[1])
                res.append(row[2])
            while(i!=len(num1)):
               assert calculator.subtraction(int(num2[i]), int(num1[i])) == int(res[i])
               i=i+1;

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
                assert round(calculator.squareRoot(float(num1[i])),8) == round(float(res[i]),8)
                i = i + 1;


def test_calc_calculate_median(self):
    input = csv.reader(open("median.csv"))
    next(input)
    list_of_floats = []
    for row in input:
        for item in row[0:10]:
            list_of_floats.append(float(item))
        assert float(scientificCalculator.calculate_median((list_of_floats))) == float(row[10])


def test_calc_stdev(self):
    input = csv.reader(open("sampleStandardDeviation.csv"))
    next(input)
    list_of_floats = []
    for row in input:
        for item in row[0:10]:
            list_of_floats.append(float(item))
        assert float(scientificCalculator.sampleStandardDeviation((list_of_floats))) == float(row[10])


def test_calc_population_proportion_variance(self):
    input = csv.reader(open("varianceOfPopulationProportion.csv"))
    next(input)
    list_of_floats = []
    for row in input:
        for item in row[0:10]:
            list_of_floats.append(float(item))
        assert float(scientificCalculator.population_proportion_variance((list_of_floats), int(row[11]))) == float(
            row[10])


def test_calc_correlationCoefficient(self):
    input = csv.reader(open("populationCoefficientCorrelation.csv"))
    next(input)
    list_of_floats = []
    for row in input:
        for item in row[0:10]:
            list_of_floats.append(float(item))
        assert float(scientificCalculator.correlationCoefficient((list_of_floats))) == float(row[10])



