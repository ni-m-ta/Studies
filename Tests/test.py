import requests
import csv
import json

API_KEY = 'KRbWrSFUyrk0LwaQEcsglL01mxaTq4f7U90KtnZclSUUT50LGxWm0AKetwdVcrmk'
SPACE_KEY = 'devlab'
PROJECT_ID = '1073983187'

# MSP_operation: 1073943423
# DXC Clerk: 1073983187

BASE_URL = f"https://{SPACE_KEY}.backlog.jp/api/v2"

def get_id(url):
    params = {
        'apiKey': API_KEY,
    }

    r = requests.get(url, params=params)
    r.raise_for_status()
    return json.loads(r.text)

# csvのタイトル
output = {}

print('・issueTypeId(課題の種別のID)用')
#  種別一覧の取得
#  https://developer.nulab.com/ja/docs/backlog/api/2/get-issue-type-list/#
#  /api/v2/projects/:projectIdOrKey/issueTypes 
datas = get_id(f"{BASE_URL}/projects/{PROJECT_ID}/issueTypes")
output['issueTypeId'] = {}
for data in datas:
    output['issueTypeId'][data['name']] = data['id']
    print(f"{data['id']}:{data['name']}")

print('・assigneeId(課題の担当者のID)用')
#  プロジェクトユーザー一覧の取得
#  https://developer.nulab.com/ja/docs/backlog/api/2/get-project-user-list/#
#  /api/v2/projects/:projectIdOrKey/users
datas = get_id(f"{BASE_URL}/projects/{PROJECT_ID}/users")
output['assigneeId'] = {}
for data in datas:
    output['assigneeId'][data['name']] = data['id']
    print(f"{data['id']}:{data['name']}")

print('・categoryId(課題のカテゴリーのID)用')
#  カテゴリー一覧の取得
#  https://developer.nulab.com/ja/docs/backlog/api/2/get-category-list/#
#  /api/v2/projects/:projectIdOrKey/categories 
datas = get_id(f"{BASE_URL}/projects/{PROJECT_ID}/categories")
output['categoryId[]'] = {}
for data in datas:
    output['categoryId[]'][data['name']] = data['id']
    print(f"{data['id']}:{data['name']}")

print('・versionId(課題の発生バージョンのID)、milestoneId(課題のマイルストーンのID)用')
#  バージョン(マイルストーン)一覧の取得
#  https://developer.nulab.com/ja/docs/backlog/api/2/get-version-milestone-list/#
#  /api/v2/projects/:projectIdOrKey/versions
datas = get_id(f"{BASE_URL}/projects/{PROJECT_ID}/versions")
output['versionId'] = {}
output['milestoneId'] = {}
for data in datas:
    output['versionId'][data['name']] = data['id']
    output['milestoneId'][data['name']] = data['id']
    print(f"{data['id']}:{data['name']}")

print('・priorityId(課題の優先度のID)用')
#  優先度一覧の取得
#  https://developer.nulab.com/ja/docs/backlog/api/2/get-priority-list/#
#  /api/v2/priorities 
datas = get_id(f"{BASE_URL}/priorities")
output['priorityId'] = {}
for data in datas:
    output['priorityId'][data['name']] = data['id']
    print(f"{data['id']}:{data['name']}")

# customField_{id}(カスタム属性の値)用
#  カスタム属性一覧の取得
#  https://developer.nulab.com/ja/docs/backlog/api/2/get-custom-field-list/#
#  /api/v2/projects/:projectIdOrKey/customFields 
datas = get_id(f"{BASE_URL}/projects/{PROJECT_ID}/customFields")
for data in datas:
    print(f"・customField_{data['id']}({data['name']})用")
    output[f"customField_{data['id']}"] = {}

with open('id_list_DXCClerk.json', 'w') as f:
    f.write(json.dumps(output, indent=4, ensure_ascii=False))