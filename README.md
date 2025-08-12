# Internship-Day---5
Data analysis on CSV files


Frist we begin by importing 'pandas' and 'matolptlib'. Pandas is a python library used for data manipulation and analysis and matplotlib is used for creating plots and charts.
Then we use the read_csv() function so that we can read CSV file using pandas.
We then use file.columns which allows us to get the names of columns and str.strip() removes any extra spaces before or after each columns name.This prevents errors when accesing columns by name.
groupby() allows us to group rows that have the same value in the 'category' column,['sales'] selects just the number or digits from the group.
Then we add the numbers using sum() in each group.
plot() allows to plot the grouped data. "kind" specifies a bar chart, "title" specifies a title for the chart.
xlabel and ylabel  specifies the label of x-axis and y-axis of the chart.
show() displays the chart on the screen
