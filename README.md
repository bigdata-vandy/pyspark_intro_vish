# pyspark_intro_vish
This is a brief Introduction to Pyspark
This tutorial should be followed in the mentioned order for best results:

1.) spark_read - This is how to go about reading a CSV file in pyspark, there are many other types of files that can be read though and data can be cleaned through python such as json,html etc. 

We also go through splitting up the line and forming a tuple for each row in the RDD which is a Resilient Distributed Dataset, in short it is simply immutable if not being operated upon its entirety.

2.)spark_divide - This follows on top of the previous tutorial and catches up on creating a total count. How to go about converting data types in the RDD and for example getting a division of each value present in each RDD.

3.)spark_key - This reads two separates files and then organizes them into tuples per row for the RDD. Keys are created for both the tables created and then both the tables are joined using the key. To be noted when keys are created pyspark ends up creating another column for us and we have to know how the data is being messed around with inside the black box.

Thats it folks !

Happy Sparking it up ;)
