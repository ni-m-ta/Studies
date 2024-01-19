# Overviews
- designed to automate the maagement and configuration of Windows operating systems and also used for other tasks, including application and system administration
- コマンドラインシェル、スクリプト言語、構成管理フレームワークで構成されるクロスプラットフォームのタスク自動化ソリューション
    - コマンドラインシェル
        - 一般的なシェルノ最良の機能を備えた最新のコマンドシェル
        - .NETオブジェクトを受け入れて返す
    - スクリプト言語
        - システムの管理の自動化に用いられる
        - CI/CD環境で、ソリューションをビルド、テスト、デプロイするため
    - 構成管理
        - 管理フレームワークであるPowerShell Desired Stare Configurationを使用すると、コードとしてインフラストラクチャを管理できる
    - Object-Oriented Pipeline
        - uses a pipeline that passes objects between commands, rather than just text
    - Cmdlets
        - small, single-purpose commands that perform specific functions. 
    - ISE
        - Integrated Scripting Environment
        - an integrated scripting environment that provides a graphical interface for writing, testing, and dubugging PowerShell scripts
    - Remoting
    - Module system
        - a waty to organize and distribute reusable units of code
        - a collection of cmdlets, functions, variables, and other assets that can be packaged together and easily shared or reused
        - module structure
            - a folder with a specific structure that contains the files and resources needed for the module
            - the module folder typically has the same name as the module itself
        - module manifest
            - a module includes a module manifest file that contains metadata about the module, such as its name, version, author, and required dependencies.
        - Exported cmdlets and functions
        - Automatic module loading
            - PowerShell can automatically load modules when a cmdlet or function from the module is used
        - module paths
            - PowerShell searches specific paths to find modules
            - these paths include system-wide locations and user-specific locations
        - module versioning
            - module supports versioning, allowing multiple versions of module to coexisit
        - module dependencies
            - module manifests can specify dependencies on other modules or modules of a specific version
        - Installation and removal
            - Online gallery
    - Closs-Platform support
    - Script execution policies
        - includes sript execution policies to control the execution of scripts on a system

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
- 

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
- スクリプトの作成
    - .PS1ファイルとして保存
- WMI
    - Windows Management Instrumentation
    - 非推奨
    - a set of specifications from Microsoft that defines a standardized way for Windows components to communicate with each other and with external systems
    - provides a consistent and unified interface for monitoring and managing various aspects of a Windows operating system and its components
        - Unified information representation
        - Standardized query language
        - Event notification
        - Remote management
        - Extensibility
        - Security
        - Integration with PowerShell
        - System administration and monitoring
- CIM
    - Common Information Model
    - Windowsマシンと非Windosマシンの両方で使用可能
    - used for managing and retrieving system-related information
    - PowerShell includes cmdlets that leverage CIM for system management tasks
    - roles
        - System information retrieval
        - Remote management
        - Hardware and software inventory
        - Event monitoring and notification
        - Performance monitoring
        - Configuration management
        - Security management
        - Application and service management
        - Storage management
        - Extensibility
- PowerShellではさまざまな方法でリモートコンピュータにコマンドを実行できる
    - PowerShellリモート処理コマンドを使用するには、リモートコンピューターでPowerShellリモート処理を有効にする必要がある
        - `Enable-PSRemoting`
    - 一対一のリモート処理
        - `Enter-PSSession`
    - 一対多のリモート処理
        - `Invoke-Command`
        - `Get-Service`入力後、実際にはリモートコンピューターで実行され、結果は逆シリアル化されたオブジェクトとして自身のローカルコンピューターに返される
            - 逆シリアル化
                - オブジェクトの状態をデータ形式から元の状態に戻すプロセス
                - データの永続化
                    - オブジェクトの状態をデータベースに保存する場合など、オブジェクトをバイト列に変換してデータ形式として永続化し、後で元に戻して再びオブジェクトとして使用
                - データの転送
                    - ネットワーク上でオブジェクトのデータを送受信する場合、オブジェクトをバイト列に変換して送信し、受信したら逆シリアル化して元のオブジェクトに戻す
                - プログラムとの相互運用性
                    - 異なるプログラムやプラットフォーム間でオブジェクトのデータを交換する場合、共通のデータ形式に変換して送受信する
                - セキュリティ
                    - 悪意のあるデータを含むシリアライズされたオブジェクトを逆シリアル化すると、セキュリティホールが生じる可能性がある
