'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''

import seaborn as sns
import matplotlib.pyplot as plt
import os

def create_p5_directory():
    os.makedirs('./data/part5_plots', exist_ok=True)

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def scatter_prediction_by_charge(merged_df):
    sns.lmplot(data=merged_df,
               x='prediction_felony',
               y='prediction_nonfelony',
               hue='has_felony_charge',
               fit_reg=False,
               height=5,
               aspect=1.2)
    plt.title('Felony vs Nonfelony prediction by charge type')
    plt.savefig('./data/part5_plots/prediction_scatter_by_charge.png', bbox_inches='tight')
    plt.clf()

print("\n The dots on the right of the plot are likely to represent people who a highly likely to have a felony and non felony rearrest"
      "Most of these are likely people with current felony charges")

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def scatter_felony_prediction_vs_outcome(merged_df):
    sns.lmplot(data=merged_df,
               x='prediction_felony',
               y='felony_rearrest' ,
               fit_reg=False,
               height=5,
               aspect=1.2)
    plt.title('Prediction vs actual felony rearrest')
    plt.savefig('./data/part5_plots/felony_prediction_vs_actual.png', bbox_inches='tight')
    plt.clf()

print("\n This plot reveals that the model is not as calibrated as it could be based on the predicted proabbilites compared with actual felony rearrests"
      "The points are spread across y=0 and y=1 w a range of predicted values suggesting its not too calibrated"
      "If it were more calibrated the model would show higher predictions closer to y=1 than y=0 ")