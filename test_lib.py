import lib.Hyposis as lb

Hypo = lb.Hypo()
head = ['Sky','Temp','Humid','Wind','Water','Forecast']
Hypo.Create(title = "Hypothesis1",content = head,solution = "Play")
data = Hypo.Format("data3.csv")
find_s = Hypo.FindS(data,Correct = 'Yes')
# Hypo.HypoAll(data)
print(find_s)
elimination = Hypo.Elimination(data,Correct = "Yes")
inp = ['Sunny', 'Cool', 'Normal', 'Strong', 'Warm', 'Change']
# score = Hypo.Score(inp,product = elimination)
# part = Hypo.Partscore(score)
# print(score)
print(elimination)