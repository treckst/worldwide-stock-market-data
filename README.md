# ELT pipeline using Azure Portal + Fabric designed to fetch daily stock market data for the Top 7 USA tech companies by extracting the data from REST API, storing it in Azure Data Lake Storage Gen2 in the bronze container as partitioned Parquet files to optimize cost

# Fabric Pipeline triggers the ingestion by timetrigger function and manages the workflow of the dataflow.

# Dataflow Gen2 cleans the data, loads it into the Lakehouse. 

# Screenshots (the biggest challenge so far is dealing with parquet at the transforming stage):
 
 **Dataflow**: 
 <img width="1810" height="655" alt="image" src="https://github.com/user-attachments/assets/a00d7234-cbd8-433d-b8e4-bdab57b3dad8" />
 
 **Pipeline**:
 
 <img width="1280" height="586" alt="image" src="https://github.com/user-attachments/assets/7add9b6d-1849-4abd-a982-67a948807d4c" />
 
**transformed data**:

<img width="1280" height="599" alt="image" src="https://github.com/user-attachments/assets/ea52c02e-7b0a-47d0-b7fc-86e4aab2e9a3" />
<img width="1280" height="598" alt="image" src="https://github.com/user-attachments/assets/bff61dea-2cb0-48be-98de-b146302cd70d" />


**time-trigger function:**

<img width="1858" height="983" alt="image" src="https://github.com/user-attachments/assets/6b0e21cc-c434-4844-87b3-7d9dcb4b0bc8" />

<img width="1280" height="571" alt="image" src="https://github.com/user-attachments/assets/30feabb1-95cb-4a03-9d86-bc7a96c4ef05" />
<img width="1280" height="557" alt="image" src="https://github.com/user-attachments/assets/52f7323e-72fa-4b07-8160-6b507806a503" />
