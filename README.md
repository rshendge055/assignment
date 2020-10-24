# assignment
## Description
In this challenge, you are asked to develop REST API for a metallics optimization service.
The metallics optimizer calculates the cheapest charge mix for an electric arc furnace (EAF)
in a steel plant. The charge materials are different scrap types and virgin material. In summary
those materials are called commodities. The optimization algorithm uses the chemical
composition of commodities as input values to guarantee that the chemical composition of the
tapped melt is within a specific range. The melt is tapped after the melting process in the EAF
is finished. One complete melting process as well as tapping the melt into a ladle is called a
heat.

## Project setup
Virtual env set up and activate
```bash
python3 -m venv env
source env/bin/activate
```

Clone the repo
```bash
git clone https://github.com/rshendge055/assignment.git
```

Install requirements.txt
```bash
pip install -r /path/to/requirements.txt
```
Now sync your database for the first time
```bash
python manage.py migrate
```
Load data
```
./manage.py loaddata db.json
```
Hit the below url in browser
```
http://localhost:8000/metallics-optimization
```
Login and password 
```
admin
password123
```
You will see
```python
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "api/v1/public/chemicals": "http://localhost:8000/metallics-optimization/api/v1/public/chemicals/",
    "api/v1/public/commodities": "http://localhost:8000/metallics-optimization/api/v1/public/commodities/",
    "api/v1/public/chemical_compositions": "http://localhost:8000/metallics-optimization/api/v1/public/chemical_compositions/"
}
```
Technology Stack
```
python 3.5+
Django
Django rest framework
mysql
```
