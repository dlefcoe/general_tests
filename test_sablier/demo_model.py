import sablier_flow as sf

API_KEY = "sk_live_haKKsl7dgZ_xCuxdw8wxHekQqnuBexJsj_5sL47ThDo"

'''
Set it in your shell: export SABLIER_API_KEY="sk_live_…"
'''

df = sf.demo_data()
fit = sf.fit(df, horizon=252)
paths = sf.generate(fit.model_id, n_paths=1000)

report = sf.robustness(my_backtest(df), [my_backtest(p) for p in paths.as_dataframes()])
print(report.summary())



