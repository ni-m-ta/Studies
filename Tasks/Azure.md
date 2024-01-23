# Overviews
- Make procedures related to data usage more efficient

- logic apps
    - problem: fix parameters
        - words
            - prameters: variables that can be abstracted to use in several actions
        - solution
            - fix json in defaults
    - problem: fix queries for SQL server in windows to ignore 0-length data
        - solution
            - add filtering like `AND LEN(STR) > 0`

- Log Analytics Workspaces
    - VMのログをLogAnalytics WorkSpaceにて収集、保管する手順を記載
        1. Data Collection Endpoints（DCE）の作成
            1. 「Azure Monitor」を開く
            1. 「Settings: Data Collection Endpoints」を開く
            1.  「Create」を押下し、DCEを作成する
            1. 各種設定を行う
                - Endpoint Name: 任意
                - Subscription: 任意
                - Resource Group: 任意
                - Region: ログ取得予定のVMが存在するリージョン
            1. 作成完了
        1. カスタムテーブルの作成
            1. 「Log Analytics Workspace」を作成する
            1. 作成後、「Settings: Tables」を開く
            1. 「Create」のプルダウンより、「New custom log (DCR-Based)」を選択する
                1. 
                - Table Name: 任意
                - Data Collection Endponts: 先ほど作成したDCE
                - Data Collection Rules: 下記手順に従う
                    1.  「Create a new data collection rule」を押下する
                    1. 「Name」に任意のDCR名を入力する
            1. 「Next」を押下する
            1. ログが記載されたJSONファイルをアップロードする
                1. 取得対象のログを用意する
                    ```powershell 
                    type=SYSCALL msg=audit(1364481363.243:24287): arch=c000003e syscall=2 success=no exit=-13 a0=7fffd19c5592 a1=0 a2=7fffd19c4b50 a3=a items=1 ppid=2686 pid=3538 auid=1000 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=pts0 ses=1 comm="cat" exe="/bin/cat" subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key="sshd_config"
                    type=CWD msg=audit(1364481363.243:24287):  cwd="/home/shadowman"
                    type=PATH msg=audit(1364481363.243:24287): item=0 name="/etc/ssh/sshd_config" inode=409248 dev=fd:00 mode=0100600 ouid=0 ogid=0 rdev=00:00 obj=system_u:object_r:etc_t:s0  nametype=NORMAL cap_fp=none cap_fi=none cap_fe=0 cap_fver=0
                    type=PROCTITLE msg=audit(1364481363.243:24287) : proctitle=636174002F6574632F7373682F737368645F636F6E666967    
                    ```
                1. JSON形式にする（Key名は「RawData」とする。大文字小文字の区別あり）
                    ```powershell
                    [
                        {
                            "RawData": "type=SYSCALL msg=audit(1364481363.243:24287): arch=c000003e syscall=2 success=no exit=-13 a0=7fffd19c5592 a1=0 a2=7fffd19c4b50 a3=a items=1 ppid=2686 pid=3538 auid=1000 uid=1000 gid=1000 euid=1000 suid=1000 fsuid=1000 egid=1000 sgid=1000 fsgid=1000 tty=pts0 ses=1 comm='cat' exe='/bin/cat' subj=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023 key='sshd_config'"
                        },
                        {
                            "RawData": "type=CWD msg=audit(1364481363.243:24287):  cwd='/home/shadowman'"
                        },
                        {
                            "RawData": "type=PATH msg=audit(1364481363.243:24287): item=0 name='/etc/ssh/sshd_config' inode=409248 dev=fd:00 mode=0100600 ouid=0 ogid=0 rdev=00:00 obj=system_u:object_r:etc_t:s0  nametype=NORMAL cap_fp=none cap_fi=none cap_fe=0 cap_fver=0"
                        },
                        {
                            "RawData": "type=PROCTITLE msg=audit(1364481363.243:24287) : proctitle=636174002F6574632F7373682F737368645F636F6E666967"
                        }
                    ]
                    ```
            1. 「Transformation editor」を押下する<
            1. 「Run」を押下し、実行する
            1. クエリをコピーし、テキストエディタに貼り付ける(後述の作業で必要)
            1. 「Apply」を押下する
            1. 「Next」を押下する
            1. 「Create」を押下し、作成完了
        1. DCRの設定
            1. 「Azure Monitor」を開く
            1. 「Settings: Data Collection Rules」を開く
            1. 先ほど作成した、DCRを選択する
            1. 「Configuration: Data Sources」を押下する
            1. 「Create」を押下する
            1. 各種設定をする
                - Data Source Type: Custom Text Logs
                - File Pattern: 収集先のログファイルパス
                - Table Name: 先ほど作成したテーブル名 (例: AnyCustomLogName_CL)
                - Transform: テーブル作成時に指定したクエリ(先ほどテキストエディタに貼り付けたクエリのワンライナー) 
                - Target: 先ほど作成したLog Analytics Workspace名<
            1. 「Create」を押下し、作成完了
            1. 「Configuration: Resources」を開く
            1. 「Add」を押下する
            1. ログの取得対象であるVMを選択する
            1. 「Apply」を押下する
            1. 対象VMの「Data collection endpoint」欄のプルダウンから、先ほど作成したDCEを選択する
            1. 「Save」を押下する
                * この操作により、VM側へAzure Monitor Agentがインストールされる。
        - 確認方法
            1. 対象VMに移動する
            1. 「Monitoring: Logs」を押下する
            1. クエリ欄に先ほど作成したテーブル名を入力する
            1. 「Run」を押下し、実行する
        - 特記事項
            - 作業完了後、対象ログが取得できるようになるまで数分程度かかる。最大2時間程度かかる場合があるらしい。
            - 正常に収集されない場合の確認事項
                - DCR上で、紐付けているVMに対してDCEが設定されているか
                - 設定したDCEは、対象VMと同じリージョンにあるか
                - VMのHeartbeatログ(毎分Log Analytics Workspacesに送られるログ)が到達しているか
                    1. 対象VMのLog Analytics Workspacesを開く
                    1. `Heartbeat | top 10 by TimeGenerated`を入力し、実行する
                    1. もし確認できない場合、多くの場合ネットワーク要件が満たされていない


