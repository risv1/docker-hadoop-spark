# Hadoop
Basic hadoop nodes

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
Setup venv with python and install requirements (just pyspark)
Simple example for line count with python
Run following command in docker terminal
`spark spark-submit /app/main.py`