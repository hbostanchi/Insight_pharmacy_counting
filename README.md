# Table of Contents
1. [Introduction](README.md#Introduction)
1. [Running the Code](README.md#Running-the-Code)
1. [Details of the code](README.md#Details-of-the-code)

## Introduction
This repository is contributed in response to Insight Data Science challenge, regarding loading, pivoting and sorting a data set with large number of rows (>24 million records). 

## Running-the-Code
Although the code is tested with specified big data set, the data is not shared in this repository due to space constrained. 

For this challenge assignment, I used Python and specifically Pandas package to load, manipulate and write the data. Additionally I used sys package to allow running the functions inside the *.py.

To run the code from the main repository directory, where “run.sh” resides, one should run ./run.sh. Within Run.sh the code is calling the “pharmacy_counting.py”, by specifying the input file location “./input/itcont.txt” and output file location “./output/top_cost_drug.txt”. In order to run the code using the big data set, it is required that the cvs file be copied to the input folder and the “run.sh” file be updated with the correct put file name, before running the shel script. 

## Details-of-the-code
The ask is to load the dataset and pivot it around the Drug_Name column and calculate the sum of Drug_Cost and number of individual prescribers. The code is segmented in different steps, each printing the function being executed, in order to determine which step was the bottleneck during processing the big data file. 

As mentioned above, I used Pandas package from Python to load and manipulate the data. After loading the data and during the code development, I delete the columns that are not used anymore. The is to open up the memory used by python that can help running the code even for big data on laptops and avoid requiring super computers. 

After loading the data, I generate a column consist of prescribers first name plus last name, in order to identify the individual UNIQUE prescribers. Then I delete the original two columns. 

AT this point we are ready to pivot the data. However, pivoting takes a lot of memory. Hence I chose to use grouping function from Pandas that simply uses pointers to each of drug names. Once the data frame is grouped by Drug_Name, I calculate the sum of cost and count of prescribers in separate data frames.

In the next step, I make a new data frame called “result” by merging the total cost and number of unique prescriber data frames. The index of these two data frames is the unique Drug_Names. The merge function also sort the result data frame by first descending Drug_Cost and then ascending Drug_Name columns. 

Lastly the code saves the data in the specified format in the output cvs file. In order to also save the Drug_Name with specified column header, I reset the index, set required columns names for cvs table and with it to output file without index column. 




