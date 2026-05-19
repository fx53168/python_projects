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
        price = int(input("價格："))
        qty = int(input("數量："))

        # 商品已存在
        if name in self.cart:

            self.cart[name]["qty"] += qty

            # 更新價格（可選）
            self.cart[name]["price"] = price

        else:
            self.cart[name] = {
                "price": price,
                "qty": qty
            }

        print(f"已新增 {name} : ${price}  {qty}")

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

        print("\n================ 購物車內容 ================")

        # 表頭（統一寬度）
        print(
            f"{'商品名稱':}\t"
            f"{'價格':}\t"
            f"{'數量':}\t"
            f"{'小計':}\t"


        )

        print("-" * 50)

        total = 0

        for name, item in self.cart.items():
            price = item["price"]
            qty = item["qty"]
            subtotal = item["price"] * item["qty"]
            total += subtotal

            print(
                f"{name:}\t"
                f"${price:.2f}\t"
                f"{qty:}\t"
                f"${subtotal:.2f}\t"
            )

        print("-" * 50)
        print(f"{'總金額':}\t${total:.2f}")

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