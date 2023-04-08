# Code by: Anh Da Dep Trai

import math
import matplotlib.pyplot as plt

def get_user_input():
    while True:
        try:
            prediction = input("Enter the predicted values (separated by commas): ")
            target = input("Enter the target values (separated by commas): ")
            prediction_list = [float(x.strip()) for x in prediction.split(',')]
            target_list = [float(x.strip()) for x in target.split(',')]
        except ValueError:
            print("Error: Please enter numeric values only.\n")
            continue

        if len(prediction_list) != len(target_list):
            print("Error: Prediction and target lists must have the same length.\n")
            continue

        return prediction_list, target_list

def calculate_regression_params(prediction_list, target_list):
    n = len(prediction_list)
    average_x = sum(prediction_list) / n
    average_y = sum(target_list) / n
    SSx = sum([(x - average_x) ** 2 for x in prediction_list])
    SSxy = sum([(x - average_x) * (y - average_y) for x, y in zip(prediction_list, target_list)])
    a = SSxy / SSx
    b = average_y - a * average_x
    return a, b

def calculate_metrics(prediction_list, target_list, a, b):
    n = len(prediction_list)
    average_y = sum(target_list) / n
    variance_y = sum([(y - average_y) ** 2 for y in target_list]) / n
    mae = sum([abs(p - t) for p, t in zip(prediction_list, target_list)]) / n
    mse = sum([(p - t) ** 2 for p, t in zip(prediction_list, target_list)]) / n
    rmse = math.sqrt(mse)
    SSR = sum([(a * x + b - y) ** 2 for x, y in zip(prediction_list, target_list)])
    SST = sum([(y - average_y) ** 2 for y in target_list])
    R1 = 1 - (SSR / SST)
    R2 = 1 - (mse / variance_y)
    return mae, mse, rmse, SSR, SST, R1, R2

def print_metrics(prediction_list, target_list, a, b, mae, mse, rmse, SSR, SST, R1, R2):
    average_x = sum(prediction_list) / len(prediction_list)
    average_y = sum(target_list) / len(target_list)
    print(f"\nAverage X: {average_x:.3f}"
          f"\nAverage Y: {average_y:.3f}"
          f"\nRegression line: Y = {a:.3f}X + {b:.3f}"
          f"\nMAE: {mae:.3f}"
          f"\nMSE: {mse:.3f}"
          f"\nRMSE: {rmse:.3f}"
          f"\nSSR: {SSR:.3f}"
          f"\nSST: {SST:.3f}"
          f"\nR-squared: {R1:.3f}"
          f"\nAlternative R-squared: {R2:.3f}")
    return average_x, average_y, mae, mse, R1, R2, SSR, SST

def draw_graph(prediction_list, target_list, a, b):
    prediction_list, target_list = zip(*sorted(zip(prediction_list, target_list)))

    plt.scatter(prediction_list, target_list)
    plt.plot(prediction_list, [a * x + b for x in prediction_list], color='red')

    for i in range(len(prediction_list)-1):
        x1, y1 = prediction_list[i], target_list[i]
        x2, y2 = prediction_list[i+1], target_list[i+1]
        slope = 1 if i % 2 == 0 else -1
        plt.plot([x1, x2], [y1, y2], color='blue', linestyle='--', linewidth=0.5, alpha=0.5, solid_capstyle='round', dash_capstyle='round', dash_joinstyle='round', dashes=[3,3], zorder=0)

    for i in range(len(prediction_list)):
        plt.annotate(f"({prediction_list[i]}, {target_list[i]})", (prediction_list[i], target_list[i]))

    plt.xlabel('Predicted Values')
    plt.ylabel('Target Values')
    plt.title('Regression Line Graph')
    plt.show()

def ask_to_continue():
    while True:
        user_input = input("Do you want to continue? (Y/N): ").upper()
        if user_input == 'Y':
            return True
        elif user_input == 'N':
            return False
        else:
            print("Error: Please enter Y or N only.\n")
            continue

def main():
    while True:
        prediction_list, target_list = get_user_input()
        a, b = calculate_regression_params(prediction_list, target_list)
        mae, mse, rmse, SSR, SST, R1, R2 = calculate_metrics(prediction_list, target_list, a, b)
        print_metrics(prediction_list, target_list, a, b, mae, mse, rmse, SSR, SST, R1, R2)
        draw_graph(prediction_list, target_list, a, b)
        if not ask_to_continue():
            break

if __name__ == '__main__':
    main()