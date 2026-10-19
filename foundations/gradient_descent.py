class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init 
        
        for it in range(iterations):
            x_prime = 2 * x
            x = x - learning_rate * x_prime
        return round(x, 5)

