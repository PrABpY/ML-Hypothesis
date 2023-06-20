import Hyposis

Hypo = Hyposis.Hypo()
data = Hypo.Format("Sample.csv")
find_s = Hypo.FindS(data,CorrectP = "Yes",CorrectN = "No")
Hypo.HypoAll(data)
print(find_s)
elimination = Hypo.Elimination(data,CorrectP = "Yes",CorrectN = ["No","-"])
Input = ['Many','Small','Yes','Affordable','Few']
Result = Hypo.Checkpart(Input,product = elimination)
print(Result)
print(elimination) 