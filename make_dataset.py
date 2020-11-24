import pandas as pd

#d1 = pd.read_csv('data_raw/sdBShortP_large_Mdot0_alpha_0.3.csv')
#d1['stability_limit'] = 0
#d1['alpha_ce'] = 0.3

#d2 = pd.read_csv('data_raw/sdBShortP_large_Mdot-1_alpha_0.3.csv')
#d2['stability_limit'] = -1
#d2['alpha_ce'] = 0.3

#d3 = pd.read_csv('data_raw/sdBShortP_large_Mdot-2_alpha_0.3.csv')
#d3['stability_limit'] = -2
#d3['alpha_ce'] = 0.3

#d4 = pd.read_csv('data_raw/sdBShortP_large_Mdot-3_alpha_0.3.csv')
#d4['stability_limit'] = -3
#d4['alpha_ce'] = 0.3

#data = pd.concat([d1, d2, d3, d4])

#data.to_csv('data/sdBShortP_training_set.csv', index=False, na_rep='NaN')



# combine the data sets
d1 = pd.read_csv('data_raw/sdBShortP_large_variable_stability_variable_ce_ce_focus.csv')
d2 = pd.read_csv('data_raw/sdBShortP_large_variable_stability_variable_ce.csv')

data = pd.concat([d1, d2])

# read the ce parameters and extract the alpha_ce value
# alpha_ce and alpha_th are the same in all our models
data['alpha_ce'] = data['ce_parameters'].apply(lambda x: eval(x)['a_ce'])

data.to_csv('data/sdBShortP_training_set.csv', index=False, na_rep='NaN')
print('Number of models: ', len(data))
