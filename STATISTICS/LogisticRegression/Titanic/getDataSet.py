from pydataset import data

# Load the Titanic dataset
titanic = data('titanic')

# Save the dataset to a CSV file
titanic.to_csv('titanic.csv', index=False)