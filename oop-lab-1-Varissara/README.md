# Data_processing

This is a object-oriented programming (OOP)  code which develop from procederal style code. The code has two important classes: 1. class Data Loader (import csv file to use) and 2. class Table (filter in formation and aggregate information).

---

## Features

To start with `DataLoader` class support the following operations:

* **base path:** Initialize by getting path to the Python file if basepath is None, it will use the same directory as the scriot file.
* **load_csv:** Load csv file and collect the data in dict form.

---

Second is `Table` class support the following operations:

* **Create Table:** Initialize by creating the table by using two parameters: 'condition' and 'dict_list'
* **Filter:** Filters the table data based on a condition and mainly using under topic e.g. city and country.
* **aggregate:** To calculate by using aggregation_function and to extract values from the cloumn is by using agrregation_key.

--

## Files

* **`Cities.csv`**: Contains the data: city, country, latitude, longitude, temperature.
* **`data_processing.py`**: A script to import, create, and use an instance from `Cities.csv`.

---

## Requirements
* Python 3.x

---

##  How to Use

To run the demonstration script, execute `data_processing.py` from your terminal:

```bash