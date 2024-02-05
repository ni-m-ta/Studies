# 運用設計の教科書

## 運用と運用設計
- 運用
    - 設計構築が終わり、システムがリリースされてサービス開始されたところから、サービス終了するまで
    - 目的
        - システムを安定稼働させて効率的にサービスを提供すること
- 運用設計
    - 運用に必要な作業を取りまとめてルールを決めること
    - サービスの目的<-運用の目的<-運用設計の目的
    - 目的
        - サービスの重要度に合わせて運用を最適化すること
    - 運用設計が運用コストに直結する
    - トラブル
        - 運用範囲の未整理
        - サービスレベルの低下
        - 属人化
        - サービス品質のばらつき
        - 運用ドキュメントが未整理
    - 範囲
        - システムを運用する人の範囲
            - 役割関連図
                - サービス開始後にシステムについての問い合わせや障害などを解消できる体制を記載した図
            - 具体的な対応
                - 利用者からサポートデスクへの問い合わせ方法
                - サポートデスク、監視オペレーター、DCオペレーターから運用担当者への連絡方法
                - 運用担当者から情報システム室の情報連携方法
                - 運用担当者から保守担当への連絡方法
        - 導入するシステムの運用業務の範囲
            - システム追加したらどの役割にどのような運用業務が必要となるか
        - 周辺システムと連携する範囲
            - システム連携相関図
    - 運用設計を目指すレベル
        - COBIT 成熟度モデル
            - どこまで運用設計を行えば完了となるのかの基準
            - 0: プロセス不在
            - 1: 個別対応
            - 2: 再現性はあるが直感的
            - 3: 定められたプロセス
            - 4: 管理測定が可能
            - 5: 最適化
    - 3つの業務
        - 業務運用
            - システムを活用して、サービスを提供するアプリケーションと利用者に関する業務
            - 目的: 利用者とシステム側のやり取りが円滑に行われるようにする
            - 構築したシステムによって運用項目が増減する
            - 業務の8割が自動化されたとして、残りの2割の人間による作業部分
        - 基盤運用
            - システムを維持して、アプリケーションが問題なく動作するためのシステム基盤に関する業務
            - アプリケーションなどの業務運用が継続されるようにする
            - システムを維持するための基盤メンテナンス部分
        - 運用管理
            - 運用全体を管理して、円滑に行えるように全体のルールと物差しを決めて管理する業務
            - 他システムも含めて、業務運用、基盤運用が統一した基準で行われるようにする
            - 運用に関わる人が守るべきルールと基準を決める

## フェーズ別
- 全体像
    - システム化計画
        - プロジェクト案件の立案から受注までの流れ
            1. 発注者側にて、サービス提供内容を中心にシステム化構想をまとめる
            1. システム化計画書としてドキュメント化
            1. 発注者内で承認されたら、予算が組まれシステム導入するSIベンダーの選定が始まる
            1. システム化計画書をもとに、発注者にて提案依頼書(RFP: Request For Proposal)を作成して、実際にシステム構築ができそうなSIベンダーに提案書作成依頼
            1. 複数のベンダーから提出された提案書を見比べて、どのSIベンダーが最も要望に沿ったシステムを作ってくれそうか判断
