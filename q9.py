import pandas as pd
import matplotlib.pyplot as plt
import statistics
filepath = "C:\\Users\\sevit\\Downloads\\Machine Learning\\ML-lab\\Session Data.xlsx"
data = pd.read_excel(filepath, sheet_name="IRCTC Stock Price")
prices = data['Price'].tolist()
mean_price = statistics.mean(prices)
variance_price = statistics.variance(prices)
print(f"Mean Price: {mean_price}")
print(f"Price Variance: {variance_price}")
wednesday_prices = data[data['Day'] == 'Wed']['Price'].tolist()
mean_wed_price = statistics.mean(wednesday_prices)
print(f"Wednesday Mean Price: {mean_wed_price}")
if mean_wed_price > mean_price:
    print("Wednesday's average price is higher than overall average.")
elif mean_wed_price < mean_price:
    print("Wednesday's average price is lower than overall average.")
else:
    print("Wednesday's average price is equal to overall average.")
april_prices = data[data['Month'] == 'Apr']['Price'].tolist()
mean_april_price = statistics.mean(april_prices)
print(f"April Mean Price: {mean_april_price}")

# Compare April mean with overall mean
if mean_april_price > mean_price:
    print("April's average price is higher than overall average.")
elif mean_april_price < mean_price:
    print("April's average price is lower than overall average.")
else:
    print("April's average price is equal to overall average.")
loss_days = data[data['Chg%'] < 0]
loss_probability = len(loss_days) / len(data)
print(f"Probability of Loss: {loss_probability:.2f}")
wednesdays = data[data['Day'] == 'Wed']
profitable_wed = wednesdays[wednesdays['Chg%'] > 0]
prob_profit_wed = len(profitable_wed) / len(wednesdays)
print(f"Probability of Profit on Wednesday: {prob_profit_wed:.2f}")
print(f"Conditional Probability of Profit given it's Wednesday: {prob_profit_wed:.2f}")
plt.scatter(data['Day'], data['Chg%'], alpha=0.7)
plt.title("Daily Price Change (%)")
plt.xlabel("Day of the Week")
plt.ylabel("Change %")
plt.grid(True)
plt.show()
