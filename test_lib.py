import lib.Hyposis as lb

Hypo = lb.Hypo()
data = Hypo.Format("data/data4.csv")
find_s = Hypo.FindS(data,CorrectP = "Yes",CorrectN = "No")
# Hypo.HypoAll(data)
print(find_s)
elimination = Hypo.Elimination(data,CorrectP = "Yes",CorrectN = ["No","-"])
inp = ['Circular','Large','Light','Irregular','Thick']
score = Hypo.Score(inp,product = elimination)
print(score)
print(elimination)