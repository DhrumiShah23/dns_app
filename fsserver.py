from flask import Flask, request, jsonify

app = Flask(__name)

# Dictionary to store hostname-to-IP mappings
hostname_to_ip = {}

@app.route('/register', methods=['PUT'])
def register_server():
    data = request.get_json()
    hostname = data['hostname']
    ip = data['ip']
    as_ip = data['as_ip']
    as_port = data['as_port']

    # Store the hostname and AS details (You can modify this to register with the AS)
    hostname_to_ip[hostname] = {'ip': ip, 'as_ip': as_ip, 'as_port': as_port}

    # You can add code here to register with the Authoritative Server

    return 'Registration successful', 201

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    number = request.args.get('number')

    try:
        number = int(number)
        # Implement Fibonacci computation here
        result = compute_fibonacci(number)
        return str(result), 200
    except ValueError:
        return 'Bad Request', 400

def compute_fibonacci(n):
    # Implement the Fibonacci computation logic here
    # ...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
