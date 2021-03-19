# Rebuild step-by-step
changes that were made described below

## Edit the .yml file
In the mascale-docker/maxcale directory:
```
nano docker-compose.yml
```
-     rename: master to master1, slave1 to master2 and delete slave2.
-     disable failover functionality by deleting or putting a # in front of any option that mentions "slave"
-     change the volumes entry for master1 and master2
		- ./sql/shrd1:/docker-entrypoint-initdb.d
		- ./sql/shrd2:/docker-entrypoint-initdb.d
-     under maxscale service, change 'depends on' entry to master1 and master2 

## Edit the .cnf file
Changes based on info from:  
https://mariadb.com/kb/en/mariadb-maxscale-14/maxscale-simple-sharding-with-two-servers/  
  
In the maxscale-docker/maxscale/maxscale.cnf.d directory:
```
nano example.cnf
```
-     delete [server3] 
-     change address entry of [server1] from master to master1
-     change address entry of [server2] from slave1 to master2
-     Under [Read-Write-Service] 
	-	change: servers= to server1, server2
	-	disable: master_failure_mode=fail_on_write, 
	-	disable: router_options=slave
	
## For Python Management
Can use the script in main.py file found int the "350 RW project" folder:
