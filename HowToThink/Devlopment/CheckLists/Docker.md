# Dockerの導入を検討する場合の主なチェックポイント
- そもそもDockerが自社に必要なのか
- 既存の仮想環境における課題は何か
- 既存の仮想環境をコンテナ型の環境に置き換えることが可能か
- 自社へDockerを適用する際の最大の障害は何か
- 現在のシステムのどの部分にDockerを採用するのか
- 物理環境の高可用性に関するSLAをDockerでも実現できそうか

# Docker導入決定後、サーバOS選定における主なチェックポイント
- Dockerを稼働させるOS環境は、コミュニティ版のLinuxで良いか、商用版のLinuxにするべきか
- コミュニティ版OSにする場合、どのディストリビューションを採用するのか
- 商用Linuxの場合、どのディストリビューションを採用するのか
- OSとDockerの保守サポートを同時に受けられるか
- 保守サポートが受けられない場合、問題切り分け作業を自社で行えるか

# サーバOS及びコンテナ専用OSの採用に関する主なチェックポイント
- 使い慣れたLinuxサーバOSからコンテナ専用のアプライアンスの利用に切り替えても良いか
- ホストOS上でサードパーティ性のアプリケーションを稼働させる必要性があるか
- OSとDockerのインstウオールに際し、手順書や人員のスキルセットを確保しているか
- サーバOSの管理は、従来と同等の手法が必要か？新たな管理手法でも問題がないか？
- コンテナはGUIによる管理が必須か？
- 外部ストレージの利用はあるか？
- ハードウェアベンダやミドルウェアベンダが提供する監視エージェント類は必要か？

# Docker Community Edition
## 物理サーバとの兼ね合い
- 物理サーバのCPUに関する留意点
    - CPUコア数に対するコンテナ数の目安はない
    - コンテナに割り当てるCPUの指定が可能
- メモリおよびディスクに関する留意点
    - こんんてな実行時にメモリ容量を指定できるが、アプリケーションごとに最低限必要なメモリ容量の一覧表を作っておくと良い
    - メモリ
        - ホストOS用の容量を考慮
        - 全てのコンテナで稼働するアプリの必要量を考慮
    - ディスクに関する留意点
        - OSとは別の論理vol.
        - 1コンテナの容量を決定
        - 利用人数とアプリを考慮
- DockerホストとしてのOSインストール
    1. 物理サーバーへのOSインストール
    1. ディスクのパーティショニング
    1. パッケージのインストール
    1. OSのアップデート
    1. Dockerのインストール
    1. Dockerのパラメータ設定
    1. Dockerの状態確認
## OS側の設定
- プロキシの設定
    - `vi /etc/dnf/dnf.conf`
- OSのアップデート
    - `dnf update -y`
- セキュリティ設定の確認
    - `systemctl is-active firewalld`
    - `grep ^SELINUX= /etc/sysconfig/selinux`
- カーネルパラメータの設定
    - `echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf`
    - `sysctl --system`
    - `cat /proc/sys/net/ipv4/ip_forward/`
- Rootfulモード
    1. `dnf remove -y podman podman-docker runc`
    1. `dnf remove -y docker,...`
    1. `dnf install -y yum-utils`
    1. `yum-config-manager --add-repo https://download.docker.com/...`
    1. `dnf install -y docker-ce,...`
    1. プロキシサーバの設定
    1. ストレージドライバの設定
        - 通常overlay2
    1. Dockerエンジンの起動
## 各種要素
- Docker Hub レジストリ
    - インターネット経由で、OS環境とアプリケーションを含んだイメージの入手先の一つ
- プライベートレジストリ
    - ローカルで作成、保管したイメージの保管庫
- Docker Image
    - コンテナを作成するための設計書
- Docker Engine
    - OSとアプリケーションのパッケージ化やイメージを使ったコンテナの実行
- Docker Container
    - アプリケーションの実行
    - ホストOS上で複数同時に起動させることができ、ホストOSから見ると分離された名前空間として見える
- Docker Client
    - Docker Daemon の捜査を担う各種コマンド
## 操作
- Docker imageの入手
    - `docker pull {name}:{tag}`
- イメージ一覧表示
    - `docker images`
- コンテナの起動
    - `docker run -it --name {name} {name}:{tag} {commands}`
- コンテナ一覧表示
    - `docker ps -a`
