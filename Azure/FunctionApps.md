# Overviews
- a serverless compute service provided by MS Azure
    - serverless architecture
    - event-driven programming
    - bindings
        - simplify integration with Azure services
            - Azure Storage
            - Azure Cosmos DB
    - scaling
    - Documents:
        - [Comparison among options](https://learn.microsoft.com/ja-jp/azure/logic-apps/logic-apps-limits-and-config?tabs=consumption%2Cazure-portal#run-high-throughput-mode)

# Findings
- Memory profilers MS shows do not work (20231211)
    - Solutions
        - Python:
            - [tracemalloc](https://docs.python.org/ja/3/library/tracemalloc.html)
                -  
        ```python
        import tracemalloc
        current, peak = tracemalloc.get_traced_memory()
        logging.info(f"Current memory usage: {current/10**6} MB")
        logging.info(f"Peak memory usage: {peak/10**6} MB")
        ```

# Problems
- code exits with 137
    - logs
        ```
        Exception while executing function
        /Functions.AzureSubscription
        sToSharePoint ---> Microsoft.Azure.WebJobs.Script.Workers.WorkerProcessExitException 
        /python exited with code 137 (0x89) ---> System.Exception    End of inner exception    
        System.Runtime.ExceptionServices.ExceptionDispatchInfo.Throw()  
        ```
    - cause:
        - out-of-memory
        - when choosing B2 with 3.5GB memory for azure service plan, encountered the error
    - solution:
        - did scale-up to B3 with 7.0 GB memory
    - how to recognize the problem
        - by looping simple tasks consumnig 250MB memory every loop, and checked how it works

