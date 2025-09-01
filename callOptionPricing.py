import numpy as np

 # Parameters
S0 = 100      # initial stock price
E = 105       # exercise price
T = 1.0       # maturity time (1 year)
r = 0.05     # risk-free rate
sigma = 0.2   # standard deviation or volatility
N = 1000000    # simulation number

def monteCarloCallPrice(I,K,time,r,sd,N):
 #stock prices being simulated 
 Z = np.random.standard_normal(N) #random numbers -1 to 1
 stockPrices = I*np.exp((r - 0.5*sd**2)*time + sd*np.sqrt(time)*Z)
 #initial stock price * e^[drift term * diffusion time]

 payoffs = np.maximum(stockPrices - K, 0) 
 #payoffs are non-negative obvs as makes no sense

 #discount rate over time makes up for risk-free alt investments
 optionPrice = np.exp(-r*time)*np.mean(payoffs)
 return(optionPrice)

def AbrSteErfApprox(x):
  #cant support scripy, so using approx for error function
    sign = np.sign(x)
    x = np.abs(x)
    t = 1 / (1 + 0.3275911 * x)
    # coefficients
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    y = 1 - (((((a5*t + a4)*t + a3)*t + a2)*t + a1) * t * np.exp(-x*x))
    return (sign * y)

def normalCDF(x):
    return 0.5 * (1 + AbrSteErfApprox((x/(np.sqrt(2)))))

def blackScholesCallPrice(I,K,time,r,sd,N) :
 d1 = (np.log(I/K) + (r + 0.5*sd**2)*time)/(sd*np.sqrt(time))
 d2 = d1 - sd*np.sqrt(time)
 optionBSPrice = I*normalCDF(d1) - K*np.exp(-r*time)*normalCDF(d2)
 return(optionBSPrice)
 
def montBlackDiff(a,b):
 return(np.abs(a-b))
 
def avrgDifference(n):
 sum = 0
 for i in range(n):
  m = monteCarloCallPrice(S0,E,T,r,sigma,N)
  b = blackScholesCallPrice(S0,E,T,r,sigma,N)
  sum = sum + np.abs(m-b)
  avrg = sum/n
  return(avrg)


print(" ") 
x = input("Enter number of test samples:")
print("Black-Scholes estimate of call option price:" + str(blackScholesCallPrice(S0,E,T,r,sigma,N)))
print("Monte Carlo estimate of call option price:" + str(monteCarloCallPrice(S0,E,T,r,sigma,N)))

print("Absolute difference is: " + str(montBlackDiff(blackScholesCallPrice(S0,E,T,r,sigma,N),monteCarloCallPrice(S0,E,T,r,sigma,N))))


print("Average difference of " + x + " samples is " + str(avrgDifference(int(x))))
