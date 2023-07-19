import hypos

Hypo = hypos.Hypo()
data = Hypo.Format("Sample.csv")
find_s = Hypo.FindS(data,Correct = "Yes	")
Hypo.HypoAll(data)
print(find_s)
elimination = Hypo.Elimination(data,Correct = "Yes")
Input = ['Many','Small','Yes','Affordable','Few']
Result = Hypo.Checkpart(Input,product = elimination)
print(Result)
print(elimination) 