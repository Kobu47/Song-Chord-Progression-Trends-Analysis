## Song-Chord-Progression-Trends-Data-Analysis

## Project Overview

A lot of popular songs in this day and age sound the same. Why is that? A big part in this is the chord progression a song uses as a lot of songs tend to use the same ones. Here i take the most popular song progressions and perform data analysis based on different metrics like popularity and genre to see how do chord progressions lead to a song's success or the opposite.

## Data Sources

Hooktheory : Used an Api to extract the chord progressions: https://www.hooktheory.com/
Spotify : Used an Api to exctract data more specific data for the matching songs : https://open.spotify.com/

## Tools

 Vs Code - Python with libraries like Pandas for data Extraction and Manipulation
-Excel - Data Cleaning and Preparation
-Tableau - Data Visualisation

## Data Extraction 

Using Python and libraries such as Pandas , Requests , Openpyxl i extracted data from the websites api and saved them in an excel file for further use. Due to limitations of the Api i could only get organised data in an automated fashion in a limited number so i opted to gather the songs that were specifically included in the sites most popular chord progressions with a total of 1450 songs. You can find the code here [Click Here](https://github.com/Kobu47/Song-Chord-Progression-Trends-Analysis/blob/main/HooktheoryApi.py)

Spotify was a similar process the only difference being i needed to extract the specific data based on the 1450 songs i had. Here i extracted the Genre, Release date and popularity number of the songs which is a number spotify uses to rank songs by their popularity.You can find the code here

## Data Cleaning 

After extracting the data into an excel file i looked for duplicates and missing values. Here i filtered the genres by keeping only the most popular genre of every artist otherwise there would be too much clutter.Also i manipulated the dates to only contain the release year of the song.