### 要件定義
- システムに必要とされる要件を決めるフェーズ
- プロジェクトとして運用設計にかかるコストと合わせて、運用を実施する項目の一覧を作成して、運用対象と運用開始後のランニングコストの概算を算出する
- 目的: 運用項目一覧という運用設計全体のガイドラインを作成して、基本設計以降で何をすればいいかわかるようにする
- 要件定義でしっかりと設計範囲を発注者と合意できなくて基本設計以降で設計範囲が拡大してしまった場合、リソース不足によりスケジュール遅延が発生して、炎上プロジェクトになる
- 流れ
    - 人的な範囲としての運用体制図を作り、発注者と合意する
        - 今回のシステムで関連する組織がいくつあって、どの組織がどのような役割を担っているのか、その組織の対応時間、対応場所などを確認
        - 運用体制
            - システムを構築したベンダーがそのまま運用を実施する->シームレスなシステムリリース、サービス開始
                - システム運用に最適な役割を決めて、その後に計画要員を立てる
            - 発注者側の既存運用体制が実施する
                - システムに必要な役割を既存運用体制へ割り当てる
                - 既存運用体制がそれぞれに何をどこまで実施するのかヒアリングして、運用業務や作業をどの組織が実施するのか整理
                - ヒアリング項目
                    - 発注者側
                        - 利用者
                            - 利用人数
                            - 利用時間
                            - 利用場所
                            - 利用方法
                        - 情報システム室
                            - 対応時間
                            - 今回のシステムで必要となるおおよその工数
                    - 運用側
                        - サポートデスク
                            - 他システムと兼務するか今回のシステムで独立されるか
                            - 対応時間
                            - 今回のシステムで必要となるおおよその人数
                        - 監視オペレーター
                            - 他システムと兼務するか今回のシステムで独立されるか
                            - 対応時間
                            - 今回のシステムで必要となるおおよその人数
                        - DCオペレーター
                            - 他システムと兼務するか今回のシステムで独立されるか
                            - 対応時間
                            - 今回のシステムで必要となるおおよその人数
                        - 運用責任者
                            - 対応時間
                            - 今回のシステムで必要となるおおよその人数
                        - 運用担当者
                            - 対応時間
                            - 今回のシステムで必要となるおおよその人数
                        - ソフトウェア保守
                            - 契約内容
                            - 対応時間
                        - ハードウェア保守
                            - 契約内容
                            - 対応時間
    - 運用項目の範囲としての運用項目一覧のドラフト版を作り、発注者と合意する
        - 目的
            - 運用中に発生する作業を明確化し、運用設計を行う全量を合意する
            - 運用作業における役割分担を明確にし、運用に必要な工数を明らかにする
            - 運用作業に必要となるドキュメントを明確にし、運用設計で作成するドキュメントを合意する
        - 運用項目一覧記載内容
            - 運用分類
                - 業務運用
                - 基盤運用
                - 運用管理
            - 運用項目名
            - 作業名
            - 作業概要
            - 関連ドキュメント名
            - 担当者/役割分担
            - 作業頻度
            - 作業工数
            - 特記事項
        - 作成手順
            - 運用項目一覧のドラフトを作成
                - 業務運用、基盤運用、運用管理わけて考える
                    - 業務運用
                        - システム更改
                            - 更改前後のユースケースを見比べて、サービスとして追加/削除されている項目を確認
                            - 既存で使っている運用項目一覧を確認
                            - 
                - 類似のサービスやフォーマットを参考に
                - 業務分類ごとに関係者へのヒアリング
            - 各ディスカッションから運用項目一覧をアップデート
                - ユースケース
                    - システムの根本的な使い方
                    - PMとアプリケーション担当
                    - 運用項目となりうるのは例外ケース
                        - 原則~だけども、~したい
                    - 議事録からもわかる
                - 機能要件
                    - サービス提供に必要な機能
                        - ユースケースで洗い出されたシステムの利用方法を実現するために、どのような機能を実装すれば良いかをアプリケーション担当が検討
                    - アプリケーション担当
                    - 基本は業務運用になりうる
                    - 機能をジョブ管理システムなどで実装する場合は、基盤運用になる場合がある
                    - 運用回避
                        - 費用対効果からシステム化されず、手作業すること
                        - ゆくゆくはシステム化されたり、運用自動化が検討される作業項目になるため運用回避された経緯は運用設計書に記載する
                        - 条件
                            - 実施するトリガーが流動的
                            - 入力情報が流動的
                            - 複雑な判断が必要
                            - 処理の途中にいくつかの承認が必要
                            - 機能実装にかなりのコストがかかる
                            - 作業頻度が低い
                            - 優先度がそれほど高くない
                            - 手作業の難易度が低い
                - 非機能要件
                    - サービス継続のために必要な機能以外の要件
                    - システム機能が必要なときに求められるパフォーマンスで利用できるようにするためにはどのようにするか
                    - サービス継続のためにシステムをどのように維持管理してくのか
                    - 具体案
                        - システム構成要素の冗長構成
                        - 拡張性
                        - バックアップ/リストア
                        - 監視
                        - ログ管理
                    - 非機能要求グレード
                        - 可用性
                            - 継続性
                            - 耐障害性
                            - 災害対策
                            - 回復性
                            - 運用設計として
                                - システムを継続するための運用スケジュール
                                    - 対応時間
                                    - メンテナンス日
                                    - リリース日
                                - バックアップ/リストアに関する方法、タイミング、目標復旧地点、目標復旧時間
                                    - 定期バックアップ: 日次、週次、月次
                                    - 臨時バックアップ: システム変更作業前後
                                    - はっきりとしたトリガー(利用者や関連システムからの依頼など)は運用項目としてリストアを考慮
                                - DRサイトの運用方法、切り替え訓練
                                - 稼働率と稼働率維持のための対策
                        - 性能・拡張性
                            - 基盤設計
                                - 業務処理量
                                - 性能目標値
                                - リソース拡張性
                                - 性能品質保証
                            - 運用について
                                - 運用管理の定期報告
                                    - 運用設計では性能が発揮されているかを定期的に計測して報告する仕組み
                                    - 定期報告の中で傾向や需要予測からいつ頃に拡張が必要になりそうかを報告
                                    - 運用開始後に追加で機器購入やライセンス購入が必要な場合、実際に運用が始まるまでのリソース(時間やコスト)は考慮すべき
                        - 運用・保守性
                            - 通常運用
                                - 運用時間と特殊日(年度末や締め日)
                                - メンテナンス時間
                                - バックアップの取得方法
                                - 取得間隔
                                - 世代管理方法
                                - システム監視方法とそのレベル
                            - 保守運用
                                - 計画停止日
                                - 運用負荷削減方針
                                - パッチ適用方針
                                    - 対象
                                    - 周期
                                    - 緊急対応
                            - 障害時運用
                                - システムの復旧方針
                                - 障害発生時の代替業務の有無
                                - 障害対応可能時間
                                - 障害レベルの設定
                            - 運用環境
                                - 開発環境や検証環境の用途と役割分担
                                - 手順書などのマニュアル記載粒度
                                - リモートオペレーションの有無
                                - 関連システムとの連携方針
                            - サポート体制
                                - 保守契約状況
                                - システムのライフサイクル
                                - 運用要員の教育方針
                                - 定期報告会の頻度とレベル
                            - その他の運用管理方針
                                - ITILに記載されているサービスデスクやインシデント管理
                                - 問題管理
                                - 変更管理
                                - 構成管理
                        - 移行性
                            - 要件
                                - 移行時期
                                - 移行方式
                                - 移行対象機器
                                - 移行対象データ
                                - 移行計画
                            - 運用設計として
                                - 並行運用期間がある場合の体制
                                - 移行リハーサルがある場合の運用テスト
                                - 運用開始後の初期流動期間をどのように乗り切るかが要件定義時の議題になるため、運用設計担当が運用引き継ぎと合わせて移行計画をまとめる場合が多い
                        - セキュリティ
                            - 代表的な運用項目
                                - 定期的なセキュリティ診断
                                    - 外部の監査員によるシステムのセキュリティ診断
                                - 運用アカウントの管理
                                    - 運用アカウントの定期的なパスワード変更
                                    - 特権アカウントの貸出運用
                                - 不正追跡・監視のためのログ管理
                                    - 定期的なアクセスログなどの確認
                                - セキュリティインシデント対応/復旧
                                    - マルウェア検知時の対応
                                    - マルウェア感染時のフォレンジック
                        - システム環境・エコロジー
                            - システム制約/前提条件
                            - システム特性の洗い出し
                            - 適合規格
                            - 機材設置環境条件
                            - データセンターの作法
                                - データセンターへの入管方法や持ち込み可能機器
                                - リードタイムやサービスレベル
                    - 基盤構築担当と運用設計担当
            - 役割分担のサマリを作成
                - 人-役割-運用工数
            - 運用に必要な工数を算出
                - 要件定義時点での精度6割
                - 作業頻度
                    - アプリケーション担当や基盤構築担当へ作業概要を聞きながら半日単位で数字を埋める
                    - 頻度の単位を揃える
                    - 月次
                    - 類似案件
                        - 問い合わせ
                        - インシデント発生件数
                    - サービスレベルから割り出す
                    - サービス開始後の初期流動期間と安定稼働後
                - 作業工数
                    - 既存運用や類似案件からの推測して概算
                    - 運用チームによる管理工数も考慮
                - 運用体制の検討
                    - 運用全体に必要な工数=頻度*一回あたりの工数
            - 要件定義書を書く
                - システムを高い解像度で想像
                - 要件と設計の違い
                    - 要件
                        - サービス提供に必要なシステムの条件
                    - 設計
                        - その条件をどのように実現するか
                - 要件定義書の目次
                    - はじめに
                        - プロジェクトの目的
                        - 対象読者
                    - ユースケース
                        - システムがどのように使われるか
                    - 機能要件
                        - ユースケースを実現するための機能
                    - 非機能要件
                        - 機能以外のシステム構成
                        - 運用保守に必要な要件
                    - 運用要件
                        - 運用上必要となる要件
                        - 詳細
                            - 運用基本要件
                                - 運用体制図
                                - 対応時間
                                - 運用スケジュールなど運用全体に関わる要件
                            - 業務運用要件
                                - 利用者登録
                                - 利用者権限管理などサービス利用に関わる運用の要件
                            - 基盤運用要件
                                - システム基盤のパッチ適用
                                - 監視運用
                                - バックアップ/リストア
                                - ログ管理
                                - 運用アカウント管理などの基盤運用に関する要件
                            - 運用管理要件
                                - 運用上の維持管理方針
                                - 情報統制方法
                                - 定期機報告についての要件
                    - 実行スケジュール
                - 注意点
                    - 簡潔に記載
                    - 句読点は1行に1つまで
                    - 言い切り
                    - 共通項目や表やマトリクス
                    - 決まっていないことを説明しない。詳細は次工程にて検討する
                    - ()や*を乱用しない。
            - 各フェーズごとに修正、変更があれば修正、確定すればアップデート。大海原でコンパスと海図を捨てるな。
    - 運用体制図と運用項目一覧ドラフト版作成の中で合意された要件を、要件定義書としてまとめる
