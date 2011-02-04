class ConsistencyLevel:
  """
  The ConsistencyLevel is an enum that controls both read and write behavior based on <ReplicationFactor> in your
  storage-conf.xml. The different consistency levels have different meanings, depending on if you're doing a write or read
  operation. Note that if W + R > ReplicationFactor, where W is the number of nodes to block for on write, and R
  the number to block for on reads, you will have strongly consistent behavior; that is, readers will always see the most
  recent write. Of these, the most interesting is to do QUORUM reads and writes, which gives you consistency while still
  allowing availability in the face of node failures up to half of <ReplicationFactor>. Of course if latency is more
  important than consistency then you can use lower values for either or both.

  Write consistency levels make the following guarantees before reporting success to the client:
    ANY          Ensure that the write has been written once somewhere, including possibly being hinted in a non-target node.
    ONE          Ensure that the write has been written to at least 1 node's commit log and memory table
    QUORUM       Ensure that the write has been written to <ReplicationFactor> / 2 + 1 nodes
    LOCAL_QUORUM Ensure that the write has been written to <ReplicationFactor> / 2 + 1 nodes, within the local datacenter (requires NetworkTopologyStrategy)
    EACH_QUORUM  Ensure that the write has been written to <ReplicationFactor> / 2 + 1 nodes in each datacenter (requires NetworkTopologyStrategy)
    ALL          Ensure that the write is written to <code>&lt;ReplicationFactor&gt;</code> nodes before responding to the client.

  Read:
    ANY          Not supported. You probably want ONE instead.
    ONE          Will return the record returned by the first node to respond. A consistency check is always done in a background thread to fix any consistency issues when ConsistencyLevel.ONE is used. This means subsequent calls will have correct data even if the initial read gets an older value. (This is called 'read repair'.)
    QUORUM       Will query all storage nodes and return the record with the most recent timestamp once it has at least a majority of replicas reported. Again, the remaining replicas will be checked in the background.
    LOCAL_QUORUM Returns the record with the most recent timestamp once a majority of replicas within the local datacenter have replied.
    EACH_QUORUM  Returns the record with the most recent timestamp once a majority of replicas within each datacenter have replied.
    ALL          Queries all storage nodes and returns the record with the most recent timestamp.
  """
  ZERO = 0
  ONE = 1
  QUORUM = 2
  LOCAL_QUORUM = DCQUORUM = 3
  EACH_QUORUM = DCQUORUMSYNC = 4
  ALL = 5
  ANY = 6