# Rose Sales Price Optimization

## Project Overview

This project analyzes **seven years of historical rose sales data** from a single producer operating within a nationwide cooperative system in Türkiye. Roses are sent to multiple cooperative branches—such as Ankara, Istanbul, Izmir, Adana, and Kayseri—where they are sold through an auction-based system without fixed prices. As a result, sales prices vary significantly.

The project focuses on identifying **controllable sales strategies** that can help maximize rose sales prices, while treating system-related factors as external constraints.

## Aim of the Project

The aim of this project is to improve my data analysis skills while using real sales data from my family’s rose production to help optimize sales strategies and increase overall earnings.

## Problem Definition

### Problem Statement

Producers sell the flowers they grow through a nationwide cooperative system in Türkiye. The cooperative operates multiple branches, including Ankara, Istanbul, Izmir, Adana, and Kayseri. Producers send their roses to these branches, where sales are conducted through an auction-based system. Since there is no fixed price, the final sales price varies significantly.

The auction price of roses is influenced by multiple factors, which can be broadly categorized into **system-related factors** and **producer-related factors**. System-related factors—such as market demand, auction dynamics, and the **randomized auction order of flower boxes**—are beyond the control of producers. However, producer-related factors, including product quality and sales timing strategies, can be optimized.

This project focuses on identifying controllable sales strategies to maximize the sales price of roses, based on an analysis of seven years of historical data from a single producer, with particular attention to timing effects, special dates, and branch-level differences.

By leveraging data-driven insights, this project seeks to provide actionable recommendations on **when**, **where**, and **under which conditions** the producer should send their roses to achieve higher sales prices.

This analysis helps the producer increase revenue without increasing production costs.

## Research Questions

- On which day(s) of the week should roses be sent to achieve higher prices?
- At which time(s) of the month should roses be sent?
- On which special days do roses sell at higher prices?
- Which cooperative branch(es) consistently achieve higher sales prices compared to others?

## Dataset

- **Time span:** 7 years
- **Scope:** Sales data from a single producer
- **Product:** Roses
- **Sales method:** Auction-based
- **Sales unit:** Flower boxes
- **Geographical coverage:** Multiple cooperative branches across Türkiye

## Methodology

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Time-based analysis (day of week, month, special days)
- Branch-level performance comparison
- Statistical analysis and visualization

## Dashboard & Visualization

In addition to the analytical study, the results of this project will be presented through an **interactive dashboard**. The dashboard is designed to enable the producer to easily explore sales patterns and make data-driven decisions.

The dashboard will include:

- Sales price trends by **day of the week**
- Monthly and seasonal price patterns
- Price behavior on **special days**
- Performance comparisons across **cooperative branches**
- Key summary metrics and visual insights

## Scope & Limitations

This analysis is based on **seven years of historical rose sales data from a single producer**. The findings are therefore specific to this producer’s sales patterns and operational conditions.

- Results may not be directly generalizable to other producers
- System-related factors, such as market demand and randomized auction order, are treated as external constraints
- The analysis focuses exclusively on **controllable factors**, including timing, special dates, and branch selection

Despite these limitations, the project provides valuable insights that can support better sales decisions without increasing production costs.

## Key Questions Answered

- When should producers send roses to maximize auction prices?
- Which branches perform better on average?
- How do special days influence price dynamics?
- Are there consistent seasonal or weekly price patterns?

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Jupyter Notebook

## Future Work

- Incorporating weather and seasonal demand data
- Predictive modeling of rose sales prices
- Expanding the analysis to include multiple producers
- Enhancing the dashboard with forecasting capabilities

## Results & Insights