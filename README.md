# Data_Analysis_Python

By taking Cars dataset (CSV) as a sample, I've prepared Jupyter notebooks for Basic EDA and Data Cleaning tasks. 

After first step, various aggregations are also shown by using Pandas library.

Main challenge in EDA is to get raw data and clean and transform it in a useful form which can drive next steps of data transformations.
This step can also find outliers.

After step 1 and 2, I've explored various common data formats used in Data Analysis like JSON, XML, Excel, Parquet and HTML.

Each data format comes with it's own pros and cons.

(1) CSV:

Pros:
- Semi structured data
- Most easy and straight-forward
- Very lightweight
- Human Readable
- Can be parsed by MS Excel too

Cons:
- Not recommended for large projects

(2) JSON:

Pros:
- JSON is semi structured data.
- Very lightweight
- Can be directly parsed by Pandas and other data analysis libraries
- Very flexible data format that supports the nested structure, meaning your data points can have multiple subcategories. Handling JSON format requires slightly less processing power compared to its counterparts and is also lightweight.
  
Cons:
- Some more processing can be required

(3) XML:

Pros:
- Semi structured data
  
Cons:
-  When it comes to data Analysis, XML is very complicated format.
-  XML is the most complicated format in data processing because it requires several steps and CPU cycles for pandas to process it.
  
(4) Parquet:

Pros:
- This format is optimized for Big data and is stored in compressed mode.
- Columnnar storage
- Language agnostic
- Used for analytics (OLAP) use cases, typically in conjunction with traditional OLTP databases.
- Highly efficient data compression and decompression.
- Supports complex data types and advanced nested data structures.
- Good for storing big data of any kind
- Increased data throughput and performance

(5) Excel:

Pros:
- Can be parsed directly through Pandas
- Very popular Microsoft technology

(6) HTML:

Pros:
- Can be parsed from any website


