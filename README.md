# Hyposis
Hyposis is a tool for generating list of hypothesis , Which will be considered from examples (csv file) 

## example
Create a hypothesis based on this form. (csv file)
   * "+" -> Accept 
   * "-" -> Reject

Sample | Header1 | Header2 | ... | Result
----- | ----- | ----- | ----- | ----- |
1 | - | - | - | (+,-) |
2 | - | - | - | (+,-) |
3 | - | - | - | (+,-) |
4 | - | - | - | (+,-) |

### _Ex_
file name "_Sample.csv_"
Sample | Citation | Size | InLibrary | Price | Edition | Buy
----- | ----- | ----- | ----- | ----- | ----- | ----- |
1 | Some | Small | No | Affordable | One | No |
2 | Many | Big | No | Expensive | Many | Yes |
3 | Many | Medium | No | Expensive | Few | Yes |
4 | Many | Small | No | Affordable | Many | Yes |

	# Find-S
	Hypo = lb.Hypo()
	data = Hypo.Format("Sample.csv")