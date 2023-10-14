from flask import Flask, request, jsonify

app = Flask(__name)

# Dictionary to store DNS records (for simplicity, you can use an actual database)
dns_records = {}

@app.route('/register', methods=['PUT'])
def register_hostname():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = data['as_port']

    # Store the DNS record in the dictionary
    dns_records[hostname] = {'ip': ip, 'as_ip': as_ip, 'as_port': as_port}

    return 'Registration successful', 201

@app.route('/dns_query', methods=['GET'])
def dns_query():
    hostname = request.args.get('hostname')

    if hostname in dns_records:
        record = dns_records[hostname]
        response = {
            'TYPE': 'A',
            'NAME': hostname,
            'VALUE': record['ip'],
            'TTL': 10
        }
        return jsonify(response), 200
    else:
        return 'Hostname not found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=53533, debug=True)

