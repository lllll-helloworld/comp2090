# main.py
# main.py
import time
from modules import Comodity, Order
from structure import OrderPriorityQueue

class SmartShopSystem:
    def __init__(self):
        self.queue = OrderPriorityQueue() # 使用 structure.py 中的类
        self.last_drink_name = None       # 修改：记录上一杯的“名字”，因为现在类都是 Comodity

    def add_order(self, order):
        # 对应 structure.py 中的方法名 push_order
        self.queue.push_order(order)

    def process_orders(self):
        print("\n--- 开始批量制作饮品 (爆单处理模式) ---")
        
        total_time_spent = 0
        
        while not self.queue.is_empty():
            # 1. 从堆顶取出最紧急的订单
            # 对应 structure.py 中的方法名 pop_order
            current_order = self.queue.pop_order()
            
            # 对应 modules.py 中的属性名 Comodity (注意大写 C)
            current_drink = current_order.Comodity 
            
            # 2. 计算制作时间 
            # (注意：modules.py 计算的是单杯时间，这里乘以 quantity 数量)
            unit_time = current_drink.calculate_time()
            total_prep_time = unit_time * current_order.quantity
            
            # 3. 模拟上下文切换 (Context Switch) 成本优化
            # 逻辑修正：因为现在只有 Comodity 一个类，我们通过比较“饮品名字”来判断是否要洗杯子
            switch_cost = 0
            current_name = current_drink.getComodity_Name()
            
            # 如果上一杯的名字存在，且和这一杯不同，则需要清洗
            if self.last_drink_name is not None and current_name != self.last_drink_name:
                print(f"   [操作] 饮品变更 (从 {self.last_drink_name} 换到 {current_name}) -> 清洗雪克杯... +10秒")
                switch_cost = 10
            
            real_time = total_prep_time + switch_cost
            total_time_spent += real_time
            
            # 模拟制作过程
            print(f"正在制作: 订单ID {current_order.Order_ID} - {current_name} x{current_order.quantity}")
            print(f"   -> 预计耗时: {real_time}秒 (制作: {total_prep_time}s + 切换: {switch_cost}s)")
            
            # 更新状态
            self.last_drink_name = current_name
            
        print(f"\n--- 所有订单完成，总耗时: {total_time_spent} 秒 ---")

# --- 模拟运行脚本 ---
if __name__ == "__main__":
    shop = SmartShopSystem()

    print("模拟：高峰期订单涌入...")
    
    # 1. 先创建商品对象 (Comodity)
    # 参数: name, size, toppings list
    bubble_tea = Comodity("珍珠奶茶", "L", ["珍珠"])
    grape_tea = Comodity("多肉葡萄", "L", []) # 没有 topping 传空列表
    coconut_tea = Comodity("椰果奶茶", "M", ["椰果"])
    orange_tea = Comodity("霸气橙子", "L", [])

    # 2. 创建订单对象 (Order)
    # 参数: Order_ID, Comodity对象, is_vip, quantity
    
    # 普通订单 101: 珍珠奶茶
    o1 = Order(101, bubble_tea, is_vip=False, quantity=1)
    
    # 普通订单 102: 多肉葡萄
    o2 = Order(102, grape_tea, is_vip=False, quantity=1)
    
    # 普通订单 103: 椰果奶茶 (这个和珍珠奶茶虽然不同，但如果排在葡萄后面也要洗杯子)
    o3 = Order(103, coconut_tea, is_vip=False, quantity=1)
    
    # VIP 订单 999: 霸气橙子 (插队)
    o4 = Order(999, orange_tea, is_vip=True, quantity=2)

    # 3. 加入系统 (注意 structure.py 的 print 可能会报错，见下方警告)
    shop.add_order(o1)
    shop.add_order(o2)
    shop.add_order(o3)
    shop.add_order(o4) 

    # 4. 开始调度
    shop.process_orders()