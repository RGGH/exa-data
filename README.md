# exa-data

User guide : 

## TLDR;

- Clone this repo
- Install Docker
- Run
    `python exa_flatten_json_csv.py`
    (flattens nested JSON files)<br>
    `python exa_parse_for_sql.py` 
    (parses CSVs and adds to SQL DB)<br>

---

#### 1. Install Docker Compose

    https://docs.docker.com/compose/install/
    
    docker-compose --version
    
    # https://docs.docker.com/engine/install/
    
##### *If you get an error :
    
    (env) rag@rag-Latitude-5490:~/env/exa-data-1/exa-data$ sudo docker-compose up
    Creating network "exa-data_default" with the default driver
    ERROR: could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network
    
    Stop your openvpn :
    sudo service openvpn stop
    
#### 2. Run Docker Comopse
 
    sudo docker-compose up
    
#### 3. Install Python Packages

    pip3 install -r requirements.tx
    
#### 4. Run the 2 Python files

- These have been kept separate to allow for batch conversion from JSON to CSV, and then import into SQL
---
    python exa_flatten_json_csv.py
    python exa_parse_for_sql.py
  
#### 5. Check the imported data in in PostgreSQL 
    python db_connect.py
    
---

### About this project

- used regex to extract nested keys from 50,000 lines of JSON
- used Vim to remove empty rows
- use Pandas to remove duplicates but preserve sort order
- used Vim to add data types in bulk, plus commas
- used Jupyter Notebook for exploratory data anlaysis and testing
- Unable to find data dictionary on FHIR site for this actual project http://hl7.org/fhir/overview-dev.html http://hl7.org/fhir/resourcelist.html
- Not all fields populated due to time constraint, have done first few in order
- had issues with lists inside dicts. Resolved this with 'typing' module https://docs.python.org/3/library/typing.html#module-typing

![screenshot](https://github.com/RGGH/exa-data/blob/main/notes/db_v_py.png)
  

   
    
   
    
    