- 関数
    - 関数をスクリプトモジュールに置き、そのモジュールを`$env:PSModulePath`に置いて、関数を呼び出す
    - PowerShellGetモジュールを使用すると、NuGetリポジトリでこれらのモジュールを簡単に共有できる
    - 再利用するコードで、エイリアスと位置指定パラメーターを使用するのは避け、読みやすさを考えてコードと書式設定
    - 名前
        - 承認されている動詞と単数系の名前を含むパスカルケース
        - 名刺の前にプレフィックス
            - `{ApprovedVerb}-{Prefix}-{SingularNoun}`
        - `Get-Verb | Sort-Object -Property Verb`
            - 承認されている動詞の一覧
    - 単純な関数
        - ```powershell
            function Get-Version {
                $PSVersionTable.PSVersion
            }
            ```
    - パラメーター
        - 値を静的に割り当てるのではなく、パラメーターと変数を使用
        - パラメーターに名前をつけるときは、可能な限り規定のコマンドレットと同じ名前を、パラメーター名として使用
        - ```powershell
            function Test-MrParameter {
                param (
                    $ComputerName
                )
                Write-Output $ComputerName
            }
            ```
    - 高度な関数
        - 多くの共通パラメーターが自動的に追加される
        - ```powershell
            function Test-MrCmdletBinding {
                [CmdletBinding()] #<<-- This turns a regular function into an advanced function
                param (
                    $ComputerName
                )
                Write-Output $ComputerName
            }
            ```
            - ```powershell
                ComputerName
                Verbose
                Debug
                ErrorAction
                WarningAction
                InformationAction
                ErrorVariable
                WarningVariable
                InformationVariable
                OutVariable
                OutBuffer
                PipelineVariable
                ```
        - ```powershell
            function Test-MrSupportsShouldProcess {
                [CmdletBinding(SupportsShouldProcess)]
                param (
                    $ComputerName
                )
                Write-Output $ComputerName
            }
            ```
            - ```powershell
                ComputerName
                Verbose
                Debug
                ErrorAction
                WarningAction
                InformationAction
                ErrorVariable
                WarningVariable
                InformationVariable
                OutVariable
                OutBuffer
                PipelineVariable
                WhatIf
                Confirm
                ```
        - ```powershell
            function Test-MrParameterValidation {
                [CmdletBinding()]
                param (
                    [Parameter(Mandatory)]
                    [string]$ComputerName
                )
                Write-Output $ComputerName
            }
            ```
        - ```powershell
            function Test-MrParameterValidation {
                [CmdletBinding()]
                param (
                    [ValidateNotNullOrEmpty()]
                    [string[]]$ComputerName = $env:COMPUTERNAME
                )
                Write-Output $ComputerName
            }
            ```
            - 必須パラメーターでは規定値を使用できない。この場合、`ValidateNotNullOrEmpty`パラメータ検証属性を既定値と共に使用する
    - コメントアウト
        - `# Commentout`
        - `Write-Verbose -Message "By writing after the cmdlet, when trying to call the function with the parameter(Verbose), PoewrShell shows the comments"`
    - パイプライン入力
        - コマンドが受け入れることができるのは値またはプロパティ名によるパイプライン入力
        - 値によるパイプライン入力を受け入れるには、その特定のパラメーターに対して`ValueFromPipleline`パラメーター属性を指定する。
            - 配列を入力として受け入れる場合には、`process`ブロックがこれらの各項目を処理する必要がある
            - ```powershell
                function Test-MrPipelineInput {
                    [CmdletBinding()]
                    param (
                        [Parameter(Mandatory,
                                ValueFromPipeline)]
                        [string[]]$ComputerName
                    )
                    PROCESS {
                        Write-Output $ComputerName
                    }
                }
                ```
        - プロパティ名によるパイプライン入力の受け入れは、`ValueFromPipelineByPropertyName`パラメーター属性で指定され、データ型に関係なく、任意の数のパラメーターに対して指定できる
            - パイプ入力中のコマンドの出力には、関数のパラメーターまたはパラメーターエイリアスの名前と一致するプロパティ名が櫃王
            - `BEGIN`->パイプラインから項目が受信される前の初期処理->`PROCESS`->`END`
    - エラー
        - `Try/Catch`
            - ```powershell
                function Test-MrErrorHandling {
                    [CmdletBinding()]
                    param (
                        [Parameter(Mandatory,
                                ValueFromPipeline,
                                ValueFromPipelineByPropertyName)]
                        [string[]]$ComputerName
                    )
                    PROCESS {
                        foreach ($Computer in $ComputerName) {
                            try {
                                Test-WSMan -ComputerName $Computer
                            }
                            catch {
                                Write-Warning -Message "Unable to connect to Computer: $Computer"
                            }
                        }
                    }
                }
                ```
            - ```powershell
                function Test-MrErrorHandling {
                    [CmdletBinding()]
                    param (
                        [Parameter(Mandatory,
                                ValueFromPipeline,
                                ValueFromPipelineByPropertyName)]
                        [string[]]$ComputerName
                    )
                    PROCESS {
                        foreach ($Computer in $ComputerName) {
                            try {
                                Test-WSMan -ComputerName $Computer -ErrorAction Stop
                            }
                            catch {
                                Write-Warning -Message "Unable to connect to Computer: $Computer"
                            }
                        }
                    }
                }
                ```
                - 終了しないエラーを終了する
    - コメントベースのヘルプ
        - 関数にはコメントベースのヘルプを追加
        - ```powershell
            function Get-MrAutoStoppedService {

            <#
            .SYNOPSIS
                Returns a list of services that are set to start automatically, are not
                currently running, excluding the services that are set to delayed start.
            .DESCRIPTION
                Get-MrAutoStoppedService is a function that returns a list of services from
                the specified remote computer(s) that are set to start automatically, are not
                currently running, and it excludes the services that are set to start automatically
                with a delayed startup.
            .PARAMETER ComputerName
                The remote computer(s) to check the status of the services on.
            .PARAMETER Credential
                Specifies a user account that has permission to perform this action. The default
                is the current user.
            .EXAMPLE
                Get-MrAutoStoppedService -ComputerName 'Server1', 'Server2'
            .EXAMPLE
                'Server1', 'Server2' | Get-MrAutoStoppedService
            .EXAMPLE
                Get-MrAutoStoppedService -ComputerName 'Server1' -Credential (Get-Credential)
            .INPUTS
                String
            .OUTPUTS
                PSCustomObject
            .NOTES
                Author:  Mike F Robbins
                Website: http://mikefrobbins.com
                Twitter: @mikefrobbins
            #>
                [CmdletBinding()]
                param (
                )
                #Function Body
            }
            ```
    - 困ったとき
        - 別のモニターでISEの2番目のコピーを開き、関数のコードを入力しながら`Cmdlet(advanced function) - Complete`スニペットを表示。巣日ペットにアクセスするには、PowerShell ISEでCtrl+J
