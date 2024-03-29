# Overviews
- an open-source container orchestration platform designed to automate the deployment, scaling, and management of containerized applications
-  allow developers to package an application and its dependencies into a standardized unit, ensuring consistency across different environments.
- Container Orchestration:
    - Kubernetes automates the deployment, scaling, and management of containerized applications, making it easier to handle complex, distributed systems.
- Containerization:
    - Kubernetes is often used with container runtimes like Docker to encapsulate applications and their dependencies into containers. Containers provide isolation and portability.
- Nodes and Clusters:
    - Kubernetes organizes machines into clusters, with each machine referred to as a "node." Nodes can be physical or virtual machines.
- Master and Worker Nodes:
    - The cluster has a master node that manages and controls the overall state of the system. Worker nodes host the containers that run the applications.
- Pods:
    - The smallest deployable units in Kubernetes are called pods. A pod can contain one or more containers that are tightly coupled and share the same network namespace.
- Services:
    - Kubernetes provides services to expose applications running in pods to the network. Services allow for load balancing and automatic discovery of applications.
- Replication Controllers and Deployments:
    - These components manage the desired number of pod replicas, ensuring that the specified number of instances is running and healthy.
- ConfigMaps and Secrets:
    - Kubernetes allows you to manage configuration data and secrets separately from the application code, enhancing security and flexibility.
- Persistent Volumes:
    - Kubernetes supports persistent storage, allowing containers to store and retrieve data across restarts.
- Scaling:
    - Kubernetes provides mechanisms for scaling applications, both manually and automatically, based on resource usage or custom metrics.
- Load Balancing:
    - Kubernetes can distribute network traffic across multiple pods using built-in load balancing.
- Declarative Configuration:
    - You define the desired state of your application in configuration files, and Kubernetes works to achieve and maintain that state.

# Architecture

## Overviews for Components
- Cluster
    - 各クラスターには1つのマスターノードがある
    - マスターノードは1つ以上のノードと接続
    - 複数の仮想またはオンプレミスマシンを1つのクラスターとして整理したもの
    - Control Plane
        - マスターノードがワーカーノードと通信を行うためのオブジェクトをまとめ、形成
        - Nodes: container
            - ワーカーノードはコンテナ化したアプリケーションとワークロードのグループであるポッドを管理する
            - Pods: components of the application workload

## Components
- Cluster
    - Control Plane
        - make global decisions about the claster
        - Master Components
            - etcd
                - a consistent and highly-available key-value store used as Kubernetes' backing store for all cluster data
                - stateful
            - kube-scheduler
                - The scheduler watches for newly created Pods with no assigned node and selects a node for them to run on
                - ensures the there are enough resources for all the Pods on a Node
            - kube-controller-manager
                - Runs controller processes, which are responsible for node and job resource management among other things.
                - Node controller
                    - assign a CIDR block to the node when it is registered
                    - keep the node controller's internal list of ndoes up to date
                    - monitor the nodes' health
                - Job controller
                - EndpointSlice controller
                - ServiceAccount controller
            - cloud-controller-manager
                - Integrates with cloud-specific APIs and manages the life-cycle of cloud resources (e.g., nodes).
                - Node controller
                - Route controller
                - Service controller
            - kube-apiserver
                - a component that exposes the Kubernetes API.
                - the front end for the Kubernetes control plane
                - the ently point for all administrative tasks and management operations in the Kubernetes cluster
                - stateless
                - designed to scale horizontally
                - Node Components
                    - may be a virtual or physical machine
                    - managed by the control plane
                    - Nodes register themselves with the API server during the initialization process
                    - contains the services necesary to run Pods
                    - typically several nodes
                    - Kubernetes keeps the object for the invalid Node
                    - can manage Node objects using kubectl
                    - kube-proxy
                        - Maintains network rules on nodes. It reflects services as defined in the Kubernetes API on each node
                        - uses the operating system packet filtering layer 
                    - Container Runtime
                        - The software responsible for running containers. Kubernetes supports several container runtimes including Docker, containerd, and others
                    - kubelet
                        - An agent that runs on each node in the cluster.
                        - makes sure that containers are running in a Pod.
                        - attempts to detect node system shutdown and terminates pods running on the node
                        - pods