- コンテナのコミット
    - `docker commit {containerID} {name}:{tag}`
- コンテナの起動
    - `docker start {name}`
- コンテナの停止
    - `docker stop {name}`
## ホストOSからコンテナへのディレクトリ提供
- bind mount
    - ホストOSが管理するボリュームとは無関係に、Dockerエンジンが稼働するホストOS上の任意のデバイスファイルやディレクトリをコンテナから参照する
    - 手順
        1. 提供用のディレクトリを作成
        1. 提供用のファイル作成
        1. `docker run -it -name {name} -h {hostname} --mount type=bind,src={host directory path},dst=/root/{target directory path} {name}:{tag}`
- Volumeの提供
    - Dockerエンジンが稼働するホストOSのボリューム(/var/lib/docker/volumes)をコンテナから参照できるようにする
    - 手順
        - `docker run -itd --name {name} -h {hostname} --mount type=volume,src={/var/lib/docker/volumes/はいかのパス},dst={コンテナ内のディレクトリ} {name}:{tag}`
    - 複数コンテナによるデータ用ボリュームの共有
        - `docker run -it -v /data/vol0001 --name {name} -h {hostname} {name}:{tag}`
        - `docker run -it --volumes-from {name} --name {name} -h {hostname} {name}:{tag}`
- データ専用コンテナ
    - アプリは稼働させない
    - 必要最低限の管理コマンド
## 管理
- Docker Imageのインポート
- コンテナのエクスポート
- Docker imageのセーブとロード
- ログ
    - `docker logs -t {name}`
    - ログファイルは`/var/lib/docker/containers/{Container ID}/{ContainerID}-json.log`として保存
    - ログ管理サービス
        - rsyslog
        - rsyslogをインストール
        - `docker run -itd --log-driver=syslog --name {name} -h {hostname} {name}:{tag}`
# Dockerfile
## 基本
- Dockerで定義されている書式に従って記述し、それに基づいてアプリケーションのインストールなどを行い、Dockerイメージの作成を行う
- コンテナがどのようなアプリケーションで構成されているか、誰がメンテナンスの担当者なのか、どういう手順で構築されているのかなどの重要な情報を含んでおり、メンテナンス効率の向上に大きく貢献する
- 流れ
    1. Dockerfileを作成
    1. ビルドして、Docker imageを作成
        - `docker build -f ./Dockerfile -t {name}:{tag} .`
    1. Docker Containerの起動
    1. アプリケーションの動作確認
- Dockerfile
```
FROM {name}:{tag}
RUN dnf install -y httpd
RUN systemctl enable httpd
```
## ホストOSからDockerイメージへのファイルコピー
- Nginx用Dockerイメージの作成
    - Ningxでは、パッケージで用意されたnginx.confファイルがあり、すぐにWebサービスが利用可能だが、バーチャルホストの設定ファイルは一から作成する必要がある
    - バーチャルホストの設定ファイルvhost.confファイルをDockerイメージにコピー
    - ```
        ...
        COPY vhost.conf /etc/nginx/conf.d/
        RUN sed -i '/listen \[\:\:\]\:80/s/^#/g' /etc/nginx/nginx.conf
        RUN systemctl enable nginx
      ```
- Dockerfileにおけるコマンド自動実行
    - ENTRYPOINT
    - コンテナの出力結果をホストOSから参照する
        - `docker run -v /tmp:/var/log {name}:{tag}`
- プロセスがすぐに終了させない方法
    - `tail -f /dev/null`
    - サービスをフォアグラウンドで稼働させる
- CMDとENTRYPOINTの違い
    - ENTRYPOINT
        - `ENTRYPOINT ["/usr/bin/uname"]
            - /usr/bin/unmameを直接実行
            - `/usr/bin/uname`
        - `ENTRYPOINT /usr/bin/uname
            - /usr/bin/unameをシェルで実行
            - `sh -c /usr/bin/uname`
    - CMD
        - `CND ["/usr/bin/uname"]`
            - /usr/bin/unameを直接実行
            - `/usr/bin/uname`
        - `CMD /usr/bin/uname`
            - /usr/bin/unameをシェルで実行
            - `sh -c /usr/bin/uname`
        - `CMD["-a"]`
            - ENTRYPOINTの引数
            - ENTRYPOINTの値 -a
