# **Indian Crime Data Analysis**  

## **INTRODUCTION**

### **PROJECT TITLE:** Indian Crime Data Analysis
![image](https://github.com/user-attachments/assets/14327347-d57a-4d81-9f61-2a2733febfd9)

### **PROJECT PURPOSE:**
- To analyze crime trends across different states in India.
- Identify the relationship between stolen and recovered properties.
- Provide visual insights for policymakers and law enforcement agencies.
- Suggest data-driven recommendations to improve crime recovery rates.

### **DATA SOURCES:**
- **National Crime Records Bureau (NCRB)** datasets.
- **State Police Records** from official portals.
- **Public Data Portals** and statistical crime reports.
- **Kaggle and Open-Source Datasets** for supplementary data.

### **TOOLS USED:**
- **Data Cleaning & Processing:** Python (Pandas, NumPy)
- **Database Management:** SQL Server
- **Data Visualization:** Power BI, Tableau, Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn (for predictive analysis)

---

## **PHASE 1: DATA COLLECTION**

### **Data Attributes:**
The dataset consists of the following key attributes:

- **Crime ID:** Unique identifier for each crime record.
- **Year:** The year in which the crime was reported.
- **State/UT:** Name of the state or union territory where the crime occurred.
- **Crime Category:** Type of crime (Burglary, Theft, Cybercrime, etc.).
- **Sub-Category:** More specific classification within a crime category.
- **Cases Reported:** Number of reported cases.
- **Property Stolen:** Total value of stolen property (in INR).
- **Property Recovered:** Total value of recovered property (in INR).
- **Recovery Rate:** Percentage of recovered vs. stolen property.

### **Data Sources & Extraction:**
- Data was collected from various government websites, NCRB reports, and API-based crime data sources.
- Data was stored in **Excel, CSV, and SQL databases** for structured querying.

---

## **PHASE 2: DATA CLEANING**

### **Challenges Identified:**
1. **Missing Values** in crime records.
2. **Inconsistent Formats** (Dates, Numbers, and Text inconsistencies).
3. **Duplicate Entries** in multiple reports.
4. **Outliers in Recovery Data** (Recovery value > Stolen value).

### **Data Cleaning Steps:**
✔ **Removing Duplicates** and irrelevant columns.
✔ **Handling Missing Data** using imputation techniques.
✔ **Standardizing Date Formats** for better consistency.
✔ **Fixing Outliers** by ensuring recovery values do not exceed stolen values.

---

## **PHASE 3: ETL PROCESS (EXTRACT, TRANSFORM, LOAD)**

### **EXTRACT:**
- Data was extracted from CSV files, SQL databases, and government APIs.

### **TRANSFORM:**
- Data was normalized for better analysis.
- Crime types were categorized into **violent, property, and cyber crimes**.
- Calculated **crime recovery rates** and **annual trends**.

### **LOAD:**
- The cleaned and structured data was stored in an **SQL database**.
- Data was also exported to **Power BI and Tableau** for visualization.

---

## **PHASE 4: DATA ANALYSIS & INSIGHTS**

### **1. Crime Trends Over Time**
- Analysis of crime trends over the past 10 years.
- Identification of peak months and seasonal crime variations.

📊 **Crime Trends Over the Years**  
![image](https://github.com/user-attachments/assets/1aa7663a-1251-4138-9897-656f59c68ce4)


### **2. State-Wise Crime Distribution**
- Identification of states with the highest crime rates.
- Crime density heatmaps were used for better insights.

📊 **State-wise Crime Distribution**  
![image](https://github.com/user-attachments/assets/0c51d523-f203-4194-bb6b-5b73fad6afea)


### **3. Recovery Success Rate**
- Comparison of stolen vs. recovered property across different states.
- Identification of states with the highest and lowest recovery efficiency.

📊 **Recovery Success Rate Analysis**  
![image](https://github.com/user-attachments/assets/52812229-6c53-49c6-9c0f-b306786b0fe4)


### **4. Crime Type Distribution**
- Burglary and theft were the most common crimes.
- Cybercrime cases showed the lowest recovery rate.

📊 **Crime Type Distribution**  
![image](https://github.com/user-attachments/assets/10001124-23c5-4ff2-8b43-29bbba279d5d)



### **5. Predictive Analysis Using Machine Learning**
- A predictive model was developed to forecast future crime trends.
- Key influencing factors: **population density, past crime rates, and law enforcement efficiency**.
![image](https://github.com/user-attachments/assets/b6e0cbf3-ef8a-4d8c-93c0-8d865e948456)




---

## **PHASE 5: VISUALIZATION & DASHBOARDS**

### **Dashboard Elements:**
✅ **Interactive Crime Heatmap** - Shows crime density per state.
✅ **Crime Type Breakdown** - Bar charts and pie charts for easy understanding.
✅ **Annual Trends** - Line charts displaying crime variations.
✅ **FIR Status Dashboard** - Insight into solved vs. pending cases.

📊 **Example Dashboard Screenshot**  
<img width="956" alt="image" src="https://github.com/user-attachments/assets/48492319-b0a8-4b14-9e6e-3c23a3777ff0" />


🔗 **Live Dashboard:** [Indian Crime Data Dashboard](https://indiancrimepy-6rphzupbhgd543oyxgiuds.streamlit.app/)

---

## **PHASE 6: CONCLUSION & RECOMMENDATIONS**

### **Key Takeaways:**
- Certain states exhibit significantly higher crime rates.
- **Crime recovery rates remain low**, requiring policy improvements.
- **Cybercrime cases have grown**, with poor recovery efficiency.
- **Predictive analytics can assist law enforcement in crime prevention**.

### **Recommendations:**
✔ **Increase Surveillance**: More CCTV deployment in high-crime areas.
✔ **Predictive Analytics**: Using ML models to detect crime-prone areas.
✔ **Better Law Enforcement Coordination**: Stronger inter-state crime management.
✔ **Public Awareness Campaigns**: Educating citizens on crime prevention.

📌 **Next Steps:** Expand the analysis by integrating **real-time crime reporting systems** and **AI-driven fraud detection models**.

---

