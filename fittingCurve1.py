import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("       ...........fitting Curve........           ")
x=[]
y=[]
x2l = []
y2l = []
xyl = []
X=[]
Y=[]

def Curve():
    try:
        def plot():
            new_points1 = []
            new_points2 = []
            ask = str(input("Want to see graph(y/n):"))
            if ask=="y":
                ask1 = int(input("Enter No. of points you want to take:"))
                for i in range(ask1):                      #straight line
                    X1 = float(input("Hence at x="))    # New points 
                    X.append(X1)
                    new_points1.append(X1)       

                    Y1 = a+b*X1
                    Y.append(Y1)
                    new_points2.append(Y1)

                print(f"x={X}, y={Y}")
                plt.scatter(new_points1,new_points2,label="Estimated",color="Green")
                plt.scatter(x,y,label="Data",color="k")
                plt.plot(X,Y,label='Straight line')

                plt.title("Fitting Curve")          #Information of plot
                plt.xlabel("x-axis")
                plt.ylabel("y-axis")
                plt.legend(loc ="lower left")

                plt.show() 
            if ask=="n":
                exit()
    
        ni = int(input("Enter no. of inputs:"))
        for i in range(ni):
                xi = float(input("Enter elements of x:"))
                x.append(xi)
                
        for i in range(ni):
                yi = float(input("Enter elements of y:"))
                y.append(yi)
        print(x)
        print(y)
        print("====================")
        dep = str(input("Dependent on(x/y):"))
        n = 0
        sum_y = 0
        sum_x = 0
        sum_x2 = 0
        sum_xy = 0
        sum_y2 = 0
        for i in x:
            n = n + (i+1)/(i+1)
        for j in y:
            sum_y = sum_y + j
            sum_y2 = sum_y2 + j**2
            y2l.append(j**2)
        for z in x:
            sum_x = sum_x + z 
            sum_x2 = sum_x2 + z**2
            x2l.append(z**2)
        for i in range(int(n)):
            sum_xy = sum_xy + x[i]*y[i]
            xyl.append(x[i]*y[i])
        sum_xyy =  float("{:.1f}".format(sum_xy))
        if dep=="x":                       # If the equation depends on x, Ex. y = mx + c
            fr = {
                'x':x,         #x,y Scatter
                'y':y,
                'x2':x2l,
                'xy':xyl
                }
            print("n =",n)
            tab = pd.DataFrame(fr)
            print(tab)
            print("---------------------------------")
            print("Sum of x:",sum_x)
            print("Sum of y:",sum_y)
            print("Sum of x2:",sum_x2)
            print("Sum of xy:",sum_xyy)

            a1 = np.array([[n,sum_x],[sum_x,sum_x2]])
            a2 = np.array([[sum_y],[sum_xyy]])
            ina1 = np.linalg.inv(a1)
            a11 = np.dot(ina1,a2)
            A = a11[0,0]
            B= a11[1,0]
            a = float("{:.3f}".format(A))
            b = float("{:.3f}".format(B))
            print(f"|a={a},b={b}|")

            plot()                                          
            exit()   
        elif dep=="y":        #If the equation depends on the y, Ex. x = my + c
            fr = {
                'x':x,
                'y':y,
                'y2':y2l,
                'xy':xyl
                }
            print("n =",n)
            tab = pd.DataFrame(fr)
            print(tab)
            print("---------------------------------")
            print("Sum of x:",sum_x)
            print("Sum of y:",sum_y)
            print("Sum of y2:",sum_y2)
            print("Sum of xy:",sum_xyy)

            a1 = np.array([[n,sum_y],[sum_y,sum_y2]])
            a2 = np.array([[sum_x],[sum_xyy]])
            ina1 = np.linalg.inv(a1)
            a11 = np.dot(ina1,a2)
            A = a11[0,0]
            B= a11[1,0]
            a = float("{:.3f}".format(A))
            b = float("{:.3f}".format(B))
            print("---------------")
            print(f"|a={a},b={b}|")
            print("---------------")
            plot()
            exit()    
        else:
            print("give valid input")   
    except Exception:
        print("Invalid Input")
Curve()






