import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt
x = np.array([0,1,2,3,4,5,6,7,8])
px = np.array([0.004,.036,.1,.232,.280,.204,.112,.028,.004])
x11 = np.array([1,2,3,4,5,6,7,8])
px11 = np.array([.008,.032,.142,.216,.240,.206,.143,.013])
x1 = np.array([2,5,8,7,11])
px1 = np.array([.1,.15,.25,.24,.26])

class stats:
    def __init__(self,x,px):
        self.x = x
        self.px = px

    def mean(self):
        sum = 0
        for i,j in zip(self.x,self.px):
            v1 = i*j
            sum += v1
        return round(sum,3)

    def geometric_mean(self):
        try:
            sum=0
            for i,j in zip(self.x,self.px):
                v1 = math.log(i)*j
                sum = v1
            return sum
        except ValueError:
            print("Domain Error of log, Remove 0 or negative values")

    def harmonic_mean(self):
        if 0 in self.x:
            print("Cannot divide by zero")
            return
        sum=0
        for i,j in zip(self.x,self.px):
            v1 = (1/i)*j
            sum = v1
        return 1/sum

    def median(self):
        sum= 0
        index = 0
        for j in self.px:
            sum += j
            if sum == 0.5:
                ans = self.x[index]
                return ans
            elif sum>0.5:
                ans = (self.x[index] + self.x[index - 1])/2
                return ans
            else:
                pass
            index += 1

    def QD(self):
        sum= 0
        index = 0
        for j in self.px:
            sum += j
            if sum == 0.25:
                q1 = self.x[index]
            elif sum < 0.25:
                q1 = (self.x[index] + self.x[index + 1])/2
            if sum == 0.75:
                q3 = self.x[index]    
                break
            elif sum > 0.75:
                q3 = (self.x[index] + self.x[index - 1])/2
                break    
            else:
                pass
            index += 1
        quartile_d = (q3 - q1)/2
        return quartile_d,q3,q1

    def MD(self):
        sum = 0
        for i,j in zip(self.x,self.px):
            sum += abs(i - self.mean())*j
        return round(sum,3)

    def m_(self,p):
        sum = 0
        if p == 1:
            return self.mean()
        for i,j in zip(self.x,self.px):
            sum += (i**p)*j
        return sum

    def SD(self):
        Var = self.m_(2) - self.mean()**2
        return round(Var,3),round(math.sqrt(Var),3)

    def plot(self):
        plt.plot(self.x,self.px)
        plt.show()
        

y = stats(x,px)
print(y.mean())
print(y.median())
print("QD:",y.QD())
print(y.geometric_mean())
print(y.harmonic_mean())
print("Md:",y.MD())
print("m'2:",y.m_(2))
print("SD:",y.SD())
y.plot()

