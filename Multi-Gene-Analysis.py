import pandas as pd
from IPython.display import display
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import dendrogram, linkage
from tabulate import tabulate

# DATA LOADING FROM EXCEL FILE

# Replace with your own file path 
data = pd.read_excel(r'C:\Users\agnie\OneDrive\Pulpit\MultiGene.xls')
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(data)


# TIME SERIES ANALYSIS

# Extract the growth stages
growth_stages = data['sample name']

# Extract gene expression levels for ech gene
gene_ctu2 = data['CTU2']
gene_trm9 = data['TRM9']
gene_urm12 = data['URM12']
gene_cnx5 = data['CNX5']
gene_urm11 = data['URM11']

# Plot the time series for ech gene
plt.figure(figsize=(12, 6))
plt.plot(growth_stages, gene_ctu2, marker='o', linestyle='-', color='b')
plt.xticks(rotation=90)
plt.xlabel('Growth Stages')
plt.ylabel('Gene Expression Level')
plt.title('Time Series Analysis for Gene CTU2')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(growth_stages, gene_trm9, marker='o', linestyle='-', color='b')
plt.xticks(rotation=90)
plt.xlabel('Growth Stages')
plt.ylabel('Gene Expression Level')
plt.title('Time Series Analysis for Gene TRM9')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(growth_stages, gene_urm12, marker='o', linestyle='-', color='b')
plt.xticks(rotation=90)
plt.xlabel('Growth Stages')
plt.ylabel('Gene Expression Level')
plt.title('Time Series Analysis for Gene URM12')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(growth_stages, gene_cnx5, marker='o', linestyle='-', color='b')
plt.xticks(rotation=90)
plt.xlabel('Growth Stages')
plt.ylabel('Gene Expression Level')
plt.title('Time Series Analysis for Gene CNX5')
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(growth_stages, gene_urm11, marker='o', linestyle='-', color='b')
plt.xticks(rotation=90)
plt.xlabel('Growth Stages')
plt.ylabel('Gene Expression Level')
plt.title('Time Series Analysis for Gene URM11')
plt.grid(True)
plt.tight_layout()
plt.show()


# MEAN EXPRESSION LEVELS AND BAR PLOT

# Calculate the mean expression level for each gene and sort the genes in descending order based on mean expression levels
mean_expression = data.iloc[:, 1:].mean().sort_values(ascending=False)
print(mean_expression)

# Set up the figure and axes for plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Define the colormap with the number of colors equal to the number of genes
num_genes = len(mean_expression)
colormap = plt.cm.get_cmap('viridis', num_genes)

# Plot the average gene expression levels using a bar plot with a custom colormap
for i, (gene, expression) in enumerate(mean_expression.items()):
    ax.bar(gene, expression, color=colormap(i))

ax.set_xlabel('Gene')
ax.set_ylabel('Mean Relative Gene Expression Level')
ax.set_title('Graph of Mean Relative Gene Expression Levels')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()


# TABLE OF AVERAGE EXPRESSION 

# Remove the 'sample name' column from the data
data = data.drop(columns='sample name')

# Calculate the average level of gene expression for each stage
average_expression = data.mean(axis=1)
average_expression_rounded = average_expression.round(3)

# Create a DataFrame to store the results
results_1 = pd.DataFrame({'Growth Stage': growth_stages,
                        'Average Expression': average_expression_rounded})

# Sort the developmental stages based on the average expression values
sorted_results = results_1.sort_values(by='Average Expression', ascending=False)

# Display the sorted growth stages and average expression values in a table
table_data = sorted_results[['Growth Stage', 'Average Expression']].values.tolist()
table_headers = ['Growth Stage', 'Average Expression']
table = tabulate(table_data, headers=table_headers, tablefmt='pretty')

print("Sorted Growth Stages based on Average Expression:")
print(table)


# GENES WITH THE LOWEST AND HIGHEST EXPRESSION FOR EACH GROWTH STAGE

# Find the gene with the lowest and highest expression for each growth stage
lowest_genes = data.idxmin(axis=1)
highest_genes = data.idxmax(axis=1)

# Create a DataFrame to store the results
results_2 = pd.DataFrame({'Growth Stage': growth_stages,
                        'The Gene With The Lowest Expression': lowest_genes,
                        'The Gene With The Highest Expression': highest_genes})

# Count the occurrences of each gene in the 'Gene with Lowest Expression' and 'Gene with Highest Expression' column
lowest_gene_counts = results_2['The Gene With The Lowest Expression'].value_counts()
highest_gene_counts = results_2['The Gene With The Highest Expression'].value_counts()

# Find the gene that appears most often with the lowest and highest expression
most_often_lowest = lowest_gene_counts.idxmax()
most_often_highest = highest_gene_counts.idxmax()

# Sort genes from most often to least often expressed (lowest expression)
sorted_lowest_genes = lowest_gene_counts.sort_values(ascending=False)
# Sort genes from most often to least often expressed (highest expression)
sorted_highest_genes = highest_gene_counts.sort_values(ascending=False)

# Display the gene that most often has the lowest and highest expression levels
print(f"The gene that most often has the highest level of expression: {most_often_highest}")
print(f"\nThe gene that most often has the lowest expression level: {most_often_lowest}")

# Display genes sorted from most often to least often expressed (highest expression)
print("\nGenes that most often have the highest expression levels:")
print(sorted_highest_genes)
# Display genes sorted from most often to least often expressed (lowest expression)
print("\nGenes that most often have the lowest expression levels:")
print(sorted_lowest_genes)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(results_2)
    
    
# CORRELATION HEATMAP 

# Calculate the correlation matrix for gene expression levels
correlation_matrix = data.corr()

# Create the heatmap and customize it
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
ax.set_title('Correlation Heatmap: Gene Expression Levels')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()


# HIERARCHICAL CLUSTERING

# Read data from the Excel file
# Replace with your own file path 
gene_expression_data = pd.read_excel(r'C:\Users\agnie\OneDrive\Pulpit\MultiGene.xls', index_col=0 )

# Standardize the data (scaling to mean=0 and variance=1)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(gene_expression_data)

# Calculate the distance matrix using Euclidean distance
distance_matrix = pdist(data_scaled, metric='euclidean')

# Perform hierarchical clustering using linkage
linkage_matrix = linkage(distance_matrix, method='ward')

plt.figure(figsize=(10, 8))
dendrogram(linkage_matrix, labels=gene_expression_data.index, orientation='right')
plt.xlabel('Distance')
plt.ylabel('Genes')
plt.title('Hierarchical Clustering Dendrogram')
plt.tight_layout()
plt.show()
