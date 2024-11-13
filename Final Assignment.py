{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p style=\"text-align:center\">\n",
    "    <a href=\"https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0220ENSkillsNetwork900-2022-01-01\" target=\"_blank\">\n",
    "    <img src=\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png\" width=\"200\" alt=\"Skills Network Logo\">\n",
    "    </a>\n",
    "</p>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Extracting and Visualizing Stock Data</h1>\n",
    "<h2>Description</h2>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some stock data, you will then display this data in a graph.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>Table of Contents</h2>\n",
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <ul>\n",
    "        <li>Define a Function that Makes a Graph</li>\n",
    "        <li>Question 1: Use yfinance to Extract Stock Data</li>\n",
    "        <li>Question 2: Use Webscraping to Extract Tesla Revenue Data</li>\n",
    "        <li>Question 3: Use yfinance to Extract Stock Data</li>\n",
    "        <li>Question 4: Use Webscraping to Extract GME Revenue Data</li>\n",
    "        <li>Question 5: Plot Tesla Stock Graph</li>\n",
    "        <li>Question 6: Plot GameStop Stock Graph</li>\n",
    "    </ul>\n",
    "<p>\n",
    "    Estimated Time Needed: <strong>30 min</strong></p>\n",
    "</div>\n",
    "\n",
    "<hr>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "***Note***:- If you are working Locally using anaconda, please uncomment the following code and execute it.\n",
    "Use the version as per your python version.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: yfinance in /opt/conda/lib/python3.11/site-packages (0.2.49)\n",
      "Requirement already satisfied: pandas>=1.3.0 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.2.3)\n",
      "Requirement already satisfied: numpy>=1.16.5 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.1.3)\n",
      "Requirement already satisfied: requests>=2.31 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.31.0)\n",
      "Requirement already satisfied: multitasking>=0.0.7 in /opt/conda/lib/python3.11/site-packages (from yfinance) (0.0.11)\n",
      "Requirement already satisfied: lxml>=4.9.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (5.3.0)\n",
      "Requirement already satisfied: platformdirs>=2.0.0 in /opt/conda/lib/python3.11/site-packages (from yfinance) (4.2.1)\n",
      "Requirement already satisfied: pytz>=2022.5 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2024.1)\n",
      "Requirement already satisfied: frozendict>=2.3.4 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.4.6)\n",
      "Requirement already satisfied: peewee>=3.16.2 in /opt/conda/lib/python3.11/site-packages (from yfinance) (3.17.8)\n",
      "Requirement already satisfied: beautifulsoup4>=4.11.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (4.12.3)\n",
      "Requirement already satisfied: html5lib>=1.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (1.1)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.5)\n",
      "Requirement already satisfied: six>=1.9 in /opt/conda/lib/python3.11/site-packages (from html5lib>=1.1->yfinance) (1.16.0)\n",
      "Requirement already satisfied: webencodings in /opt/conda/lib/python3.11/site-packages (from html5lib>=1.1->yfinance) (0.5.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.0->yfinance) (2.9.0)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.0->yfinance) (2024.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (2.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (2024.6.2)\n",
      "Collecting bs4\n",
      "  Downloading bs4-0.0.2-py2.py3-none-any.whl.metadata (411 bytes)\n",
      "Requirement already satisfied: beautifulsoup4 in /opt/conda/lib/python3.11/site-packages (from bs4) (4.12.3)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4->bs4) (2.5)\n",
      "Downloading bs4-0.0.2-py2.py3-none-any.whl (1.2 kB)\n",
      "Installing collected packages: bs4\n",
      "Successfully installed bs4-0.0.2\n",
      "Requirement already satisfied: nbformat in /opt/conda/lib/python3.11/site-packages (5.10.4)\n",
      "Requirement already satisfied: fastjsonschema>=2.15 in /opt/conda/lib/python3.11/site-packages (from nbformat) (2.19.1)\n",
      "Requirement already satisfied: jsonschema>=2.6 in /opt/conda/lib/python3.11/site-packages (from nbformat) (4.22.0)\n",
      "Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /opt/conda/lib/python3.11/site-packages (from nbformat) (5.7.2)\n",
      "Requirement already satisfied: traitlets>=5.1 in /opt/conda/lib/python3.11/site-packages (from nbformat) (5.14.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (0.35.1)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (0.18.0)\n",
      "Requirement already satisfied: platformdirs>=2.5 in /opt/conda/lib/python3.11/site-packages (from jupyter-core!=5.0.*,>=4.12->nbformat) (4.2.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install yfinance\n",
    "!pip install bs4\n",
    "!pip install nbformat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import plotly.graph_objects as go\n",
    "from plotly.subplots import make_subplots"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In Python, you can ignore warnings using the warnings module. You can use the filterwarnings function to filter or ignore specific warning messages or categories.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "# Ignore all warnings\n",
    "warnings.filterwarnings(\"ignore\", category=FutureWarning)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Define Graphing Function\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this section, we define the function `make_graph`. **You don't have to know how the function works, you should only care about the inputs. It takes a dataframe with stock data (dataframe must contain Date and Close columns), a dataframe with revenue data (dataframe must contain Date and Revenue columns), and the name of the stock.**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def make_graph(stock_data, revenue_data, stock):\n",
    "    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=(\"Historical Share Price\", \"Historical Revenue\"), vertical_spacing = .3)\n",
    "    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']\n",
    "    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']\n",
    "    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype(\"float\"), name=\"Share Price\"), row=1, col=1)\n",
    "    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype(\"float\"), name=\"Revenue\"), row=2, col=1)\n",
    "    fig.update_xaxes(title_text=\"Date\", row=1, col=1)\n",
    "    fig.update_xaxes(title_text=\"Date\", row=2, col=1)\n",
    "    fig.update_yaxes(title_text=\"Price ($US)\", row=1, col=1)\n",
    "    fig.update_yaxes(title_text=\"Revenue ($US Millions)\", row=2, col=1)\n",
    "    fig.update_layout(showlegend=False,\n",
    "    height=900,\n",
    "    title=stock,\n",
    "    xaxis_rangeslider_visible=True)\n",
    "    fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the make_graph function that we’ve already defined. You’ll need to invoke it in questions 5 and 6 to display the graphs and create the dashboard. \n",
    "> **Note: You don’t need to redefine the function for plotting graphs anywhere else in this notebook; just use the existing function.**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 1: Use yfinance to Extract Stock Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is Tesla and its ticker symbol is `TSLA`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: yfinance in /opt/conda/lib/python3.11/site-packages (0.2.49)\n",
      "Requirement already satisfied: pandas>=1.3.0 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.2.3)\n",
      "Requirement already satisfied: numpy>=1.16.5 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.1.3)\n",
      "Requirement already satisfied: requests>=2.31 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.31.0)\n",
      "Requirement already satisfied: multitasking>=0.0.7 in /opt/conda/lib/python3.11/site-packages (from yfinance) (0.0.11)\n",
      "Requirement already satisfied: lxml>=4.9.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (5.3.0)\n",
      "Requirement already satisfied: platformdirs>=2.0.0 in /opt/conda/lib/python3.11/site-packages (from yfinance) (4.2.1)\n",
      "Requirement already satisfied: pytz>=2022.5 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2024.1)\n",
      "Requirement already satisfied: frozendict>=2.3.4 in /opt/conda/lib/python3.11/site-packages (from yfinance) (2.4.6)\n",
      "Requirement already satisfied: peewee>=3.16.2 in /opt/conda/lib/python3.11/site-packages (from yfinance) (3.17.8)\n",
      "Requirement already satisfied: beautifulsoup4>=4.11.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (4.12.3)\n",
      "Requirement already satisfied: html5lib>=1.1 in /opt/conda/lib/python3.11/site-packages (from yfinance) (1.1)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4>=4.11.1->yfinance) (2.5)\n",
      "Requirement already satisfied: six>=1.9 in /opt/conda/lib/python3.11/site-packages (from html5lib>=1.1->yfinance) (1.16.0)\n",
      "Requirement already satisfied: webencodings in /opt/conda/lib/python3.11/site-packages (from html5lib>=1.1->yfinance) (0.5.1)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.0->yfinance) (2.9.0)\n",
      "Requirement already satisfied: tzdata>=2022.7 in /opt/conda/lib/python3.11/site-packages (from pandas>=1.3.0->yfinance) (2024.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (2.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.11/site-packages (from requests>=2.31->yfinance) (2024.6.2)\n",
      "Requirement already satisfied: bs4 in /opt/conda/lib/python3.11/site-packages (0.0.2)\n",
      "Requirement already satisfied: beautifulsoup4 in /opt/conda/lib/python3.11/site-packages (from bs4) (4.12.3)\n",
      "Requirement already satisfied: soupsieve>1.2 in /opt/conda/lib/python3.11/site-packages (from beautifulsoup4->bs4) (2.5)\n",
      "Requirement already satisfied: nbformat in /opt/conda/lib/python3.11/site-packages (5.10.4)\n",
      "Requirement already satisfied: fastjsonschema>=2.15 in /opt/conda/lib/python3.11/site-packages (from nbformat) (2.19.1)\n",
      "Requirement already satisfied: jsonschema>=2.6 in /opt/conda/lib/python3.11/site-packages (from nbformat) (4.22.0)\n",
      "Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /opt/conda/lib/python3.11/site-packages (from nbformat) (5.7.2)\n",
      "Requirement already satisfied: traitlets>=5.1 in /opt/conda/lib/python3.11/site-packages (from nbformat) (5.14.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (0.35.1)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in /opt/conda/lib/python3.11/site-packages (from jsonschema>=2.6->nbformat) (0.18.0)\n",
      "Requirement already satisfied: platformdirs>=2.5 in /opt/conda/lib/python3.11/site-packages (from jupyter-core!=5.0.*,>=4.12->nbformat) (4.2.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install yfinance\n",
    "!pip install bs4\n",
    "!pip install nbformat\n",
    "\n",
    "import yfinance as yf\n",
    "import pandas as pd\n",
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import plotly.graph_objects as go\n",
    "from plotly.subplots import make_subplots"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the ticker object and the function `history` extract stock information and save it in a dataframe named `tesla_data`. Set the `period` parameter to ` \"max\" ` so we get information for the maximum amount of time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               Open      High       Low     Close     Volume  \\\n",
      "Date                                                                           \n",
      "2010-06-29 00:00:00-04:00  1.266667  1.666667  1.169333  1.592667  281494500   \n",
      "2010-06-30 00:00:00-04:00  1.719333  2.028000  1.553333  1.588667  257806500   \n",
      "2010-07-01 00:00:00-04:00  1.666667  1.728000  1.351333  1.464000  123282000   \n",
      "2010-07-02 00:00:00-04:00  1.533333  1.540000  1.247333  1.280000   77097000   \n",
      "2010-07-06 00:00:00-04:00  1.333333  1.333333  1.055333  1.074000  103003500   \n",
      "\n",
      "                           Dividends  Stock Splits  \n",
      "Date                                                \n",
      "2010-06-29 00:00:00-04:00        0.0           0.0  \n",
      "2010-06-30 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-01 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-02 00:00:00-04:00        0.0           0.0  \n",
      "2010-07-06 00:00:00-04:00        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a Ticker object for Tesla\n",
    "tesla_ticker = yf.Ticker(\"TSLA\")\n",
    "\n",
    "# Extract the stock history with the maximum time period\n",
    "tesla_data = tesla_ticker.history(period=\"max\")\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(tesla_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Reset the index** using the `reset_index(inplace=True)` function on the tesla_data DataFrame and display the first five rows of the `tesla_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 1 to the results below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                       Date      Open      High       Low     Close  \\\n",
      "0 2010-06-29 00:00:00-04:00  1.266667  1.666667  1.169333  1.592667   \n",
      "1 2010-06-30 00:00:00-04:00  1.719333  2.028000  1.553333  1.588667   \n",
      "2 2010-07-01 00:00:00-04:00  1.666667  1.728000  1.351333  1.464000   \n",
      "3 2010-07-02 00:00:00-04:00  1.533333  1.540000  1.247333  1.280000   \n",
      "4 2010-07-06 00:00:00-04:00  1.333333  1.333333  1.055333  1.074000   \n",
      "\n",
      "      Volume  Dividends  Stock Splits  \n",
      "0  281494500        0.0           0.0  \n",
      "1  257806500        0.0           0.0  \n",
      "2  123282000        0.0           0.0  \n",
      "3   77097000        0.0           0.0  \n",
      "4  103003500        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a Ticker object for Tesla\n",
    "tesla_ticker = yf.Ticker(\"TSLA\")\n",
    "\n",
    "# Extract the stock history with the maximum time period\n",
    "tesla_data = tesla_ticker.history(period=\"max\")\n",
    "\n",
    "# Reset the index\n",
    "tesla_data.reset_index(inplace=True)\n",
    "\n",
    "# Display the first five rows of the DataFrame\n",
    "print(tesla_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 2: Use Webscraping to Extract Tesla Revenue Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm Save the text of the response as a variable named `html_data`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "<!DOCTYPE html>\n",
      "<!--[if lt IE 7]>      <html class=\"no-js lt-ie9 lt-ie8 lt-ie7\"> <![endif]-->\n",
      "<!--[if IE 7]>         <html class=\"no-js lt-ie9 lt-ie8\"> <![endif]-->\n",
      "<!--[if IE 8]>         <html class=\"no-js lt-ie9\"> <![endif]-->\n",
      "<!--[if gt IE 8]><!--> <html class=\"no-js\"> <!--<![endif]-->\n",
      "    <head>\n",
      "        <meta charset=\"utf-8\">\n",
      "        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n",
      "\t\t<link rel=\"canonical\" href=\"https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue\" />\n",
      "\t\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# URL of the webpage\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Save the text content of the response\n",
    "html_data = response.text\n",
    "\n",
    "# Display the first 500 characters of html_data to verify the content\n",
    "print(html_data[:500])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<!--[if lt IE 7]>      <html class=\"no-js lt-ie9 lt-ie8 lt-ie7\"> <![endif]-->\n",
      "<!--[if IE 7]>         <html class=\"no-js lt-ie9 lt-ie8\"> <![endif]-->\n",
      "<!--[if IE 8]>         <html class=\"no-js lt-ie9\"> <![endif]-->\n",
      "<!--[if gt IE 8]><!-->\n",
      "<html class=\"no-js\">\n",
      " <!--<![endif]-->\n",
      " <head>\n",
      "  <meta charset=\"utf-8\"/>\n",
      "  <meta content=\"IE=edge,chrome=1\" http-equiv=\"X-UA-Compatible\"/>\n",
      "  <link href=\"https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue\" rel=\"canonical\"/>\n",
      "  <title>\n",
      "   Te\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# Parse the HTML data with BeautifulSoup using html.parser or html5lib\n",
    "soup = BeautifulSoup(html_data, 'html.parser')  # You can also use 'html5lib' here\n",
    "\n",
    "# Display the parsed HTML structure (first 500 characters)\n",
    "print(soup.prettify()[:500])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `BeautifulSoup` or the `read_html` function extract the table with `Tesla Revenue` and store it into a dataframe named `tesla_revenue`. The dataframe should have columns `Date` and `Revenue`.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Step-by-step instructions</summary>\n",
    "\n",
    "```\n",
    "\n",
    "Here are the step-by-step instructions:\n",
    "\n",
    "1. Create an Empty DataFrame\n",
    "2. Find the Relevant Table\n",
    "3. Check for the Tesla Quarterly Revenue Table\n",
    "4. Iterate Through Rows in the Table Body\n",
    "5. Extract Data from Columns\n",
    "6. Append Data to the DataFrame\n",
    "\n",
    "```\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Click here if you need help locating the table</summary>\n",
    "\n",
    "```\n",
    "    \n",
    "Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab\n",
    "    \n",
    "soup.find_all(\"tbody\")[1]\n",
    "    \n",
    "If you want to use the read_html function the table is located at index 1\n",
    "\n",
    "We are focusing on quarterly revenue in the lab.\n",
    "```\n",
    "\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Date  Revenue\n",
      "0  2021  $53,823\n",
      "1  2020  $31,536\n",
      "2  2019  $24,578\n",
      "3  2018  $21,461\n",
      "4  2017  $11,759\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# Parse the HTML data with BeautifulSoup\n",
    "soup = BeautifulSoup(html_data, 'html.parser')\n",
    "\n",
    "# Find the table (assuming it is the first table, adjust if necessary)\n",
    "table = soup.find('table')\n",
    "\n",
    "# Initialize an empty list to store rows of the table\n",
    "data = []\n",
    "\n",
    "# Loop through each row in the table\n",
    "for row in table.find_all('tr')[1:]:  # Skip the header row\n",
    "    cols = row.find_all('td')\n",
    "    date = cols[0].text.strip()  # Extract date\n",
    "    revenue = cols[1].text.strip()  # Extract revenue\n",
    "    data.append([date, revenue])\n",
    "\n",
    "# Create a DataFrame\n",
    "tesla_revenue = pd.DataFrame(data, columns=[\"Date\", \"Revenue\"])\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(tesla_revenue.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execute the following line to remove the comma and dollar sign from the `Revenue` column. \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_revenue[\"Revenue\"] = tesla_revenue['Revenue'].str.replace(',|\\$',\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execute the following lines to remove an null or empty strings in the Revenue column.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla_revenue.dropna(inplace=True)\n",
    "\n",
    "tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != \"\"]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the last 5 row of the `tesla_revenue` dataframe using the `tail` function. Take a screenshot of the results.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Date Revenue\n",
      "8   2013  $2,013\n",
      "9   2012    $413\n",
      "10  2011    $204\n",
      "11  2010    $117\n",
      "12  2009    $112\n"
     ]
    }
   ],
   "source": [
    "print(tesla_revenue.tail())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 3: Use yfinance to Extract Stock Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the `Ticker` function enter the ticker symbol of the stock we want to extract data on to create a ticker object. The stock is GameStop and its ticker symbol is `GME`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'address1': '625 Westport Parkway', 'city': 'Grapevine', 'state': 'TX', 'zip': '76051', 'country': 'United States', 'phone': '817 424 2000', 'website': 'https://www.gamestop.com', 'industry': 'Specialty Retail', 'industryKey': 'specialty-retail', 'industryDisp': 'Specialty Retail', 'sector': 'Consumer Cyclical', 'sectorKey': 'consumer-cyclical', 'sectorDisp': 'Consumer Cyclical', 'longBusinessSummary': 'GameStop Corp., a specialty retailer, provides games and entertainment products through its stores and ecommerce platforms in the United States, Canada, Australia, and Europe. The company sells new and pre-owned gaming platforms; accessories, such as controllers, gaming headsets, and virtual reality products; new and pre-owned gaming software; and in-game digital currency, digital downloadable content, and full-game downloads. It sells collectibles comprising apparel, toys, trading cards, gadgets, and other retail products for pop culture and technology enthusiasts, as well as engages in the digital asset wallet and NFT marketplace activities. The company operates stores and ecommerce sites under the GameStop, EB Games, and Micromania brands; and pop culture themed stores that sell collectibles, apparel, gadgets, electronics, toys, and other retail products under the Zing Pop Culture brand, as well as offers Game Informer magazine, a print and digital gaming publication. The company was formerly known as GSC Holdings Corp. GameStop Corp. was founded in 1996 and is headquartered in Grapevine, Texas.', 'fullTimeEmployees': 8000, 'companyOfficers': [{'maxAge': 1, 'name': 'Mr. Ryan  Cohen', 'age': 37, 'title': 'President, CEO & Executive Chairman', 'yearBorn': 1986, 'fiscalYear': 2023, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Daniel William Moore', 'age': 40, 'title': 'Principal Accounting Officer & Principal Financial Officer', 'yearBorn': 1983, 'fiscalYear': 2023, 'totalPay': 277711, 'exercisedValue': 0, 'unexercisedValue': 0}, {'maxAge': 1, 'name': 'Mr. Mark Haymond Robinson', 'age': 45, 'title': 'General Counsel & Secretary', 'yearBorn': 1978, 'fiscalYear': 2023, 'totalPay': 337657, 'exercisedValue': 0, 'unexercisedValue': 0}], 'auditRisk': 8, 'boardRisk': 6, 'compensationRisk': 7, 'shareHolderRightsRisk': 3, 'overallRisk': 5, 'governanceEpochDate': 1730419200, 'compensationAsOfEpochDate': 1703980800, 'irWebsite': 'http://phx.corporate-ir.net/phoenix.zhtml?c=130125&p=irol-irhome', 'maxAge': 86400, 'priceHint': 2, 'previousClose': 26.84, 'open': 26.26, 'dayLow': 26.2575, 'dayHigh': 28.22, 'regularMarketPreviousClose': 26.84, 'regularMarketOpen': 26.26, 'regularMarketDayLow': 26.2575, 'regularMarketDayHigh': 28.22, 'exDividendDate': 1552521600, 'fiveYearAvgDividendYield': 9.52, 'beta': -0.098, 'trailingPE': 195.06572, 'forwardPE': -2730.9202, 'volume': 9569631, 'regularMarketVolume': 9569631, 'averageVolume': 8848971, 'averageVolume10days': 10638870, 'averageDailyVolume10Day': 10638870, 'bid': 27.75, 'ask': 27.79, 'bidSize': 1300, 'askSize': 1200, 'marketCap': 12193831936, 'fiftyTwoWeekLow': 9.95, 'fiftyTwoWeekHigh': 64.83, 'priceToSalesTrailing12Months': 2.6787856, 'fiftyDayAverage': 21.964, 'twoHundredDayAverage': 19.97215, 'currency': 'USD', 'enterpriseValue': 7776817664, 'profitMargins': 0.00934, 'floatShares': 390217891, 'sharesOutstanding': 446510016, 'sharesShort': 35943712, 'sharesShortPriorMonth': 38133807, 'sharesShortPreviousMonthDate': 1727654400, 'dateShortInterest': 1730332800, 'sharesPercentSharesOut': 0.0805, 'heldPercentInsiders': 0.08495, 'heldPercentInstitutions': 0.23472999, 'shortRatio': 6.14, 'shortPercentOfFloat': 0.096499994, 'impliedSharesOutstanding': 446510016, 'bookValue': 10.278, 'priceToBook': 2.657054, 'lastFiscalYearEnd': 1706918400, 'nextFiscalYearEnd': 1738540800, 'mostRecentQuarter': 1722643200, 'netIncomeToCommon': 42500000, 'trailingEps': 0.14, 'forwardEps': -0.01, 'pegRatio': 16.23, 'lastSplitFactor': '4:1', 'lastSplitDate': 1658448000, 'enterpriseToRevenue': 1.708, 'enterpriseToEbitda': 164.763, '52WeekChange': 1.0226073, 'SandP52WeekChange': 0.328925, 'lastDividendValue': 0.095, 'lastDividendDate': 1552521600, 'exchange': 'NYQ', 'quoteType': 'EQUITY', 'symbol': 'GME', 'underlyingSymbol': 'GME', 'shortName': 'GameStop Corporation', 'longName': 'GameStop Corp.', 'firstTradeDateEpochUtc': 1013610600, 'timeZoneFullName': 'America/New_York', 'timeZoneShortName': 'EST', 'uuid': '8ded85bd-8171-3e2e-afa6-c81272285147', 'messageBoardId': 'finmb_1342560', 'gmtOffSetMilliseconds': -18000000, 'currentPrice': 27.3092, 'targetHighPrice': 10.0, 'targetLowPrice': 5.75, 'targetMeanPrice': 7.88, 'targetMedianPrice': 7.88, 'recommendationMean': 4.5, 'recommendationKey': 'underperform', 'numberOfAnalystOpinions': 2, 'totalCash': 4204199936, 'totalCashPerShare': 9.857, 'ebitda': 47200000, 'totalDebt': 533500000, 'quickRatio': 5.442, 'currentRatio': 6.233, 'totalRevenue': 4552000000, 'debtToEquity': 12.171, 'revenuePerShare': 13.97, 'returnOnAssets': 0.00043000001, 'returnOnEquity': 0.015039999, 'freeCashflow': -93387504, 'operatingCashflow': -33100000, 'revenueGrowth': -0.314, 'grossMargins': 0.26237, 'ebitdaMargins': 0.010369999, 'operatingMargins': -0.03558, 'financialCurrency': 'USD', 'trailingPegRatio': None}\n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a Ticker object for GameStop (GME)\n",
    "gme_ticker = yf.Ticker(\"GME\")\n",
    "\n",
    "# Display information about the GameStop ticker object (optional)\n",
    "print(gme_ticker.info)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using the ticker object and the function `history` extract stock information and save it in a dataframe named `gme_data`. Set the `period` parameter to ` \"max\" ` so we get information for the maximum amount of time.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                               Open      High       Low     Close    Volume  \\\n",
      "Date                                                                          \n",
      "2002-02-13 00:00:00-05:00  1.620129  1.693350  1.603296  1.691667  76216000   \n",
      "2002-02-14 00:00:00-05:00  1.712708  1.716074  1.670626  1.683251  11021600   \n",
      "2002-02-15 00:00:00-05:00  1.683250  1.687458  1.658002  1.674834   8389600   \n",
      "2002-02-19 00:00:00-05:00  1.666418  1.666418  1.578047  1.607504   7410400   \n",
      "2002-02-20 00:00:00-05:00  1.615920  1.662209  1.603295  1.662209   6892800   \n",
      "\n",
      "                           Dividends  Stock Splits  \n",
      "Date                                                \n",
      "2002-02-13 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-14 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-15 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-19 00:00:00-05:00        0.0           0.0  \n",
      "2002-02-20 00:00:00-05:00        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a Ticker object for GameStop (GME)\n",
    "gme_ticker = yf.Ticker(\"GME\")\n",
    "\n",
    "# Extract the stock history with the maximum time period\n",
    "gme_data = gme_ticker.history(period=\"max\")\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(gme_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Reset the index** using the `reset_index(inplace=True)` function on the gme_data DataFrame and display the first five rows of the `gme_data` dataframe using the `head` function. Take a screenshot of the results and code from the beginning of Question 3 to the results below.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                       Date      Open      High       Low     Close    Volume  \\\n",
      "0 2002-02-13 00:00:00-05:00  1.620129  1.693350  1.603296  1.691667  76216000   \n",
      "1 2002-02-14 00:00:00-05:00  1.712707  1.716073  1.670626  1.683250  11021600   \n",
      "2 2002-02-15 00:00:00-05:00  1.683250  1.687458  1.658001  1.674834   8389600   \n",
      "3 2002-02-19 00:00:00-05:00  1.666418  1.666418  1.578047  1.607504   7410400   \n",
      "4 2002-02-20 00:00:00-05:00  1.615921  1.662210  1.603296  1.662210   6892800   \n",
      "\n",
      "   Dividends  Stock Splits  \n",
      "0        0.0           0.0  \n",
      "1        0.0           0.0  \n",
      "2        0.0           0.0  \n",
      "3        0.0           0.0  \n",
      "4        0.0           0.0  \n"
     ]
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "\n",
    "# Create a Ticker object for GameStop (GME)\n",
    "gme_ticker = yf.Ticker(\"GME\")\n",
    "\n",
    "# Extract the stock history with the maximum time period\n",
    "gme_data = gme_ticker.history(period=\"max\")\n",
    "\n",
    "# Reset the index\n",
    "gme_data.reset_index(inplace=True)\n",
    "\n",
    "# Display the first five rows of the DataFrame\n",
    "print(gme_data.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 4: Use Webscraping to Extract GME Revenue Data\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `requests` library to download the webpage https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html. Save the text of the response as a variable named `html_data_2`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<!-- saved from url=(0105)https://web.archive.org/web/20200814131437/https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue -->\n",
      "<html class=\" js flexbox canvas canvastext webgl no-touch geolocation postmessage websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface g\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "# URL of the webpage\n",
    "url = \"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html\"\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Save the text content of the response\n",
    "html_data_2 = response.text\n",
    "\n",
    "# Display the first 500 characters of html_data_2 to verify the content\n",
    "print(html_data_2[:500])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parse the html data using `beautiful_soup` using parser i.e `html5lib` or `html.parser`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<!-- saved from url=(0105)https://web.archive.org/web/20200814131437/https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue -->\n",
      "<html class=\"js flexbox canvas canvastext webgl no-touch geolocation postmessage websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface ge\n"
     ]
    }
   ],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# Parse the HTML data with BeautifulSoup using html.parser or html5lib\n",
    "soup = BeautifulSoup(html_data_2, 'html.parser')  # You can also use 'html5lib'\n",
    "\n",
    "# Display the parsed HTML structure (first 500 characters)\n",
    "print(soup.prettify()[:500])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Using `BeautifulSoup` or the `read_html` function extract the table with `GameStop Revenue` and store it into a dataframe named `gme_revenue`. The dataframe should have columns `Date` and `Revenue`. Make sure the comma and dollar sign is removed from the `Revenue` column.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Note: Use the method similar to what you did in question 2.**  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Click here if you need help locating the table</summary>\n",
    "\n",
    "```\n",
    "    \n",
    "Below is the code to isolate the table, you will now need to loop through the rows and columns like in the previous lab\n",
    "    \n",
    "soup.find_all(\"tbody\")[1]\n",
    "    \n",
    "If you want to use the read_html function the table is located at index 1\n",
    "\n",
    "\n",
    "```\n",
    "\n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Date Revenue\n",
      "0  2020    6466\n",
      "1  2019    8285\n",
      "2  2018    8547\n",
      "3  2017    7965\n",
      "4  2016    9364\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# Parse the HTML data with BeautifulSoup\n",
    "soup = BeautifulSoup(html_data_2, 'html.parser')\n",
    "\n",
    "# Find the table (assuming it is the first table, adjust if necessary)\n",
    "table = soup.find('table')\n",
    "\n",
    "# Initialize an empty list to store rows of the table\n",
    "data = []\n",
    "\n",
    "# Loop through each row in the table\n",
    "for row in table.find_all('tr')[1:]:  # Skip the header row\n",
    "    cols = row.find_all('td')\n",
    "    date = cols[0].text.strip()  # Extract date\n",
    "    revenue = cols[1].text.strip()  # Extract revenue\n",
    "    \n",
    "    # Remove commas and dollar signs from the revenue value\n",
    "    revenue = revenue.replace(',', '').replace('$', '')\n",
    "    \n",
    "    data.append([date, revenue])\n",
    "\n",
    "# Create a DataFrame\n",
    "gme_revenue = pd.DataFrame(data, columns=[\"Date\", \"Revenue\"])\n",
    "\n",
    "# Display the first few rows of the DataFrame\n",
    "print(gme_revenue.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Display the last five rows of the `gme_revenue` dataframe using the `tail` function. Take a screenshot of the results.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Date Revenue\n",
      "11  2009    8806\n",
      "12  2008    7094\n",
      "13  2007    5319\n",
      "14  2006    3092\n",
      "15  2005    1843\n"
     ]
    }
   ],
   "source": [
    "print(gme_revenue.tail())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 5: Plot Tesla Stock Graph\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `make_graph` function to graph the Tesla Stock Data, also provide a title for the graph. Note the graph will only show data upto June 2021.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Hint</summary>\n",
    "\n",
    "```\n",
    "\n",
    "You just need to invoke the make_graph function with the required parameter to print the graphs.The structure to call the `make_graph` function is `make_graph(tesla_data, tesla_revenue, 'Tesla')`.\n",
    "\n",
    "```\n",
    "    \n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA90AAAJOCAYAAACqS2TfAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjkuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8hTgPZAAAACXBIWXMAAA9hAAAPYQGoP6dpAAC42klEQVR4nOzdd3xT5eLH8W/apnvRQlvKBtmyQabIBkUUwT0ARbk/Ra8KLq4D0at4HXjVi+OqF3EgioqKolBUQAVkKEMZsncBGS2lK03O74+SNGmTNi3pSPt5v168TM55zsmT5IGX3zzLZBiGIQAAAAAA4HMBlV0BAAAAAACqK0I3AAAAAADlhNANAAAAAEA5IXQDAAAAAFBOCN0AAAAAAJQTQjcAAAAAAOWE0A0AAAAAQDkhdAMAAAAAUE4I3QAAAAAAlBNCNwBIMplMpf7Tr1+/cq3TuHHjZDKZ9M4775Tr69ilpaXpn//8p7p3766YmBiZzWYlJiaqXbt2uummm/TGG2/ozJkzFVKXsrB/L77SuHHjIt95SEiIGjZsqGuuuUY//vhjme5b0d9rWV1xxRUKCwvTgQMHXI7bP4ulS5cWe32/fv1kMpn0+OOPl18lK1l1fo9Hjx7Vu+++q+uvv17NmzdXaGiowsPD1apVK/3973/Xnj17ir0+NzdX//rXv9ShQwdFRESoVq1a6tevnz755BO35S0Wi7777jvdf//96tatm2JjY2U2m5WUlKTLLrtMX3/9tcfX2r9/v9544w1NmDBBXbp0UUhIiEwmk2699dZi6zho0CBFR0crNTW1xM8DAM5FUGVXAACqgrFjxxY5lpqaqkWLFnk836pVq3KvV0XZtm2bBg0apAMHDigkJETdu3dXcnKysrOztWXLFr3//vt6//331bt3b51//vmO6x5//HFNmzZNU6dOrZbBQ5J69+6t8847T5J06tQprV27Vh9//LHmzZun559/XpMmTarkGvrekiVL9Pnnn+u+++5T/fr1K7s6JVq6dKn69++viy66qMQfA+CdSZMm6YMPPlBAQIDOP/98XXbZZTpz5ozWrFmjV155Rf/73/80f/58DR48uMi1mZmZGjx4sFasWKHY2FgNGzZMGRkZ+v7777Vs2TJNnjxZzz//vMs1y5Ytc9wrKSlJffr0UUREhDZv3qwFCxZowYIFmjBhgl5//fUiP659+umnuvfee0v9Hp955hl169ZNU6ZM0axZs0p9PQB4i9ANAJLbXselS5c6QndV75U8VzfeeKMOHDig/v3766OPPlKdOnVczu/bt0+zZ89WZGRkJdWw8tx6660aN26c43l2drb+9re/6d1339UDDzygSy+9VC1atPD6ftOnT9dDDz2kunXrlkNtfePee+9VaGioHnroocquCipJXFycpk2bpvHjx6tevXqO4xkZGbrttts0d+5cXXvttdqxY4dq1arlcu0//vEPrVixQu3atdP333+v2rVrS5LWrVunfv366YUXXlC/fv106aWXOq4JCAjQ6NGjdffdd+vCCy90ud9HH32kG264Qf/973/Vu3dvjRkzxuV8kyZNdNddd6lz587q3LmzPv74Yz311FMlvseuXbvq0ksv1ezZs3XPPfeoQ4cOpf6cAMAbDC8HgBpu586dWrt2rSTp9ddfLxK4Jalhw4Z69NFH1bhx4wquXdUTGhqqmTNnKiIiQlarVZ999lmprq9bt65atWqlmJiYcqrhuUlJSdHvv/+ukSNHKj4+vrKrg0ry8ssv67HHHnMJ3JIUGRmpt99+W1FRUTpx4kSRYd8nT57Ua6+9Jkl67bXXHIFbkrp06aIHH3xQkoqE4gEDBuiTTz4pErgl6ZprrnH88PXuu+8WOX/55Zfr5Zdf1rhx49S+fXsFBXnfpzR+/HgZhqGXXnrJ62sAoLQI3QBQRllZWXrhhRfUo0cPxcbGKjQ0VC1bttQDDzyg48ePu71m3rx5GjRokOLj42U2mxUfH682bdrotttu08aNG7163dOnT+vNN9/UqFGj1Lx5c0VERCgiIkLt2rXTww8/rFOnTpXqfRw5csTxOCEhwevrTCaTpk2bJkmaNm2ay9xn555hSTpx4oT+8Y9/qG3btgoPD1dUVJS6dOmiZ599VllZWR5f4+DBg7r//vvVrl07RUVFKSIiQi1atNC4ceO0YsUKr+pptVp1++23y2QyqV27dtq/f7/X79GTyMhItWzZUpJc5rY6zyufNWuWevbsqZiYGJlMJke5kuZ0r1u3TmPHjlWTJk0UGhqquLg4dejQQffff7/27t1bpPyhQ4c0adIktW7d2vHZduvWTf/5z3+Ul5dX6vf2n//8x1HP8uD8/jds2KBRo0apTp06CgsLU/v27fXSSy/JarV6fb9+/fqpf//+kvKHKDu3w8I/EuXl5en1119Xr169FBMTo9DQUDVv3lx///vfdfDgQZ+9x8cff7zYud5Lly51uy6E83GLxaJ//etfatu2rcLCwhQfH69Ro0Zpy5YtHl/35MmTmjp1qjp27KioqCiFh4erXbt2+uc//6nMzEyfvb/w8HBH+y/892nhwoXKzc1Vw4YN1bt37yLXXn/99ZKkVatW6dChQ16/ZqdOndy+3rkaPny4ateurQ8//FAnTpzw6b0BwI7h5QBQBocOHdKwYcO0adMmxcXFqVu3boqKitKvv/6q5557TvPmzdPSpUvVqFEjxzVPPPGEpk6dqqCgIPXq1Uv16tVTWlqa9u3bp7fffltt27ZV+/btS3ztDRs2aMKECapTp45atmypLl266OTJk1q3bp2efvppffzxx1q1apXXvZQNGzZ0PH7ppZc0depUr64bO3as1q9frw0bNqhDhw7q2LGj41yfPn0cj3ft2qUBAwZo7969qlOnji655BJZLBb98MMPevDBB/XRRx9pyZIlRYaofvfdd7ryyit16tQpJSQkaODAgQoODtaePXs0Z84cSVKvXr2KrWNGRoauvvpqffPNNxo8eLA++eQTRUdHe/X+SpKeni5JCgkJKXLurrvu0quvvqpevXpp+PDh2rVrl1eLvD333HN66KGHZLPZ1KJFC11++eXKysrSjh079Pzzz6tt27YuYXj58uUaOXKkTp48qcaNG2vw4MHKycnR6tWrddddd2nBggX66quvZDabvXpP2dnZWrRokcxms/r27evdB1FGq1ev1u23366kpCQNHDhQJ0+e1NKlS3XPPffop59+0scff+zVZzZs2DCFhoZq0aJFSkxM1LBhwxznnHtZc3JydOmll2rJkiUKDQ1V//79FR0drRUrVuiVV17Rhx9+qEWLFqlz587l8n5Lw2Kx6JJLLtGKFSvUt29ftW7dWqtXr9b8+fP1ww8/6Lfffivyg8LmzZs1bNgw7d+/X3Xr1lWfPn1kNpu1evVqPfroo/r000+1dOlSn4ywsFgsjh+RCk+T+O233yTlD912p2nTpoqLi9OJEye0fv16JScne/Wa27dvd/t658psNjsWeFu0aJGuu+46n94fACRJBgDArR9++MGQZBT+p9Jmsxm9e/c2JBnjx4830tPTHecsFosxefJkQ5LRv39/x/Hs7GwjLCzMiIyMNLZu3Vrktfbs2WNs2bLF5djYsWMNScasWbNcju/fv99YsmSJYbVaXY6fOXPGGDNmjCHJuOOOO0r1Xi+//HLHe23Tpo1x3333GR999JGxY8eOYq+bOnWqIcmYOnWqxzLdu3c3JBmXXXaZkZGR4Th+9OhRo3PnzoYk4/rrr3e5Zt++fUZMTIwhyXjooYeMnJwcl/NHjhwxfvzxR5djhb+rAwcOGB07djQkGTfffLORm5tb0sfgolGjRm4/f8MwjA0bNhgBAQGGJON///tfkTpER0cbK1eudHtfT9/rF198YUgyQkNDjY8++qjIdX/88YexefNmx/PDhw8b8fHxhslkMl599VWX9vDXX38ZAwYMMCQZ06ZN8/o9L1myxJBkdOvWzWMZ+3v84Ycfir3XRRdd5LZt2N+/vZ1aLBbHud9//92oU6eOIcl4/fXXva63/e/qRRdd5LHMgw8+aEgymjVrZuzevdtxPDc31xg/frwhyWjSpEmRtlYcT++xpL8Xnurr/G9Op06djMOHDzvOZWVlGUOHDjUkGRMmTHC5LjMz02jWrJkhyXjkkUdc3sOZM2eM6667zvH3wBdee+01Q5IRFhZmpKamupwbNWqUIcm45557PF7fvn17Q5Lxn//8x6vXO3z4sOPfg5dffrnE8vbPf/z48V7df8aMGaUqDwClRegGAA88he5vvvnGkGR07NjRJTDYWa1W4/zzzzckGZs2bTIMIz9gSjLat2/v9et7CmfFOXPmjBEUFGTUqVPH62sMwzDS09ONG2+80TCZTI73bP9Tv359Y8qUKcaJEyeKXFdSuPjxxx8NSUZ4eHiR/zk3DMNYu3atIckICAgw9u/f7zh+zz33GJKMESNGeP0enL+rDRs2GPXr1zckGU888YTX93DmLnSfOnXK+Prrrx0BJzk52eWHBHsdintNT9+r/QeCF154wav62UPknXfe6fb8gQMHDLPZbNSpU8ew2Wxe3fO5554zJBljxozxWMZXobtu3bpGVlZWketeeeUVQ5LRvHlzr+psGCWH7qysLCMyMtKQZHz55ZdFzp85c8ZITEw0JBkffPCB169bXqHbZDIZ69evL3LdqlWrDElG06ZNXY7bQ/Cll17q9vVOnz5tJCQkGEFBQW7/HpfGxo0bHZ/l008/XeT84MGDDUnGww8/7PEevXr18nh9YRaLxRg4cKAhyWjXrp1XP4qUNnQvWrTI8UMHAJQH5nQDQCnZFw4aPXq02wV7AgICHENz7fOO69Spo8aNG2vjxo2aPHmyNm/efM71WLFihf71r39p4sSJuvnmmzVu3DjdcccdCg4O1rFjx3Ty5Emv7xUVFaX33ntPO3fu1IwZM3TllVeqadOmkqQDBw5o+vTp6tixY4l78xZm375p2LBhSkxMLHK+S5cu6tChg2w2m5YtW+Y4/u2330qSJkyYUKrXk6RFixapT58+Onr0qN577z09+uijpb6Hs5tvvtkxRzg2NlbDhw/Xzp071axZMy1cuFARERFFrrnyyitL9Rqpqalav369AgICNH78eK+usbfDa665xu35evXqqXnz5jp27JhjaG5J7PP7K2IBtauvvlqhoaFFjtu359u+fXup5vwWZ+3atcrIyFBcXJxGjBhR5Hx4eLiuvfZaSdIPP/zgk9c8Fw0bNnS7knbr1q0lqcj885LaQmRkpLp27aq8vDytWbOmzPU6cOCARowYoYyMDF122WUVsrr9//3f/+m7775TfHy8PvnkEwUHB/v8Nezt3Xl9CwDwJeZ0A0Ap7dq1S5L06KOPlhjojh075nj87rvv6sorr9SMGTM0Y8YMxcXFqXv37ho8eLBuuukml/mnxTl69KhGjx6tn376qdhy6enpReZJl6RJkya69957HXve7t27V2+//baeffZZ7du3TxMnTiyyWnFx7OGgSZMmHss0a9ZMGzZscAkS9gXDyrIX+qWXXqq8vDy9//77uuGGG0p9fWHO+3QHBwcrISFBPXr00LBhwzyuklzaVd737dsnKX++qrdzbu3t0N1qz4UdO3bMq23N0tLSJMmree+GYXh13tO8bE9tIioqSvHx8Tp+/LgOHDjg9Zzf4njbDp3LVibndRac2b+XnJwcl+P2tnDTTTfppptuKvbezv8mlUZqaqoGDhyovXv3aujQoR7n3EdFRUmSzpw54/FeGRkZkkpuZ3fffbfefvtt1apVSykpKaXamq807PUozQ+VAFAahG4AKCWbzSYpf7Ew+/+oe9K2bVvH4wsvvFB79uzR119/rWXLlmnFihVatGiRvvnmG02dOlXz58/XwIEDS3z9W2+9VT/99JN69uypadOmqUOHDqpVq5Zjsazk5GQdPny4xFDkjUaNGumJJ55QrVq1NGnSJC1evFhZWVkKCws753uXl7Fjx+rtt9/Wo48+ql69ehUbtLxReJ9ub1TE52Nvh1deeaXb3nZn3vZcx8bGSipYJM6diIgInTlzpthQJRUEq3PZ290Xbbgqsn93ngQElG4gov1+nkaUOHNe3NFbR48e1YABA/Tnn39q0KBB+vzzz90uICgV/OBk/yHJnQMHDriUdWfy5Ml6+eWXFRsbq8WLFztWLy8P9h+bSvsjJQB4i9ANAKXUoEEDSfl7w953332lujYsLExXXnmlY/jxsWPH9Mgjj+i///2vbrnlFrdbQjk7c+aMFi5cqICAAC1cuNARkpzPp6amlqpO3hgyZIik/C2XTp065XWotO/xa++Jc8d+znk/4IYNG2rbtm3aunWro5fZW2+++aYiIyP10ksv6cILL9SSJUvK1GNekew9m4cPH1ZaWppXvd0NGjTQ9u3b9eCDD3pcKbq07FvGedryzl7XLVu2aMeOHR7LGIahnTt3Osq7s3v3brfHT58+7Xj9+vXre1XvktjblqfXlNy3w7KyD4E+ffq02/Ml/T0vrQYNGmjr1q0aP358qac2lOTYsWMaMGCAtmzZooEDB+rLL790Oy3Azr76+9q1a92e37Vrl2NrLk9B+oEHHtCMGTMUExOjxYsX+6x9e2JvbyX9YAEAZcWcbgAopYsvvlhS/p7b59oTV6dOHT377LOS8nuGShremJaWJqvVqujo6CKBW5Lef//9UtfJm/L2XquQkBCXYfD2cOFpP2j7PsTffvut2/mSv/32m2Mus/MWVfZtn958803v3oQTk8mkf//733rkkUd08OBB9e3bV+vXry/1fSpSUlKSY277//73P6+usbfDjz/+2Gf1sAem4tYcGDBggCTp008/9VgmJSVFaWlpCgoK8jj8fd68eUWGSUvSe++9J0k677zzvA7AJbXDrl27KjIyUidOnNCXX35Z5HxWVpbmzp0rSY49v8+Fvd6e9tQuzRQNb5RHW5Ckv/76SwMGDNAff/yhgQMHasGCBSX+4HbJJZcoODhY+/bt088//1zkvH27vx49eridOvDQQw/pueeeU0xMjFJSUtStWzffvJli/P7775Ly15gAgHJReWu4AUDV5mn1cqvVanTr1s2QZIwdO9Y4evRokWtPnDhhvPbaa47Vzffs2WO8+eabRlpaWpGy7733niHJqFWrlpGXl+c47m6V67y8PKNWrVqGJOPdd991uc/KlSsd5yS5bItUnPXr1xv9+vUzPvvsM7crA69fv95o3ry52629Zs+ebUgyRo4c6fH+9i3DLr/8cuPMmTOO48eOHXN8joXvu3fvXiMqKsqxCnLh7b682TLMMAzj2WefNSQZsbGxxooVK4r/IAopbsswT9zVoTBPq5d/9tlnjm2YPvnkkyLXFd4ybP/+/UZsbKwRGBhoPP/8826/u127dhnvvfee1/XPysoyQkJCDLPZbGRmZrot8+effxqhoaGO7cic26xhGMaWLVuMpk2bGpKMW2+9tcj1zluG3XnnnS7Xb9682bGK+MyZM72u9969ew1JRkJCgset4eyrvZ933nnGnj17HMdzc3ON2267zadbhu3bt88ICAgwAgICjKVLlzqO22w246WXXnK8f0+rlxe39Zm7NpaRkeForw888IDLNoZ2hw8fNv773/96/d6OHz/u2Npr0KBBHtuDO3fffbdjt4a//vrLcXzdunWOlc8XLFhQ5LqHH37Y8fd19erVXr9eYaVdvdy+zdmcOXPK/JoAUBxCNwB44Cl0G4ZhHDx40LHFU0REhNGrVy/j2muvNUaNGmV07NjRCAwMNCQ5tkT67bffDEmG2Ww2unXrZlx99dXG1VdfbXTq1MmxRdBbb73l8hqewtmLL77oqFf37t2N6667zujdu7dhMpmMm266yfE/396Gbnvd7O+lT58+xjXXXGNcccUVjveos1ukFf6BITU11YiIiDAkGb179zbGjRtnjB8/3mXv6p07dzrqlJCQYFx55ZXG5ZdfbkRHRxuSjM6dO7vdxmjRokWO4J2YmGiMHDnSuOqqq4wLLrjAMJvNxtixY13Ke/quXnvtNcNkMhkRERHGd99959VnYhgVH7oNwzCeeuopx7ZtrVq1Mq655hrjsssuM9q0aeP2mmXLlhm1a9d2fLYDBgwwbrjhBuPSSy91bGvWvXt3r+tvGIZx2WWXGZKMhQsXeiwzb948R/BOTk42Ro4caVx//fVG7969HW2/X79+LtupFX7///d//2eEhoYaTZo0Ma699lpj6NChRnBwsCHJuOKKK7ze5syua9euhiSjZcuWxg033GCMHz/eePDBBx3ns7OzHVtPhYWFGZdccolxzTXXGA0bNjQkGfHx8cbatWtL9Zr20O1uL3R78AwMDDT69etnjBo1ymjWrJlhNpuNhx56yKeh2zDy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AADAv1Sp0P32228Xez40NFQzZ87UzJkzPZZp1KiRFi5c6OuqVUtnzpzRzp07NX78eN12222O43l5eYqJiZEkjRs3ToMHD1bLli01bNgwXXrppRoyZIjHe3700Ud6+eWXtXPnTmVkZCgvL6/YediGYZSpt37Lli2aMGGCy7HevXvrpZdekiRdddVV+ve//62mTZtq2LBhuuSSSzRixAgFBQVp06ZNslqtLmFXyl/FPj4+vtjXffDBB/XII484Vtd/5plnNHz4cMf5rl27Fnv9+vXr1adPH7dzkbz5PgAAAAD4lyoVuv1RmDlQm58YWmmvfS4yMjIkSW+++aa6d+/ucs6+/VTnzp21e/duffPNN1qyZImuvvpqDRo0SJ988kmR+61cuVI33HCDpk2bpqFDhyomJkZz587VCy+84LEOLVq0UFpamg4fPlzq3u7iNGjQQNu2bdOSJUuUkpKiO+64Q88995yWLVumjIwMBQYGat26dUW22SppQbn7779f48aNU2RkpBITE4v8YBAREVHs9WFhYR7PefN9AAAAAPAvhO5zZDKZznmId2VJTExUcnKydu3apRtuuMFjuejoaF1zzTW65pprdOWVV2rYsGE6ceKE4uLiXMqtWLFCjRo10sMPP+w4tnfv3mLrcOWVV+qhhx7Ss88+qxdffLHI+cKr1du1bt1aP//8s8uQ659//llt2rRxPA8LC9OIESM0YsQITZw4Ua1atdKmTZvUqVMnWa1WHT16VBdeeGGx9Susdu3ajtX1y6J9+/aaPXu22/0Avf0+AAAAAG+98/NuvbZsp94b310tEqMquzo1kn+mRfjMtGnT9Pe//10xMTEaNmyYcnJytHbtWp08eVKTJk3SjBkzVLduXXXq1EkBAQGaN2+ekpKS3Abh5s2ba9++fZo7d666deumr7/+WvPnzy/29Rs0aKAXX3xRd955p9LT0zVmzBg1btxYBw4c0LvvvqvIyEi3PeX333+/rr76anXq1EmDBg3SggUL9Nlnn2nJkiWSpHfeeUdWq1Xdu3dXeHi43n//fYWFhalRo0aKj4/XDTfcoDFjxuiFF15Qp06ddOzYMX333Xdq3769y3BxX7vzzjv1yiuvaPz48XrkkUdUq1YtrVq1ShdccIFatmxZ4vcBAAAAFCfPatMX6w/pgiZxahAXrscXbJYkvb50p2Zc07FyK1dD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7ty5+Oyzz5CXl+e2X2lp6SUfKyMjA0IIxMTENHi7Vqu9+oKJiIhaCDbdRERELdzp06dRWlqKLl26AABuu+02bN26FU8++SQSEhLg5+cHWZYxYsQIyLJ8yceTZRmSJGHt2rVQq9X1bvfz81P8NRARETVXbLqJiIhauGXLlgEAhg8fjuLiYmzcuBFz587F7NmzXftkZGTUu58kSQ0+XufOnSGEQHR0NLp27eqZoomIiFoIntNNRETUgm3atAnz5s1DdHQ07rjjDtfIdO0q5bUWLFhQ776+vr4AUG818rS0NKjVasydO7fe4wgh3C49RkRE1NpxpJuIiKiFWLt2LQ4fPgy73Y5z585h06ZN2LBhA6KiovDNN9/AYDDAYDBg0KBBeO2112Cz2RAeHo7169cjKyur3uMlJSUBAJ599llMmjQJWq0WY8eORefOnfHSSy9h1qxZOHHiBMaNGwd/f39kZWXhyy+/xAMPPIAnnnjiWr98IiKiJolNNxERUQtRO11cp9MhKCgIPXv2xIIFCzBt2jT4+/u79vv0008xffp0vP/++xBCYNiwYVi7di3CwsLcHu/666/HvHnzsHjxYqxbtw6yLCMrKwu+vr54+umn0bVrV7z99tuYO3cuACAyMhLDhg3DzTfffO1eNBERURMnid/PCyMiIiIiIiIiRfCcbiIiIiIiIiIPYdNNRERERERE5CFsuomIiIiIiIg8hE03ERERERERkYew6SYiIiIiIiLyEDbdRERERERERB7CppuIiIiIiIjIQ9h0ExEREREREXkIm24iIiIiIiIiD2HTTUREREREROQhbLqJiIiIiIiIPIRNNxEREREREZGHsOkmIiIiIiIi8pD/D4c6dw3wEVlaAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Create a Ticker object for Tesla (TSLA)\n",
    "tesla_ticker = yf.Ticker(\"TSLA\")\n",
    "\n",
    "# Extract the stock history up to June 2021\n",
    "tesla_data = tesla_ticker.history(period=\"max\")\n",
    "\n",
    "# Filter the data up to June 2021\n",
    "tesla_data = tesla_data[tesla_data.index <= '2021-06-30']\n",
    "\n",
    "# Create the plot using the 'Close' column\n",
    "plt.figure(figsize=(10,6))\n",
    "plt.plot(tesla_data.index, tesla_data['Close'], label=\"Tesla Close Price\")\n",
    "\n",
    "# Add a title and labels\n",
    "plt.title('Tesla Stock Price (Up to June 2021)', fontsize=16)\n",
    "plt.xlabel('Date', fontsize=12)\n",
    "plt.ylabel('Stock Price (USD)', fontsize=12)\n",
    "\n",
    "# Rotate the x-axis labels for better readability\n",
    "plt.xticks(rotation=45)\n",
    "\n",
    "# Display the graph\n",
    "plt.legend()\n",
    "plt.grid(True)\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Question 6: Plot GameStop Stock Graph\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `make_graph` function to graph the GameStop Stock Data, also provide a title for the graph. The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`. Note the graph will only show data upto June 2021.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<details><summary>Hint</summary>\n",
    "\n",
    "```\n",
    "\n",
    "You just need to invoke the make_graph function with the required parameter to print the graphs.The structure to call the `make_graph` function is `make_graph(gme_data, gme_revenue, 'GameStop')`\n",
    "\n",
    "```\n",
    "    \n",
    "</details>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Ll1MfHy8kWT69evn9Zx5/X4riJkzZxpJJjY21pw+fdpjm3MMiDlz5ng9dvbs2UaSKV++vN/Pl5KSYsqVK+f3d3FearqPHj1qoqKiTLFixbLV2gOIfCTdAMLW1VdfbSSZzp07F+g8K1eu9JrE/fXXX66Bbz7++GOPbe4XsrVr1zY7d+50bTt48KCpW7eukWSaNGli2rRpYw4ePOjavn37dlfiuXTpUo/zfvXVV8bhcJhy5cpla0a4bt06U7Vq1WwD6qSnp5vmzZu74mndurV56KGHzMyZM83u3btzfO25NXc9ffq068Lwpptu8rjY27Ztm2uQtgcffNDjOPdmzRdeeKE5dOiQa9vhw4ddyezQoUNzjM/dH3/84Wq6WaRIEdOzZ08zceJEs2DBAnPkyJEcj80tuVi3bp0pUqSIcTgcZvr06R7b5s2b50oIsg6Q9OKLLxpJpmzZsuabb77Jdt4VK1aYP/74w7XsLen+9NNPTXx8vElISDCzZ8/O5V3wlFvSfe+99xpJJi4uzpw8edIjBuffztGjR70e6+u8AwYMcN2YyPp+pqammlmzZnmse/31140kU6dOHbN27VqPbd99950pUaKEiY2NNVu2bPH3Zbu6lUyZMsXr9kAm3fHx8WbRokUe25599lkjyZQsWdLs27fP77iD9feW39dY0KRbknnooYdMWlqaa9v69etdN7l+/PFHj+Py8/2WXxkZGaZt27auG6fukpKSXPH/8ssvXo9fs2aNax9/u+1MnTrVVWb27t2b6/55SbqNMeb888/P0/4AIgdJN4Cwddlll+WYuP3yyy8etUnOn7xcsHz99ddGkhk0aJDHevcL2S+++CLbcc8//7yRZBwOh9eE3lk7mrVW54ILLjCSzKeffuo1no8//thVY+tuz549rvcj60+9evXMM88840q63OWWBDj7RFapUiVbTZExNmGUZEqUKGFOnTrlWu+e2P3888/Zjlu3bp1xOBwmKioq1xsD7pYtW2YaNGiQ7TVGRUWZiy66yMyYMcPrcbklF6NHj/Z6ce502223GUmma9eurnWpqamumt3PPvvMr/izJt3//ve/jcPhMBUrVjSrVq3y6xzuvCXdGRkZZteuXebJJ580RYoUMZLMHXfckS2GmJgYs23bNp/n9pZ0//LLL64k/s8//8w1vvT0dFOlShUjyfz0009e93EmsPfc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JbnGL52Z1+krMXTekLn44otdiXGrVq1Urlw5HThwQLNmzco1tqyqVKmiJUuWqHnz5vroo480YMCAHOc2Dgc9evSQJM2bN89jPAJfWrdurXLlymnDhg367bffAhaHMxHasGGD1+3Nmzd3JdE5zbP86aefSrKfv68k8N13381xvfvc5rkJ9t9bXjkT940bN2bbtnfvXq1Zs6bAz+GU3+83f8ydO1eDBw9WWlqapk6dqhtvvDHXY5zjMMyYMSNbjX5GRoY++ugjSbYffVYHDx5Up06d9Ntvv6lz586aO3fuGWk58uuvv0pSQD57AOGFpBtAWJsyZYrq1KmjrVu36qKLLtJ3333ndb+dO3d67XvpHPBn0aJF2S7gX3/9ddeF15ny5JNPSpKuueYazZ07N9t2Y4xWrFih+fPnu9bNnTtX/fr104IFC5Senp7tmMWLF+uxxx6TZAdocudMTn0lRIMGDVL16tW1Z88ejRkzxiNZ2LFjh+655x5J0u233+61lscYo5tvvtmjD+LRo0d18803yxijgQMHumrAcvPQQw/p9ttv95rEp6Wl6bXXXnMlUXl9nXfeeaeKFCmiWbNmZbvRMn/+fL322muSpHvvvde1vkiRInrooYckSTfccIOWLFmS7byrVq3Ksc9vuXLl9O2336pdu3aaO3euevXqlWuT6FBq1qyZ+vbtq1OnTqlv377ZxkFIS0vTnDlzXMsxMTEaN26cjDHq37+/li5dmu2c6enp+uabb7R8+XK/43D251+2bJnX7TExMRozZowkaezYsVqxYoXHdmOM3njjDc2YMUMOh0P333+/z+eaOnWqa4Azp0mTJmnlypUqUaKERo8e7Xfcwf57y6suXbpIkiZOnKgjR4641h84cEAjRozwaH4fCPn5fsvNvHnzdMUVVygtLU2vvvqqXwm3ZAdNrFKlirZs2aJHHnnEY9sjjzyiLVu2qGrVqhoxYoTHtn/++UedO3fWr7/+qi5dupyxhPvo0aPasGGDihcvrjZt2gT9+QCcYWd6uHQAyKt9+/aZzp07u6Z3qVq1qundu7e56qqrzMCBA835559vHA6H0f/mzc46hVffvn2NJBMbG2u6detmhg4daho0aGAcDod56KGHvE495JyGx9eURM6pnDp06OB1u7f5mp1eeOEF11RPderUMb169TLDhw83Xbt2NRUqVDCSzL/+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lSun/v37e7yunD4/AAAAAPlDTXcOjJFC1co4IUHyZ4DoQ4cOaf78+Xr66adVrFgxr/u4jzQdFRWlF198UbVq1dL27dt1yy236P7779crr7zi2ufkyZN68cUXNWPGDB07dkwDBgxQ//79VapUKc2bN0/bt2/XwIED1a5dOw0ZMkSSdNttt2nDhg2aMWOGqlSpopkzZ6pHjx5av3696tatq0qVKum7777Trl27VKNGjWwx3nvvvdq4caOSkpJcSWqZMmV04sQJde/eXW3bttWqVau0f/9+XXfddbrtttv09ttvu45ftGiR4uLitHjxYu3cuVPXXHONypQpo/vvv9/re/L++++rfv366tu3r9f3q2TJkl6Pu//++/XZZ5/pnXfeUY0aNfTss8+qe/fu+v3331WmTBk98sgj2rBhg7788kuVK1dOv//+u06dOiXJ1kA7X8v333+vIkWK6Mknn1SPHj20bt06xcbGen3OrJw12O43FR544AE999xzat68ueLi4vT11197HPPFF1+of//+euihhzR9+nSlpKRo3rx5ru25fX4AAAAA8smcZY4ePWokmaNHj2bbdurUKbNhwwZz6tQpY4wxx48bY1PvM/9z/Lh/r2f58uVGkvn888891pctW9YUK1bMFCtWzNx///0+j//kk09M2bJlXcvTpk0zkszvv//uWnfjjTeahIQEc+zYMde67t27mxtvvNEYY8yuXbtMdHS0+euvvzzO3blzZzN27FhjjDF79uwxF154oZFk6tWrZ0aOHGk++ugjk56e7tp/5MiRpm/fvh7neP31103p0qXNcbc35IsvvjBRUVFm7969ruPKlCljTpw44dpn6tSppnjx4ubQoUMez+HUsGFD06dPH5/vi7eYjh8/bmJiYsz777/v2p6SkmKqVKlinn32WWOMMZdffrm55pprvJ7r3XffNfXr1zcZGRmudcnJySY+Pt58/fXXXo/ZsWOHkWR+/vlnY4wxhw8fNv379zfFixc3e/fudW2fPHmyx3HTpk0zJUuWdC23bdvWXHnllV6fw5/PL6usfysouJSUFDNr1iyTkpIS6lAAv1BmEUkor4g0lNnIkFNu6Y6a7kJq5cqVysjI0JVXXqnk5GTX+oULF2rChAnatGmTkpKSlJaWptOnT+vkyZNKSEiQJCUkJKh27dquYypWrKiaNWuqePHiHuv2798vyTb/Tk9PV7169TxiSE5OVtmyZSVJlStX1rJly/Trr79qyZIl+vHHHzVy5Ei9+eab+uqrrxQV5b2nw8aNG9W0aVOPWvx27dopIyNDmzdvVsWKFSVJTZs2dcUvSW3bttXx48f1559/eu33bIzx6310t23bNqWmpqpdu3audTExMWrTpo02btwoSbr55ps1cOBArVmzRt26dVO/fv100UUXSZLWrl2r33//XSVKlPA47+nTp7Vt27Ycn/uiiy5SVFSUTpw4oXPPPVcfffSRKlas6Gqa3qpVqxyP/+WXX3T99dd73ebP5wcAAAAgf0i6c5CQILl1HT7jz+2POnXqyOFwaPPmzR7rzz33XEnyGExr586d6t27t26++WY99dRTKlOmjJYuXarRo0crJSXFlbTGxMR4nMvhcHhdl5GRIUk6fvy4oqOjtXr1akVHR3vs556oS1Ljxo3VuHFj3XLLLbrpppt08cUX67vvvvPZhzpY6tWrp02bNgX8vJdddpl27dqlefPmacGCBercubNuvfVW/d///Z+OHz+uli1b6v333892XPny5XM870cffaTzzjtPZcuW9XoTwVfXAqecBlXLy+cHAAAAIG8YSC0HDodUrFhofvzpzy3ZAba6du2ql19+WSdOnMhx39WrVysjI0PPPfecLrzwQtWrV0979uwp8PvUvHlzpaena//+/apTp47HT6VKlXwed95550mSK+7Y2FiPwdkkqWHDhlq7dq3Ha/vhhx8UFRWl+vXru9atXbvW1XdakpYvX67ixYuratWqXp97+PDh2rJli2bPnp1tmzFGR48ezba+du3aio2N1Q8//OBal5qaqlWrVrlei2QT6JEjR+q9997T5MmT9frrr0uSWrRooa1bt6pChQrZ3idffcidqlWrptq1a+d77u3zzz9fixYt8rotv58fAAAA4K5/f6l9e+l/dXP4H5LuQuCVV15RWlqaWrVqpY8++kgbN27U5s2b9d5772nTpk2u2ss6deooNTVVL730krZv3653331Xr776aoGfv169erryyis1YsQIff7559qxY4dWrlypCRMm6IsvvpBkm10/8cQT+uGHH7Rr1y4tX75cI0aMUPny5dW2bVtJUs2aNbVu3Tpt3rxZBw8eVGpqqq688krFxcVp5MiR+vXXX/Xtt9/q9ttv19VXX+1qWi7ZQcVGjx6tDRs2aN68eRo3bpxuvfVWn83WBw8erCFDhmjYsGF6+umn9dNPP2nXrl3673//qy5duujbb7/NdkyxYsV0880367777tNXX32lDRs26Prrr9fJkyc1evRoSdKjjz6q2bNn6/fff9dvv/2m//73v2rYsKEk6corr1S5cuXUt29fff/999qxY4cWL16sO+64Q3/++WeBP4ecjBs3Th9++KHGjRunjRs3av369Zo4caIk/z4/AAAAIDezZkk//CD9r+cl/oekuxCoXbu2fv75Z3Xp0kVjx45V06ZN1apVK7300ku699579cQTT0iy/Z6ff/55TZw4UY0bN9b777+vCRMmBCSGadOmacSIEbrnnntUv3599evXT6tWrVL16tUlSV26dNHy5cs1aNAg1atXTwMHDlRcXJwWLVrk6jd8/fXXq379+mrVqpXKly+vH374QQkJCfr666/1zz//qHXr1rriiivUuXNnvfzyyx7P37lzZ9WtW1eXXHKJhgwZoj59+mjcuHE+43U4HPrggw/0/PPPa9asWerQoYPOP/98PfbYY+rbt6+6d+/u9bhnnnlGAwcO1NVXX60WLVro999/19dff63SpUtLsrX1Y8eO1fnnn69LLrlE0dHRmjFjhiTbV37JkiWqXr26BgwYoIYNG2r06NE6ffq0EhMTC/wZ5KRjx4765JNPNGfOHDVr1kydOnXSypUrXdtz+/wAAAAA5I/D5GdEqQiWlJSkkiVL6ujRo9kSndOnT2vHjh2qVauW4uLiQhQh8mrUqFE6cuSIZs2a5bE+IyNDSUlJSkxM9FnjjfzhbyXwUlNTNW/ePPXs2TPbGApAOKLMIpJQXhFpIrXMOrvI/vqr1KhRaGM5E3LKLd2RiQAAAAAAECQk3QAAAAAABAlThiHivf3226EOAQAAAAC8oqYbAAAAABAwZ9eoYbkj6QYAAAAAIEhIur3IYDZ3IEf8jQAAAMAdtdu+0afbTWxsrKKiorRnzx6VL19esbGxcjjHvUfEycjIUEpKik6fPs2UYQFijFFKSooOHDigqKgoxcbGhjokAAAAhBlSKE8k3W6ioqJUq1Yt/f3339qzZ0+ow0EBGWN06tQpxcfHc/MkwBISElS9enVuZgAAAAC5IOnOIjY2VtWrV1daWprS09NDHQ4KIDU1VUuWLNEll1yimJiYUIdTaERHR6tIkSLcyAAA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",
      "text/plain": [
       "<Figure size 1000x600 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import yfinance as yf\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Function to create the graph\n",
    "def make_graph(stock_data, revenue_data, stock_name):\n",
    "    # Filter the stock data up to June 2021\n",
    "    stock_data_filtered = stock_data[stock_data.index <= '2021-06-30']\n",
    "    \n",
    "    # Plotting the stock closing prices\n",
    "    plt.figure(figsize=(10, 6))\n",
    "    plt.plot(stock_data_filtered.index, stock_data_filtered['Close'], label=f'{stock_name} Close Price', color='blue')\n",
    "\n",
    "    # Add title and labels\n",
    "    plt.title(f'{stock_name} Stock Price (Up to June 2021)', fontsize=16)\n",
    "    plt.xlabel('Date', fontsize=12)\n",
    "    plt.ylabel('Stock Price (USD)', fontsize=12)\n",
    "    \n",
    "    # Rotate the x-axis labels for better readability\n",
    "    plt.xticks(rotation=45)\n",
    "    \n",
    "    # Display the grid and legend\n",
    "    plt.grid(True)\n",
    "    plt.legend()\n",
    "\n",
    "    # Display the graph\n",
    "    plt.tight_layout()\n",
    "    plt.show()\n",
    "\n",
    "# Create a Ticker object for GameStop (GME)\n",
    "gme_ticker = yf.Ticker(\"GME\")\n",
    "\n",
    "# Extract the stock history for GameStop up to June 2021\n",
    "gme_data = gme_ticker.history(period=\"max\")\n",
    "\n",
    "# Filter the data up to June 2021\n",
    "gme_data = gme_data[gme_data.index <= '2021-06-30']\n",
    "\n",
    "# Assuming gme_revenue has been extracted already and has the necessary format\n",
    "# For this example, gme_revenue is assumed to be a DataFrame, so passing a dummy gme_revenue\n",
    "gme_revenue = pd.DataFrame(columns=[\"Date\", \"Revenue\"])  # Placeholder, replace with actual revenue data if available\n",
    "\n",
    "# Call the make_graph function to plot the data\n",
    "make_graph(gme_data, gme_revenue, 'GameStop')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>About the Authors:</h2> \n",
    "\n",
    "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n",
    "\n",
    "Azim Hirjani\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Change Log\n",
    "\n",
    "| Date (YYYY-MM-DD) | Version | Changed By    | Change Description        |\n",
    "| ----------------- | ------- | ------------- | ------------------------- |\n",
    "| 2022-02-28        | 1.2     | Lakshmi Holla | Changed the URL of GameStop |\n",
    "| 2020-11-10        | 1.1     | Malika Singla | Deleted the Optional part |\n",
    "| 2020-08-27        | 1.0     | Malika Singla | Added lab to GitLab       |\n",
    "\n",
    "<hr>\n",
    "\n",
    "## <h3 align=\"center\"> © IBM Corporation 2020. All rights reserved. <h3/>\n",
    "\n",
    "<p>\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  },
  "prev_pub_hash": "83a07babb305ceb42e09cd85ba8721036292c63a89e4dfdc9f0eaa89fb9cd33d"
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
