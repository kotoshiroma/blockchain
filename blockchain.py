from time import time
import json
import hashlib

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
  return 'hello'

if __name__ == '__main__':
  app.run(host='localhost', port=5000)


class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

    # ジェネシスブロックを作る
    self.new_block(previous_hash=1, proof=100)

  def new_block(self, proof, previous_hash=None):
    # 新しいブロックを作り、チェーンに加える
    block = {
      'index': len(self.chain) + 1,
      'timestamp': time(),
      'transactions': self.current_transactions,
      'proof': proof,
      'previous_hash': previous_hash
    }

    # 現在のトランザクションをリセット（ブロックへのセットが完了したため）
    self.current_transactions = []

    self.chain.append(block)
    return block

  def new_transaction(self, sender, recipient, amount):
    # 新しいトランザクションをリストに加える
    self.current_transactions.append({
      'sender': sender,
      'recipient': recipient,
      'amount': amount
    })

    return self.last_block['index'] + 1 # このトランザクションを含む（はずの？）ブロックのindex

  @staticmethod
  def hash(block):
    # ブロックをハッシュ化する
    block_byte = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_byte).hexdigest()
    
  @property
  def last_block(self):
    # チェーンの最後のブロックを返す
    return self.chain[-1]

  def proof_of_work(self, last_proof):
    proof = 0
    while self.valid_proof(last_proof, proof) is False:
      proof += 1

    return proof

  @staticmethod
  def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[0:4] == "0000" # ハッシュ値の先頭で合致する0の数を変えることで、難易度の調整ができる