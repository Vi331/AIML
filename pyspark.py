# Databricks notebook source
import pyspark
from pyspark.sql import SparkSession

# COMMAND ----------

spark =SparkSession.builder.appName("PySparkExample").getOrCreate()

# COMMAND ----------

data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# COMMAND ----------

df.show()

# COMMAND ----------

spark.stop()


# COMMAND ----------

