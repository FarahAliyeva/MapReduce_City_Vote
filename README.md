City Vote
A Python-based MapReduce implementation using mrjob to extract and calculate minimum and maximum vote counts per city from a dataset.



 MapReduce City Vote Analytics

This project utilizes the `mrjob` library to process city-based voting data and determine the range of votes (minimum and maximum) for each city using the MapReduce paradigm.

 Features
- Data Parsing: Processes CSV-like structured input lines (expected format: `city,info,votes`).
- Analytics: Calculates the minimum and maximum vote counts for each city grouping.


Word Frequency
A simple Python implementation of the MapReduce paradigm using the mrjob library to calculate word frequency from text files.

MapReduce Word Frequency Counter
This project demonstrates how to perform a word frequency analysis on text data using the MapReduce programming model in Python with the mrjob library.

Features
Mapper: Splits input text into individual words and counts occurrences.
Combiner & Reducer: Efficiently aggregates counts for each unique word.
Case Insensitive: Converts all words to lowercase to ensure accurate frequency counts.
