#spark-submit --master spark://ip-172-31-0-104:7077 --executor-memory 14000M --driver-memory 14000M reddit2cassandra.py "ec2-52-40-27-174.us-west-2.compute.amazonaws.com:9092,ec2-52-37-195-19.us-west-2.compute.amazonaws.com:9092,ec2-52-39-242-87.us-west-2.compute.amazonaws.com:9092"
spark-submit --master spark://ip-172-31-0-104:7077 reddit2cassandra.py 2015_12
