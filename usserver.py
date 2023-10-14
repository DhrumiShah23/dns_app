from flask import Flask, request, jsonify
import requests

app = Flask(__name)

# Dictionary to store DNS mappings (for simplicity, you can use an actual database)
dns_mappings = {}

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    # Get parameters from the request
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    # Check for missing parameters
    if None in [hostname, fs_port, number, as_ip, as_port]:
        return 'Bad Request', 400

    # Query the Authoritative Server to get the IP address
    as_response = requests.get(f'http://{as_ip}:{as_port}/dns_query?hostname={hostname}')
    
    if as_response.status_code != 200:
        return 'Hostname not found', 404

    fs_ip = as_response.text.strip()  # Extract the IP address
    # Query the Fibonacci Server to get the Fibonacci number
    fs_response = requests.get(f'http://{fs_ip}:{fs_port}/fibonacci?number={number}')

    return fs_response.text, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

