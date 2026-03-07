from k_top_calculator import calculator
from product import PRODUCT

def test_number_top_k():
    print("=== 测试 1: 寻找数字流中的 Top K ===")
    k = 3
    # 初始化你的 calculator
    calc = calculator(k)
    
    # 模拟输入一组数据流
    data_stream = [15, 8, 22, 5, 40, 12, 50]
    print(f"输入数据流: {data_stream}")
    print(f"正在计算 Top {k} ...")
    
    # 将数据逐一送入 calculator
    for num in data_stream:
        calc.caculate_if_insert_KTOP(num)
        
    # 获取结果
    top_k = calc.get_KTOP()
    print(f"提取结果: {top_k}\n")


def test_product_top_k():
    print("=== 测试 2: 寻找产品销量 Top K ===")
    k = 2
    calc = calculator(k)
    
    # 实例化几个 PRODUCT 对象并设置名字和销量
    p1 = PRODUCT("苹果")
    p1.set_sales(100)
    
    p2 = PRODUCT("香蕉")
    p2.set_sales(50)
    
    p3 = PRODUCT("橘子")
    p3.set_sales(200)
    
    p4 = PRODUCT("西瓜")
    p4.set_sales(150)

    products = [p1, p2, p3, p4]
    
    print("输入产品清单 (名称: 销量):")
    for p in products:
        print(f" {p.get_name()}: {p.get_sales()}")
        # 把销售量 (Sales) 送入 calculator 计算
        calc.caculate_if_insert_KTOP(p.get_sales())

    # 获取结果
    top_k_sales = calc.get_KTOP()
    print(f"提取 Top {k} 的销量结果: {top_k_sales}\n")

if __name__ == "__main__":
    test_number_top_k()
    test_product_top_k()