# フロー
- 操作: kubectl -> kube-apiserver -> kube-controller-manager -> kubelet
- デプロイ
    1. クラスターの新しい状態についてYAMLファイル形式で記述
    1. kube-controller-manager がYAMLファイルを受け取り、kube-schedulerを実行
    1. kube-schedulerはポッドを開始し、マシンの状態を監視/全体的なリソースを管理
    1. 期待値がetcdに最新の状態として反映

# Learn
## Kubernetesとは
- Kubernetes
    - コンテナー化されたワークロードの管理およびオーケストレーションのための、移植可能で拡張可能なオープンソース プラットフォーム
    - 複雑なコンテナー管理タスクを単純化し、さまざまなコンピューティング環境でコンテナーを調整するための宣言型の構成を提供
- コンテナ管理
    - 多数のコンテナーを整理、追加、削除、または更新するプロセス
- コンテナオーケストレーター
    - コンテナー化されたアプリを自動的にデプロイおよび管理するシステム
- 利点
    - 自己復旧
    - 動的スケーリング
    - ローリングアップデート

## How it works
- Overview
    - クラスター
        - 連携して 1 つのシステムとして見なされるように構成するコンピューターのセット
        - 同じ種類のタスクを処理
        - これらのタスクのスケジュール設定と制御を担当する一元化されたソフトウェアが使用
        - 1つのメインプレーンと1つ以上のノード
    - ノード
        - タスクを実行するクラスター内のコンピューター
    - コントロールプレーン
        - スケジュールソフトウェアを実行するコンピューター
- Architecture
    - コントロールプレーン
        - kube-api-server
            - Node
                - kubelet
                - kube-proxy
                - container runtime
                - pod
                    - container
        - コントローラー
        - スケジューラー
        - etcd
- Details
    - コントロールプレーン
        - Kubernetesのオーケストレーション機能を管理するサービスのコレクションが実行
    - ノード
        - コンピューティング ワークロードが実行される場所
        - 各ノードは、API サーバーを介してコントロール プレーンと通信し、ノードの状態の変化について通知
    - kube-api-server
        - Kubernetes クラスターのコントロール プレーンのフロント エンド
        - Kubernetes 内のコンポーネント間のすべての通信は、この API を介す
    - etcd
        - Kubernetes クラスターが自身の完全な構成を内部に保存する永続的なストレージ
        - クラスター内のすべてのオブジェクトについて現在の状態と必要な状態が格納
    - スケジューラ
        - すべてのノードにわたってワークロードの割り当てを担当するコンポーネント
        - クラスターで新しく作成されたコンテナーの有無が監視され、それらのコンテナーがノードに割り当て
        - For every Pod that the scheduler discovers, the scheduler becomes responsible for finding the best Node for that Pod to run on
        - the sheduler finds feasible Nodes for a Pod and then runs a set of functions to score the feasible Nodes and picks a Node with the highest score among the feasible ones to run the Pod
            - binding
                - the schduler notifies the API server about the decision
        - filtering
            - finds the set of Nodes wheere it's feasible to schedule the Pod
                - PodsFitsResources
                    - check whether a chandidate Node has enough available resource to meet a Pod's specific resource requests. 
        - scoring
            - the scheduler ranks the remaining nodes to choose the most suitable Pod placement. The schduler assigns a score to each Node that survived filtring, basing this score on the active scoring rules.
        - scheduling policies
            - allow you to configure Predicates for filtering and prorities for scoring
        - scheduling profiles
            - allow you to configure Plugins that implement different schduleing stages
    - コントローラマネージャー
        - API サーバーを介してクラスター用に構成されたコントローラーが起動され、監視
    - kubelet
        - クラスター内の各ノードで実行されるエージェントで、API サーバーからの作業要求を監視
        - ノードを監視し、各ノードにスケジュールされているコンテナーが想定どおりに実行
    - kube-proxy
        - ローカル クラスター ネットワークを担当し、各ノードで実行
        - 各ノードが一意の IP アドレスを持つ
        - iptables と IPVS を使用したトラフィックのルーティングと負荷分散を処理する規則も実装
    - container runtime
        - Kubernetes クラスター上でコンテナーを実行する基盤のソフトウェア
        - コンテナー イメージのフェッチ、開始、および停止を担当
    - pod
        - Kubernetes で実行されているアプリの 1 つのインスタンス
        - コンテナーを、ポッドと呼ばれる Kubernetes オブジェクトにパッケージ化
        - ポッドには、共有ストレージとネットワーク構成に関する情報、およびパッケージ化されたコンテナーの実行方法に関する仕様が含まれる
        - ポッドテンプレート
            - ポッドのデプロイを管理するために他のオブジェクトに含めて再利用する YAML コード ファイル
        - 状態
            - 保留中
                - ポッドがスケジュールされるのを待機している時間
                - コンテナー イメージのダウンロードに費やされる時間
            - 実行中
                - ポッド内のすべてのリソースが準備できた後、ポッドは実行中状態に遷移
            - 成功
                - ポッドが目的のタスクを完了し、実行が正常に終了した後、ポッドが成功状態に遷移
            - 失敗
            - Unknown
                - ポッドの状態を特定できない場合
        - ポッドの状態または動的に割り当てられた構成はクラスターには保存されない
        - ライフサイクル
            - 待機中
                - コンテナーの既定の状態
            - 実行中
            - 終了
        - デプロイ
            - ベストプラクティス
                - デプロイ定義ファイルを使用してすべてのデプロイを管理し、バージョンコンロールシステムを使用して変更を追跡すること
            - デプロイオプション
                - ポッドテンプレート
                - レプリケーションコントローラー
                - レプリカセット
                - デプロイ
        - グループ化
            - IPアドレスでポッドを管理しない
            - セレクターラベルを使用することにより、クラスター内の特定のポッドをターゲットにして管理する
            - セレクターラベルはポッドの定義ファイルで定義されているポッドラベルと一致するようにサービス定義で設定
