# Sales Statistics and Recommendation System

A Python-based application designed to efficiently calculate and manage the top K performing items in a dataset, alongside user recommendation and statistical analysis tools. This project features a custom-built Heap data structure and is tailored to analyze product sales data and user preferences.

---

## 📁 Project Structure

### Data Structures & Algorithms
* **`heap.py`**: Contains the `heap_object` class. A custom Heap implementation providing foundational tree operations like `insert`, `sift_up`, `sift_down`, and `pop_out`.
* **`k_top_calculator.py`**: Contains the `TopKCalculator` base class and the `calculator` subclass. It leverages the custom heap to maintain the top K elements efficiently from a data stream.
* **`Pearson_Correlation_Coefficient.py`**: Implements the `PCC` class to calculate the Pearson Correlation Coefficient, a statistical tool useful for finding similarities in recommendation engines.

### Core Models
* **`product.py`**: Defines the `PRODUCT` data model, storing essential attributes such as name, price, score, total sales, and product type.
* **`user.py`**: Defines the `user` class, managing basic user credentials (username, password) and maintaining a list of preferred items.

### System Modules
* **`sales_statistics_system.py`**: The main driver class `SalesStatisticsSystem`. It aggregates products and uses the `calculator` to execute Top-K sales analysis (defaulted to Top 10).
* **`recommand_system.py`**: A lightweight `recommondation_system` class that generates item recommendations based on a user's specific preferences.

### Testing
* **`test.py`**: Verifies the insertion and extraction logic of the `heap_object`, as well as the basic calculation flow of the `PCC` module.
* **`test_k_top.py`**: Contains targeted test cases (`test_number_top_k` and `test_product_top_k`) to validate the Top-K logic using both raw number streams and instantiated `PRODUCT` objects.

---

## 🚀 How It Works

1. **Data Modeling**: Users and Products are instantiated using their respective classes, encapsulating state and behavior.
2. **Top-K Heap Management**: The `calculator` maintains a heap bounded to size K. 
    * If the heap is under capacity, new sales figures are inserted directly.
    * If at capacity, it compares incoming data against the existing heap elements, ejecting the smaller values to ensure only the highest K values are retained.
3. **Statistical Analysis**: The PCC module calculates linear correlation between datasets, serving as the mathematical backbone for potential collaborative filtering in the recommendation system.

---

## 🛠️ Usage

To test the core Top-K calculation logic with simulated data streams and product sales, run the provided test script:

```bash
python test_k_top.py