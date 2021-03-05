# LCP 27. 黑盒光线反射
来自中文 leetcode [LCP 27. 黑盒光线反射](https://leetcode-cn.com/problems/IQvJ9i/)

思路：找出光线在每个点经一次反射后对应到的点

32 / 39 个通过测试用例

超出时间限制

```cpp
class BlackBox {
 public:
  BlackBox(int n, int m): N(n), M(m) {
    for (int i = 0; i < 2 * (n + m); i++) {
      if (i <= 2 * m) { // i ≤ 2m 范围内
        if (i == 0 || i == m + n) { // 左上和右下, 只有 y=-x 方向
          map2_[i] = 2 * m - i;
        } else if (i == m) { // 右上, 只有 y=x 方向
          map1_[i] = 2 * (m + n) - i;
        } else {
          map1_[i] = 2 * (m + n) - i;
          map2_[i] = 2 * m - i;
        }
      } else { // i > 2m 范围内
        if (i == m + n) { // 右下, 只有 y=-x 方向 (右下角的那个点可能位于 i ≤ 2m 或 i > 2m)
          map2_[i] = 2 * m + 2 * (m + n) - i;
        } else if (i == 2 * m + n) { // 左下, 只有 y=x 方向
          map1_[i] = 2 * (m + n) - i;
        } else {
          map1_[i] = 2 * (m + n) - i;
          map2_[i] = 2 * m + 2 * (m + n) - i;
        }
      }
    }
  }

  int open(int index, int direction) {
    opened_.insert(index);
    for (;;) {
      index = next(index, direction);
      if (opened_.find(index) != opened_.end()) {
        return index;
      }
      // 如果达到顶点则反射的方向不变, 否则改变方向
      if (index != 0 && index != M &&
        index != M + N && index != 2 * M + N) {
        direction = -direction;
      }
    }
    return -1;
  }

  void close(int index) {
    opened_.erase(index);
  }

 private:
  int N, M;
  std::unordered_map<int, int> map1_; // y=x 方向
  std::unordered_map<int, int> map2_; // y=-x 方向
  std::unordered_set<int> opened_;

  int next(int index, int direction) {
    return (direction == 1) ? map1_[index] : map2_[index];
  }
};
```

如果把`std::unordered_map`改成`int`数组，则可以通过 37 / 39 个测试用例：

```cpp
class BlackBox {
 public:
  BlackBox(int n, int m): N(n), M(m) {
    map1_ = new int[2 * (m + n)];
    map2_ = new int[2 * (m + n)];
    opened_ = new char[2 * (m + n)];
    memset(opened_, 0, sizeof(char) * (2 * (m + n)));

    for (int i = 0; i < 2 * (n + m); i++) {
      if (i <= 2 * m) { // i ≤ 2m 范围内
        if (i == 0 || i == m + n) { // 左上和右下, 只有 y=-x 方向
          map2_[i] = 2 * m - i;
        } else if (i == m) { // 右上, 只有 y=x 方向
          map1_[i] = 2 * (m + n) - i;
        } else {
          map1_[i] = 2 * (m + n) - i;
          map2_[i] = 2 * m - i;
        }
      } else { // i > 2m 范围内
        if (i == m + n) { // 右下, 只有 y=-x 方向 (右下角的那个点可能位于 i ≤ 2m 或 i > 2m)
          map2_[i] = 2 * m + 2 * (m + n) - i;
        } else if (i == 2 * m + n) { // 左下, 只有 y=x 方向
          map1_[i] = 2 * (m + n) - i;
        } else {
          map1_[i] = 2 * (m + n) - i;
          map2_[i] = 2 * m + 2 * (m + n) - i;
        }
      }
    }
  }

  ~BlackBox() {
    delete[] map1_;
    delete[] map2_;
    delete[] opened_;
    map1_ = nullptr;
    map2_ = nullptr;
    opened_ = nullptr;
  }

  int open(int index, int direction) {
    opened_[index] = 1;
    for (;;) {
      index = next(index, direction);
      if (opened_[index]) {
        return index;
      }
      // 如果达到顶点则反射的方向不变, 否则改变方向
      if (index != 0 && index != M &&
        index != M + N && index != 2 * M + N) {
        direction = -direction;
      }
    }
    return -1;
  }

  void close(int index) {
    opened_[index] = 0;
  }

 private:
  int N, M;
  int* map1_; // y=x 方向
  int* map2_; // y=-x 方向
  char* opened_;

  int next(int index, int direction) {
    return (direction == 1) ? map1_[index] : map2_[index];
  }
};
```