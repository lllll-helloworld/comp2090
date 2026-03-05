sorry for changing the topic

# Sales Statistics and Top-K System

A Python-based application designed to efficiently calculate and manage the top *K* performing items in a dataset. This project features a custom-built Heap data structure and is specifically tailored to analyze product sales data to find the highest-selling products.

---

## 📁 Project Structure

* **`heap.py`**: Contains the `heap_object` class. This is a custom Max-Heap implementation that provides foundational tree operations like `insert`, `sift_up`, `sift_down`, and `pop_out`.
* **`k_top_calculator.py`**: Contains the `TopKCalculator` base class and the `calculator` subclass. It uses the `heap_object` to maintain the top *K* elements. *Note: It cleverly negates the data upon insertion to simulate a Min-Heap using the Max-Heap core, which is a standard algorithm for keeping the largest K elements.*
* **`product.py`**: Defines the `PRODUCT` data model. It stores essential product attributes including name, price, score, total sales, and product type.
* **`sales_statistics_system.py`**: The main driver class `SalesStatisticsSystem`. It aggregates products and uses the `calculator` to execute a Top-10 sales analysis (`execute_top_k_analysis`).
* **`test.py`**: A simple testing script to verify the insertion and extraction logic of the `heap_object`.

---

## 🚀 How It Works

1.  **Data Modeling**: Products are instantiated using the `PRODUCT` class.
2.  **Heap Management**: The Top-K Calculator maintains a heap of exactly *K* size. 
3.  **Algorithmic Efficiency**: When calculating the Top K sales:
    * If the heap has less than *K* items, it inserts the new sales figure.
    * If the heap is full, it compares the new sales figure against the smallest value in the current Top-K pool (the root of the simulated min-heap). 
    * If the new value is larger, the smallest value is popped out and the new sales figure is inserted, maintaining an optimal time complexity.

---

## 🛠️ Usage

To test the core heap functionality, run the test script from your terminal:

```bash
python test.py