import random
import math

def box_muller():
    """Generate a sample from a standard normal distribution using the Box-Muller transform."""
    u1 = random.random()  # Uniform(0, 1] random number    
    u2 = random.random()  # Uniform(0, 1] random number

    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)    
    # z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)
    
    return z0  # We only return one of the values, but you could return both if needed.

def monte_carlo_cdf(x, n_samples=100000):
    """Approximate the CDF of the standard normal distribution using Monte Carlo simulation."""
    count = 0
    for _ in range(n_samples):
        sample = box_muller()
        if sample <= x:
            count += 1
            
    return count / n_samples

def black_scholes_call(S, K, T, r, sigma):
    """
    S: Current stock price
    K: Option strike price
    T: Time to expiration (in years)
    r: Risk-free rate (annualized)
    sigma: Volatility of the stock (annualized)
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    
    call_price = S * monte_carlo_cdf(d1) - K * math.exp(-r * T) * monte_carlo_cdf(d2)
    return call_price

S = 100      # Current stock price
K = 100      # Option strike price
T = 1        # Time to expiration (in years)
r = 0.05     # Risk-free rate (5% annualized)
sigma = 0.2  # Volatility (20% annualized)

call_option_price = black_scholes_call(S, K, T, r, sigma)
print(f"The theoretical price of the European call option is: ${call_option_price:.2f}")
