# 第一阶段总结：AI测试基础（5.28-5.30）

## Day 1（5.28）— API 调用基础

### 任务
- 配置 DeepSeek API，用 Anthropic SDK 发送请求
- 写 `lesson1_prompt.py`：调用模型生成测试用例

### 踩坑
- 中文逗号 `，` vs 英文逗号 `,` → 语法错误
- `chieos` → `choices`、`__mian__` → `__main__`、`message` → `messages`
- DeepSeek Anthropic 端点 `thinking` 默认开启 → 必须加 `thinking={"type": "disabled"}`
- OpenAI SDK 调 DeepSeek 报 `reasoning_content` 错误 → 改用 Anthropic SDK + `/anthropic` 端点

### 收获
- API Key / base_url / model 三要素配置
- 从报错定位语法问题的能力
- `temperature` 参数含义（0.3=稳定，0.9=创意）

---

## Day 2（5.29）— Python 基础 + Dify 配置

### Python：json.dumps / loads
- dumps = dict → 格式化文本字符串（"门票"）
- loads = 字符串 → 可操作的字典（"拆封回执"）
- sort_keys=True 按 Unicode 码点排序
- datetime / set / 自定义对象 → 三种不可序列化类型的解决方案

### Dify：平台搭建
- 配置 DeepSeek 模型提供商（OpenAI-API-compatible，端点 `https://api.deepseek.com/v1`）
- 搞清楚 Chat Assistant vs Agent vs Chatflow 三种应用类型的区别
- 搭建知识库 + 接入 WebSearch 工具
- 解决 "Model not supported" 报错

---

## Day 3（5.30）— Dify Agent 实操 + GitHub 提交

### 任务
- 创建 Agent 应用「AI测试用例生成助手」
- 编写系统提示词
- 用两条需求（登录功能、购物车功能）测试 Agent 输出
- 截图 + 写文档 + 提交 GitHub

### 测试结果

#### 测试1：用户登录功能
- 输入需求：用户登录功能：输入用户名和密码，点击登录。密码错误3次锁定账号30分钟。
- Agent 返回了 6 条结构化用例（TC-001 ~ TC-006），覆盖正常登录、错误锁定、超时解锁、空输入

#### 测试2：购物车功能
- 输入需求：购物车功能：用户可以添加商品到购物车、修改数量、删除商品、清空购物车
- 输出结果：

![购物车测试](screenshots/dify0.png)

---

## 技能清单（第一阶段结束后）

| 分类 | 掌握的 |
|------|--------|
| API 调用 | Anthropic SDK + DeepSeek 端点，报错排查 |
| Python | json.dumps/loads、dict/list/str 类型区分、for 循环 |
| Dify | 模型配置、Agent 创建、知识库、WebSearch 工具 |
| Git/GitHub | git add / commit / push、仓库管理 |
| 测试思维 | 提示词工程基础（角色设定、输出格式、规则约束） |