- 理解しておくべきこと
    - RFP
    - 提案書
    - システム化計画書
    - 発注者のプロジェクトに対する期待度
        - システム更改で提供するサービスはそのまま変わらないのか
        - 新規サービスを提供するためにシステム追加するのか
        - 期待度は予算に反映されている可能性が高い
    - システム化計画時に検討されたが採用されなかったアイデア
        - 要件定義でシステム化計画と同じ検討をしてしまう可能性あり
        - 要件を詰めていく中で、システム化計画で採用されなかったアイデアの方が要件を満たせる場合もある
        - 要件を固めていく前提条件として、システム化計画時に検討されたアイデアはヒアリングして聴き出すか、議事録に目を通すかする
    - プロジェクトとシステムの変動要素
        - プロジェクト変動要素
            - リリース日はどの時点で確定するか
            - スケジュールの延長に対する許容があるか
            - 途中で要員の追加は可能か
        - システム変動要素
            - システムの利用者数
                - 要件定義時に確定できない場合は、予想される最大値と最小値で、それぞれの運用ケースとして想定する必要がある
            - サービス提供時間
                - 要件定義時に確定できない場合は、予想される最大値と最小値で、それぞれの運用ケースとして想定する必要がある
            - 運用中にシステム拡張があるか
                - システム拡張がある場合、運用の範囲なのか別途プロジェクトとして対応する範囲なのかは必ず確認する
    - 発注者側重要人物の把握: 重要人物からの信頼
        - 誰がプロジェクト全体の決定権を持っているのか
        - 誰が運用設計に対する承認権を持っているのか
        - 最終的に誰が承認したら運用引き継ぎ完了となるか
        - 誰にヒアリングを行えば必要な情報を正確に引き出せるのか
            - よく喋る人がいちばん運用を把握しているわけではない
            - よく理解していそうな人
                - 発注側担当者の話す内容を訂正する人
                - 質疑応答で必ず質問する人
                - ディスカッション会やヒアリング会をした際に、端の方に不満げで座っている人