- ONBUILD
    - 通常ベースのDockerイメージを作成し、そのベースのイメージを使って派生したDockerイメージを次々と作成
    - 具体的には、派生版のDockerfileで実行させたいコマンドをベースのDockerfile内のONBUILD命令に記述
        - ベースのDockerfileでは、ONBUILD命令の行を除いた内容でベースのDocker Imageが作成され、派生版のDockerイメージでは、派生版のDockerfileコマンドと、ベースのDockerfile内のONBUILD命令に指定したコマンドを合わせたもので構成される
- Dockerfileにおけるマルチステージビルド
    - マルチステージビルドは、Dockerfileの中に処理対象とするDockerイメージを複数記述し、それらの複数のイメージから生成されたファイルやバイナリを最終的なDockerイメージに埋め込む
    - メリット
        - 開発用のDockerイメージと本番環境用のDockerイメージを1つのDockerfileで記述
        - Dockerイメージのファイルサイズを減らす作業の簡素化
    - `FROM {name}:{tag} AS {name}`
- HEALTHCHECK
    - コンテナ内のサービスの死活監視
    - wgetコマンドによる死活監視
- SHELL命令によるシェルの変更
- RUN命令によるヒアドキュメントの利用
    - ヒアドキュメント
        - Dockerfile内において1つのRUN命令で複数のコマンドを並べて実行したい場合
    - 具体的には、RUN命令に「<<EOF」を付与し、それ以降は結びの「EOF」が出現するまで、Docker Image に対して処理したいLinuxのコマンドを複数行にわたって記述
    - ヒアドキュメントを利用するには、パーサディレクティブを利用
        - パーサディレクティブ
            - `syntax = docker/dockerfile:1`
        - docker buildコマンドがヒアドキュメントの構文を理解するのに必要
    - BuildKitを使ったDockerfileのビルド
        - コンテナイメージのビルド処理の並列実行やCPUアーキテクチャの異なるマルチプラットフォーム向けのイメージの生成などの機能を提供
## Dockerfileの利用方針
- tarアーカイブへの保管
    - 本番システムに適用すべきDockerイメージを生成できたら、その時点でDockerfileとDockerイメージのバックアップを取得する
    - 具体的には、docker saveコマンドを使って対象のDocker Imageを圧縮済みのtarアーカイブ形式で保存する
- 不要なファイルやディレクトリを置かない
    - .dockerignoreの利用
- キャッシュ機能の落とし穴
    - ビルド時に、「--no-cache=true」を付与
- cdコマンドを使わない
    - RUN命令の数を削減する
# ネットワーキング
- 1つのホストOS上で稼働する各Dockerコンテナには固有のイーサネットインターフェイスが存在する
- イーサネットインターフェイスにはIPアドレスが割り当てられる
- 各コンテナにはそのネットワークインtなーフェイスとIPアドレスのみが表示されるため、Dockerエンジンは名前空間のiptablesを操作することによりネットワークを分離
- コンテナ内の各インターフェイスは、Dockerネットワークに接続されたvethインターフェイスに接続
- 外部クライアントがコンテナ内のサービスに到達するにはホストOSの物理NICに割り当てられたIPアドレスは、通常、Dockerネットワークおよびコンテナインターフェイスで使用されているものとは異なるネットワークが割り当てられる
## 複数の物理ホストOSで稼働するコンテナ同士の通信
- weave
    - マルチホストで稼働するコンテナ同士をソフトウェア定義型の仮想ネットワークで通信させる
- etcd
    - OSSのKVSでマルチホスト環境において設定情報などを共有するために利用される
- CNI
    - VXLANなどのオーバレイネットワークを実現するソフトウェアであり、マルチホスト環境におけるコンテナ同士のネットワーク通信を実現
- Swarmモード
    - Dockerエンジンに標準で搭載されているクラスタリング機能
    - docker networkコマンドによるコンテナ用のネットワーク作成機能を併用
    - サードパーティ性のソフトウェアを利用することなく、マルチホストを実現
