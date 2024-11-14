# distributed_file_system
client and server side will be hosted on webpages 

Here's a simple `README.md` file that will guide users through setting up, running, and accessing the distributed file system.

---

# Distributed File System

This project is a simple distributed file system implemented in Python with a Flask-based web interface. It includes a master server, storage nodes, and a client application that allows users to upload and download files.

## Prerequisites

- **Python**: Make sure Python 3 is installed. [Download Python](https://www.python.org/downloads/)
- **pip**: Python's package manager should be installed with Python.

## Setup and Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/distributed_file_system.git
   cd distributed_file_system
   ```

2. **Install Required Packages**:
   Install Flask and Requests using `pip`:
   ```bash
   pip install flask requests
   ```

## Running the Distributed File System

Follow these steps to start the master server, storage nodes, and client application.

1. **Start the Master Server**:
   ```bash
   cd master
   python3 master.py
   ```
   The master server runs on `http://localhost:5000`.

2. **Start the Storage Nodes**:
   Open a new terminal for each node.

   - **Node 1**:
     ```bash
     cd server_node1
     python3 server.py
     ```
     Node 1 runs on `http://localhost:5001`.

   - **Node 2**:
     ```bash
     cd server_node2
     python3 server.py
     ```
     Node 2 runs on `http://localhost:5002`.

3. **Start the Client Application**:
   Open another terminal for the client application.

   ```bash
   cd client
   python3 client.py
   ```
   The client application runs on `http://localhost:5003`.

## Accessing the Web Interface

Once the servers and client are running, open a web browser and go to `http://localhost:5003` to access the client interface.

### Client Interface Features
- **Upload Files**: Select a file to upload to the distributed file system.
- **Download Files**: See the list of available files with download buttons to retrieve files.

### Summary of URLs

- **Master Server**: `http://localhost:5000`
- **Storage Node 1**: `http://localhost:5001`
- **Storage Node 2**: `http://localhost:5002`
- **Client Interface**: `http://localhost:5003`

## Troubleshooting

If you encounter any issues:
- Ensure each server and the client is running on its designated port.
- Check for firewall or security software that might block access to ports `5000`, `5001`, `5002`, and `5003`.

---
