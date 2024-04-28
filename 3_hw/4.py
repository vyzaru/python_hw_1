class Wallet:
    supported_currencies = ["RUB", "USD", "EUR"]
    payment_system = "SberBank"

    def __init__(self, name: str, currency: str):
        if currency not in self.supported_currencies:
            raise ValueError("Неподдерживаемая валюта")
        self.name = name
        self.currency = currency
        self._balance = 0

    def top_up_balance(self, amount: float):
        if amount < 0:
            raise ValueError("Нельзя пополнить отрицательную сумму")
        self._balance += amount

    def pay(self, amount: float):
        if amount < 0:
            raise ValueError("Нельзя оплатить отрицательную сумму")
        if self._balance < amount:
            raise ValueError("Недостаточно средств на счете")
        self._balance -= amount

    def get_balance_info(self):
        print(f"Баланс кошелька '{self.name}': {self._balance} {self.currency}")

    def delete_account(self):
        print(f"Кошелек '{self.name}' удален")


class CryptoWallet(Wallet):
    supported_currencies = ["BTC", "ETH"]

    def __init__(self, name: str, currency: str, coins: float):
        if currency not in self.supported_currencies:
            raise ValueError("Неподдерживаемая криптовалюта")
        super().__init__(name, currency)
        self.coins = coins

    def get_balance_info(self):
        print(f"На балансе крипто-кошелька '{self.name}': {self.coins} {self.currency}")

    def get_balance_in_usd(self, btc_price: float, eth_price: float):
        if self.currency == "BTC":
            balance_in_usd = self.coins * btc_price
        elif self.currency == "ETH":
            balance_in_usd = self.coins * eth_price
        else:
            raise ValueError("Неподдерживаемая криптовалюта")
        print(f"На балансе крипто-кошелька '{self.name}' в долларах: {balance_in_usd} USD")

wallet1 = Wallet("Мой кошелек", "USD")
wallet1.top_up_balance(100)
wallet1.pay(50)
wallet1.get_balance_info()
wallet1.delete_account()


crypto_wallet1 = CryptoWallet("Мой крипто-кошелек", "BTC", 2)
crypto_wallet1.get_balance_info()

btc_price = 100
eth_price = 20

crypto_wallet1.get_balance_in_usd(btc_price, eth_price)
