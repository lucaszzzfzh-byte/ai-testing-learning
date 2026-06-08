import json
nums = [3, 1, 4, 1, 5, 6, 2, 4, 7, 5, 9, 19,78]
print(nums)             # [3, 1, 4, 1, 5, 9]

nums.sort()              # 原地排序，nums 变成 [1, 1, 3, 4, 5, 9]
# vs
new = sorted(nums)       # 原列表不动，new 是排好序的副本对字典列表排序——用 key 参数指定按什么排：
print(new)              # [1, 1, 3, 4, 5, 9]\

nums = [78, 91, 666, 21, 512, 922, 123, 456, 789, 321]

# sorted() 返回新列表，不碰原数据
new = sorted(nums)
print("原始:", nums)   # [78, 91, 666, 21, 512, 922, 123, 456, 789, 321]  没变
print("排序:", new)    # [21, 78, 91, 123, 321, 456, 512, 666, 789, 922]  排好的

# sort() 直接改原数据
nums.sort()
print("sort后:", nums) # [1, 1, 3, 4, 5, 9]  没了原始顺序

cases = [
    {"id": "TC-003", "priority": "高"},
    {"id": "TC-001", "priority": "中"},
    {"id": "TC-002", "priority": "低"},
]

# 按 id 排序
cases.sort(key=lambda c: c["id"])
# 结果：TC-001, TC-002, TC-003

# 按 priority，自定义顺序
order = {"高": 1, "中": 2, "低": 3}
cases.sort(key=lambda c: order[c["priority"]])
print(json.dumps(cases, ensure_ascii=False, indent=2))

with open("test_cases.json", "w", encoding="utf-8") as f:
    json.dump(cases, f, ensure_ascii=False, indent=2)

with open("test_cases.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)