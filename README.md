# distributed_file_system
client and server side will be hosted on webpages 

# File Architecture
distributed_file_system/
├── client/
│   ├── client.py                # Client application to interact with the master server
│   └── templates/
│       └── index.html           # HTML template for the client web interface
│
├── master/
│   ├── master.py                # Master server to handle file metadata and replication
│   └── master_files.db          # SQLite database for metadata (created automatically)
│
├── server_node1/
│   ├── server.py                # Storage node server application
│   ├── uploads_node1/           # Directory to store files on Node 1
│   └── files.db                 # SQLite database for metadata on Node 1 (created automatically)
│
├── server_node2/
│   ├── server.py                # Storage node server application
│   ├── uploads_node2/           # Directory to store files on Node 2
│   └── files.db                 # SQLite database for metadata on Node 2 (created automatically)
│
└── utils/
    └── sync.py                  # Optional script for periodic file synchronization across nodes
