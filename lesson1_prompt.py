from anthropic import Anthropic

client = Anthropic(
    api_key="sk-000bb38731c04b6e93d4cad104da46d4",
    base_url="https://api.deepseek.com/anthropic"
)

def generate_test_cases(requirement):
    response = client.messages.create(
        model="deepseek-chat",
        max_tokens=2000,
        temperature=0.3,
        thinking={"type": "disabled"},
        system="""你是一个刚入行的测试新手。
请根据用户输入的功能需求，生成结构化的测试用例。
每个测试用例必须包含：用例编号、测试场景、前置条件、操作步骤、预期结果。
输出格式用 Markdown 表格。""",
        messages=[
            {
                "role": "user",
                "content": f"请为以下功能生成测试用例：\n{requirement}"
            }
        ]
    )
    return response.content[0].text

if __name__ == "__main__":
    req = input("请输入功能需求描述：\n> ")
    print("\n正在生成测试用例...\n")
    result = generate_test_cases(req)
    print(result)