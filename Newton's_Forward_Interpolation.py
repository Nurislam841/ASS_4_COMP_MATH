import math
x_values = [1, 2, 3]
y_values = [-6, -1, 16]

def calculate_forward_differences(x_vals, y_vals):
# Formula: Δ^k(y) = y[i + k] - y[i]

    n = len(x_vals)
    diff_table = [y_vals[:]]

    for level in range(1, n):
        current_differences = []
        for i in range(n - level):
            delta = diff_table[level - 1][i + 1] - diff_table[level - 1][i]
            current_differences.append(delta)
        diff_table.append(current_differences)

    return diff_table

# Formula: P(x) = y0 + u*Δ(y0) + u(u-1)/2! * Δ^2(y0) + ...
# where u is equal to (target_x - x0) / h

def newton_forward_interpolation(x_vals, y_vals, target_x):
    h = x_vals[1] - x_vals[0]
    forward_diff = calculate_forward_differences(x_vals, y_vals)

    u = (target_x - x_vals[0]) / h
    result = forward_diff[0][0]
    u_term = 1
    # u, u(u-1), u(u-1)(u-2), ...

    for i in range(1, len(forward_diff)):
        u_term *= (u - (i - 1))
        term = (u_term * forward_diff[i][0]) / math.factorial(i)
        result += term

    return result

# Formula: f'(x) ≈ Δ(y) / h

def calculate_derivative(x_vals, y_vals, point_index):
    h = x_vals[1] - x_vals[0]
    forward_diff = calculate_forward_differences(x_vals, y_vals)
    derivative = forward_diff[1][point_index] / h
    return derivative

target = 1.5
interpolated_y = newton_forward_interpolation(x_values, y_values, target)

derivative_at_2 = calculate_derivative(x_values, y_values, 1)

print(f"Interpolated value y(1.5): {interpolated_y}")
print(f"Derivative y'(2): {derivative_at_2}")