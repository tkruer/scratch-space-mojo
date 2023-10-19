from math import sqrt, exp, log, cos, sin
from random import rand, random_float64

"""
    We don't have a norm cdf in the standard library so we can just create a monte_carlo funciton to approximate it.
    We also don't have a random number sampler from a normal distribution so we can use the Box-Muller transform to create one.
    All of these functions induce complexities and aren't going to give us the most accurate results but they are good enough for this example.
"""

fn box_muller() -> Float64:
    let pi: Float64 = 3.1415926
    let uniform_one: Float64 = random_float64(0, 1)
    let uniform_two: Float64 = random_float64(0, 1)
    let z_one: Float64 = sqrt(-2 * log(uniform_one)) * cos(2 * pi * uniform_two)
    
    return z_one

fn monte_carlo_cdf(x: Float64) -> Float64:
    let n: Int = 1000000
    var sum: Float64 = 0
    for i in range(n):
        let sample: Float64 = box_muller()
        if sample <= x:
            sum += 1
    return sum / n

fn black_scholes_call(stock_price: Float64, strike_price: Float64, exp_time_yr: Float64, ann_risk_free_rate: Float64, volt_ann_stock: Float64) -> Float64:
    let deriv_one: Float64 = (log(stock_price / strike_price) + (ann_risk_free_rate + 0.5 * volt_ann_stock ** 2) * exp_time_yr) / (volt_ann_stock * sqrt(exp_time_yr))
    let deriv_two: Float64 = deriv_one - volt_ann_stock * sqrt(exp_time_yr)
    let call_price: Float64 = (stock_price * monte_carlo_cdf(x=deriv_one) - (strike_price * exp(-ann_risk_free_rate * exp_time_yr) * monte_carlo_cdf(x=deriv_two)))
    return call_price

fn main():
    let result: Float64 = black_scholes_call(stock_price=100, strike_price=100, exp_time_yr=1, ann_risk_free_rate=0.05, volt_ann_stock=0.2)
    print("The theoretical price of the European call option is: $", result)
    print("""
        If it works, it works.       
    """)
    
    
