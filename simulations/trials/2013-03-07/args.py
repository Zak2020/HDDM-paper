from collections import OrderedDict

def args():
    """
    trials experiment
    """
    run_type='trials'
    estimators=['HDDM2', 'HDDM2Single', 'HDDMGamma', 'Quantiles_group',
                'Quantiles_subj']
    n_subjs=12
    n_trials=[30,50]
    n_params=10
    n_datasets=10
    seed_data=1
    seed_params=1
    equal_seeds=True
    include=['sv']
    depends_on = {'v':'condition'}
    factor3_vals=[1]
    subj_noise = OrderedDict([('v', 0.2), ('a', 0.2), ('t', 0.1)])
    if 'z' in include:
        subj_noise['z'] = .1
    if 'sz' in include:
        subj_noise['sz'] = .05
    if 'st' in include:
        subj_noise['st'] = .1
    if 'sv' in include:
        subj_noise['sv'] = .1
    if run_type == 'regress':
        subj_noise['v_inter':] = 0.1
    return locals()