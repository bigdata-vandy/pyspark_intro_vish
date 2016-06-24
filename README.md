# pyspark_intro_vish
This is a brief Introduction to Pyspark
This tutorial should be followed in the mentioned order for best results:

1.) spark_read - This is how to go about reading a CSV file in pyspark, there are many other types of files that can be read though and data can be cleaned through python such as json,html etc. 

We also go through splitting up the line and forming a tuple for each row in the RDD which is a Resilient Distributed Dataset, in short it is simply immutable if not being operated upon its entirety.

2.)spark_divide - This follows on top of the previous tutorial and catches up on creating a total count. How to go about converting data types in the RDD and for example getting a division of each value present in each RDD.

3.)spark_key - This reads two separates files and then organizes them into tuples per row for the RDD. Keys are created for both the tables created and then both the tables are joined using the key. To be noted when keys are created pyspark ends up creating another column for us and we have to know how the data is being messed around with inside the black box.

Thats it folks !

Happy Sparking it up ;)

Useful Tutorial Links:

1.) This one outlines the configuration for pyspark before we start launching jobs. https://spark.apache.org/docs/0.9.1/python-programming-guide.html 

2.) This has good explanations for the most basic functions in pyspark which are brief and to the point.
http://www.mccarroll.net/blog/pyspark2/

3.) This is the list of all the functions/utilities provided in spark for RDD's.
https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html

How to get started:

1.) Python 2.7. Happy base. Pyspark. Follow the below commands:

- First one creates a virtual environment:

conda create -n venv python=2.7

- Activates the new environment:

source activate venv

- Installs Happy base:

pip install happybase

- Ensure you have these in the bashrc:

export HADOOP_HOME=/usr/lib/hadoop-mapreduce/
export PYSPARK_PYTHON=/opt/anaconda2/python27/bin/python
