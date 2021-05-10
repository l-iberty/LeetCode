## 工具函数
- 求序列最值： `std::min_element`, `std::max_element`
- 序列求和：`std::accumulate`

## `decltype`和lambda
`std::priority_queue`自定义谓词（比较函数）：
```cpp
auto cmp = [](int left, int right) { return (left ^ 1) < (right ^ 1); };
std::priority_queue<int, std::vector<int>, decltype(cmp)> q3(cmp);
```