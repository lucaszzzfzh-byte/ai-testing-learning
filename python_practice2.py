import json
class Person:
    pass

p = Person()
p.name = "张三"

data = {"person": p.__dict__}
json.dumps(data, ensure_ascii=False, indent=2)
print(json.dumps(data, ensure_ascii=False, indent=2))