# Ovewviews
- Purpose:
    - notes for concepts applied to any languages

# Concepts
- Buffer
    - overviews:
        - a region of memory that holds a certain amount of data. It acts as a temporary storage area during I/O operations
        - Buffered I/O:
            - In buffered I/O, data is not transferred one byte at a time. Instead, it is read or written in larger chunks or blocks. The buffer is used to accumulate a certain amount of data before initiation the actuaal I/O operations
    - advantages:
        - reduced system calls
        - improved performance especially for disk or network operations 
        - minimized overhead
            - overhead:
                - any additional resources or time required by a system, process, or operation beyond the minimum necessary for its primary purpose
                
