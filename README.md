# Student Engagement & Churn Analysis

## Project Overview

This project analyzes **student engagement, participation patterns, and churn behavior** to identify factors that influence student retention.

Using **8,541 student records**, the analysis explores demographic, behavioral, and program-related variables to understand why some students successfully complete programs while others drop out.

The project combines **data cleaning, exploratory data analysis, and predictive modeling** to generate actionable insights that can help institutions **improve retention and support at-risk students earlier**.

---

# Business Problem

Student retention is critical for educational platforms and institutions.
When students drop out, organizations lose:

* program effectiveness
* revenue opportunities
* long-term reputation

The goal of this analysis is to:

* identify patterns in student participation
* understand factors contributing to churn
* develop predictive models to identify at-risk students early

---

# Dataset

The dataset contains **8,541 student records** and **20 variables**, including:

* demographic information
* opportunity category
* application behavior
* geographic location
* participation outcomes

Key dataset attributes include:

* age
* gender
* continent
* institution name
* opportunity category
* application timing
* participation status

---

# Data Collection

Data used in this analysis originates from structured program databases capturing student applications and engagement activities.

Typical sources for analytics datasets like this include:

* transactional databases
* application platforms
* institutional records
* program participation logs

These sources are commonly extracted using **SQL queries, CSV exports, or API pipelines** before being prepared for analysis.

---

# Data Preparation

The raw dataset required extensive cleaning before analysis.

Key preparation steps included:

### Data Cleaning

* Removed invalid values in academic major fields
* Standardized text formatting (lowercase categories)
* Removed redundant variables
* Standardized date formats
* Normalized institution names

### Feature Engineering

Several new variables were created to improve analysis:

* **Age at application**
* **Institution participation count**
* **Days between signup and application**

### Data Validation

After cleaning:

* records reduced from **8,558 to 8,327 valid entries**
* missing values were reviewed and validated
* dataset schema and types were verified

---

# Exploratory Data Analysis

Exploratory analysis was conducted to identify patterns across multiple dimensions.

### Geographic Distribution

Participation was concentrated in:

* North America
* Africa
* Asia

Lower participation occurred in Europe and Australia.

---

### Demographic Insights

* **58.65% male**
* **41.14% female**

Age distribution concentrated between **18–25 years**, peaking around **20–22**.

---

### Opportunity Category Trends

Student preferences showed:

* **Internships had the highest participation**
* **Courses and events had moderate participation**

Internships appeared to offer more practical value for students.

---

### Temporal Trends

Application volume increased significantly between **2023 and 2024**, indicating rapid platform growth.

Seasonal spikes aligned with **academic cycles and program launches**.

---

# Predictive Modeling

The project developed machine learning models to predict student churn.

## Models Used

* Random Forest
* Logistic Regression

The dataset was split:

* **80% training**
* **20% testing**

Features were standardized for Logistic Regression to ensure consistent model weighting.

---

# Key Predictive Features

The most important predictors of churn were:

* Days to apply
* Age at application
* Institutional participation level
* Opportunity category
* Geographic region
* Gender

---

# Model Performance

Both models achieved:

**Accuracy:** 97.74%

However, the dataset contained **class imbalance** because churn represented only **2.26% of students**.

Future improvements could include:

* SMOTE sampling
* class weight adjustments
* advanced ensemble methods

---

# Key Findings

## Overall Churn Rate

* **2.26% churn**
* **193 students dropped out**

---

## Course vs Internship Retention

Course programs showed significantly higher churn.

| Program Type | Churn Rate |
| ------------ | ---------- |
| Courses      | 6.50%      |
| Internships  | 1.07%      |

This suggests internships provide stronger engagement and perceived value.

---

## Application Timing

The strongest behavioral predictor of churn was **application delay**.

Students who waited longer to apply were significantly more likely to drop out.

---

## Geographic Risk

South America showed the highest churn rate:

**16.67% churn**

This suggests potential regional barriers such as:

* time zone challenges
* language barriers
* infrastructure limitations

---

## Institutional Influence

Students from institutions with **higher participation levels** demonstrated stronger retention.

Possible explanations include:

* peer influence
* institutional support
* stronger program awareness

---

# Strategic Recommendations

Based on the findings, several interventions could improve retention.

### Improve Course Engagement

* increase interactive learning
* introduce projects and case studies
* build peer learning communities

---

### Implement Early Engagement

Students should receive onboarding communication **within 24–48 hours after signup** to maintain engagement momentum.

---

### Provide Regional Support

For high-risk regions:

* localized support
* language assistance
* time-zone friendly scheduling

---

### Institutional Partnerships

Strengthening relationships with high-performing institutions can increase overall participation and retention.

---

# Expected Impact

If implemented, these interventions could reduce churn by **40–50%**, potentially retaining:

**80–100 additional students per year.**

---

# Technologies Used

Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn

Machine Learning
Statistical Analysis
Exploratory Data Analysis

---

# Project Structure

```
data/
notebooks/
scripts/
visualizations/
report/
README.md
```

---

# Future Improvements

Future iterations of this project could include:

* churn prediction dashboards
* real-time early warning systems
* improved class imbalance handling
* additional behavioral features
* student satisfaction analysis

---

# Author

Angela Mokhele

Data Analyst | Business Intelligence Developer

LinkedIn:
https://www.linkedin.com/in/matlhogonolo-mokhele-38a977283/

