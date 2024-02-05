# Overviews
- a serivce monigoring and gaining insights into the performance and suage of your applications 
- performance monitoring
- error tracking
- availability monitoring
- dependency tracking
    - automatically discovers and monitors dependencies such as databases, external services, and REST APIs, providing insights into their performance
- User analytics
    - track and analyze user interactions with your application, including user flows, page views, and custome events
- custom event tracking
    - can instrument their code to track custom events, enabling the coolection of specific telemetry data releveant to their application
- live metrics stream
- integration with Azure DevOps
    - integrates seamlessly with Azure DevOps, enabling a streamlined workflow for monitoring and improving application performance during development and in production
- powerful query language
    - Kusto Query Language

# tips
- time
    -  when setting time range, be careful about whether the time is reflected or not actually
    - difference between UTC and local time
        - set -9 from JST

# applications
- function apps
    - `traces`
        - get messages and other info
        - [document](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/traces)
- web app services
    - `AppServiceHTTPLogs`
        - App Serviceでの受信HTTP要求。これらのログを使用して、アプリケーションの正常性、パフォーマンス、および使用パターンを監視
        - [document](https://learn.microsoft.com/ja-jp/azure/azure-monitor/reference/tables/appservicehttplogs)
        