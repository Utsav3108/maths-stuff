import math 
import matplotlib.pyplot as plt

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
        try:
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
            return {'QuartileD':quartile_d,'Q3':q3,'Q1':q1}

        except Exception:
            print("Invalid Inputs")

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
        return {'Variance':round(Var,3),'SD':round(math.sqrt(Var),3)}

    def plot(self,xlabel,ylabel):
        plt.plot(self.x,self.px)
        plt.xlabel(f'{xlabel}')
        plt.ylabel(f'{ylabel}')
        plt.show()
        