- スクリプトモジュール
    - PowerShellのワンライナーやスクリプトを頻繁に使用する予定がある場合、再利用可能なツールに変換する作業が、より重要
    - ```powershel
        MyModule\
            MyModule.psd1
            MyFunction.ps1
            ```
    - `Import-Module MyModule`
    - ドットソース関数
        - スクリプトの関数がモジュールの一部ではない場合、その関数をメモリに読み込むには、それが保存されている`.PS1`ファイルをドットソースする必要がある
        - 関数がScriptスコープに読み込まれている場合、スクリプトが完了するとそのスコープは削除され、そのスコープと一緒に関数も削除される
        - 関数はGlobalスコープに読み込む必要がある
        - そのために関数を含むスクリプトをドットソースする
            - `. .\Get-MrPSVersion.ps1`
            - `. C:\Demo\Get-MrPSVersion.ps1`
    - スクリプトモジュール
        - 1つ以上の関数を含むファイル
        - `.PSM1`
    - モジュールマニフェスト
        - すべてのモジュールにモジュールマニフェストが必要
        - モジュールマニフェストには、モジュールに関するメタデータが含まれる
        - `.PSD1`
        - [How to write a module manifest](https://learn.microsoft.com/en-us/powershell/scripting/developer/module/how-to-write-a-powershell-module-manifest?view=powershell-7.4)
    - How to define modules
        1. Move to designated folder
            - C:\Users\nisatot\Documents\WindowsPowerShell\Modules
            - C:\Program Files\WindowsPowerShell\Modules
            - C:\Windows\system32\WindowsPowerShell\v1.0\Modules
        1. Create a module folder
        1. Under the created module folder, create a module file
            - `New-Item {FileName.ps1}`
        1. Store codes into a variable
            - ```powershell
                $code = {
                    function Say-Hello {
                        param(
                            [string]$Name
                        )
                        PROCESS {
                            Write-Output "Hello, $Name"
                        }
                    }
                }
                ```
        1. Write codes in the file
            - `Set-Content -Path .\MyFunctions.ps1 -Value $code`
        1. Dot source
            - `. .\MyFunctions.ps1`
        1. Done
    - Public/Private functions
        - helper functions
            - a function that performs a specific task or provides utility within a script or module
        - `Export-ModuleMember -Function {FunctionNameDefined}`
            -  .psm1ファイル内に記述
            - 指定した関数のみ外部で使用可能
        - `FunctionsToExport = '{FunctionNameDefined}'`
            - .psd1ファイル内に記述
- 文字コード
    - default
        - ```powershell
            IsSingleByte      : True
            BodyName          : us-ascii
            EncodingName      : US-ASCII
            HeaderName        : us-ascii
            WebName           : us-ascii
            WindowsCodePage   : 1252
            IsBrowserDisplay  : False
            IsBrowserSave     : False
            IsMailNewsDisplay : True
            IsMailNewsSave    : True
            EncoderFallback   : System.Text.EncoderReplacementFallback
            DecoderFallback   : System.Text.DecoderReplacementFallback
            IsReadOnly        : True
            CodePage          : 20127
            ```
        - `437`
    - 変換方法
        - chcp
            - 文字コード表を指定する
                - 結果: chcpの値は変わるが、日本語入力ができない
            - 文字コード表
                - 932: Shift_JIS
                - 20127: US-ASCII
                - 65001: UTF-8
            - `chcp`
                - 現在の文字コード確認
            - `chcp {AnyChrCode}`
                - 指定した文字コードに変換
        - `$OutputEncoding = [System.Text.Encoding]::[System.Text.Encoding]::UTF8`
            - OutputEncodingを指定
                - 結果: OutputEncodingの中身は変わるが、日本語入力できない
        - `$OutputEncoding = [Console]::InputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8`
            - 結果: 日本語入力が可能になった
                - どうやらコンソールの言語も変える必要がある
                - 一応動くが、ISEのコンソール上ではエラーが出る。
                    - ```powershell
                         Exception setting "InputEncoding": "The handle is invalid.
                        "
                        At C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1:2 char:1
                        + [Console]::InputEncoding = [System.Text.Encoding]::UTF8
                        + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            + CategoryInfo          : NotSpecified: (:) [], SetValueInvocationException
                            + FullyQualifiedErrorId : ExceptionWhenSetting
                        
                        Exception setting "OutputEncoding": "The handle is invalid.
                        "
                        At C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1:3 char:1
                        + [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
                        + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            + CategoryInfo          : NotSpecified: (:) [], SetValueInvocationException
                            + FullyQualifiedErrorId : ExceptionWhenSetting 
                        ```
            - $OutputEncoding
                - 環境変数
            - []
                - クラス
            - `::`
                - スタティックなメンバにアクセスする場合
                    - スタティック
                        - インスタンスを生成しなくても、アクセスできるメソッドやプロパティ
                    - 普通のメソッドの呼び出しでは`.`を使うが、スタティックなメソッドでは`::`を使える
        - `$PSDefaultParameterValues['*:Encoding'] = 'utf8'`
            - [ドキュメント推奨の方法](https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_character_encoding?view=powershell-7.4)
            - 結果: できない
            - PowerShellのバージョンのせいもあるかも(検証環境: v:5.1)
- Profile
    - a script that runs when PowerShell starts
    - able to add commands, aliases, functions, variables, modules, PowerShell drives,...
    - Users/Hosts
        - 適用可能なprofileパスの確認
            - `$profile | Get-Member | where MemberType -eq NoteProperty`
        - User Profile
            - Scope: specific to an individual user account
                - Current user, Current hosts: 
                    - `$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1`
                    - `$profile`
            - allows users to customize their PowerShell environment based on their preferences
        - Host Profile
            - Scope: specific to a PowerShell host or console
                - All users, All hosts: 
                    - `$PSHOME\Profile.ps1`
                    - `$profile.AllUsersAllHosts`
            - allows administrators to define settings or configurations that should be applied to all users when they start PowerShell on a speciic host
    - How to set up
        1. Check an execution policy
            - [document](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4&viewFallbackFrom=powershell-6)
            1. input `Get-ExecutionPolicy`
            1. If you got, `Unrestricted`, file
            1. If not, input `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`
        1. Check whether a profile exists or not
            1. input `Test-Path $profile`
            1. If it returns false, the input `New-Item -Path $profile -Type File -Force`
        1. Edit the PowerShell Profile
            1. input `ise $profile`
- Execution Policy
    - a security feature that determines the conditions under which PowerShell loads configuration files and rns scripts
    - classifications
        - Restricted
            - No scripts are allowed to run
            - can be used only for interactive commands
        - AllSigned
            - only scripts singed by a trusted publisher are allowed to run
            - scripts must have a digital signature from a trusted publisher to run
        - RemoteSinged
            - Local scripts can run without a digital signature
            - donladed scripts need to be singed by a trusted publisher
        - Unrestricted
            - No digital signatures are required
            - all scripts can run
            - least restrictive policy
        - Bypass
            - No restrictions
            - all scripts can run
        - Undefined
            - no execution policy is set
            - PowerShell operates in Undefined mode untile a policy is explicitly set
- PowerShell ISE
    - a GUI application designed specifically for PowerShell scipt dev
    - provides a script editor with features like syntax highligting, debugging, and script execution panes 
- WinRM
    - WIndows Remote Management
    - a management prtocol used by Windows operating systems to enable the remote management of computers, servers, and devices over a network
    - communication protocol
        - uses a SOAP-based protcol over HTTP or HTTPS
    - configuration
        - WinRM must be configured on both the client and the server
    - authentication
        - supports various authentication methods
        - Kerberis
        - NTLM
        - Basic authentication
    - Trusted hosts
        - to establish a connection between machine that are not part of the same domain, might need to configure TrustedHosts setting
        - specifying which remote computers are trusted to receive commands
    - Encryption
        - supports encryption through the use of HTTPS
    - Fiarewall consideration
        - Firewall rules must be configured to allow WinRM traffic
        - default
            - HTTP: 5985
            - HTTPS: 5986
- AzureRM PowerShell Module 2 Az PowerShell Module
    - 2024/02/29に完全移行
- Az PowerShell
    - 利点
        - セキュリティと安定性
            - トークンキャッシュの暗号化
            - 中間者攻撃の防止
            - ADFS 2019による認証のサポート
            - PowerShell7でのユーザー名とパスワード認証
            - 継続的アクセス評価のようなサポート
        - すべてのAzureサービスのサポート
            - 一般提供されているすべてのAzureサービスでは対応するPowerShellモジュールがサポートされる
        - 新機能
            - Cloud Shellとクロスプラットフォームでのサポート
            - アクセストークンを取得し、Azureリソースにアクセスするための
            - Azureリソースを使用した高度なREST操作に使用できるCLI



# Cases
- send a file in a Windows Server A to a Windows Server B
    - answer from documents
        - ```powershell
            $Session = New-PSSession -ComputerName "Server01(In Azure you can check from 'Computer name')" -Credential "Contoso\User01"
            Copy-Item "D:\Folder001\test.log" -Destination "C:\Folder001_Copy\" -ToSession $Session
            ```
        - [document](https://learn.microsoft.com/ja-jp/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.4)
    - problems
        - ` FullyQualifiedErrorId : ServerNotTrusted,PSSessionOpenFailed`
            - an issue with trust between the machines when attempting to establish a PowerShell remoting session
    - Solution
        - [Procedures](https://4sysops.com/archives/connect-to-azure-vm-using-powershell/)
        1. Prerequisits
            - Host (Machine operated remotely)
                - `Install-Module AzureRM`
                    - Install the Azure Resource Manager PowerShell module
                    - `Install-Module Az`
                - `Connect-AzAccount`
                    - login Azure
                    - `Connect-AzAccount -Tenant {TenantID} -Subscription {SubscriptionID}`
            - Client (Machine operating locally)
                - `Start-Service WinRM`
                    - Verify the WinRM service is running
                - `Set-Item WSMan:\localhost\Client\TrustedHosts -Value {PublicIPAddressOfTheVMToConnect}`
                    - Add the VM's public IP address to the trusted hosts 
                    - `Get-Item WSMan:\localhost\Client\TrustedHosts`
                        - Check the current trusted VM's public IP address 
        1. Open the ports in the network security group
            - Host
                - ```powershell
                    Get-AzureRmNetworkSecurityGroup -Name {NSGNameInYourResourceGroupStoringHostVM} -ResourceGroupName {NameOfYourResourceGroupStoringHostVM} | Add-AzureRmNetworkSecurityRuleConfig -Name AllowingWinRMHTTPS -Description "To Enable PowerShell Remote Access" -Access Allow -Protocol Tcp -Direction Inbound -Priority 102 -SourceAddressPrefix Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 5986 | Set-AzureRmNetworkSecurityGroup
                    Get-AzureRmNetworkSecurityGroup -Name {NSGNameInYourResourceGroupStoringHostVM} -ResourceGroupName {NameOfYourResourceGroupStoringHostVM} | Add-AzureRmNetworkSecurityRuleConfig -Name AllowingWinRMHTTP -Description "To Enable PowerShell Remote Access" -Access Allow -Protocol Tcp -Direction Inbound -Priority 103 -SourceAddressPrefix Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 5985 | Set-AzureRmNetworkSecurityGroup
                    ```
                    - ```powershell
                        Get-AzNetworkSecurityGroup -Name {NSGNameInYourResourceGroupStoringHostVM} -ResourceGroupName {NameOfYourResourceGroupStoringHostVM} | Add-AzNetworkSecurityRuleConfig -Name AllowingWinRMHTTPS -Description "To Enable PowerShell Remote Access" -Access Allow -Protocol Tcp -Direction Inbound -Priority 102 -SourceAddressPrefix Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 5986 | Set-AzNetworkSecurityGroup
                        Get-AzNetworkSecurityGroup -Name {NSGNameInYourResourceGroupStoringHostVM} -ResourceGroupName {NameOfYourResourceGroupStoringHostVM} | Add-AzNetworkSecurityRuleConfig -Name AllowingWinRMHTTP -Description "To Enable PowerShell Remote Access" -Access Allow -Protocol Tcp -Direction Inbound -Priority 103 -SourceAddressPrefix Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 5985 | Set-AzNetworkSecurityGroup
                        ```
        1. Preparing to access the VM using PowerShell
            - Host
                1. `New-Item -ItemType File -Path {AnyPathForScriptFile}`
                1. ```powershell
                    $Content = "winrm qc /force
                    netsh advfirewall firewall add rule name= WinRMHTTP dir=in action=allow protocol=TCP localport=5985
                    netsh advfirewall firewall add rule name= WinRMHTTPS dir=in action=allow protocol=TCP localport=5986"
                    ```
                    - Enable WinRM on the VM
                    - Open the required WinRM firewall ports on hte VM if the local WIndows Firewall is activated
                1. ```powershell
                    Invoke-AzureRmVMRunCommand -ResourceGroupName {NameOfResourceGroupStroingHostMachine} -Name {HostMachineName} -CommandId "RunPowerShellScript" -ScriptPath C:\injectedscript.ps1
                    ```
                    - ```powershell
                        Invoke-AzVMRunCommand -ResourceGroupName {NameOfResourceGroupStroingHostMachine} -Name {HostMachineName} -CommandId "RunPowerShellScript" -ScriptPath C:\injectedscript.ps1
                        ```
                    - Run the script in the created file inside the VM
        1. Connect to the VM using PowerShell
            - Client
                - `Enter-PSSession -ComputerName {PublicIPAddressOfHostMachine}`
- do tasks automatically
    - Description
        - more specifically, send a file from a Windows Server A to a Windows Server B via PowerShell with Time Schduler
    - Solution
        1. Create a script file
        1. Register a schedule
            - `Register-ScheduledTask -TaskName {TaskName} -Trigger {TriggerLikeWhenOrWhere} -Action {ActionToExecute}`
                1. `$Trigger = New-SchduledTaskTrigger -At {00:00~23:59} -Once/-Daily/...`
                1. `$Action = New-SchduledTaskAction -Execute {ProgramsToExecuteLikePowerShell.exe} -Argument {ScriptFileAbsPathToExecute}`
                1. `Register-Scheduled -TaskName {TaskName} -Trigger $Trigger -Action $Action`
            - You can see Timer Sceduler
            - `Set-ScheduledTask -TaskName {TaskName} -Trigger -Action`
                - modify a schduled task
            - `Stop-ScheduledTask -TaskName {TaskName}`
                - Stop the current running task
            - `Unregister-ScheduledTask -TaskName {TaskName}`
                - Remove a scheduled task
            - `Get-ScheduledTaskInfo -TaskName {TaskName}`
                - get detail info of a schduled task
- set up UTF-8 as the default char codes for PowerShell
    - Description
        - When booting PowerShell, run a $Profile to execute commands automatically
    - Keywords
        - `$Profile`: current user, current host
        - `$Profile.AllUsersAllHosts`: all user, all hosts
    - Solution
        1. Check an execution policy
            - [document](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4&viewFallbackFrom=powershell-6)
            1. input `Get-ExecutionPolicy`
            1. If you got, `Unrestricted`, file
            1. If not, input `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`
        1. Check whether a profile exists or not
            1. input `Test-Path $profile`
            1. If it returns false, the input `New-Item -Path $profile -Type File -Force`
        1. Edit the PowerShell Profile
            1. input `ise $profile`
            1. write the following codes
                - ```powershell
                    # To set the character code as UTF-8
                    [Console]::InputEncoding = [System.Text.Encoding]::UTF8
                    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
                    $OutputEncoding = [System.Text.Encoding]::UTF8 
                    ```


# Commands
- `break`
    - ループから抜け出す
    - ```powershell
        for ($i = 1; $i -lt 5; $i++) {
            Write-Output "Sleeping for $i seconds"
            Start-Sleep -Seconds $i
            break
            }
        ```
- `continue`
    - ループの次の反復にスキップ
    - ```powershell
        while ($i -lt 5) {
            $i += 1
            if ($i -eq 3) {
                continue
            }
            Write-Output $i
        }
        ```
- `do`
    - `do until`
        - 指定された条件がfalseの間実行される
        - ```powershell
            $number = Get-Random -Minimum 1 -Maximum 10
            do {
            $guess = Read-Host -Prompt "What's your guess?"
            if ($guess -lt $number) {
                Write-Output 'Too low!'
            }
            elseif ($guess -gt $number) {
                Write-Output 'Too high!'
            }
            }
            until ($guess -eq $number)
            ```
    - `do while`
        - 指令された条件がtrueの間実行される
        - ```powershell
            $number = Get-Random -Minimum 1 -Maximum 10
            do {
            $guess = Read-Host -Prompt "What's your guess?"
            if ($guess -lt $number) {
                Write-Output 'Too low!'
            } elseif ($guess -gt $number) {
                Write-Output 'Too high!'
            }
            }
            while ($guess -ne $number)
            ```
- `Enable-PSRemoting`
    - リモートコンピューターでPowerShellリモート処理を有効にする
- `Enter-PSSession`
    - 一対一のPowerShellリモート処理セッションを作成
    - `Enter-PSSession -ComputerName dc01 -Credential $Cred`
        `$Cred = Get-Credential`
- `$env:PSModulePath -split ';'`
    - モジュールの配置場所一覧を表示
- `Exit-PSSession`
    - 一対一のリモート処理セッションの終了
- `Export-ModuleMember -Function {FunctionNameDefined}`
    -  .psm1ファイル内に記述
    - 指定した関数のみ外部で使用可能
- `Find-Module`
    - PowerShellギャラリーにあるモジュールを検索する
    - `Find-Module -Name {AnyModuleName}`
    - `Find-Module -Name {AnyModuleName} | Install-Module`
        - モジュールのインストール
- `for`
    - 指定された条件がtrueである間、処理が繰り返される
    - ```powershell
        for ($i = 1; $i -lt 5; $i++) {
            Write-Output "Sleeping for $i seconds"
            Start-Sleep -Seconds $i
            }
            ```
- `ForEach-Object`
    - PowerShellワンライナーなどを使用してパイプライン内の項目を反復処理する
        - `Get-Command`のModuleパラメータは、文字列である複数の値を取得。プロパティ名によるパイプライン入力経由またはパラメーター入力経由でのみ、値を受け取る
            - ```powershell
                'ActiveDirectory', 'SQLServer' | ForEach-Object {Get-Command -Module $_} | Group-Object -Property ModuleName -NoElement | Sort-Object -Property Count -Descending ```
        - ```powershell
            $ComputerName = 'DC01', 'WEB01'
            foreach ($Computer in $ComputerName) {
            Get-ADComputer -Identity $Computer
            }
            ```
            - foreachを使う時は、反復処理するすべての項目を事前にメモリに格納する必要がある。 
- `Format-List`
    - 規定の書式設定をオーバーライドし、結果をリストで返す。
- `Format-Table`
    - 書式設定を手動でオーバーライドし、リストではなくテーブルに出力する
- `Get-Alias`
    - エイリアスを見つける
    - `Get-Alias -Name {AnyAlias}`
    - `Get-Alias -Definition {AnyCmdlet}, {AnyCmdlet}`
- `Get-ChildItem`
    - 格納されたアイテムの取得
    - `Get-ChildItem -Path Function:\{FunctionNameLookedFor}`
        - `Get-ChildItem -Path Function:\Get-*Version`
        - `Get-ChildItem -Path Function:\Get-*Version | Remove-Item`
            - 登録した関数を現在のセッションから削除
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
        - `Get-Command -Noun WMI*`
            - WMIコマンドのの検索
        - `Get-Command -Module CimCmdlets`
            - CIMコマンドの検索
- `Get-Content`
    - ファイルの中身を表示
    - `Get-Content {FileName}`
- `Get-Credential`
    - ドメイン管理者または管理者特権の資格情報の取得
    - `$Cred = Get-Credential`
        - 資格情報を変数に格納
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
- `Get-ScheduledTaskInfo`
    - Show a scheduled task's info
    - ` Get-ScheduledTaskInfo -TaskName {TaskName}`
- `Get-Service`
    - サービスの一覧とその状態を取得するためのコマンドレット
- `Get-Verb`
    - 動詞一覧を表示
    - `Get-Verb | Sort-Object -Property Verb`
        - 承認されている動詞の一覧
- `help {AnyCmdlet} -Parameter Name`
    - 指定したコマンドレットの概要を出力
- `Import-Module -Name {AnyModule}`
    - 指定したモジュールをインポート
- `Invoke-Command`
    - 一対多のリモート処理を行う
    - `Invoke-Command -ComputerName dc01, sql02, web01 {Get-Service -Name W32time} -Credential $Cred`
- `New-Item`
    - ファイルの新規作成
    - `New-Item {FileName}`
- `New-ModuleManifest`
    - モジュールマニュフェストを作成
    - PowerShellGetを使用してモジュールをNuGetリポジトリにアップロードする場合に備えて、AuthorとDescriptionを指定した方がいい
    - ```powershell
        New-ModuleManifest -Path $env:ProgramFiles\WindowsPowerShell\Modules\MyScriptModule\MyScriptModule.psd1 -RootModule MyScriptModule -Author 'Mike F Robbins' -Description 'MyScriptModule' -CompanyName 'mikefrobbins.com'
        ```
- `New-PSSession`
    - リモートコンピューターに対して複数のコマンドを実行可能
    - コマンドごとに新しいセッションを使用するオーバーヘッドは発生しない
    - `$Session = New-PSSession -ComputerName dc01, sql02, web01 -Credential $Cred`
- `$PSVersionTable`
    - PowerShellに関するバージョン情報を表示
- `Register-ScheduledTask`
    - registers a scheduled task definition on a local computer
    - ```powershell
        $Time = New-ScheduledTaskTrigger -At 12:00 -Once
        $User = "Contoso\Administrator"
        $PS = New-ScheduledTaskAction -Execute "PowerShell.exe"
        Register-ScheduledTask -TaskName "SoftwareScan" -Trigger $Time -User $User -Action $PS
        ```
- `Remove-Module`
    - 現在のPowerShellセッションのメモリからモジュールが削除
    - ただしシステムまたはディスクからは削除されない
    - `Remove-Module -Name {ModuleName}`
- `Remove-PSSession`
    - 使い終わったセッションの削除
    - `Get-PSSession | Remove-PSSession`
- `Return`
    - 既存のスコープを終了
    - ```powershell
        $number = 1..10
        foreach ($n in $number) {
            if ($n -ge 4) {
                Return $n
            }
        }
        ```
- `Set-Content`
    - ファイルにコードを記述
    - ```powershell
        # Define the file path
        $filePath = "C:\Path\To\Your\File.ps1"
        # Define the code to write
        $code = @"
        # Your PowerShell code here
        Write-Host "Hello, World!"
        "@
        # Write the code to the file
        Set-Content -Path $filePath -Value $code -Force
        ```
- `Set-ExecutionPolicy`
    - 実行ポリシーを変更する
    - `Set-ExecutionPolicy RemoteSigned`
- `Start-Process`
    - ネイティブコマンドを実行するために使用可能
    - コマンドの実行方法を制御する必要がある場合のみ使用
    - 用途
        - 別の資格情報を使ってコマンドを実行
        - 新しいプロセスによって作成されるコンソールウィンドウを非表示にする
        - stdin, stdout, stderrストリームをリダイレクトする
        - コマンドに対して別の作業をする
- `Set-ScheduledTask`
    - modify and a scheduled task
    - ```powershell
        PS C:\> $Time = New-ScheduledTaskTrigger -At 12:00 -Once
        PS C:\> Set-ScheduledTask -TaskName "SoftwareScan" -Trigger $Time
        ```
- `UnInstall-Module`
    - `Uninstall-Module {AnyModuleNameToUninstall}`
- `while`
    - 指定された条件がtrueである場合、実行
    - コードが実行される前にループの先頭で条件が評価
    - ```powershell
        $date = Get-Date -Date 'November 22'
        while ($date.DayOfWeek -ne 'Thursday') {
        $date = $date.AddDays(1)
        }
        Write-Output $date
        ```