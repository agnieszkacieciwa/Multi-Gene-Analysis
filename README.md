# Multi-Gene-Analysis

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Analyses](#analyses)
  - [Time Series Analysis](#time-series-analysis)
  - [Mean Expression Levels and Bar Plot](#mean-expression-levels-and-bar-plot)
  - [Table of mean Expression for Growth Stages](#table-of-mean-expression-for-growth-stages)
  - [Genes with Lowest and Highest Expression](#genes-with-lowest-and-highest-expression)
  - [Correlation Heatmap](#correlation-heatmap)
  - [Hierarchical Clustering](#hierarchical-clustering)
- [License](#license)


## Introduction

The MultiGene Analysis is a Python tool developed for the comprehensive analysis of gene expression data. In the realm of biological research, understanding how genes are regulated and how their expression changes across various biological contexts, such as tissues and developmental stages, is crucial. This project facilitates this exploration through a set of functionalities, including time series analysis, mean expression level calculations, hierarchical clustering, and correlation heatmap generation. 

By leveraging Python 3.11 and popular libraries like `pandas`, `seaborn`, `matplotlib`, and `scikit-learn`, the MultiGene Analysis empowers researchers to gain deeper insights into gene expression dynamics. Whether visualizing time series data, identifying genes with extreme expression levels, or uncovering correlation patterns, this project provides a robust framework for exploring and interpreting complex gene expression datasets.


## Features

- **Time Series Analysis:** Visualize gene expression changes across different growth stages.
- **Mean Expression Levels and Bar Plot:** Calculate and visualize mean gene expression levels.
- **Table of Mean Expression for Growth Stages:** Create a table of sorted growth stages based on mean expression levels.
- **Genes with Lowest and Highest Expression:** Identify genes with extreme expression levels at each growth stage.
- **Correlation Heatmap:** Generate a heatmap to visualize gene expression relationships.
- **Hierarchical Clustering:** Utilize hierarchical clustering to group genes based on expression patterns.


## Prerequisites

- Python 3.11
- Required Python packages (`pandas`, `seaborn`, `matplotlib`, `scikit-learn`, `tabulate`)
- Excel file "MultiGene.xls."


## Analyses

### Time Series Analysis
The time series analysis section visualizes gene expression changes across different growth stages. Each gene's expression is plotted over time to understand its dynamics during plant development.

![obraz](https://github.com/agnieszkacieciwa/Multi-Gene-Analysis/assets/88035266/582a5924-d003-4dc7-bf8b-0baf237448b5)

### Mean Expression Levels and Bar Plot
The mean expression levels section calculates and visualizes the average gene expression levels, providing insights into the overall gene activity. The results are presented in a bar plot with a custom colormap.

![obraz](https://github.com/agnieszkacieciwa/Multi-Gene-Analysis/assets/88035266/b5f36aa5-6c9f-4831-bbca-837fee0c2d06)

### Table of Mean Expression for Growth Stages
This section creates a table of sorted growth stages based on mean expression levels, offering a comparative view of gene expression patterns during different developmental stages.

### Genes with Lowest and Highest Expression
Identifies genes with the lowest and highest expression levels at each growth stage. The results are presented in a table, highlighting genes that consistently exhibit extreme expression levels.

### Correlation Heatmap
Generates a heatmap to visualize the correlation between gene expression levels, aiding in the identification of genes with similar or opposite expression patterns.

![obraz](https://github.com/agnieszkacieciwa/Multi-Gene-Analysis/assets/88035266/4ea963bb-7277-41d2-a3f8-6ac0b5327dc9)

### Hierarchical Clustering
Utilizes hierarchical clustering to group genes based on their expression patterns. The resulting dendrogram provides insights into relationships between genes and their potential functional connections.

![obraz](https://github.com/agnieszkacieciwa/Multi-Gene-Analysis/assets/88035266/51cded44-b763-4d9d-b2cd-f01e17303f89)


## License

This project is licensed under the MIT License.

