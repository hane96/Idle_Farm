# ui.py
import tkinter as tk
from tkinter import messagebox
import threading
import time
from item import item_catalog 
from shop import purchase_item 

def open_shop(state):
    shop_window = tk.Toplevel()
    shop_window.title("商店")

    row = 0
    for item_name, item_obj in item_catalog.items(): #shop list
        item_text = f"{item_obj.name} - {item_obj.description} 💰{item_obj.cost}"
        label = tk.Label(shop_window, text=item_text, anchor="w")
        label.grid(row=row, column=0, sticky="w", padx=10, pady=2)
        row += 1

    entry_label = tk.Label(shop_window, text="輸入要購買的道具：") 
    entry_label.grid(row=row, column=0, padx=10, pady=(10, 2), sticky="w")

    entry = tk.Entry(shop_window)
    entry.grid(row=row + 1, column=0, padx=10, pady=2, sticky="w")

    def handle_purchase():
        item_name = entry.get()
        if not item_name:
            messagebox.showwarning("輸入錯誤")
            return

        prev_resources = state.resources
        prev_items = list(state.item)

        purchase_item(state, item_name)

        if item_name in state.item or item_name in prev_items:
            messagebox.showinfo("購買成功", f"你購買了：{item_name}")
        elif state.resources == prev_resources:
            messagebox.showinfo("購買失敗", f"資源不足或道具不存在")

    purchase_button = tk.Button(shop_window, text="購買", command=handle_purchase)
    purchase_button.grid(row=row + 2, column=0, padx=10, pady=5, sticky="w")


def start_ui(state, apply_passive_items):
    def update_status():
        resources_label.config(text=f"資源：{round(state.resources, 1)}")
        items_label.config(
            text="道具：" + (", ".join([f"{item.name} x{item.amount}" for item in state.item]) if state.item else "無")
            )

        root.after(500, update_status)  # refresh window

    def add_resource():
        state.resources += 1
        state.save()

    def passive_loop():
        while True:
            total = sum( (item.passive_rate*item.amount) for item in state.item)
            state.resources += total
            state.save()
            time.sleep(1)
        
    def reset_game():
        confirm = messagebox.askyesno("重製遊戲", "確定要重製所有進度嗎？")
        if confirm:
            state.resources = 0
            state.item = []
            state.save()
            messagebox.showinfo("", "重置完成")

    

    t = threading.Thread(target=passive_loop, daemon=True) #passive item
    t.start()

    # construct UI
    root = tk.Tk()
    root.title("Idle Farm")
    root.geometry("300x200")

    resources_label = tk.Label(root, text="")
    resources_label.pack(pady=10)

    items_label = tk.Label(root, text="")
    items_label.pack(pady=5)

    collect_btn = tk.Button(root, text=" 點擊獲得資源", command=add_resource)
    collect_btn.pack(pady=5)

    shop_btn = tk.Button(root, text=" 開啟商店", command=lambda: open_shop(state))
    shop_btn.pack(pady=5)

    reset_btn = tk.Button(root, text="重製遊戲", command=reset_game)
    reset_btn.pack(pady=5)


    update_status()
    root.mainloop()
