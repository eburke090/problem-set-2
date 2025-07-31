'''
- You will run Problem Set 2 from this .py, so make sure to set things up to return outputs accordingly
- Go through each PART and write code / make updates as necessary to produce all required outputs
- Run main.py before you start
'''

import src.part1_etl as part1
import src.part2_plot_examples as part2
import src.part3_bar_hist as part3
import src.part4_catplot as part4
import src.part5_scatter as part5

def main():
    ##  PART 1: ETL  ##
    # ETL the datasets into dataframes
    directories = ['data/part2_plots', 'data/part3_plots', 'data/part4_plots', 'data/part5_plots']
    part1.create_directories(directories)
    
    pred_universe, arrest_events, charge_counts, charge_counts_by_offense, felony_charge, merged_df = part1.extract_transform()
    
    ##  PART 2: PLOT EXAMPLES  ##
    # Apply plot theme
    part2.seaborn_settings()

    # Generate plots
    part2.barplots(charge_counts, charge_counts_by_offense)
    part2.cat_plots(charge_counts, pred_universe)
    part2.histograms(pred_universe)
    part2.scatterplot(pred_universe)


    ##  PART 3: BAR PLOTS AND HISTOGRAMS  ##

    part3.create_p3_directory()

    # 1
    part3.barplot_fta(pred_universe)
    print("Saved: barplot_fta.png")

    # 2
    part3.barplot_fta_by_sex(pred_universe)
    print("Saved: barplot_fta_by_sex.png")

    # 3
    part3.histogram_age(pred_universe)
    print("Saved: histogram_age.png")

    # 4
    part3.histogram_age_binned(pred_universe)
    print("Saved: histogram_age_binned.png")

    ##  PART 4: CATEGORICAL PLOTS  ##
    part4.create_p4_directory()

    # 1
    part4.catplot_felony_prediction(merged_df)
    print("Saved: felony_prediction_by_charge_type.png")
    
    # 2
    part4.catplot_nonfelony_prediction(merged_df)
    print("Saved: nonfelony_prediction_by_charge_type.png")

    # 3
    part4.catplot_actual_rearresst(merged_df)
    print("Saved: felony_prediction_actual.png")

    ##  PART 5: SCATTERPLOTS  ##
    part5.create_p5_directory()

    # 1
    part5.scatter_prediction_by_charge(merged_df)
    print("Saved: prediction_scatter_by_charge.png")
    
    # 2
    part5.scatter_felony_prediction_vs_outcome(merged_df)
    print("Saved: felony_prediction_vs_actual.png")


if __name__ == "__main__":
    main()