- Networks
    - ノード間でネットワーク アドレス変換 (NAT) を使用せずにポッドが相互に通信できる
    - NAT を使用せずにノードからすべてのポッドと通信でき、また、ポッドからすべてのノードと通信
    - ノード上のエージェントからすべてのノードおよびポッドと通信

## AKS
- Azure Kubernetes
- 料金はクラスターでノードVM、ストレージ、ネットワークリソースが消費された分だけかかる
- 規定の構成はスケーリング、認証、ネットワーク、監視を含む
- Dockerイメージ形式をサポート
    - 任意の開発環境を使用してワークロードを作成し、ワークロードをコンテナーとしてパッケージ化し、コンテナーを Kubernetes ポッドとしてデプロイ
- Bridge to Kubernetes
    - 開発用のコンピューター上でコードの実行とデバッグを行いながら、Kubernetes クラスターおよび残りのアプリケーションやサービスとの接続を保つ
    - 開発用コンピューターからクラスターへの直接接続を作成
    - 接続されたKubernetesクラスターと開発用コンピューターの間でトラフィックをリダイレクト。同じKubernetesクラスター内に存在するかのように通信
    - Kubernetesクラスター内のポッドに利用できる環境変数とマウントされたvol.を開発用コンピューターにレプリケートする
- 最適な選択であるかどうか
    - IDとセキュリティ管理
        - Microsoft Entra ID と統合し、既存の ID とグループ メンバーシップを再利用するように AKS クラスターを構成
    - ログ記録と監視の統合
        - Azure Monitorを用いた監視
    - 自動クラスターノード及びポッドのスケーリング
        - 水平ポッドオートスケーラー
            - ポッドのリソース需要を監視し、需要に合うようにポッドのリソースを増やす
        - クラスターオートスケーラー
            - ノードの制約のためにスケジュールできないポッドを監視
    - クラスターノードのアップグレード
    - GPU対応ノード
    - ストレージボリュームのサポート
        - 静的と動的の両方補ストレージボリュームがサポート
    - 仮想ネットワークのサポート
    - HTTPアプリケーションルーティングサポートを使用
    - Dockerイメージのサポート
    - プライベートコンテナレジストリー
