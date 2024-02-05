# Overviews
- a cloud-based email platform that provides services for sending and receiving email
- designed to simplify the complexities of email infrastructure, improve deliverability, and provide analytics to help users optimize their email campaigns

# Settings
- Sender Authentication
    - [Document](https://sendgrid.kke.co.jp/docs/Tutorials/D_Improve_Deliverability/using_whitelabel.html#-Domain-Whitelabel)
    - SendGridから送信するメールのブランドやレプテーションを守り、到達性を改善するための機能
    - SendGridが利用者の許可を得た上でメールを送信していることを公に証明
    - 構成要素
        - Domain Authentication (SPF/DKIM settings)
            - 送信ドメイン認証をSendGridドメインから独自ドメインに変更する
        - Link Branding
            - メール本文内のトラッキング用URLをSendGridドメインから独自ドメインに変更
        - Reverse DNS
            - メールの送信元IPの逆引き結果をSendGridドメインから独自ドメインに変更する
- Domain
    - Envelope From
        - 基本SendGridによって自動生成
        - Domain Authenticationを設定することで独自ドメインに変更できる