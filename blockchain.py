from time import time
import json
import hashlib

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