- TCP/IPを実現
    - ブリッジネットワーク
        - Dockerホストが提供するデフォルトのブリッジインターフェイス
        - Dockerデーモンが稼働する1台のホスト上に稼働している複数のコンテナに適用
        - ブリッジネットワークに接続されているコンテナ同士は、通信を行うことができるが、ブリッジネットワークに接続していないコンテナは隔離される
    - オーバレイネットワーク
        - Dockerホストが提供するデフォルトのブリッジインターフェイスが所属するネットワークとは別に、コンテナ専用の通信ネットワークを形成
        - 複数のDockerホスト上で稼働するコンテナ間で通信を行う場合に利用
    - Macvlanネットワーク
        - Dockerホストの物理NICのサブインターフェイスにMACアドレスとIPアドレスを割り当てることでVLANを形成する
        - ホストOSと同じIP空間にコンテナを所属させたい場合に有用
    - IPvlanネットワーク
        - DockerホストのNICのサブインターフェイスには上位デバイスのMACアドレスを共有し、IPアドレスを割り当てる
        - Dockerホストのオヤインターフェイスで取り扱えるMACアドレスの数に制限がある場合や、IPvlanネットワークが設定されたホストに接続されているネットワークスイッチ側で利用できるMACアドレスが1つしか許可されていない倍などにIPvlanが有用
- 管理ノードと管理対象のノード
- Swarmクラスタにおけるサービス
    - 複製サービス
        - 複数の管理対象ノードに対して、アプリケーションが稼働するコンテナが複製されるタスクを意味する
            - タスク
                - 管理ノードが管理対象ノードに割り当てるスケジューリングの最小単位
        - 管理ノードで稼働するSwarmマネージャがコンテナの複製のタスクをノードにスケジュールする
    - グローバルサービス
        - スケジューラはサービスの配置の制約やリソース要件を満たすノードごとに1つのタスクを配置する
    - docker serviceにより起動したコンテナはSwarmクラスタの管理下に置かれる
        - Swarmクラスタでは起動しているサービスを簡単にスケールできる
    - docker serviceコマンドで配備されたサービスには、仮想IPアドレスが付与されるが、コンテナに割り当てられた実際のIPアドレスは、管理対象ノード上でdocker inspectコマンドで確認できる
- 複数サービスの一括管理
    - docker stack
        - 複数のサービスをグループ化する機能
        - 管理者が複数の異なる種類のコンテナをグループ化したYAML形式の定義ファイルを作成
# 資源管理
## DockerにおけるCPU資源管理
- 1つのCPUコアを複数のコンテナで利用する
- そのCPUを割り当てる時間の割合をコンテナ実行時に指定する
- CPUの負荷テスト
    - openssl
## メモリ容量の制限
- `docker run -m 512m -it --name mem0001 rockylinux:9.0 /bin/bash`
- メモリ容量制限のテスト
    - `/dev/null < $(yes)` を使ってbashプロセスのメモリ使用率を徐々に上げていく方法がある
- 現在のメモリ容量を確認
    - sysディレクトリの「memory.limit_in_bytes」の値を確認
    - docker inspect
## I/O帯域幅の制限
- コンテナが利用するブロックデバイスのI/O優先度や、読み書きのI/O帯域幅を変更
- ディスクI/O帯域幅の設定
    - `--device-write-bps=/dev/sdb:1mb`
- ネットワーク帯域幅の制御
## GUIアプリケーション用コンテナ
# 管理ツール
## Docker Compose
- 複数のDockerコンテナの設定を別々に手動で行うのではなく、1つのYAMLファイルに複数のコンテナを定義し、Dockerコンテナを一括で構築、連携、管理することで、管理者の管理負荷を低減するツールが提供されている
- Docker ComposeにおけるDockerコンテナのスケール
    - docker composeでは管理下にあるコンテナを簡単にスケールできる
        - `docker compose up --scale websvr=8`
- Docker compose におけるDockerfileの利用
    - Dockerfileを組み合わせて複数のDockerイメージから構成されるサービスをビルドできる
    - アプリケーションのインストールやコンテンツの配置をDockerfileに記述することで、YAMLファイルの記述量の低減が期待できる
- Composerize
    - YAMLファイル自体を自動生成し、開発工数を削減できるツール
    - docker runコマンドを指定すると、YAMLファイルの雛形を自動生成する
    - 手順
        1. Node.jsとnpmをインストール
        1. Composerizeのインストール
        1. YAMLファイルの自動生成
