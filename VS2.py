import matplotlib.pyplot as plt
import matplotlib.animation as animation
import heapq
import random
import time

# --- 1. 简化的模型 (为了动画独立运行) ---
class Order:
    def __init__(self, oid, name, priority):
        self.oid = oid
        self.name = name
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority

class AnimatedShop:
    def __init__(self):
        self.queue = [] # 堆
        self.history = [] # 用于记录每一步的状态 (快照)
        self.current_order = None
        self.time_step = 0

    def add_order(self, order):
        heapq.heappush(self.queue, order)
        self.snapshot(f"新订单入队: {order.name} (Priority={order.priority})")

    def pop_order(self):
        if not self.queue:
            self.snapshot("队列为空，等待中...")
            return None
        
        order = heapq.heappop(self.queue)
        self.current_order = order
        self.snapshot(f"正在制作: {order.name}")
        return order

    def snapshot(self, action_desc):
        # 记录当前堆的状态，用于画图
        # 我们复制一份列表，并排序(为了展示堆的层级或简单排序)
        queue_state = sorted(self.queue, key=lambda x: x.priority) 
        self.history.append({
            'time': self.time_step,
            'queue': queue_state, # 当前排队的人
            'action': action_desc,
            'current': self.current_order
        })
        self.time_step += 1

# --- 2. 模拟全过程 ---
def run_simulation():
    shop = AnimatedShop()
    
    # 初始订单
    shop.add_order(Order(101, "A:珍珠奶茶", 50))
    shop.add_order(Order(102, "B:多肉葡萄", 45))
    shop.add_order(Order(103, "C:纯牛奶", 60))
    
    # 开始处理一个
    shop.pop_order()
    
    # 突然来了个 VIP (优先级极低=极高优先)
    shop.add_order(Order(999, "VIP:霸气橙子", 10)) 
    
    # 又来个普通单
    shop.add_order(Order(104, "D:冰淇淋", 48))
    
    # 继续处理
    shop.pop_order() # 应该是 VIP
    shop.pop_order() # 应该是 B
    shop.pop_order() # 应该是 D
    shop.pop_order() # 应该是 A (如果不按顺序，看优先级)
    
    return shop.history

# --- 3. 制作动画 ---
def animate_schedule():
    history = run_simulation()
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [3, 1]})
    plt.subplots_adjust(hspace=0.5)

    def update(frame_idx):
        ax1.clear()
        ax2.clear()
        
        state = history[frame_idx]
        current_queue = state['queue']
        
        # --- 上半部分：排队状态 (柱状图) ---
        if current_queue:
            names = [o.name for o in current_queue]
            priorities = [o.priority for o in current_queue]
            colors = ['red' if 'VIP' in n else 'skyblue' for n in names]
            
            bars = ax1.bar(names, priorities, color=colors)
            ax1.set_ylim(0, 100)
            ax1.set_title(f"步骤 {frame_idx}: 实时等待队列 (Min-Heap)", fontsize=12)
            ax1.set_ylabel("优先级分数 (越低越急)")
            
            # 在柱子上标数字
            for bar, p in zip(bars, priorities):
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height,
                        f'{p}', ha='center', va='bottom')
        else:
            ax1.text(0.5, 0.5, "队列为空", ha='center', va='center', fontsize=15)
            ax1.set_title(f"步骤 {frame_idx}: 实时等待队列")

        # --- 下半部分：当前状态 (文字) ---
        ax2.axis('off') # 不显示坐标轴
        status_text = f"当前操作: {state['action']}\n"
        if state['current']:
            status_text += f"\n[ 正在制作 >>> {state['current'].name} ]"
        
        ax2.text(0.5, 0.5, status_text, ha='center', va='center', 
                 fontsize=14, color='darkblue', 
                 bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=1'))

    # 创建动画
    ani = animation.FuncAnimation(fig, update, frames=len(history), 
                                  interval=1500, repeat=True) # interval=1500 表示每1.5秒换一步
    
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial'] # 解决中文显示
    plt.rcParams['axes.unicode_minus'] = False
    
    plt.show()

if __name__ == "__main__":
    animate_schedule()