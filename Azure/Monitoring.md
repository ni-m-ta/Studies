# Overviews about Azure Monitor
- a comprehensive monitoring solution provided by Microsoft Azure that allows you to collect and analyze telemetry data from your applications, infrastructure, and network
- to provide insights into the performance, availability, and usage of your resources
- Architecture
    - <img src="/Users/tatsuya.nisato/Documents/Project/Studies/Repo/Studies/imgs/ArchitectureOfAzureMonitor.png">
    - Applications
    - VMs
    - Guest OS
    - Containers including Prometheus metrics
    - DB
    - Security events in combination with Azure Sentinel
    - Networking events and health in combination with Network Watcher
    - Custom sources that use the APIs to get data into Azure Monito
- shortcuts
    - datastore -> Log Analytics Workspaces, Metrics, Insights...
    - data from core systems -> Azure Resource

# Knowledge


# Insights
- 

# Pattern
- fact: データベースの切断が検知されたことによるアラート
    - MS側で適用しているバッチ処理により、DBが切断されている
    