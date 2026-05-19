class ShoppingCart:
    def __init__(self):
        self.cart = {}

        # 功能映射表
        self.actions = {
            "1": self.add_item,
            "2": self.remove_item,
            "3": self.update_item,
            "4": self.view_cart,
            "5": self.exit_program
        }

    # 新增商品
    def add_item(self):
        name = input("商品名稱：").strip()
        qty = int(input("數量："))

        self.cart[name] = self.cart.get(name, 0) + qty

        print(f"已新增 {name} x {qty}")

    # 刪除商品
    def remove_item(self):
        name = input("要刪除的商品：").strip()

        if self.cart.pop(name, None):
            print(f"{name} 已刪除")
        else:
            print("商品不存在")

    # 修改商品
    def update_item(self):
        name = input("要修改的商品：").strip()

        if name not in self.cart:
            print("商品不存在")
            return

        qty = int(input("新的數量："))

        if qty <= 0:
            self.cart.pop(name)
            print(f"{name} 已移除")
        else:
            self.cart[name] = qty
            print(f"{name} 更新為 {qty}")

    # 查看購物車
    def view_cart(self):
        if not self.cart:
            print("購物車是空的")
            return

        print("\n===== 購物車內容 =====")

        for idx, (name, qty) in enumerate(self.cart.items(), start=1):
            print(f"{idx}. {name} x {qty}")

    # 離開系統
    def exit_program(self):
        print("感謝使用，再見！")
        exit()

    # 顯示選單
    def show_menu(self):
        print("""
======== 購物車 ========
1. 新增商品
2. 刪除商品
3. 修改商品
4. 查看購物車
5. 離開
""")

    # 主程式
    def run(self):
        while True:
            self.show_menu()

            choice = input("請選擇功能：").strip()

            # 從映射表取出對應函式
            action = self.actions.get(choice)

            if action:
                action()
            else:
                print("無效選項")


# 執行
if __name__ == "__main__":
    app = ShoppingCart()
    app.run()