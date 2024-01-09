import matplotlib.pyplot as plt

def euler_method(b, k, initial_conditions, days):
    """Calculates and plots the SIR Model using Euler's Method.

    Args:
        b: Infection rate.
        k: Recovery rate.
        initial_conditions: Tuple representing initial susceptible, infected, and removed populations.
        days: Number of days for the simulation.

    Returns:
        t, S, I, R: Time, Susceptible, Infected, and Removed populations over time.
    """
    t, S, I, R = [0], [initial_conditions[0]], [initial_conditions[1]], [initial_conditions[2]]

    for day in range(days):
        prev_day = day - 1
        N = S[prev_day] + I[prev_day] + R[prev_day]
        t.append(day)
        S.append(S[prev_day] + ((-b * S[prev_day] * I[prev_day]) / N))
        I.append(I[prev_day] + ((b * S[prev_day] * I[prev_day]) / N) - (k * I[prev_day]))
        R.append(R[prev_day] + (k * I[prev_day]))

    return t, S, I, R

def plot_SIR(t, S, I, R):
    """Plots the SIR Model.

    Args:
        t, S, I, R: Time, Susceptible, Infected, and Removed populations over time.
    """
    plt.plot(t, S, label="Susceptible")
    plt.plot(t, I, label="Infected")
    plt.plot(t, R, label="Removed")
    plt.legend()
    plt.title("SIR Model")
    plt.ylabel("Number of People / millions")
    plt.xlabel("Time / days")
    plt.show()

# Example usage:
b = 0.5
k = 0.1
initial_conditions = (1000, 1, 0)
days = 100

t, S, I, R = euler_method(b, k, initial_conditions, days)
plot_SIR(t, S, I, R)time / days")
    plt.show()
    
Euler_Method(0.1, 0.05, [1240000, 1, 0], 1000)
