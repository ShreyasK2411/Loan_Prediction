import os
import sys
import happybase

# os.environ["SPARK_HOME"] = "/home/talentum/spark"
# os.environ["PYLIB"] = os.environ["SPARK_HOME"] + "/python/lib"
# os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3.6" 
# os.environ["PYSPARK_DRIVER_PYTHON"] = "/usr/bin/python3"
# sys.path.insert(0, os.environ["PYLIB"] +"/py4j-0.10.7-src.zip")
# sys.path.insert(0, os.environ["PYLIB"] +"/pyspark.zip")
import pyspark
    
def put(row):
    """
    This function inserts the incoming row in the hbase table,
    should be called with foreach method of the spark sql dataframe
    """
    # converting the Row into dictionary
    row = row.asDict()
    data = dict()

    # creating the row key
    row_key = bytes(str(row['app_id']) + '_' + str(row['transaction_number']),encoding='utf-8')

    # creating a dictionary to insert data in hbase
    for key,value in row.items():
        key = bytes('details:'+key,encoding='utf-8')
        value = bytes(str(value),encoding='utf-8')
        data[key] = value

    # deleting the columns that are not required
    del data[b'details:app_id']
    del data[b'details:transaction_number']

    # Finally putting the data in the table
    connection = happybase.Connection(host='localhost')
    try:
        data_copy = data
        connection.table('transactions').put(row_key,data_copy)
    finally:
        connection.close()

# Creating a spark session
spark = pyspark.sql.SparkSession.builder.appName("Put data in Hbase").getOrCreate()
try:
    # Reading the data
    # read all the files and combine them into a single dataframe
    df = ""
    path = input('Enter Path: ')
    for file in os.listdir(path):
        rdd1 = spark.read.parquet("file://" + path + "/" + file)

        if df == "":
            df = rdd1
        else:
            df = df.union(rdd1)

    connection = happybase.Connection(host='localhost')
    if bytes('transactions',encoding='utf-8') not in connection.tables():
        # setting the name of the column family
        column_family = input('Enter column family name: ')
        connection.create_table('transactions',{column_family:dict()})
        connection.close()
        print("Table created successfully !!")

    df.foreach(put)
finally:
    # Closing the connection
    spark.stop()