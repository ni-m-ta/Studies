# Azure IoT
- Azure IoT
    - IoTデバイスの接続、監視、管理のために使用できる一連のマネージドクラウドサービス
- IoTデバイス
    - 回路基盤とそれに接続されたセンサーとで構成され、センサーはWiFiを使用してインターネットに接続
    - デバイスSDK
        - 毒死の埋め込みデバイスコードを実装可能
        - OSをサポート
    - IoTプラグアンドプレイ規則
        - デバイスの埋め込みコードの作成を簡素化
- 接続
    - IoTデバイスはソリューション内のクラウドサービスに対し、アタッチされたセンサーのテレメトリを送信する。
    - クラウドサービスからデバイスにコマンドを送信できる
- Azure IoT Central
    - IoTソリューションの開発、管理、保守の負担とコストを軽減するマネージドアプリプラットフォーム
- 開発
    - デバイス開発
        - クラウドエンドポイントへのセキュリティで保護された接続を確立
        - 接続されているセンサーから収集されたテレメトリをクラウドに送信
        - デバイスの状態を管理し、その状態をクラウドと同期する
        - クラウドから送信されたコマンドに応答する
        - クラウドからソフトウェアとファームウウェアの更新プログラムのインストールを可能にする
        - デバイスからクラウドから切断されている間もデバイスが機能し続けることができるようにする
    - デバイスの種類
        - Micro Controler
        - Micro Processor
    - プリミティブ
        - device-to-cloud
        - file upload
        - device twin
        - degital twin
        - direct method
        - cloud-to-device
    - 接続
        - 直接
            - ホスト名を含む接続文字列をデバイスに渡す
        - DPS
            - Device Provisioning Service
            - 既知のDPSエンドポイントに接続して、割り当てられているIoTハブの接続文字列を取得
    - 認証と権限承認
        - 接続先のIoTハブまたはDPSエンドポイントの信頼性を検証
        - SAS
        - X.509証明書