
from openai import OpenAI


client = OpenAI(api_key='')

COMPLETION_MODEL = "gpt-4-turbo-preview"

def get_desc(repo):
    for i in range(3):
        try:
            completions = client.chat.completions.create(model=COMPLETION_MODEL, messages=[
                {"role": "system", "content": f"github项目 {repo} 是干嘛的，用30个字概括一下，用中文概括，要求格式：{repo}..."}], timeout=5)
            message = completions.choices[0].message.content
            # 判断 message 宝不包含 "截至我"
            if not "截至我" in message:
                return message
            completions = client.chat.completions.create(model=COMPLETION_MODEL, messages=[
                {"role": "system", "content": f"请实时联网查询，github项目 {repo} 是干嘛的，用30个字概括一下，用中文概括，要求格式：{repo}..."}], timeout=5)
            message = completions.choices[0].message.content
            return message
        except:
            continue
    return ""

