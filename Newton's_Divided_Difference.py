x_values = [1, 2, 3, 4, 5]
y_values = [30, 15, 32, 18, 25]

def divided_difference_table(x_values, y_values):
    n = len(x_values)
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y_values[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_values[i + j] - x_values[i])
    return table

def newton_interpolation(x_values, y_values, target):
    table = divided_difference_table(x_values, y_values)
    n = len(x_values)
    result = table[0][0]
    product_term = 1
    for i in range(1, n):
        product_term *= (target - x_values[i - 1])
        result += product_term * table[0][i]
    return result

def newton_derivative(x_values, y_values, target):
    table = divided_difference_table(x_values, y_values)
    n = len(x_values)
    derivative = table[0][1]
    product_term = 1
    for i in range(2, n):
        product_term *= (target - x_values[i - 2])
        derivative += i * product_term * table[0][i]
    return derivative

y_at_2_5 = newton_interpolation(x_values, y_values, 2.5)
dy_at_3 = newton_derivative(x_values, y_values, 3)

print(f"y(2.5) = {y_at_2_5:.3f}")
print(f"y'(3) = {dy_at_3:.3f}")
