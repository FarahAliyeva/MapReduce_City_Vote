# MapReduce-City-Vote-Analytics
A Python-based MapReduce implementation using mrjob to extract and calculate minimum and maximum vote counts per city from a dataset.



# MapReduce City Vote Analytics

This project utilizes the `mrjob` library to process city-based voting data and determine the range of votes (minimum and maximum) for each city using the MapReduce paradigm.

## Features
- **Data Parsing**: Processes CSV-like structured input lines (expected format: `city,info,votes`).
- **Analytics**: Calculates the minimum and maximum vote counts for each city grouping.
