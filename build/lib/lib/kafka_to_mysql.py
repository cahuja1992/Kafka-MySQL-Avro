# Divolte Kafka Consumer to Insert into Database
from kafka import KafkaConsumer
import avro.schema
import avro.io
import io
import MySQLdb
from Configurations import Configuration

# Insert Into Database
def insertIntoDatabase(d):
    keys=[]
    values=[]
    for k, v in d.iteritems():
        keys.append(k)
        values.append(v)
    columns=','.join(str(k) for k in keys)
    data=','.join("'"+str(v)+"'" for v in values)
    sql="insert into raw_clicks ("+columns+") values("+data+")"
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    
# get configuration parameters from confguration file
conf = Configuration("default.yml")

host,username,password,dbName = conf.getMySQLDetails()
kafka_host,kafka_port = conf.getBrokerDetails()
topic,consumergroup = conf.getConsumerDetails()
schemaAvro = conf.getAvroSchema()  

# Kafka Broker Configuration
broker_config=kafka_host+":"+str(kafka_port)
# To consume messages
consumer = KafkaConsumer(topic,
                         group_id=consumergroup,
                         bootstrap_servers=[broker_config])
# read Avro schema
schema = avro.schema.parse(open(schemaAvro).read())

# Open database connection
db = MySQLdb.connect(host,username,password,dbName)
# prepare a cursor object using cursor() method
cursor = db.cursor()

for msg in consumer:
    bytes_reader = io.BytesIO(msg.value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    user1 = reader.read(decoder)
    insertIntoDatabase(user1)

# disconnect from server
db.close()