### 基本設計
- システムの基本的な仕組み、実現方法について決めるフェーズ
- 機能を利用する上で登場人物間のやりとりをまとめた運用フロー図や、システム稼働後に必要となる作業をまとめる
- 運用設計担当として
    - 運用のルール、やること、やらないことを記載した「運用設計書」を発注者と合意する
    - 複数の関係者が登場する運用業務について、運用フロー図で役割分担を整理して発注者と合意する
    - 運用項目一覧を修正して、詳細設計で作成するドキュメントを発注者と合意する
- 注意点
    - 「作成」「レビュー」「修正」「合意」を繰り返す
- 運用設計書
    - 基本設計書の別冊
        - 基本設計書
            - システムの機能と構成が書かれたドキュメント
            - 要件を実現するためのアプリケーションの機能実装方式や基盤構成など
    - 運用設計内容を発注者と合意するために作成
    - 運用項目一覧と補完関係
    - 構成
        - 今回の運用に求められていること
        - 運用するにあたって知っておかなければならないシステムに対する知識
        - 今回の運用で出てくる登場人物とその役割
        - 運用項目ごとの目的とゴール
        - 各運用項目で利用するドキュメント
        - 採用されなかった運用方針とその理由
    - 構成例
        1. はじめに
            - 運用設計書が何の目的で誰向けに書かれているか
            - インプット情報
                - システム化計画書
                - 要件定義書
            - 合意内容
                - 今回の運用に求められていること
        1. 利用者のユースケース
            - 何のためにどのように利用者から使われているか
            - インプット情報
                - 要件定義書
                - 基本設計書
            - 合意内容
                - 運用するにあたって知っておかなければならないシステムに対する知識
        1. 機器構成・機能
            - 主に基本設計書からの転記。機器構成、ネットワーク構成などの構成から、システムが実装している機能概要
            - システム構成図
            - ネットワーク構成図
            - システムが実装しているアプリケーション・ミドルウェア機能一覧
            - インプット情報
                - 基本設計書
            - 合意内容
                - 運用するにあたって知っておかなければならないシステムに対する知識
        1. 運用概要
            - 運用スケジュール、運用体制など、運用全体に関わること
            - 登場人物と役割説明、登場人物ごとの対応時間
            - 関係者間の連絡ルール、共通で利用する運用管理ツール
            - インプット情報
                - 要件定義書
            - 合意内容
                - 今回の運用で出てくる登場人物とその役割
        1. 業務運用
            - アプリケーション利用レベルでの運用。利用者とシステム間のやり取りで必要となる運用項目
            - インプット情報
                - 要件定義書
                - 基本設計書
                - 運用項目一覧
            - 合意内容
                - 運用項目ごとの目的とゴール
                - 各運用項目で利用するドキュメント
        1. 基盤運用
            - サービス提供を支える基盤の運用項目を記載
            - インプット情報
                - 要件定義書
                - 基本設計書
                - 運用項目一覧
            - 合意内容
                - 運用項目ごとの目的とゴール
                - 各運用項目で利用するドキュメント
        1. 運用管理
            - 運用していく上での全体的な管理の運用項目を記載
            - インプット情報
                - 要件定義書
                - 基本設計書
                - 運用項目一覧
            - 合意内容
                - 運用項目ごとの目的とゴール
                - 各運用項目で利用するドキュメント
        1. 特記事項
            - 明示的に採用されなかった運用や、上記に当てはまらない特殊な運用
            - 合意内容
                - 採用されなかった運用方針とその理由
    - Tips
        - 前半に基本設計書との関係、後半に運用項目一覧との関連をまとめる構成