- Architecture
    - Kubernetesクラスター
        - 1つのものとして動作する複数のマシンが使用される
    - クラスターノード
        - コントロールプレーンノード
            - クラスターのコントロールプレーンの側面をホストするために使用され、クラスターを制御するサービスように予約
            - ユーザーや他のすべてのノードが通信に使用するAPIを提供
        - ノード
            - カスタムのワークロードとアプリケーションを実行する
    - コンテナーレジストリ
        - あとでデプロイするためにコンテナイメージをクラウドに安全に格納する
        - 複数のバージョンのコンテナイメージを格納するアーカイブ
        - パブリックまたはプライベートのどちらでも指定可能
        - コンテナレジストリでホストされているイメージのみをデプロイできる
    - Kubernetesポッド
        - ポッドによってコンテナとアプリケーションが論理構造にグループ化
        - 1つ以上のアプリケーションんコンテナで構成
        - 各ポッドにはIPアドレス、ネットワークルール、公開されたポートがある
    - Kubernetesデプロイ
        - ポッドの進化
        - ポッドをインテリジェントなオブジェクトにラップし、スケールアウトできる
        - アプリケーションの複製や、スケーリングなど
        - イメージタグを変更するだけでダウンタイムなしでアプリケーションを更新
        - 更新時オンラインアプリを1つずつオフにし、最新バージョンに置き換え
    - Kubernetesマニフェストファイル
        - ワークロードをYAML形式で宣言的に記述、Kubernetesオブジェクトの管理が簡素化する
        - パラメーター
            - `apiVersion`
                - デプロイするオブジェクトを管理するAPIサーバーエンドポイント
            - `kind`
                - このデプロイで作成するワークロードを定義
            - `metadata`
                - `name`
                    - Kunernetesリソースの名前
            - `spec:`
                - `selector`
                    - `matchLabels`
                        - `app`
                            - グループを定義
    - Kubernetesラベル
        - Kunernetesオブジェクトを論理的にグループ化
    - Namespaces
        - a way to divide cluster resources between multiple users
        - uses namespaces to organize and and isolate different workloads and applications within a single Kubernetes cluster
    - workloads
        - the application or services that are deployed and run on the Kubernetes cluster
        - AKS allows you to deploy, scale, and manage various types of workloads, making it easy to run and operatecontainerized application
        - KubernetesのサービスアカウントとマネージドIDを紐付けることで権限分離できる
    - custom resources
        - enable users to define and use their own custom 
    - Node selector
        - allow you to constrain which nodes your Pod is eligible to be scheduled based on node labels
    - Node affinity
        - allowing you to define what happens if the pod can't be matched with a node
            - require that Kubernetes scheduler mathces a pod with a labeld host
            - prefer a match but allow the pod to be scheduled on different host if no match is available
    - Inter-pod affinity and anti-affinity
        - allow you to constrain the placement of Pods relative to other Pods
        - approach for the Kunernetes schduler to logically isolate workload
        - specify rules to either attract Pods to nodes with specific characeristics (affinity) or repel Pods from nodes with specific characteristics (anti-affinity)
        - define that pods either shouldn't or should be scheduled on a node that has an existing matching pod
            - Default: Kunernetes scheduler tries to schdule multiple pods in a replica set across nodes
    - predicates and priorities
        - scheduler's decisions, whether or where a pod can or cannot be schduled, are guided by its configurable policy which coprises of set of rules
    - Deschduler
        - finds pods that can be moved and evicts them
        - does not schdule replacement of evicted pods but relies on the default schduler for that
    - 構成
        - Kubernetesクラスターにデプロイするコントロールプレーンとノードの数を概念化
        - クラスター内のノードの数は、常に2つより多くする
        - パターン
            - 単一のコントロールプレーンと複数のノード
            - 単一のコントロールプレーンと単一のノード
        - ノードプール
            - AKSクラスター内のノードをグループ化
            - 作成時、アプリケーションの要件に基づいてノードプールの各ノードのVMサイズとOSの種類を指定
            - ユーザーアプリケーションポッドをホストするには、ノードプールのモードがユーザーまたはシステムである必要がある
        - ノード数
            - クラスターのノードプール内に存在するノードの数
            - Azure VM
            - クラスターの構成パネルを使用して後から変更できる
        - ノードVMサイズ
- アプリケーションをデプロイ
    - 