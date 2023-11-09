# Load the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the data sets
df1 = pd.read_csv("TSLA.csv")
df2 = pd.read_csv("BMW.DE.csv")
df3 = pd.read_csv("BYDDY.csv")
df4 = pd.read_csv("GM.csv")

import pandas as pd
import matplotlib.pyplot as plt

def create_line_plot(data_frames, x_col, y_cols, x_label, y_label, title, file_name=None):
    """
    Create a line plot from multiple DataFrames.

    Args:
    data_frames (list of pandas DataFrames): List of DataFrames to plot.
    x_col (str): Column name for the x-axis.
    y_cols (list of str): List of column names for the y-axis.
    x_label (str): Label for the x-axis.
    y_label (str): Label for the y-axis.
    title (str): Title for the chart.
    file_name (str, optional): If provided, save the plot as a file with this name.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))  # Set the figure size

    for df, y_col in zip(data_frames, y_cols):
        plt.plot(df[x_col], df[y_col], label=y_col)

    # Customize the plot with labels, title, and legend
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()

    # Rotate the x-axis labels for better readability (optional)
    plt.xticks(rotation=45)

    # Save the plot as a file (if file_name is provided)
    if file_name:
        plt.tight_layout()
        plt.savefig(file_name, format='png')

    # Show the plot
    plt.show()

# Load the data sets
df1 = pd.read_csv("TSLA.csv")
df2 = pd.read_csv("BMW.DE.csv")
df3 = pd.read_csv("BYDDY.csv")
df4 = pd.read_csv("GM.csv")

# Rename the 'Close' columns in the DataFrames
df1 = df1.rename(columns={'Close': 'Tesla Close'})
df2 = df2.rename(columns={'Close': 'BMW Close'})
df3 = df3.rename(columns={'Close': 'BYD Close'})
df4 = df4.rename(columns={'Close': 'GM Close'})

# Define the DataFrames and column names for the line plot
data_frames = [df1, df2, df3, df4]
x_column = 'Date'
y_columns = ['Tesla Close', 'BMW Close', 'BYD Close', 'GM Close']
x_label = 'Date'
y_label = 'Close Price'
plot_title = 'Popular EV Car Companies Close Price Over Time'

# Create a line plot with the specified parameters
create_line_plot(data_frames, x_column, y_columns, x_label, y_label, plot_title, 'lineplot.png')

import pandas as pd
import matplotlib.pyplot as plt

def create_pie_chart_from_csv(file_path, title, file_name=None):
    """
    Create a pie chart from data in a CSV file.

    Args:
    file_path (str): Path to the CSV file containing the data.
    title (str): Title for the chart.
    file_name (str, optional): If provided, save the plot as a file with this name.

    Returns:
    None
    """
    data = pd.read_excel(file_path)  # Read data from the CSV file
    browsers = data['Browser']
    usage = data['Usage']

    plt.figure(figsize=(8, 8))  # Set the figure size

    # Plot the pie chart
    plt.pie(usage, labels=browsers, autopct='%1.1f%%', startangle=140, shadow=True)

    # Add a title
    plt.title(title)

    # Save the plot as a file (if file_name is provided)
    if file_name:
        plt.tight_layout()
        plt.savefig(file_name, format='png')

    # Show the pie chart
    plt.show()

# Path to the CSV file containing browser and usage data
csv_file_path = "Internet Usage.xlsx"

# Title for the pie chart
chart_title = 'Web Browsers Usage in 2023'

# Create a pie chart using the data from the CSV file
create_pie_chart_from_csv(csv_file_path, chart_title, 'pie_chart.png')

data= pd.read_csv("smoking.csv")

import pandas as pd
import matplotlib.pyplot as plt

# Assuming your dataset is loaded into a variable called 'data'
# Replace 'data.csv' with your actual dataset filename if you're loading from a CSV file
# data = pd.read_csv('data.csv')

# Clean the data by removing rows with NaN values in the 'smoke' and 'age' columns
cleaned_data = data.dropna(subset=['smoke', 'age'])

# Define age bins
age_bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create age groups using pd.cut() function
age_groups = pd.cut(cleaned_data['age'], bins=age_bins, right=False)

# Count the number of people who smoke and do not smoke for each age group
smokers_count = cleaned_data[cleaned_data['smoke'] == 'Yes']['age'].groupby(age_groups).count()
non_smokers_count = cleaned_data[cleaned_data['smoke'] == 'No']['age'].groupby(age_groups).count()

# Plotting the histogram chart
plt.figure(figsize=(10, 6))
plt.bar(age_bins[:-1], smokers_count, width=8, label='Smokers', alpha=0.7)
plt.bar(age_bins[:-1], non_smokers_count, width=8, label='Non-Smokers', alpha=0.7, bottom=smokers_count)
plt.xlabel('Age Groups')
plt.ylabel('Number of People')
plt.title('Age Groups vs Number of People Who Smoke and Do Not Smoke')
plt.xticks(age_bins[:-1], ['10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90-100'])
plt.legend()
plt.tight_layout()
plt.show()
