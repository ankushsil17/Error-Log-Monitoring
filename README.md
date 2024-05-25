Error Log Monitoring Platform

Description

This repository contains a solution for an Error Log Monitoring platform. The solution processes log entries and performs various operations such as computing statistics based on timestamps and log types. The project is implemented in Python and includes functionality to generate test input files and Dockerize the solution for easy deployment.

Features

1. Submit Log Entry: Store a new log entry with timestamp, log type, and severity.
2. Compute Statistics by Log Type: Compute the min, max, and mean severity for a specified log type.
3. Compute Statistics Before/After Timestamp: Compute the min, max, and mean severity for all log entries occurring before or after a specified timestamp.
4. Compute Statistics by Log Type and Timestamp: Compute the min, max, and mean severity for all log entries of a specified log type occurring before or after a specified timestamp.

Assumptions

1. Timestamps will come in an ascending sorted order.
2. Log types can be any UTF-8 supported string with a maximum length of 100 characters.
3. Severity will be a positive non-zero floating-point number.
4. The solution ensures precision to 10E-6 for severity results.

File Structure

- `index.py`: Main script for processing log entries and generating the output.
- `generate_inputs.py`: Script for generating test input files.
- `input.txt`: Input file containing log entries and commands.
- `output.txt`: Output file for storing the results.
- `Dockerfile`: Dockerfile for containerizing the application.

Prerequisites

- Python 3.8-slim
- Docker

Running the Solution

1. Generate Test Input File:
    python generate_inputs.py
2. Run the Main Script:
    python index.py

Dockerizing the Solution

1. Build the Docker Image:
    docker build -t errorlogmonitoring .
    
2. Run the Docker Container:
    docker run --name errorlogmonitoring -v C:/path/to/your/project/input.txt:/app/input.txt -v C:/path/to/your/project/output.txt:/app/output.txt errorlogmonitoring
   

Example

1. Sample Input (input.txt):
    
     1 1715744138011;INTERNAL_SERVER_ERROR;23.72 <br/>
     1 1715744138012;INTERNAL_SERVER_ERROR;10.17 <br/>
     2 INTERNAL_SERVER_ERROR <br/>
     1 1715744138012;BAD_REQUEST;15.22 <br/>
     1 1715744138013;INTERNAL_SERVER_ERROR;23.72 <br/>
     3 BEFORE 1715744138011 <br/>
     3 AFTER 1715744138010 <br/>
     2 BAD_REQUEST <br/>
     4 BEFORE INTERNAL_SERVER_ERROR 1715744138011 <br/>
     4 AFTER INTERNAL_SERVER_ERROR 1715744138010
    

2. Sample Output (output.txt):
   
    No output <br/>
    No output <br/>
    Min: 10.17, Max: 23.72, Mean: 16.945000 <br/>
    No output <br/>
    No output <br/>
    Min: 0.00, Max: 0.00, Mean: 0.000000 <br/>
    Min: 10.17, Max: 23.72, Mean: 18.207500 <br/>
    Min: 15.22, Max: 15.22, Mean: 15.220000 <br/>
    Min: 0.00, Max: 0.00, Mean: 0.000000 <br/>
    Min: 10.17, Max: 23.72, Mean: 19.203333
   

Author

Ankush Sil Sarma


