x_points = [1, 2, 3, 4]
y_points = [1, 5, 11, 8]

def lagrange_interpolation(x_values, y_values, target):
    n = len(x_values)
    interpolation_sum = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (target - x_values[j]) / (x_values[i] - x_values[j])
        interpolation_sum += term

    return interpolation_sum

def lagrange_derivative(x_values, y_values, target):
    n = len(x_values)
    derivative_sum = 0

    for i in range(n):
        term_sum = 0
        for j in range(n):
            if i != j:
                numerator = 1
                for k in range(n):
                    if k != i and k != j:
                        numerator *= (target - x_values[k])
                term_sum += numerator / (x_values[i] - x_values[j])
        derivative_sum += term_sum * y_values[i]
    return derivative_sum

y_at_1_5 = lagrange_interpolation(x_points, y_points, 1.5)
dy_at_3 = lagrange_derivative(x_points, y_points, 3)

print(f"y(1.5) = {y_at_1_5:.3f}")
print(f"y'(3) = {dy_at_3:.3f}")

