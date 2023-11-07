import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
llm = OpenAI(api_token="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")

df = pd.read_csv('jobs.csv')
df = SmartDataframe(df, config={"llm": llm})
print(df.chat('How many data are in th jobs.csv file?'))

print("here")