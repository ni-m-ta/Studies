# Web概論
## Webとは
- 用途
    - Webサイト
    - UI
    - API
- Web
    - ハイパーメディア
        - テキストや画像、音声、映像など様々なメディアをハイパーリングで結びつけて構成したシステム
    - 分散システム
        - 複数のコンピュータを組み合わせて処理を分散させる形式
## REST
- RESTはWebのアーキテクチャスタイル
- リソース
    - web上の情報である
    - 世界中の無数のリソースは、それぞれURIで一位の名前を持つ
    - URIを用いることで、プログラムはリソースが表現する情報にアクセスできる
    - Resource Representation
        - サーバとクライアントの間でやり取りするデータ
- クライアント/サーバ
    - ステートレスサーバ
        - クライアントのアプリケーション状態をサーバで管理しない
        - ただしCookieを使ったセッション管理は、例外
    - キャッシュ
        - リソースの鮮度に基づいて、一度取得したリソースをクライアント側で使い回す方式
        - サーバとクライアントの間の通信を減らすことでネットワーク帯域の利用や処理時間を縮小し、より効率的に処理できること
    - 統一インターフェース
        - URIでさし示したリソースに対する操作を、統一した限定的なインターフェースで行う
        - APIのメソッド
    - 階層化システム
        - システム全体が階層化しやすい
        - サーバとクライアントの間にロードバランサーを設置して負荷分散
        - プロキシを設置してアクセス制限
    - コードオンデマンド
        - プログラムコードをサーバからダウンロードし、クライアント側でそれを実行する
        - 利点は、クライアントを後から拡張できる
        - 欠点は、ネットワーク通信におけるプロトコルの可視性が低下すること
- REST/Hyper Media
    - Hypermedia as the engine of application state
# URI
## URIの仕様
- URI
    - Uniform Resource Identifier
    - リソースを統一的に識別するID
- 構文
    - URIスキーム
        - そのURIが利用するプロトコル
    - ホスト名
        - DNSで名前解決ができるドメイン名かIPアドレス
    - パス
        - そのホストの中でリソースを一意に示す
    - クエリパラメータ
        - クライアントから動的にURIを生成するときに利用
    - URIフラグメント
        - さらに細かい部分を特定するときに利用
- ASCII以外の文字を入れるときは、%エンコーディングをしている
## URIの設計
- アンチパターン
    - プログラミング言語に依存した拡張子やパスを含める
    - メソッド名やセッションIDを含める
    - URIはリソースを表現する名詞以外のものを使う
        - URIとHTTPメソッドの関係は、名詞と動詞の関係
- セミコロン
    - パラメータの順序が意味を持たない場合に用いる
- コンマ
    - パラメータの順序が意味を持つ場合
- クライアント側からの不透明性
# HTTP
## HTTPの基本
- リクエストとレスポンス
    - クライアントで行われること
        - リクエストメッセージの構築
        - リクエストメッセージの送信
        - レスポンスが返るまで待機
        - レスポンスメッセージの受信
        - レスポンスメッセージの解析
        - クライアントの目的を達成するために必要な処理
    - サーバで行われること
        - リクエストの待機
        - リクエストメッセージの受信
        - リクエストメッセージの解析
        - 適切なアプリケーションプログラムへの処理の委譲
        - アプリケーションプログラムから結果を取得
        - レスポンスメッセージの構築
        - レスポンスメッセージの送信
- HTTPメッセージ
    - リクエストメッセージ
        - リクエストライン
        - ヘッダ
        - ボディ
    - レスポンスメッセージ
        - ステータスライン
        - ヘッダ
        - ボディ
- アプリケーション状態
    - ステートフルサーバでは、サーバは常にクライアントのアプリケーション状態を覚えていなければならない
    - ステートレスなアーキテクチャでは、サーバがクライアントのアプリケーション状態を覚える代わりに、クライアントが自らのアプリケーション状態を覚え、全てのリクエストを自己記述的メッセージで送信
        - 冗長的
        - ネットワーク障害に弱い
## HTTPメソッド
- メソッド
    - GET
        - リソースの取得
    - POST
        - 子リソースの作成
        - リソースへのデータの追加
        - その他
    - PUT
        - リソースの更新
        - リソースの作成
    - DELETE
        - リソースの削除
    - HEAD
        - リソースのヘッダの取得
    - OPTIONS
        - リソースがサポートしているメソッドの取得
    - TRACE
        - 自分宛にリクエストメッセージを返す試験
    - CONNECT
        - プロキシ動作のトンネル接続への変更
- ヘッダ
    - 認証
        - Basic認証
            - `Authorization: Basic xxxx`
            - ユーザ名とパスワードをコロンで連結し、Base64でエンコード
        - Digest認証
            - メッセージダイジェスト
                - あるメッセージに対してハッシュ関数を適用した結果のハッシュ値
            - nonce
                - number used once
                - リクエストごとに変化する文字列
            - qop
                - quority of protection
                - クライアントが送信するダイジェストの作成方法に影響を与える
                - auth
                    - メソッドとURIからダイジェストを作成
                - auth-init
                    - メソッドとURI、メッセージボディからダイジェストを作成
                    - メッセージ全体が改竄されていないことを保証
            - ダイジェストの生成
                - ユーザ名、realm、パスワードをコロンでで連結し、MD5ハッシュ値を求める
                - メソッドとURIのパスをコロンで連結し、MD5ハッシュ値を求める
                - 色々連結してMD5ハッシュ値を得る
        - OpenID
            - シンプルなシングルサインオン
            - IdP
                - Identity Provider
                - Webサービスのアカウントを他のWebサービスにも提供する側
            - SP
                - Service Provider
                - IdPのアカウントを利用して独自のWebサービスを提供する側のこと
        - OAuth
            - Webサービス間での認可の委譲
## キャッシュ
- キャッシュ用ヘッダの使い分け
    - キャッシュさせない場合、PragmaとCache-Controlの「no-cache」を同時に指定
    - キャッシュの有効期限が明確に決まっている場合、「Expires」を指定
    - キャッシュの有効期限を相対的に指定したい場合は、Cache-Controlの「max-age」で相対時間を指定
# ハイパーメディアフォーマット
## HTML
- Hypertext Markup language
## ATOM
- Atom Syndication Format
# Webサービスの設計
- リソース指向アーキテクチャ
    1. Webサービスで提供するデータを特定する
    1. データをリソースに分ける
    1. リソースにURIで名前をつける
    1. クライアントに提供するリソースの表現を設計する
    1. リンクとフォームを利用して、リソース同士を結びつける
    1. イベントの標準的なコースを検討する
    1. エラーについて検討する
- 設計のバランス
    - なるべくシンプルに保つ
    - 困ったらリソースに戻って考える
    - 本当に必要ならPOSTでなんでもできる
    