class Item:
    def __init__(self, name, description, passive_rate=0.0, cost=0):
        self.name = name
        self.description = description
        self.passive_rate = passive_rate
        self.cost = cost

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "passive_rate": self.passive_rate,
            "cost": self.cost
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["description"],
            data.get("passive_rate", 0.0),
            data.get("cost", 0)
        )

item_catalog = {
    "Auto Generator": Item(
        name="Auto Generator",
        description="每10秒自動產出 0.2 資源",
        passive_rate=0.2,
        cost=20
    ),
    "Mega Generator": Item(
        name="Mega Generator",
        description="每10秒自動產出 0.5 資源",
        passive_rate=0.5,
        cost=50
    ),
}
