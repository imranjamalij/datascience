import seaborn as sns
import pandas as pd 

data = [[0.95, 0.95,'A'], [0.87,0.95,'B'], [0.94,0.99,'C']] 
df = pd.DataFrame(data, columns = ['Senitivity', 'Specificity','Class']) 
data = df.pivot_table(index='Senitivity', columns='Specificity', values='Class')
sns.heatmap(df, annot=True)


heatmap1_data = pd.pivot_table(df, values='Senitivity', 
                     index=['Class'], 
                     columns='Specificity')

sns.heatmap(heatmap1_data, cmap="YlGnBu")