- 運用フロー図
    - 1つの運用項目に対して「いつ」「誰が」「どんな情報をもとに」「何をするのか」を合意すること
    - 大きな流れと情報連携方法を確定
    - 既存の類似運用フローはまとめる
    - 流れ
        - 運用項目一覧から、どの項目で運用フローズが必要か検討する
        - どの順番で運用フロー図を作成するか優先度を決める
            - 登場人物が多い場合
        - 運用フロー図を作成する項目と優先度を発注者と合意する
        - 運用設計担当でドラフト版の運用フローを作成する
            - 必要な情報
                - 処理の流れ
                    - アプリケーション担当
                    - 基盤構築担当
                - 運用担当者の作業範囲
                - 実施タイミング
            - 次工程の詳細設計で作成する関連ドキュメントを記載
            - 運用設計書で合意した内容をもとに、作業項目を見直し作業概要を修正
            - 運用フローずで合意した内容をもとに、役割分担を見直す
        - 関係者間でレビューを行い、細かい役割などを決定する
        - 運用設計担当にてレビュー結果を修正する
        - 関係者で最終レビューして、運用フロー図について合意する

- 修正
    - 基本設計書のどこに修正が入ったら、運用設計書のどこを直せばいいか把握
    - 運用設計書と運用項目一覧の並びの目次は合わせる
    - 手順
        - 機能変更箇所確認
        - 運用項目一覧の点検/修正
        - 運用設計書修正
        - 必要であれば運用フロー図の修正

