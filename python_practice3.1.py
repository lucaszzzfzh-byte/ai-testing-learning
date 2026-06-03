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
    # 测试
English1, Chinese1 = check_score(50)   # 两个值分别接收
print(English1)
print(Chinese1)
English2, Chinese2 = check_score(1)
print(English2)
print(Chinese2)
English3, Chinese3 = check_score(-1)
print(English3)
print(Chinese3)
English4, Chinese4 = check_score("abc")
print(English4)
print(Chinese4)
def greet(name, greeting="你好"):    # greeting有默认值
    return f"{greeting}，{name}"

print(greet("樊泽豪"))              # 不传第二个 → 你好，樊泽豪
print(greet("樊泽豪", "晚上好"))     # 传了就用传的 → 晚上好，樊泽豪
def classify_score(score):
    if score < 0 or score > 100:
        return False, "无效"
    return True, "有效"

English, Chinese = classify_score(50)   # 两个值分别接收
print(English)  # True
print(Chinese)  # 有效
