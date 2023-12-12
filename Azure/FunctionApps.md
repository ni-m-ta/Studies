# Overviews
- 

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
