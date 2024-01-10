# Overviews
- Make procedures related to data usage more efficient
- Use SSMS to manage csv files' data

# Problems
- Many tasks to get, create, store, and check data by using Excel and SSMS
- These tasks leads to wasted time and mistakes

# Objectives
- Make tasks done by humans fewer to realize "NO MISTAKES" "EFFICIENT TIME USAGE"

# How
- Execute scripts to check data in SSMS and send the results via email (or teams) automatically
- Get, create, and store csv data automatically

# Details
- Execute scripts to check data in SSMS and send the results via email (or teams) automatically
    - By bullding test environments for SSMS, test automatic executable scripts and send the results via email
        - built vm via Azure, and connect to the vm via MS Remote Desktop
        - install SSMS and SQL Server in the vm
        - start SQL Server Agent
            - SQL Server Services > SQL Server Agent:Start
                - https://qiita.com/tsurumiii/items/b27726e02ec310933d5c
            - SSMS > execute the following query
                - `https://learn.microsoft.com/ja-jp/sql/database-engine/configure-windows/agent-xps-server-configuration-option?view=sql-server-ver16`
                - https://learn.microsoft.com/ja-jp/sql/database-engine/configure-windows/agent-xps-server-configuration-option?view=sql-server-ver16
            - Windows Server including SQL Server > Start:Computer management > Service and Application:Service > SQL Server Agent
                - https://sql-oracle.com/sqlserver/?p=706
        - set SQL Server Agent Mail
            - https://sql55.com/column/send-email-from-sql-server-agent-on-job-failures.php
            - SSMS: Management > Database Mail: Configure Database Mail
            - <img src="imgs/SSMS-SQLServerAgentMailConfigurationForSendGrid.png">
                - port: 587
                - username: `apikey`
                - password: `{APIKey}`
                - SMTP Server: smtp.sendgrid.net
                - E-mail address: `{EmailAddressAuthenticatedAtSendGrid}`
            - Add a stored procedure and job to SSMS
                - When adding a job, `owner` in "general" should be `sa`. Otherwise, you can get error 
                    - `@owner_login_name' is invalid (valid values are returned by sp_helplogins [excluding Windows NT groups]). (Microsoft SQL Server, Error: 14234)`
            - Set an email when a job is done
            - Also, possible to send email at a stored procedure
                - [Procedures](https://www.projectgroup.info/tips/SQLServer/MSSQL_00000014.html)
                - [documents for a query to send email](https://learn.microsoft.com/ja-jp/sql/relational-databases/system-stored-procedures/sp-send-dbmail-transact-sql?view=sql-server-ver16)

