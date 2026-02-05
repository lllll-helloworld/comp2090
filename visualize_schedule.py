import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import random

# --- 模拟数据生成 (你也可以从 main.py 导出真实数据) ---
def generate_mock_data():
    # 格式: (订单ID, 饮品名, 开始时间(秒), 持续时间(秒), 是否VIP, 状态)
    data = []
    current_time = 0
    
    # 模拟场景：普通单 -> 普通单 -> VIP插队 -> 切换清洗 -> 普通单
    events = [
        ("101", "珍珠奶茶", 30, False), # 普通
        ("102", "珍珠奶茶", 30, False), # 普通 (同类，不洗)
        ("999", "霸气橙子", 45, True),  # VIP (插队)
        ("SWITCH", "清洗设备", 10, False), # 切换成本
        ("103", "多肉葡萄", 40, False), # 普通
    ]
    
    for oid, name, duration, is_vip in events:
        if oid == "SWITCH":
            color = 'gray'
            label = "清洗/切换"
        elif is_vip:
            color = 'red'
            label = f"VIP订单 {oid}"
        else:
            color = 'skyblue'
            label = f"订单 {oid}"
            
        data.append({
            'Task': label,
            'Start': current_time,
            'Finish': current_time + duration,
            'Color': color,
            'Name': name
        })
        current_time += duration
        
    return data

# --- 绘图函数 ---
def plot_gantt_chart(schedule_data):
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # 设置中文字体 (根据你的系统可能需要调整，这里用默认无衬线字体尝试)
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial'] 
    plt.rcParams['axes.unicode_minus'] = False

    y_pos = 0
    labels = []
    
    for task in schedule_data:
        start = task['Start']
        duration = task['Finish'] - start
        
        # 画条形
        ax.barh(y_pos, duration, left=start, height=0.6, align='center', 
                color=task['Color'], edgecolor='black', alpha=0.8)
        
        # 在条形中间写字
        center = start + duration/2
        ax.text(center, y_pos, f"{task['Name']}\n({duration}s)", 
                ha='center', va='center', color='black', fontsize=9)
        
        labels.append(task['Task'])
        y_pos += 1

    # 美化图表
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels)
    ax.set_xlabel('时间 (秒)')
    ax.set_title('奶茶店智能调度流水线 (Gantt Chart)')
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    
    # 翻转Y轴，让第一个任务在最上面
    ax.invert_yaxis()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    data = generate_mock_data()
    plot_gantt_chart(data)