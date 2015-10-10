# Divolte Kafka Consumer to Insert into Database
from kafka import KafkaConsumer
import avro.schema
import avro.io
import io
import MySQLdb
from Configurations import Configuration

class kafkamysql:

	def __init__(self,filename,schema):
		self.conf = Configuration(filename)

		self.host,self.username,self.password,self.dbName = self.conf.getMySQLDetails()
		self.kafka_host,self.kafka_port = self.conf.getBrokerDetails()
		self.topic,self.consumergroup = self.conf.getConsumerDetails()
		self.schemaAvro = schema
		# Open database connection
		self.db = MySQLdb.connect(self.host,self.username,self.password,self.dbName)
		self.cursor = self.db.cursor()

	# Insert Into Database
	def insertIntoDatabase(self,d):
		keys=[]
		values=[]
		for k, v in d.iteritems():
		    keys.append(k)
		    values.append(v)
		columns=','.join(str(k) for k in keys)
		data=','.join("'"+str(v)+"'" for v in values)
		sql="insert into raw_clicks ("+columns+") values("+data+")"
		try:
		    self.cursor.execute(sql)
		    self.db.commit()
		except:
		    self.db.rollback()

	def divoltecall(self):    
		# get configuration parameters from confguration file
		  

		# Kafka Broker Configuration
		broker_config=self.kafka_host+":"+str(self.kafka_port)
		# To consume messages
		consumer = KafkaConsumer(self.topic,
		                         group_id=self.consumergroup,
		                         bootstrap_servers=[broker_config])
		# read Avro schema
		schema = avro.schema.parse(open(self.schemaAvro).read())

		

		for msg in consumer:
		    bytes_reader = io.BytesIO(msg.value)
		    decoder = avro.io.BinaryDecoder(bytes_reader)
		    reader = avro.io.DatumReader(schema)
		    user1 = reader.read(decoder)
		    self.insertIntoDatabase(user1)

		# disconnect from server
		self.db.close()