## Song-Chord-Progression-Trends-Data-Analysis

## Project Overview

A lot of popular songs in this day and age sound the same. Why is that? A big part in this is the chord progression a song uses as a lot of songs tend to use the same ones. Here i take the most popular song progressions and perform data analysis based on different metrics like popularity and genre to see how do chord progressions lead to a song's success or the opposite.

## Data Sources

Hooktheory : Used an Api to extract the chord progressions: [link](https://www.hooktheory.com/)
Spotify : Used an Api to exctract data more specific data for the matching songs : [link](https://open.spotify.com/)

## Tools

-Vs Code - Python with libraries like Pandas for data Extraction and Manipulation
-Excel - Data Cleaning and Preparation
-Tableau - Data Visualisation

## Data Extraction 

Using Python and libraries such as Pandas , Requests , Openpyxl i extracted data from the websites api and saved them in an excel file for further use. Due to limitations of the Api i could only get organised data in an automated fashion in a limited number so i opted to gather the songs that were specifically included in the sites most popular chord progressions with a total of 1450 songs. You can find the code [here](https://github.com/Kobu47/Song-Chord-Progression-Trends-Analysis/blob/main/HooktheoryApi.py)

Spotify was a similar process the only difference being i needed to extract the specific data based on the 1450 songs i had. Here i extracted the Genre, Release date and popularity number of the songs which is a number spotify uses to rank songs by their popularity.You can find the code [here](https://github.com/Kobu47/Song-Chord-Progression-Trends-Analysis/blob/main/Spotify%20Api.py)

## Data Cleaning 

After extracting the data into an excel file i looked for duplicates and missing values. Here i filtered the genres by keeping only the most popular genre of every artist otherwise there would be too much clutter.Also i manipulated the dates to only contain the release year of the song. You can find the Excel file [here](https://github.com/Kobu47/Song-Chord-Progression-Trends-Analysis/blob/main/Song_data.xlsx)

## Data Analysis and Visualisation

The visualisation was done with Tableau Public. The dashboard can be filtered by Genre, Year as well as a specific Chord Progression of your choice as well as presenting usage percentages for each Chord Progression. You can find the dashboard [here](https://public.tableau.com/app/profile/dimitris.kompouras/viz/ChordProgressionDataAnalysisDashboard/Dashboard1).


## Results

From the visualisation we can see chord progression ( C,G,am,F ) is the most used with a majority of the data. It wasn't the most successful Chord Progression though that being ( F,dm,C/G,G,C ) which is measured by the popularity number from spotify. So if an artist wants to follow the trends this dashboard will give him an idea of what chord progression route he should take to have a more safe and standard sound that is ont the same page as some of the most successful songs in the world.
