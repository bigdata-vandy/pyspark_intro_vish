
from pyspark import SparkConf, SparkContext

import sys
import re

from variables import MACHINE, VUID, PAGE_TABLE, INDEX_TABLE, COLUMN_FAMILY, COLUMN

MIN_OCCURRENCES = 10
MAX_WORDS = 5000

index_file = 'hdfs:///user/%s/movie_join/' % VUID

def index(spark, movie_file, tags_file):
    movie_data = spark.textFile(movie_file)
    movie_data = movie_data.map(lambda line: line.split(",")) \
        .map(lambda movie: (movie[0],movie[1],movie[2])) \
        .keyBy(lambda (movieid,name,genre):movieid) \

    tags_data = spark.textFile(tags_file)
    tags_data = tags_data.map(lambda row: row.split(",")) \
	.map(lambda tags: (tags[0],tags[1],tags[2],tags[3])) \
	.keyBy (lambda (user,movie,tag,timestamp):movie) \
    
    joined_data = movie_data.join(tags_data)

    joined_data.saveAsTextFile(index_file)

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
    index(spark, sys.argv[2], sys.argv[3])

