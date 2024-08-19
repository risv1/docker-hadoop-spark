# Hadoop
Basic hadoop nodes 

# Hive

## Connect to Hive Server
 - `docker-compose exec hive-server bash`
 - Next connect to server using Hive's JDBC client 'beeline' `/opt/hive/bin/beeline -u jdbc:hive2://localhost:10000` 

## Create sample table
  - `CREATE TABLE pokes (foo INT, bar STRING);`
  - `LOAD DATA LOCAL INPATH '/opt/hive/examples/files/kv1.txt' OVERWRITE INTO TABLE pokes;`

## Query with PrestoDB
  - Get jar file `wget https://repo1.maven.org/maven2/io/prestosql/presto-cli/308/presto-cli-308-executable.jar`
  - Rename `mv presto-cli-308-executable.jar presto.jar`
  - Give it access `chmod +x presto.jar`
  - Run Presto session by connecting to Presto's server and using Hive's data source (catalog) `./presto.jar --server localhost:8080 --catalog hive --schema default`
  - `select * from pokes;`


# MapReduce

## Example Jar file
Jar file with multiple mapreduce example programs
Copy jar file and sample text into hdfs
Run any example with `hadoop jar hadoop-mapreduce-examples-2.7.1.jar <example> input output`

## Custom Word Count Script
Copy java files to docker
Once inside docker terminal, compile Java files with hadoop classpath
``javac -classpath `hadoop classpath` -d . WordCountMapper.java WordCountReducer.java WordCountDriver.java``
Create a jar file for the compiled classes
`jar -cvf wordcount.jar -C . .`
Run the Hadoop Job
`hadoop jar wordcount.jar WordCountDriver /user/hadoop/input/input.txt /user/hadoop/output`
Verify output
`hdfs dfs -cat /user/hadoop/output/part-r-00000` 

# Spark
Setup venv with python and install requirements (just pyspark) \
Simple example for line count with python \
Run following command in docker terminal \
`spark spark-submit /app/main.py`

