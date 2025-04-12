class Item:
    def __init__(self, name, description, passive_rate=0.0, cost=0, amount=1):
        self.name = name
        self.description = description
        self.passive_rate = passive_rate
        self.cost = cost
        self.amount = amount

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "passive_rate": self.passive_rate,
            "cost": self.cost,
            "amount": self.amount
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["description"],
            data.get("passive_rate", 0.0),
            data.get("cost", 0),
            data.get("amount", 1)
        )

item_catalog = {
    "Farmer 1": Item(
        name="Farmer 1",
        description="每10秒自動產出 0.1 資源",
        passive_rate=0.1,
        cost=20
    ),
    "Farmer 2": Item(
        name="Farmer 2",
        description="每10秒自動產出 0.3 資源",
        passive_rate=0.3,
        cost=50
    ),
    "Farmer 3": Item(
        name="Farmer 3",
        description="每10秒自動產出 1 資源",
        passive_rate=1,
        cost=150
    )
}