### 詳細設計
- 基本設計で決めた内容を、実際の設定値まで落とし込んで実装・構築を行うフェーズ
- アプリケーション担当と基盤構築担当から運用開始後に利用する手順書を受領し、ユーザー利用手順書や運用手順書を作成
- 運用上で可変情報を記載しておく台帳や、運用上執拗な情報をまとめた一覧
- 申請書や報告書など、運用上で必要となるドキュメント作成
- 運用設計担当が行うこと
    - WBSの作成
        - WBS
            - Work Breakdown Structure
            - 役割とスケジュールの決め方
                - 運用項目一覧の関連ドキュメントを一覧化して、作成対象を発注者と合意する
                - 引き継ぎ先の既存運用担当から既存のフォーマットをもらう
                - 運用手順書、台帳、一覧について、プロジェクト内の役割分担を決める
                - 申請書を発注者側or運用設計担当が作成
                - ドキュメントごとのWBS作成
    - 運用手順書の作成
        - 製品マニュアルやアプリケーションなどの操作手順書を導入する会社やシステムに合わせてカスタマイズし、必要な情報を負荷した手順書のこと
        - 注意点
            - アプリケーションや基盤製品に対する知識がない場合は、事前にレクチャを受けておき、可能であればどこかで実機を触っておく
            - パスワードなどの可変データは、手順書には書き込まない
            - 共通する作業項目をすべての手順書に書くのか、外出しして参照する形にするのか確認
            - 手順書実施時のエビデンス取得ルール、ログ保管場所などに指定があるか
            - 実際に実機で確認
            - 実際の担当者に粒度の確認
        - 記載内容
            - 運用手順書の目的
            - 作業実施トリガー
            - 関連ドキュメント
            - 前提条件
            - 実施手順
            - 事後作業
    - 運用中に発生する可変データを管理する台帳、頻繁に参照するパラメーターを見やすくする一覧を作成
        - 一覧
            - 他のドキュメントのよく参照する静的データを集約
            - 障害発生時
                - 障害対応時に何がどのような方式で監視されているのかを確認できるように一覧としてまとめる
                - メーカーとの保守契約情報
            - 一覧化は二重管理
        - 台帳
            - 手順書実施など、運用上で更新されるデータをまとめておく
            - 運用手順書や運用フロー図と紐付け
        - 主に必要なもの
            - ネットワーク系
                - IPアドレス一覧
                - ポート管理表
                - けービル結線管理表
            - サーバー/ストレージ系
                - 機器構成/ラック構成
                - サーバー構成管理表
                - ソフトウェアライセンス一覧
            - 
    - 利用者依頼で、システムを変更するための申請書を作成
    - 運用項目一覧と運用フローを修正して発注者と合意する
    - 運用状況を報告するための報告書のフォーマットを作成する
    - 運用テスト仕様書を作成
