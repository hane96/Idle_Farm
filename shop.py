# shop.py
from item import Item, item_catalog

def show_shop(state):
    print("\n🛒 === Shop Menu ===")
    for item_name, item_obj in item_catalog.items():
        print(f"- {item_obj.name}: {item_obj.description} |  Cost: {item_obj.cost}")
    print("Type the item name to purchase it, or 'back' to return.")


def purchase_item(state, item_name):
    item = item_catalog.get(item_name)
    if not item:
        print("❌ 沒有這個商品。")
        return

    cost = getattr(item, "cost", item.cost)  
    if state.resources < cost:
        print(" 資源不足，無法購買。")
        return
    
    for existing_item in state.item:
        if existing_item.name == item.name:
            existing_item.amount += 1
            state.resources -= cost
            return 

    state.resources -= cost
    state.item.append(item)
    state.save()
    print(f"✅ 成功購買：{item.name} - {item.description}")

