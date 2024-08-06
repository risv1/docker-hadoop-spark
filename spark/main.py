import logging
from pyspark.sql import SparkSession

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

spark = SparkSession.builder.appName("CountLines").getOrCreate()

text_file = spark.read.text("/app/input.txt")

line_count = text_file.count()

logger.info(f"Number of lines: {line_count}")

spark.stop()