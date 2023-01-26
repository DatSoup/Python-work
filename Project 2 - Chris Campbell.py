#Chris Campbell
#c.campbell.1@und.edu
#Project #2
import math

def readTempData (fileName):
    temperatures = open('MarchTemps.txt', 'r')
    highTemps = []
    lowTemps = []
    x = 0
    for line in temperatures:
        if x == 0:
            MonthYear = line
            x=1
            continue
        temps = line.split(',')
        highTemps.append(int(temps[1]))
        lowTemps.append(int(temps[2].strip()))
    return highTemps, lowTemps, MonthYear

def dailyHigh (highTemps, date):        
    if 0 < date <= len(highTemps):
        return highTemps[date - 1]
    else:
        return None

def dailyLow (lowTemps, date):
    if 0 < date <= len(lowTemps):
        return lowTemps[date - 1]

def biggestDailyDifference (highTemps, lowTemps):
    maxDifference = 0
    for index in range(len(highTemps)):
        difference = abs(highTemps[index] - lowTemps[index]) > maxDifference
        if difference > maxDifference:
            maxDifference = difference
    return maxDifference

def dayOfBiggestDailyDifference (highTemps, lowTemps):
    maxDifference = 0
    maxIndex = -1
    for index in range(len(highTemps)):
        difference = abs(highTemps[index] - lowTemps[index]) > maxDifference
        if difference > maxDifference:
            maxDifference = difference
            maxIndex = index
    return maxIndex + 1

def smallestDailyDifference (highTemps, lowTemps) :
    minDifference = 9999
    for index in range(len(highTemps)):
        difference = abs(highTemps[index] - lowTemps[index]) < minDifference
        if difference < minDifference:
            minDifference = difference
    return minDifference

def dayOfSmallestDailyDifference (highTemps, lowTemps) :
    minDifference = 9999
    minIndex = -1
    for index in range(len(highTemps)):
        difference = abs(highTemps[index] - lowTemps[index]) < minDifference
        if difference < minDifference:
            minDifference = difference
            minIndex = index
    return minIndex + 1

def monthlyAverage (temps):
    total = 0
    for n in temps:
        total += n
    return total / len(temps)

def biggestDifferenceBetweenDays (temps):
    maxDifference = 0
    maxIndex = -1
    for index in range(len(temps) - 1):
        difference = abs(temps[index] - temps[index + 1]) > maxDifference
        if difference > maxDifference:
            maxDifference = difference
            maxIndex = index
    return maxIndex + 1

def printTemps (MonthYear, highTemps, lowTemps):
    print("----------%s----------" % MonthYear.strip())
    print("%-5s %10s %10s" % ("Day", "High Temp", "Low Temp"))
    for x in range(len(highTemps)):
        print("%-5d %10d %10d" % (x + 1, highTemps[x], lowTemps[x]))

def main():
    highTemps, lowTemps, MonthYear = readTempData('MarchTemps.txt')
    dailyHigh(highTemps, 5)
    dailyLow(lowTemps, 5)
    biggestDailyDifference(highTemps, lowTemps)
    dayOfBiggestDailyDifference (highTemps, lowTemps)
    smallestDailyDifference (highTemps, lowTemps)
    dayOfSmallestDailyDifference (highTemps, lowTemps)
    monthlyAverage (lowTemps)
    biggestDifferenceBetweenDays (lowTemps)
    printTemps(MonthYear, highTemps, lowTemps)
    
main()