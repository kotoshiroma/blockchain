from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()

### API ここから ###
@app.route('/', methods=['GET'])
def hello():
  return 'hello'

@app.route('/transactions/new', methods=['POST'])
def new_transactions():
  req_vals = request.get_json()
  required = ['sender', 'recipient', 'amount']
  for key in required:
    if not key in req_vals.keys():
      return "Missing values¥n", 400

@app.route('/mine', methods=['GET'])
def mine():
  pass

@app.route('/chain', methods=['GET'])
def full_chain():
  # return 'chain'
  response = {
    'chain': blockchain.chain,
    'length': len(blockchain.chain)
  }

  return jsonify(response), 200

### API ここまで ###

if __name__ == '__main__':
  app.run(host='localhost', port=5000)