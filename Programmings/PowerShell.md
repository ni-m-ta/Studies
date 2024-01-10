# Overviews
- コマンドラインシェル、スクリプト言語、構成管理フレームワークで構成されるクロスプラットフォームのタスク自動化ソリューション
    - コマンドラインシェル
        - 一般的なシェルノ最良の機能を備えた最新のコマンドシェル
        - .NETオブジェクトを受け入れて返す
    - スクリプト言語
        - システムの管理の自動化に用いられる
        - CI/CD環境で、ソリューションをビルド、テスト、デプロイするため
    - 構成管理
        - 管理フレームワークであるPowerShell Desired Stare Configurationを使用すると、コードとしてインフラストラクチャを管理できる
- PowerShell コマンド
    - コマンドレット
        - ネイティブのPowerShellコマンドであり、スタンドアロンの実行可能ファイルではない。
        - 必要に応じて読み込み可能なPowerShellモジュールにまとめられる
        - 任意のコンパイルされた.NET言語またはPowerShellスクリプト言語自体で記述可能
- PowerShellの用途
    - Windowsタスクの自動化
    - クラウド管理
        - クラウドリソース管理。クラウドのリソースに関する情報の取得、新しいリソースの更新または配置
    - CI/CD
        - 継続的インテグレーション/継続的配置パイプラインの一部として使用
    - Active DirectoryとExchangeのタスクの自動化
        - Active Directoryのユーザーや、Exchangeのメールボックスの作成など、Windowsでのほぼすべてのタスクを自動化
- 権限
    - 通常のドメインユーザー
    - ローカル管理者であるドメインユーザー
        - Run as administrator
- 実行ポリシー
    - ユーザーが無意識のうちにスクリプトを実行するのを防ぐ
    - RemoteSigned Policy
        - ダウンロードしたスクリプトを実行する際に、スクリプトが信頼できる公開元によって署名されていることが求められる

# Rules
- Syntax
    - []
        - パラメータ名
        - パラメーター名とデータ型の全体が[]で囲まれている場合、省略可能なパラメーター
        - データ型の後のみに表示される空[]もあり、その型の値を複数受け入れることが可能
    - <>
        - データ型
        - データ型の指定がない場合、スイッチパラメーター
        - このパラメーターが指定されている場合、値はTrue。そうでない場合、False
- One Liner
    - 1つの連続パイプラインであり、必ずしも1つの物理業にあるコマンドではない
- パラメーターをできるだけ指定して、必要な情報のみを取得するようにする
- パイプライン
- PowerShellGet
    - NuGetリポジトリとの間でPowerShellモジュールの検出、インストール、発行、更新を行うためのPowerShellモジュール
    - MSは、PowerShellギャラリーというオンラインNuGetリポジトリをホストしている
    - 大半はOSS
    - 使用する前に悪意がないものであることを十分に確認する必要がある
- 左でフィルター処理、右で書式設定
- エイリアス
    - 短いコマンド名
    - 独自のエイリアスを定義することも可能
- プロバイダー
    - 様々なデータに対して、PowerShellで柔軟に操作できるよってこと
    - データストアに、ファイルシステムのようにアクセスできるようにするインターフェイス
        - レジストリ
        - エイリアス
        - 環境変数
        - ファイルシステム
        - 関数
        - 変数
        - 証明書
        - WSMan
- 比較演算子
    - `-eq`
    - `-ne`
    - `-gt`
    - `-ge`
    - `-lt`
    - `-le`
    - `-Like`
        - *を使用した一致
        - `'PowerShell' -like '*shell'`
            - `True`
    - `-NotLike`
        - *を使用した不一致
    - `-Match`
        - 指定した正規表現と一致
        - `'PowerShell' -match '^*.shell$'`
            - `True`
    - `-NotMatch`
        - 指定した正規表現と不一致
    - `-Contains`
        - コレクションに指定した値が含まれているかどうかを確認する
    - `-NotContains`
        - コレクションに特定の値が含まれていないことを確認する
    - `-In`
        - 指定した値がコレクションに存在するかどうかを確認する
        - `$Numbers -contains 15`
            - `True`
    - `-NotIn`
        - 指定した値がコレクションに存在していないことを確認する
    - `-Replace`
        - 指定した値を置き換える
        - `'PowerShell' -replace 'Shell'`
            - `Power`
        - `'SQL Saturday - Baton Rouge'.Replace('saturday','Sat')`
            - `SQL Saturday - Baton Rouge`