## Docker Imageの社内配信、集中管理
- インターネットから切り離されて、外部への接続が許されない社内LAN内に閉じた環境は、エアギャップ環境と呼ばれる
- DPRサーバの構築
    1. インターネットに接続可能なDockerホストでDPRを起動
    1. DPRに登録するDockerイメージをインターネット経由で入手
    1. 入手したDocker Imageにタグを付与し、DPRに登録
    1. エアギャップ環境のクライアントマシンでDPRに登録されたDockerイメージを入手
    1. クライアントマシンでコンテナを起動
## セキュリティ管理ツール
- プライベートレジストリのユーザ認証
    - Authorization Service
        - DPRに対するトークンベースの認証
        - 手順
            1. クライアントのDockerホストを利用しているユーザはDPRサーバに対してdocker pull やdocker push によりDockerイメージの入手やアップロードを試みる
            1. DPRサーバ側は認証方法に関する情報とHTTPの応答に関するステータスコードをDockerホストに返す
            1. クライアントのDockerホストがASに対してトークンを要求する
            1. ユーザからトークンを要求されたASはアクセス許可用のトークンをクライアントのDockerホストに返す
            1. クライアントのDockerホストはASから与えられたトークンを使用し、DPRサーバにアクセス要求を行う
            1. DPRサーバはユーザから送られてきたトークンを検証かつ認証を行い、クライアントのDockerホストにおけるdocker pull やdocker pushのセッションを開始する
## 脆弱性チェックツール
- Docker Hubで提供されているDocker Imageにはバージョンが古い、あるいはセキュリティ的に不具合が存在するソフトウェアが収録されていることも少なくない
- Trivy
    - Docker Imageの診断
- Docker Bench for Security
    - Dockerホストの構成と稼働中のコンテナなどを検査し、セキュリティ診断を行う
    - よりセキュアなコンテナ環境を実現するためにホストOSの設定の見直しや監査に利用できる
## GUI管理ツール
- Docker Registory Browser
- Portainer
- Lazydocker
    - コマンドラインの仮想端末でコンテナの状況をグラフィカルに表示する管理ツール
    - コンテナのリソース使用量を時系列で表示する機能や、Docker Imageを構成している元のDockerfileの命令の表示。さらに仮想端末上でのマウスクリック操作にも対応
- Ctop
    - Webブラウザを使わずにコマンドラインの仮想端末上でコンテナを管理するツール
- Docker Hub Tool
    - Docker社が提供するパブリックレジストリのDockerHubに登録されているDocker Imageの情報やアカウント情報をコマンドラインで取得
# Kubernetesによるコンテナオーケストレーション
## 基本
- 複数の物理サーバからなるマルチホストのコンテナ環境を統合的に管理するためのフレームワーク
- マルチホストにおけるコンテナのスケールや複数のコンテナでサービスを負荷分散させることも可能
- マスターノード
    - マルチホストのコンテナ環境全体を管理する
- ワーカノード
    - コンテナが稼働する管理対象
- Pod
    - 管理対象ノード上で稼働する複数のアプリケーションをひとまとめにしたもの
    - 通常同一ホストOS上で稼働
    - Podのレプリカを作成可能
        - Kubernetes上でPodの稼働状況を監視しておくことにより、障害が発生しても、複製されたPodを自動的に起動させることでサービスを継続させることができる
    - Podにはラベルをつけることができ、異なる管理対象ノード上のアプリケーションをラベルで区別して管理
- CNI
    - Container Network Interface
    - ネットワークで接続された複数の物理サーバで稼働するコンテナ同士が通信できる経路を提供
    - Overlay Network
        - ネットワークインターフェイスで通信hできるネットワーク
    - Kubernetes環境において、ネットワークの情報はマスターノードで稼働するEtcdと呼ばれるKVSに保持される
## コンテナによる冗長システム
- ReplicaSet
- Deployment
## 永続的ボリュームの利用
- コンテナが失われてもデータは外部ストレージに残り、再び起動した別のコンテナでも外部ストレージのデータを利用できる
- PV
    - PersistentVolume
    - 実際の外部ストレージの両機をどれだけ用意するかを定義
    - 例として、NFSサーバの公開ディレクトリ名、確保する容量、書き込み権限の有無など、永続的ストレージとして利用するボリュームを定義
- PVC
    - PersistentVolumeClaim
    - 永続的ストレージのボリューム領域を論理的に表現したもので、アプリケーションが使用するPVの必要な容量などを動的に確保する