# 字典和json —— AI API返回的就是这种东西
import json

# 这是一个字典（Python里的数据容器）
test_case = {
    "编号": "TC-001",
    "场景": "正确用户名和密码登录",
    "前置条件": "用户已注册",
    "步骤": ["1. 打开登录页", "2. 输入用户名", "3. 输入密码", "4. 点击登录"],
    "预期结果": "跳转到首页，显示用户名"
}

# 把字典转成 JSON 字符串（API返回的就是这种格式）
json_str = json.dumps(test_case, ensure_ascii=False, indent=2)
print("JSON格式输出：")
print(json_str)

# 从 JSON 字符串转回字典（你处理API返回时要做的）
parsed = json.loads(json_str)
print(f"\n读取第1条用例：{parsed['编号']} - {parsed['场景']}")

# 加这几行，你就能"感觉到"dumps和loads的区别了
print("\n=== 类型对比 ===")
print(f"test_case 的类型：{type(test_case)}")        # 会显示 <class 'dict'>
print(f"json_str 的类型：{type(json_str)}")           # 会显示 <class 'str'>
print(f"parsed 的类型：{type(parsed)}")                # 会显示 <class 'dict'>

print(f"\ntest_case 是字典吗？{isinstance(test_case, dict)}")   # True
print(f"json_str 是字典吗？{isinstance(json_str, dict)}")       # False! 它是字符串
print(f"parsed 是字典吗？{isinstance(parsed, dict)}")           # True