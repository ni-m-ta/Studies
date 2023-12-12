# Ovewviews
- General-Purpose Language: Python is a versatile, general-purpose programming language. It's widely used in various domains, including web development, data science, artificial intelligence, machine learning, scientific computing, automation, and more.
- Easy to Read and Write: Python syntax is designed to be clear and readable. The language emphasizes code readability, and its syntax allows developers to express concepts in fewer lines of code than might be possible in languages such as C++ or Java.
- Interpreted Language: Python is an interpreted language, which means that the source code is executed line by line, and errors can be detected early in the development process. This makes it an excellent language for rapid prototyping and development.
- High-Level Language: Python abstracts many low-level details, making it easier for developers to focus on solving problems rather than dealing with complex system management tasks.
- Dynamically Typed: Python is dynamically typed, which means that the type of a variable is interpreted at runtime. This provides flexibility but requires careful attention to variable types.
- Large Standard Library: Python comes with a large standard library that includes modules and packages for a wide range of tasks, from working with databases to handling web requests.
- Community and Ecosystem: Python has a large and active community of developers. There are numerous third-party libraries and frameworks available, making it easy to find tools and solutions for almost any programming task.
- Object-Oriented: Python supports object-oriented, imperative, and functional programming paradigms. It allows developers to use and create classes and objects.
- Platform-Independent: Python is designed to be cross-platform. Code written in Python can run on various operating systems with little to no modification.
- Popular Frameworks: Python has several popular frameworks, such as Django for web development, Flask for lightweight web applications, NumPy and pandas for data science, TensorFlow and PyTorch for machine learning, and more.

# Problems & Solutions
- when dealing with tasks to read large CSV files, feared with the lack of memory usage
    - use chunking: read the file in chunks
        - example
            - pandas:
                - 
        ```python
        import pandas as pd

        chunk_size = 10000  # Adjust this based on your available memory
        for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
            # Process each chunk as needed
            process_data(chunk)
        ```
    - use generators: with open...
        - example
            - 
        ```python
        def read_large_file(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    yield line.strip()

        for row in read_large_file('large_file.csv'):
            process_data(row)
        ```
    - streaming processing
        - when files are encoded by utf-8
            - example
                - 
        ```python
        with open('large_file.csv', 'r', encoding='utf-8') as file:
            for line in file:
                process_data(line)
        ```
    - use dask
        - overviews
            - an open-source distributed computing library that provides parallel processing capabilities for data analysis
            - can handle data sets that are larger than the available memory by partitioning the data and processing it in parallel across multiple processors or machines
        - example
            - 
        ```python
        import dask.dataframe as dd
        df = dd.read_csv('large_file.csv')
        ```
    - use compression
        - example
            - 
        ```python
        import pandas as pd
        df = pd.read_csv('large_file.csv.zip', compression='zip')
        ```

# Libraries

## io
- references:
    - [Python Documents](https://docs.python.org/3/library/io.html)
- overviews: to deal with various types of i/o. Can be called a file object, stream, file-like object.
    - classifications
        - text I/O
        - binary I/O
        - raw I/O
    - Sensitive to types
    - capabilities
        - read-only
        - write-only
        - read-write
        - random acess
        - only sequential access
- Text I/O
    - overviews: 
        - expects and produces str objects
        - examples
            - to create a text stream
                - `f = open("myfile.txt","r")`
            - to in-memory text streams
                - `f = io.StringIO("some initial text data")`
- Binary I/O
    - ovewviews: 
        - expects bytes-like objects and produces bytes objects
        - no encoding, decoding, or newline translation is performed
    - examples
        - to create a binary stream
            - `f = open("myfile.jpg","rb")`
        - in-memory binary streams
            - `f = io.BytesIO(b"some initial binary data: \x00\x01)`
- Raw I/O
    - overviews:
        - used as a low-level building-block for binary and text streams
            - low-level operations: tasks or operations that deal directly with the hardware or the fundamental components of a system
                - manipulation of memory addresses
                - bitwise operations
                - direct hardware interaction
                - interrupt handling
                - file I/O at the byte level
    - examples
        - to create a raw stream by openining a file in binary mode
            - `f = open("myfile.jpg", "rb")`

## tracemalloc
- overviews:
    - a debug tool to trace memory blocks allocated by Python
    - example usages:
        - traceback where an object was allocated
        - statistics on allocated memory blocks per filename and per line number
            - total size
            - total number
            - average size 
        - compute the differences between two snapshots to detect memory leaks
    - documents:
        - [tracemalloc](https://docs.python.org/3/library/tracemalloc.html)

