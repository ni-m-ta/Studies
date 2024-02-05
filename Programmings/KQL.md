# Overview
- 

# Command
- common kinds of query statements
    - case-sensitive
    - tabular expression statement
        - input and output consist of tables or tabular datasets
    -  common operators
        - `| count`
            - find the number of storm records in a table
        - `| distinct`
            - list all of the unique storm tpes
        - `| extend`
            - view the calculated column along with all of the other column
            - an added column is added as the last column
            - `| extend Duration = EndTime - StartTime`
        - `| project`
            - simplify the view and select a specfic subset of columns
            - `| project State, EventType, DamageProperty`
            - `| project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty`
                - add a column which is based on the caluculation
        - `| render`
            - visualize query results in a chart or graph
            - `| render barchart`
        - `| search`
            - pick records storing specific keywords
            - `| search "Alex"`
        - `| sort`
            - arrange the rows in descending order based on a specific column
            - `| sort by DamageProperty`
        - `| summarize`
            - essential to performiing aggregations over your data
            - groups together rows based on the by clause and uses the provided aggregation function to combine each group in a single row
            - `| summarize TotalStorms = count() by State`
            - `countif()`
                - count rows based on a specific condition to understand how many rows meet the given criteria
                - `| summarize StormsWithCropDamage = countif(DamageCrops > 0) by State`
        - `| take`
            - view a sample of records
            - `| take 5`
        - `| top`
            - returns the first n rows sorted by the speficied column
            - `| top 5 by DamageProperty`
        - `| where`
            - filters rows of data based on certain criteria
            - `| where State == 'TEXAS' and EventType == 'Flood'`
            - ```kql
                | where TimeGenerated > datetime(2023-01-01) and TimeGenerated < datetime(2023-01-02)
                | where Location == "JP"
                ```
            - `bins()`
                - can help understand how values are distributed within a certain range and make comparisons between different periods
                - `| summarize EventCount = count() by bin(StartTime, 7d)`
    - management commands
        - requests to Kusto to process or modify data or metadata
    - keywords
        - operators
            - sequenced by a pipe