from cassandra.cluster import Cluster
import time


cluster = Cluster(['cassandra_1', 'cassandra_2', 'cassandra_3'])
session = cluster.connect()

version = session.execute("SELECT release_version FROM system.local").one()
print(f'connected to cassandra {version} :-)')


yay = input("say nam nam")

print(f'did you say {yay}')