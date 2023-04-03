# C19 Dashboard
## Overview
This project is my submission for [CS50's final project](https://cs50.harvard.edu/x/2020/project/) after completing the ["Web Development Track"](https://cs50.harvard.edu/x/2020/tracks/web/).

![](/screenshots/LandingPageMapCountryInfo.png)

The website aims to represent important data and multiple different charts for the official reports of [Covid-19/Corona virus](https://en.wikipedia.org/wiki/Coronavirus_disease_2019). This was my first attempt at creating a data dashboard.

---

## Steps
For those who are familiar with Pandas, Numpy and other data science related topics in python, you can check the back-end code located in the **views.py** file in the **"landing"** folder. But for those who have not worked with or even heard about these, I will provide some links for the tutorials I myself watched to get started with them *(all of them will be linked at the end)*. For starters, I tried out different well-renowned websites and verified/approved databases which would offer me clean sheets of data without going through a lot of trouble getting them. The one I used is this:
[CSSEGISandData](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv)

After that, decided to go with Django over Flask, as I heard it was the better framework. As per usual, created the project and then ran the server (and migrated the files of course):

```
django-admin startproject [...]
python manage.py runserver
```

After setting up everything (including the `index.html` file and the needed URL paths located in the python files), wrote the actual first lines of code. For those interested, I would highly suggest running their tests or attempts in a [Jupyter Notebook](https://jupyter.org/), as it helps you to visualize the data and take some load off of your system.

Then, defined my first function for the index page. In which, I stored the data received from the sourced link and then used the plotting commands in the notebook to get a grasp on the table and understood how the rows & columns were filled.
Then stored the [sum](https://www.w3schools.com/python/ref_func_sum.asp) of each column in a variable to work with later. I believe the comments are pretty self-explanatory, hence I will not go over each and every single line of code in here, but will give a short description and  the general idea behind most of them.

Since I didn't need the extra content, I got rid of the [unwanted data](https://www.geeksforgeeks.org/python-pandas-dataframe-reset_index/), [sorted](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html) them and then created a [list](https://www.geeksforgeeks.org/python-pandas-series-tolist/) out of them.
Later, created a [dictionary](https://www.w3schools.com/python/python_dictionaries.asp) to store my data in a collection. In the end, [rendered](https://www.geeksforgeeks.org/render-a-html-template-as-response-django-views/) all of it by passing the 3 main arguments: request, html file and the dictionary.

With some data to work with, I went back to the `index.html` file and laid out some of the main structure of the website. After creating the [navigation bar](https://www.w3schools.com/Css/css_navbar.asp), started working on the chart which is shown on the right-hand side of the screen. For this particular bar-chart, I used some JavaScript code and the script tag provided by this website: [Chart.js](https://www.chartjs.org/)
I had to tweak some portion of the styling to make it look better and more suitable for the grid (*definitely recommend reading the documents provided by them*), and then, used my processed data to build the chart and make it fully functional. Fortunately enough, this [API](https://en.wikipedia.org/wiki/API) was easy to work with and didn't consume that much time to get it going. However, unlike the bar-chart, the world map view was a completely different story. First, I found this website which provided the initial structure for it: [Highcharts JS](https://www.highcharts.com)

But then, couldn't really tell why the map wasn't working as intended, and I'm not going to address the elephant in the room; but you can clearly tell which one I'm talking about, a certain country which is pretty well-known all around the world. After writing some extra back-end code for the map's data by using the [JSON](https://json.org) file provided by [JSdelvir](https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json), I somehow managed to get the map working, but it still has some room for improvements, might even work on it later.

Now for the python code, I first passed the data from the bar-chart plus the names of the countries. Then, based on the attributes of the **JSON** file, created a dictionary to store those elements, and finally, [appended](https://www.tutorialspoint.com/python/list_append.htm) the data to a list to later pass on.

Last but certainly not least, started working on the third plot. For those interested, I'd recommend trying out [SageMath](https://www.sagemath.org/). It surely helped me out for the plotting section of the last function. Even though not necessary, but might be helpful for some. For this part, I used the ["DataFrame"](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) data structure to initiate the analysis for each country and making their own respected graphs. After that,I  used [shift(x)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shift.html) for some index shifting and manipulation based on the [time series](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html) plus the [fillna(x)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.fillna.html) function.

At last, used a method called [Moving/Rolling Average](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) to create a series of averages of the full data set to plot them later on. In the end, created the 2 graphs by assigning their labels, data, styles, colors & etc.


![](/screenshots/AnalysisPageEachCountry.png)

---

## How To Run
If you want to test it out, first you have to clone the project via Github. Then, after getting into the directory of the project, open up the terminal and type in:

```bash
git clone "https://github.com/KouroshKSH/C19-Data-Dashboard.git"
python manage.py runserver
```

In case of encountering a problem, hard refresh the page (*Ctrl+Shift+R*) or disconnect the server (*simply type in Ctrl+C a bunch of times*) and rerun it. It isn't that often to see some random 400 error or something, but keep in mind, a few attempts might be needed to get this thing running; but after that, you're good to go. You can zoom into the map, hover over the countries to view their data, maybe even clicking the hamburger button and saving the map as a `.png` format.

You can even scroll down the right panel to view the charts, hover over them as well for extra content and click on the names of the countries to get directed to the detail chart for each and every single one of them (*since they're all buttons linked to their individual graphs and not a plain text*)
Lastly, you can view the numbers, the reports, the moving mean of the numbers over the last 7 days, hover over the nodes to gain more info, and maybe even conclude some stuff based on your own observations, why not?

Be sure to check the nav-bar as well. By the way, the view might not look as desired/intended at first, since I didn't spend much time making it responsive. I'd recommend changing some widths and heights if needed or even the margins and paddings.

---

## Resources
These are the main ones, but if anything new comes to my mind, I'll update it:
* [Data Analysis with Python by FreeCodeCamp on YT](https://youtu.be/r-uOLxNrNk8)
* [Time Series Talk: Moving Average Model by Ritvikmath on YT](https://youtu.be/voryLhxiPzE)
* [Learn Pandas by Analyzing Covid-19 by Giles McMullen on YT](https://youtu.be/MYU9W34dZh0) Probably the video which inspired me to tackle this project.
* [Andrew Ng's Machine Learning Course by Stanford on Coursera](https://www.coursera.org/learn/machine-learning) Don't miss out on this!
