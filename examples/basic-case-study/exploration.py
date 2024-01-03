import pandas as pd
from plotnine import ggplot, geom_line, aes, labs

# data load
injuries = pd.read_table(
    "neiss/injuries.tsv.gz", 
    delimiter="\t", 
    compression="gzip",
    parse_dates=['trmt_date']
)
products = pd.read_table("neiss/products.tsv")
population = pd.read_table("neiss/population.tsv")

# product: 649, "toilets"
selected = injuries[injuries['prod_code']==649].copy()
selected.shape[0]

## basic summaries
selected.groupby(['location']).agg(n=('weight', 'sum')).sort_values('n', ascending=False).reset_index()
selected.groupby(['body_part']).agg(n=('weight', 'sum')).sort_values('n', ascending=False).reset_index()
selected.groupby(['diag']).agg(n=('weight', 'sum')).sort_values('n', ascending=False).reset_index()

## pattern across age and sex
summary = selected.groupby(['age', 'sex']).agg(n=('weight', 'sum')).reset_index()
summary

(ggplot(summary, aes('age', 'n', colour='sex'))
 + geom_line()
 + labs(y="Estimated number of injuries"))

## injury rate
summary = selected.groupby(['age', 'sex']).agg(n=('weight', 'sum')).reset_index().\
    merge(population, how='left', on=['age', 'sex'])
summary['rate'] = summary['n'] / summary['population'] * 1e4

(ggplot(summary, aes('age', 'rate', colour='sex'))
 + geom_line(na_rm=True)
 + labs(y="Injuries per 10,000 people"))

## narratives
selected.sample(10)['narrative']

