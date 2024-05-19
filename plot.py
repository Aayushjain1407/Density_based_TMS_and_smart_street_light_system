import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Specify the CSV file name
file_name = "sensor1_data.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_name, parse_dates=['TimeStamp'])

# Plot the data
plt.figure(figsize=(10, 6))

plt.plot(df['TimeStamp'], df['Car count 1'], label='Cars on Lane 1', marker='o')
plt.plot(df['TimeStamp'], df['Car count 2'], label='Cars on Lane 2', marker='o')
plt.plot(df['TimeStamp'], df['Street light cars'], label='Cars under street light', marker='o')
# Add more lines for additional columns as needed

plt.title('Traffic plot')
plt.xlabel('Timestamp')
plt.ylabel('Car count')
plt.legend()
plt.grid(True)
plt.show()
print(df.columns)


# Read the CSV file into a DataFrame
file_name = "sensor1_data.csv"
df = pd.read_csv(file_name, parse_dates=['TimeStamp'])

# Display basic information about the DataFrame
print(df.info())

# Display the first few rows of the DataFrame
print(df.head())

# Summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# EDA Plots

# Line plot for Car count 1 vs time
plt.figure(figsize=(12, 6))
plt.plot(df['TimeStamp'], df['Car count 1'], label='Car count 1', marker='o')
plt.title('Car count 1 vs Time')
plt.xlabel('TimeStamp')
plt.ylabel('Number of Cars')
plt.legend()
plt.grid(True)
plt.show()

# Line plot for Car count 2 vs time
plt.figure(figsize=(12, 6))
plt.plot(df['TimeStamp'], df['Car count 2'], label='Car count 2', marker='o')
plt.title('Car count 2 vs Time')
plt.xlabel('TimeStamp')
plt.ylabel('Number of Cars')
plt.legend()
plt.grid(True)
plt.show()

# Line plot for Street light cars vs time
plt.figure(figsize=(12, 6))
plt.plot(df['TimeStamp'], df['Street light cars'], label='Street light cars', marker='o')
plt.title('Street light cars vs Time')
plt.xlabel('TimeStamp')
plt.ylabel('Number of Cars')
plt.legend()
plt.grid(True)
plt.show()

# Pairplot to visualize relationships between numerical variables
sns.pairplot(df[['Car count 1', 'Car count 2', 'Street light cars']])
plt.show()

# Correlation heatmap
correlation_matrix = df[['Car count 1', 'Car count 2', 'Street light cars']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()
