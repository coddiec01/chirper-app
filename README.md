# Chirper App
# About
A script that is interacting with a hypothetical chirper service through HTTP requests using the requests library in Python, which allows users to log in, read chirps, post chirps, and search for chirps.
# Install Python
Ensure Python is installed on your computer. 
1. To set up python locally, first check to see if it's already installed by opening your CLI (commmand line interface) and inputting python --version or python3 --version.
2. If you do not have python installed, refer to this website: https://www.python.org/ and follow the installation instructions for your operating system.
3. Once this is complete, ensure that its installation directory is added to your PATH environment varibale. This will enable your shell to find the "python" command.
4. To ensure step 3 is complete, in your terminal, type in "echo $PATH" to verify that the directory  (where python is installed) is included in the output.
# Install basicdb
Refer here: https://pypi.org/project/basicdb/ and follow the installation instructions.
# Running the application
1. Ensure the Backend Service is Running: The code appears to interact with a backend service running locally at http://localhost:5000. Make sure this backend service (chirper service) is running on your computer.

2. Install Required Dependencies: Make sure you have the requests library installed. You can install it using pip if you haven't already:

pip install requests

3. Execute the Python Script: Run the Python script in your terminal or command prompt:

python chirper_client.py

4. Interact with the CLI: Once the script is running, follow the prompts in the command-line interface to log in, read chirps, post chirps, or search for chirps.

- Note: The chirperclient.py will interact with a server-side service (the chirper service) via HTTP requests to perform various actions like logging in, reading chirps, posting chirps, and searching chirps.

- The client-side script is responsible for handling user input, making requests to the server-side endpoints defined by the chirper service, and displaying the results to the user.

# Advanced Instruction
If you would like to be more advanced, you can develop a SQL database to store the chirps. For example, you could have the script interact with pgAdmin and store user information in a PostgreSQL database.

Here's how you can use pgAdmin:

1. Install pgAdmin:

    Download and install pgAdmin from the official website: pgAdmin.
    Follow the installation instructions for your operating system.

2. Launch pgAdmin:

    - After installation, launch pgAdmin. It typically runs as a desktop application.

3. Connect to PostgreSQL Server:

    - In pgAdmin, you'll need to connect to your PostgreSQL server instance.
    - Click on the "Add New Server" button or select "Add New Server" from the File menu.
    - Enter the connection details for your PostgreSQL server, such as hostname, port, username, and password.
    - Once connected, you'll see your PostgreSQL databases listed in the pgAdmin interface.

4. Manage Databases:

    - You can perform various tasks on your databases using pgAdmin, including creating, editing, and deleting databases and database objects.
    - You can run SQL queries, view table structures, and perform other database administration tasks through the pgAdmin interface.

5. Access Web Interface:

    - pgAdmin also provides a web-based interface in addition to the desktop application. By default, it runs on http://localhost:5050.
    - You can access the web interface in your browser and log in with your pgAdmin credentials.
    install basicdb for Python: https://pypi.org/project/basicdb/

While pgAdmin and the client-side script serve different purposes, they both can be used together to manage a PostgreSQL database while also interacting with the chirper service. Just ensure that the database schema and data access methods used by the chirper service are compatible with pgAdmin for effective database management.





