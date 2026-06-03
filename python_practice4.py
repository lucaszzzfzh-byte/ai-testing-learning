nums = [10, 20, 30, 40, 50]

print(nums[0:3])   # [10, 20, 30]    索引0到2（不含3）
print(nums[1:4])   # [20, 30, 40]    索引1到3
print(nums[:3])    # [10, 20, 30]    从头开始，0可以省略
print(nums[2:])    # [30, 40, 50]    一直到尾
print(nums[-1])    # 50              倒数第一个
print(nums[-3:])   # [30, 40, 50]    倒数三个

squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)
# squares = [1, 4, 9, 16, 25]
squares1 = [i * i for i in range(1, 6)]
# 结果同样是 [1, 4, 9, 16, 25]
print(squares1)
evens = [i for i in range(1, 11) if i % 2 == 0]
# [2, 4, 6, 8, 10]  — 只要偶数
print(evens)

# 这是一个函数的基本结构（框架，不完整）
def check_score(score):
    """文档字符串（可选）：说明这函数干嘛的"""
    # 处理逻辑
    if not isinstance(score , int):
        return False, "无效等价类(非整数)"
    if score < 0 or score > 100:
        return False, "无效等价类(边界外)"
    if 0 < score < 100:
        return True, "有效等价类(普通有效值)"
    if score == 0 or score == 100:
        return True, "有效等价类(边界值)"

results = [check_score(s) for s in [50, 0, -1, 101, "abc"]]
print(results)


squares2 = [i * 2 for i in range(1, 6)]
print(squares2)

square_dict = {i: i * i for i in range(1, 6)}
print(square_dict)

case = {"编号": "TC-001", "场景": "登录成功", "优先级": "高"}
for k, v in case.items():
    print(f"{k} → {v}")   # 编号 → TC-001 ...
test_methods = { "等价类": "单条件分类", "边界值": "在分类边界上定点", "判定表": "多条件交叉组合", "因果图": "加条件间逻辑约束", "正交实验": "条件太多时用正交表压缩", "状态迁移": "跳出输入思维,测状态流转" }
for 名字, 描述 in test_methods.items():
    print(f"{名字} → {描述}")