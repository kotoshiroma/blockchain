# class Blockchain(object): # (object)は何なのか？ => pythonの公式ドキュメント（クラス定義）に記載あった
# 基底クラス object を継承
class Blockchain:
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  def new_block(self):
    # 新しいブロックを作り、チェーンに加える
    pass

  def new_transaction(self):
    # 新しいトランザクションをリストに加える
    pass

  @staticmethod
  def hash(block):
    # ブロックをハッシュ化する
    pass

  @property
  def last_block(self):
    # チェーンの最後のブロックを返す
    pass