### 運用テスト
  - 詳細設計で作成したドキュメントが運用上問題ないかのテスト行うフェーズ
  - 運用テストとして合意した運用フローが問題なく実施できるかと、作成した手順書が問題なく実施できるかという2つの観点でテストを実施
- 登場人物
    - 想定外な問題は常に人と人の間に発生する
    - 発注者側
        - システム責任者
            - プロジェクトの最終意思決定者
            - 定期的にプロジェクトの進捗の報告を受けて、会社として判断が必要な仕様変更、重要課題に対する対応方針の決定を行う
        - システム担当者
            - プロジェクトを含め、システムに対する発注者側の実担当者
            - プロジェクトマネージャー、プロジェクト各担当者とサービスの利用方法や機能の討議を行い、発注者側としてシステム設計を進める
            - システム責任者へプロジェクトの進捗報告、プロジェクト課題の社内調整
        - 運用担当者
            - システムリリース後の運用を行う担当者
            - プロyエクトを通じて情報連携を図り、運用テスト、運用引き継ぎフェーズでは受けてとしてプロジェクトに参加
    - SIベンダー側
        - プロジェクトマネージャー
            - プロジェクト全体の推進担当
            - 全体の進捗を管理して、発注者との課題、問題の調整を行う
            - 担当者間の調整
                - 運用設計担当と、プロジェクト全体に対して、運用上無理な設計がなされていないかをチェックする必要がある
        - アプリケーション担当
            - サービス提供するアプリケーションの開発担当
            - 発注者とディスカッションを行いながら、プロジェクトで導入を求められているサービスを提供できるアプリケーションの開発を行う
            - アプリケーション担当と連携しながら、サービスを利用するために行わなければならない作業、サービス開始に必要な情報を連携するための申請書やワークフローなどを取りまとめる
        - 基盤構築担当
            - システムの基盤部分の構築担当
            - 可用性要件やサービスレベルを維持するために、システムとしてどのような基盤機能を実装するかを考える
            - 基盤構築担当が実装した機能をいつどのような時に利用するかを考えていく
        - 運用設計担当
            - 追加する新システムの特徴と特徴と現行運用を理解して、その橋渡しをする担当
            - 構築したシステムが最大の効果を発揮できるように、ステークホルダーと調整
- 運用ドキュメント
    - 種類
        - 運用設計書
            - 運用項目ごとの方針、概要が記載されているドキュメント
            - 方針と合わせて、方針決定の理由やあえて採用しなかった方針なども記載する
        - 運用項目一覧
            - 導入するシステムで実施するすべての運用項目、作業項目、役割分担、関連ドキュメントが記載
        - 運用フロー図
            - 運用項目の中で、複数の役割が情報のやり取りをする場合、情報伝達方法、タイミングなどを図で表す
        - 運用手順書
            - 運用項目一覧記載の作業、運用フロー図内の処理プロセスを実施するために必要な手順をまとめたもの
        - 申請書
            - 運用フロー図内で情報連携のために必要項目をまとめたドキュメント
            - 社内ワークフローシステムなどで代替される場合がある
        - 台帳
            - 運用中に定期的に変更するデータを集めたドキュメント
        - 一覧
            - 運用中によく参照するパラメータ値などをカテゴリに集めたドキュメント
    - 運用ドキュメントが完成したら、運用テストで検証する必要あり
        - 運用テスト計画書
            - 運用テストの目的、実施範囲、スケジュールなどを取りまとめて記載
        - 運用テスト仕様書
            - 運用フローテスト、運用手順書テストの実施項目が記載されたドキュメント