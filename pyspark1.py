# Databricks notebook source
from pyspark.sql import SparkSession

# COMMAND ----------

spark = SparkSession.builder.appName("StudentAssignment").getOrCreate()

# COMMAND ----------

data = [
(1, "Alice", "Engineering", 65000),
(2, "Bob", "Marketing", 58000),
(3, "Charlie", "Sales", 52000),
(4, "David", "Engineering", 72000),
(5, "Eve", "Sales", 54000)
]

# COMMAND ----------

schema = ["ID", "Name", "Department", "Salary"]
df = spark.createDataFrame(data, schema=schema)
df.show()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.filter(df["Salary"] > 60000).show()

# COMMAND ----------

df.groupBy("Department").count().show()

# COMMAND ----------

df.groupBy("Department").avg("Salary").show()


# COMMAND ----------

