
from pyspark import SparkConf, SparkContext

import sys
import re

from variables import MACHINE, VUID, PAGE_TABLE, INDEX_TABLE, COLUMN_FAMILY, COLUMN

MIN_OCCURRENCES = 10
MAX_WORDS = 5000

index_file = 'hdfs:///user/%s/movie_tutorial/' % VUID

def index(spark, movie_file):
    movie_data = spark.textFile(movie_file)
    movie_data = movie_data.map(lambda line: line.split(",")) \
#	.map(lambda movie: (movie[0])) \
	
    movie_data.saveAsTextFile(index_file)

if __name__ == '__main__':
    conf = SparkConf()
    if sys.argv[1] == 'local':
        conf.setMaster("local[3]")
        print 'Running locally'
    elif sys.argv[1] == 'cluster':
        conf.setMaster("spark://10.0.22.241:7077")
        print 'Running on cluster'
    conf.set("spark.executor.memory", "10g")
    conf.set("spark.driver.memory", "10g")
    spark = SparkContext(conf = conf)
    index(spark, sys.argv[2])