- 範囲演算子
    - `$VARIABLE = X..Y`
        - `$Numbers = 1..10`

# Commands
- `Find-Module`
    - PowerShellギャラリーにあるモジュールを検索する
    - `Find-Module -Name {AnyModuleName}`
    - `Find-Module -Name {AnyModuleName} | Install-Module`
        - モジュールのインストール
- `Format-List`
    - 規定の書式設定をオーバーライドし、結果をリストで返す。
- `Format-Table`
    - 書式設定を手動でオーバーライドし、リストではなくテーブルに出力する
- `Get-Alias`
    - エイリアスを見つける
    - `Get-Alias -Name {AnyAlias}`
    - `Get-Alias -Definition {AnyCmdlet}, {AnyCmdlet}`
- `Get-Command`
    - コマンドを見つけるため
    - 使用可能なすべてのコマンドの一覧を表示
    - パラメーターやヘルパーコマンドレットを使って応答をフィルター処理する
        - `Get-Command -Name Get-Process`
        - `Get-Command -Name *-Process`
        - `Get-Command -Verb 'Get'`
        - `Get-Command -Noun U*`
        - `Get-Command | Select-Object -First 5 -Property Name, Source`
        - `Get-Command -Name {AnyProcess} -Syntax`
            - コマンドの使用方法を確認
        - `Get-Command -Module ActiveDirectory`
            - ActiveDirectory PowerShell モジュールの一部として追加されたコマンドを確認
- `Get-ExecutionPolicy`
    - 現在の実行ポリシー設定を確認
- `Get-Help`
    - どういうコマンドかを知るため
    - あるコマンドを見つけた後に、そのコマンドの使用方法を確認する上で役立つ
    - 初めて実行した際、`Do you want to run Update-Help?...`が表示される。実行後、PowerShellヘルプをダウンロードする。
    - `Get-Help {AnyCmdlet}`
    - `Get-Help -Name {AnyCmdlet} -Full`
    - `Get-Help -Name {AnyCmdlet} -Detailed`
    - `Get-Help -Name {AnyCmdlet} -Examples`
    - `Get-Help -Name Get-Command -Online`
- `Get-Member`
    - コマンドで使用できるオブジェクト、プロパティ、及びメソッドを調べるのに役立つ
    - `{AnyCmdlet} | Get-Member`
        - オブジェクトの種類
    - `{AnyCmdlet} | Get-Member -MemberType Method`
        - メソッドの表示
- `Get-MrPipelineInput -Name {AnyCmdlet}`
    - コマンドのどのパラメーターがパイプライン入力を受け取るのか、それらが受け取るオブジェクトの種類は何か、値とプロパティ名のどちらによるパイプライン入力が受け取られるのか、が簡単に特定できる。
- `Get-Process`
    - 実行中のプロセスを確認するためのコマンドレット
- `Get-PSProvider`
    - 使用可能なPowerShellプロバイダーを表示
- `Get-Service`
    - サービスの一覧とその状態を取得するためのコマンドレット
- `Get-Verb`
    - 動詞一覧を表示
- `help {AnyCmdlet} -Parameter Name`
    - 指定したコマンドレットの概要を出力
- `Import-Module -Name {AnyModule}`
    - 指定したモジュールをインポート
- `$PSVersionTable`
    - PowerShellに関するバージョン情報を表示
- `Set-ExecutionPolicy`
    - 実行ポリシーを変更する