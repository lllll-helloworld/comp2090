import matplotlib.pyplot as plt
import time
import heapq
import random

# --- 1. 你的堆排序算法 (Min-Heap) ---
def test_heap_speed(n):
    data = list(range(n))
    random.shuffle(data)
    
    start = time.time()
    heap = []
    # 模拟入队
    for item in data:
        heapq.heappush(heap, item)
    # 模拟出队
    while heap:
        heapq.heappop(heap)
    return time.time() - start

# --- 2. 普通列表算法 (List Sort) ---
def test_list_speed(n):
    data = list(range(n))
    random.shuffle(data)
    
    start = time.time()
    lst = []
    # 模拟入队
    for item in data:
        lst.append(item)
    # 模拟每次取最优先（必须排序）
    # 这里模拟最坏情况：每次取都要 sort，或者插入时保持有序
    # 为了演示差异，我们简化为只 sort 一次 (即便是这样，量大时也慢)
    lst.sort() 
    while lst:
        lst.pop(0)
    return time.time() - start

# --- 3. 绘图主程序 ---
def plot_performance_comparison():
    # 测试规模：从 1000 单 到 50000 单
    x_values = [1000, 5000, 10000, 20000, 40000, 50000]
    heap_times = []
    list_times = []
    
    print("正在进行性能测试，请稍候...")
    
    for n in x_values:
        t_heap = test_heap_speed(n)
        t_list = test_list_speed(n)
        
        heap_times.append(t_heap)
        list_times.append(t_list)
        print(f"规模 {n}: Heap={t_heap:.4f}s, List={t_list:.4f}s")

    # 开始绘图
    plt.figure(figsize=(10, 6))
    
    plt.plot(x_values, list_times, marker='o', label='普通列表 (List)', color='orange', linestyle='--')
    plt.plot(x_values, heap_times, marker='s', label='最小堆 (Min-Heap - 你的算法)', color='green', linewidth=2)
    
    plt.title('算法性能对比：爆单场景下的处理耗时', fontsize=14)
    plt.xlabel('订单数量 (N)', fontsize=12)
    plt.ylabel('处理耗时 (秒)', fontsize=12)
    plt.legend()
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    plot_performance_comparison()