# AI Usage vs Productivity | Exploratory Data Analysis

### Exploring the Relationship Between Artificial Intelligence Usage and Productivity Using Python

## Project Overview

Artificial Intelligence is increasingly becoming part of everyday academic and professional workflows. However, an important question remains: **Is greater AI usage associated with higher productivity?**

This project explores the relationship between daily AI usage hours and productivity scores among students and professionals through exploratory data analysis (EDA).

Using Python and its data science libraries, the analysis examines statistical relationships, identifies patterns, and visualizes the association between AI usage and productivity.

## Technologies Used

- **Python** — Data processing and statistical analysis
- **Pandas** — Data manipulation, cleaning, and exploration
- **NumPy** — Numerical computations and linear regression
- **Matplotlib** — Data visualization and trend analysis

## Project Objectives

- Explore the relationship between AI usage and productivity.
- Prepare and validate numerical data for analysis.
- Handle missing and invalid values.
- Calculate Pearson's correlation coefficient.
- Fit a linear regression trend line.
- Visualize relationships using a scatter plot.
- Interpret statistical findings without assuming causation.

## Data Analysis Workflow

### 1. Data Preparation

The project begins by loading a cleaned CSV dataset using Pandas.

The analysis focuses on two variables:

- `AI_Usage_Hours_Per_Day`
- `Productivity_Score`

Both columns are converted to numeric values, and rows containing missing or invalid values in either column are excluded from the analysis.

### 2. Statistical Analysis

Pandas and NumPy are used to calculate:

- Total records analyzed
- Average daily AI usage
- Average productivity score
- Pearson correlation coefficient
- Linear regression slope and intercept

### 3. Data Visualization

A scatter plot illustrates the relationship between daily AI usage and productivity scores.

A fitted linear regression line helps visualize the overall direction of the relationship.

## Key Findings

The visualization indicates a **moderate positive correlation (r ≈ 0.53)** between daily AI usage and productivity scores.

This suggests that individuals reporting greater AI usage tend to have higher productivity scores within the analyzed dataset.

However, correlation does not establish causation. Productivity may also be influenced by individual skills, work complexity, task requirements, and other factors not examined in this analysis.

## Project Visualization

![AI Usage vs Productivity](AI_Usage_vs_Productivity.png)

*Scatter plot illustrating the relationship between daily AI usage and productivity scores, including a fitted linear regression trend line.*


## How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/hunainpy/ai-usage-productivity-analysis.git
```

**2. Navigate to the project directory**

```bash
cd ai-usage-productivity-analysis
```

**3. Install the required libraries**

```bash
pip install pandas numpy matplotlib
```
## Limitations

- The analysis examines correlation rather than causation.
- The fitted regression line represents a simple linear relationship.
- Other factors influencing productivity are not included.
- Extreme observations may influence the correlation and regression results.
- Findings depend on the quality and representativeness of the dataset.

## Future Improvements

- Compare AI usage patterns across students and professionals.
- Explore productivity differences across usage categories.
- Investigate outliers and their statistical influence.
- Perform additional exploratory analysis.
- Evaluate regression performance and model assumptions.

## Author

**Syed Hunain**

Computer Science Student | Python | Data Science | Artificial Intelligence
---

*This project is part of my ongoing practical learning journey in Python, Data Science, and Artificial Intelligence.*
