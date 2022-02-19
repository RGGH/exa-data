# exa-data

User guide : 

### TLDR;

#### Install Docker Compose

    https://docs.docker.com/compose/install/
    
    docker-compose --version
    
    # https://docs.docker.com/engine/install/
    
##### *If you get an error :
    
    (env) rag@rag-Latitude-5490:~/env/exa-data-1/exa-data$ sudo docker-compose up
    Creating network "exa-data_default" with the default driver
    ERROR: could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network
    
    Stop your openvpn :
    sudo service openvpn stop
    
#### Run Docker Comopse
 
    sudo docker-compose up
    
#### Install Python Packages

    pip3 install -r requirements.tx
    
#### Run the 2 Python files

- These have been kept separate to allow for batch conversion from JSON to CSV, and then import into SQL
---
    python exa_flatten_json_csv.py
    python exa_parse_for_sql.py
  
#### Check the imported data in in PostgreSQL 
    python db_connect.py
  

   
    
   
    
    
