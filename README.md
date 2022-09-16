# test-duckdb-companylookup
Lookup a UK company using duckdb


## 1. Install duckdb

[https://duckdb.org/docs/installation/](https://duckdb.org/docs/installation/)

Do this in a virtual environments to remain sane.

```
pip install duckdb
```

## 2. Download all companies from companies house

[http://download.companieshouse.gov.uk/en_output.html](http://download.companieshouse.gov.uk/en_output.html)

```
wget http://download.companieshouse.gov.uk/BasicCompanyDataAsOneFile-2022-09-01.zip
unzip BasicCompanyDataAsOneFile-2022-09-01.zip
```

## 3. Find a company

```
python company_lookup.py
```


```
$ time python company_lookup.py 
[('MATATIKA LIMITED', '08275103', 'Private Limited Company')]

real	0m17.092s
user	0m17.280s
sys	0m1.150s
```
