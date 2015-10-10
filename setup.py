from setuptools import setup

setup(name='divolte-mysql',
      version='0.1',
      description='Divolte Kafka Consumer for MySQL',
      author='Chirag',
      author_email='mail.ahujachirag@gmail.com',
      license='bigdatachef',
      packages=['src','conf'],
      install_requires=[
          'kafka-python','avro','MySQL-python','PyYAML'
      ],
      scripts=['bin/divolte-mysql'],
      zip_safe=False)
