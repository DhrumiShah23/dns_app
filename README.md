# FiboDNS: Distributed Microservices with DNS Lookup & Fibonacci Computation

This project simulates a distributed microservice architecture using Flask-based Python servers. It demonstrates how service discovery and communication can happen in a simple networked environment. It’s structured into three main components:

- **AS (Authoritative Server):** Acts like a DNS server to register and resolve hostnames.
- **FS (Fibonacci Server):** Computes Fibonacci numbers.
- **US (User Server):** Takes user requests, queries AS for service resolution, and communicates with FS to fetch results.

---

## 🏗️ Architecture

User Request
|
v
User Server (US)
|
v
Authoritative Server (AS) <--- FS registered here
|
v
FS IP returned
|
v
Fibonacci Server (FS) -> Computes Fibonacci number

yaml
Copy
Edit

---

## 🧰 Requirements

- Python 3.7 or higher
- Flask
- `requests` library (only for US)

Install using:

```bash
pip install flask requests
🚀 How to Run
Step 1: Run the Authoritative Server (AS)

bash
Copy
Edit
python asserver.py
# Runs on http://localhost:53533
Step 2: Run the Fibonacci Server (FS)

bash
Copy
Edit
python fsserver.py
# Runs on http://localhost:9090
Step 3: Run the User Server (US)

bash
Copy
Edit
python usserver.py
# Runs on http://localhost:8080
📡 API Endpoints
🧾 AS Server (asserver.py)
PUT /register
Registers hostname and IP mapping
Body Example:

json
Copy
Edit
{
  "hostname": "fibonacci.com",
  "ip": "127.0.0.1",
  "as_ip": "127.0.0.1",
  "as_port": "53533"
}
GET /dns_query?hostname=fibonacci.com
Returns A record with IP if registered

🔢 FS Server (fsserver.py)
GET /fibonacci?number=5
Returns 5th Fibonacci number

🌐 US Server (usserver.py)
GET /fibonacci?hostname=fibonacci.com&fs_port=9090&number=7&as_ip=127.0.0.1&as_port=53533
Resolves hostname via AS and gets Fibonacci result from FS

🔍 Example
bash
Copy
Edit
# Register FS to AS
curl -X PUT http://127.0.0.1:53533/register \
-H "Content-Type: application/json" \
-d '{"hostname":"fibonacci.com", "ip":"127.0.0.1", "as_ip":"127.0.0.1", "as_port":"53533"}'

# Get 7th Fibonacci number via User Server
curl "http://127.0.0.1:8080/fibonacci?hostname=fibonacci.com&fs_port=9090&number=7&as_ip=127.0.0.1&as_port=53533"
💡 Notes
This project demonstrates basic microservice communication and service discovery.

DNS and registry simulation is kept simple using dictionaries.

Could be extended to use a database, Docker, or orchestrated via Kubernetes.

🧠 Created by
Dhrumi Shah
Passionate about simplifying complexity with code and building systems that talk to each other like a dream.
