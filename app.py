from flask import Flask, jsonify
from flask_cors import CORS
import os
import pymysql

app = Flask(__name__)
CORS(app)

def get_db_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER', 'admin'),
            password=os.getenv('DB_PASSWORD', ''),
            database=os.getenv('DB_NAME', 'bankingapp'),
            connect_timeout=5
        )
        return connection
    except Exception as e:
        return None

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "faustina-banking-backend",
        "version": "1.0.0"
    }), 200

@app.route('/api/status', methods=['GET'])
def status():
    db_status = "connected"
    conn = get_db_connection()
    if conn is None:
        db_status = "unavailable"
    else:
        conn.close()

    return jsonify({
        "api": "running",
        "database": db_status,
        "cloud": "AWS EKS",
        "infrastructure": "Terraform",
        "cicd": "GitHub Actions",
        "gitops": "Argo CD"
    }), 200

@app.route('/api/accounts', methods=['GET'])
def accounts():
    return jsonify({
        "accounts": [
            {
                "id": "ACC001",
                "name": "Faustina Nwokolo",
                "type": "Savings",
                "balance": 250000.00,
                "currency": "NGN",
                "status": "Active"
            },
            {
                "id": "ACC002",
                "name": "Moniepoint Demo",
                "type": "Current",
                "balance": 1500000.00,
                "currency": "NGN",
                "status": "Active"
            }
        ]
    }), 200

@app.route('/api/transactions', methods=['GET'])
def transactions():
    return jsonify({
        "transactions": [
            {
                "id": "TXN001",
                "type": "Credit",
                "amount": 50000.00,
                "description": "Salary Payment",
                "date": "2026-04-03",
                "status": "Completed"
            },
            {
                "id": "TXN002",
                "type": "Debit",
                "amount": 15000.00,
                "description": "Transfer",
                "date": "2026-04-03",
                "status": "Completed"
            }
        ]
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('APP_PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)