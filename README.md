# Kafka-MySQL-Avro
Kafka Consumer to insert avro records to mysql


```
git clone https://github.com/cahuja1992/Kafka-MySQL-Avro.git
python kafka-mysql-avro/setup.py install
```

```
#!/usr/bin/env python

from divoltemysql.kafkamysql import kafkamysql
km=kafkamysql("conf/default.yml","conf/DefaultEventRecord.avsc")
km.divoltecall()
```


## Apache Avro
In the emerging need of Serialization frameworks including Thrift, 
Protocol Buffersand Avro for a solution to address our needs as a demand side platform, 
but also for a protocol framework to use for the OpenRTB marketplace as well. 
The working draft of OpenRTB 2.0 uses simple JSON encoding, 
which has many advantages including simplicity and ubiquity of support. 
Many OpenRTB contributors requested we support at least one binary standard as well, 
to improve bandwidth usage and CPU processing time for real-time bidding at scale.

Apache Avro is one such serialization framework which is in turn an efficient way to serialize data with schema

 The following are the key advantages of Avro 1.5:

* <b>Schema evolution</b> – Avro requires schemas when data is written or read. Most interesting is that you can use different schemas for serialization and deserialization, and Avro will handle the missing/extra/modified fields.

* <b>Untagged data</b> – Providing a schema with binary data allows each datum be written without overhead. The result is more compact data encoding, and faster data processing.

* <b>Dynamic typing</b> – This refers to serialization and deserialization without code generation. It complements the code generation, which is available in Avro for statically typed languages as an optional optimization.

### Schema Evolution

This is the most exciting feature! 
It allows for building less decoupled and more robust systems. 
Below, I made significant changes to the schema, and things still work fine. 
This flexibility is a very interesting feature for rapidly evolving protocols like OpenRTB.

```
{
    "type": "record",
    "name": "Employee",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "age", "type": "int"},
        {"name": "emails", "type": {"type": "array", "items": "string"}},
        {"name": "boss", "type": ["Employee","null"]}
    ]
}
```

```
{
    "type": "record",
    "name": "Employee",
    "fields": [
        {"name": "name", "type": "string"},
        {"name": "yrs", "type": "int", "aliases": ["age"]},
        {"name": "gender", "type": "string", "default":"unknown"},
        {"name": "emails", "type": {"type": "array", "items": "string"}}
    ]
}
```

In the above example you can see that if schema changes then how we will handle that in JSON.
This is one such example of Avro, similarily there are several such use cases in which we prefer Avro.


Read More
* https://avro.apache.org/docs/1.7.7/spec.html
* http://blog.cloudera.com/blog/2009/11/avro-a-new-format-for-data-interchange/
* http://www.tutorialspoint.com/avro/avro_quick_guide.htm

## Apache Kafka

#### Features of Kafka
1. Kafka is a distributed messaging queue: A queue which can scale on 100 or 1000s of machine.
2. It supports replication: Because there are multiple broker available, for fault tolerance and high availability.
3. Partitioned the data: To limit the data coming basically disk usage on each machine (node) depending on each node machine.
4. No single point failure: Every node in a cluster is same as another, no master-slave architecture.
5. High read and write performance: Push and Pull mechanism is followed. If Producer is producing data 1000 records/sec, consumer at same rate. 99% data will come from RAM and Cache. That is why we have high read and write speed.
6. Persist data into disk; All cache and RAM goes into disk
7. Support the data retention : How much data I want to retain
8. For high availability of required data : How much amount of old data I want to retain

Read More
* http://getdatainsights.com/blog/?p=89
* http://getdatainsights.com/blog/?p=168
* http://hortonworks.com/hadoop-tutorial/simulating-transporting-realtime-events-stream-apache-kafka/
* http://www.michael-noll.com/blog/2014/08/18/apache-kafka-training-deck-and-tutorial/
