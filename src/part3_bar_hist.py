'''
PART 3: BAR PLOTS AND HISTOGRAMS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part3_plots`
'''

import seaborn as sns 
import matplotlib.pyplot as plt
import os 

def create_p3_directory():
    os.makedirs('./data/part3_plots',exist_ok=True)
    
# 1. Using the pre_universe data frame, create a bar plot for the fta column.
def barplot_fta(pred_universe):
    sns.countplot(data=pred_universe,x='fta')
    plt.title('FTA Counts')
    plt.savefig('./data/part3_plots/barplot_fta.png',bbox_inches='tight')
    plt.clf()


# 2. Hue the previous barplot by sex
def barplot_fta_by_sex(pred_universe):
    sns.countplot(data=pred_universe,x='fta', hue='sex')
    plt.title('FTA Counts by Sex')
    plt.savefig('./data/part3_plots/barplot_fta_by_sex.png', bbox_inches='tight')
    plt.clf()


# 3. Plot a histogram of age_at_arrest
def histogram_age(pred_universe):
    sns.histplot(data=pred_universe,x ='age_at_arrest')
    plt.title('Histogram of Age of Arrerest')
    plt.savefig('./data/part3_plots/histogram_age.png',bbox_inches='tight')
    plt.clf()

# 4. Plot the same histogram, but create bins that represent the following age groups 
#  - 18 to 21
#  - 21 to 30
#  - 30 to 40
#  - 40 to 100 
def histogram_age_binned(pred_universe):
    bins=[18,21, 30, 40, 100]
    sns.histplot(data=pred_universe, x='age_at_arrest', bins=bins)
    plt.title('Histogram of Age of Arrest(Binned)')
    plt.savefig('./data/part3_plots/histogram_age_binned.png', bbox_inches='tight')
    plt.clf()
