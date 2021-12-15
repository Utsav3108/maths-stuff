import math
import pandas as pd
def coin():
    print(math.comb(6,2))
    fair_coins = 12
    total_space = 2**fair_coins
    upper = fair_coins
    lower = 0
    probability = []
    x = []
    for i in range(lower,upper+1):
        x.append(i)
        print(f"P(X={i})")
        no_of_favEve = math.comb(fair_coins,i)
        prob = no_of_favEve/total_space
        probability.append(prob)
    
    data = {'X=x':x,
            'P(X=x)':probability}
    print(x)
    df = pd.DataFrame(data)
    print(df)
    print("Sum:",sum(probability))

def problem_of_car():
    def_car = 5
    selected_car = 15
    total_car = 30
    total_space = math.comb(total_car,selected_car)
    print("Space:",total_space)
    upper = selected_car
    lower = 0
    non_def = total_car-def_car
    probability = []
    x = []
    for i in range(lower,upper+1):
        if i<=def_car:
            x.append(i)
            c1 = math.comb(non_def,selected_car-i)
            c2 = math.comb(def_car,i)
            no_of_favEve = c1*c2
            prob = no_of_favEve/total_space
            print(f"P(X={i}) = {prob}")
            probability.append(prob)
    data = {'X=x':x,
            'P(X=x)':probability}
    print(x)
    df = pd.DataFrame(data)
    print(df)
    print("Sum:",sum(probability))

problem_of_car()