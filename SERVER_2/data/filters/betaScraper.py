from finvizApproach import FinLister
import json 


#Beta 1-2:https://finviz.com/screener.ashx?v=111&f=ta_beta_1to2&ft=3 DONE
#Beta over 2:https://finviz.com/screener.ashx?v=111&f=ta_beta_o2&ft=3 DONE
#Beta over 3:https://finviz.com/screener.ashx?v=111&f=ta_beta_o3&ft=3 DONE
#Beta 1-1.5 :https://finviz.com/screener.ashx?v=111&f=ta_beta_1to1.5&ft=3 DONE
lister = FinLister("https://finviz.com/screener.ashx?v=111&f=ta_beta_1to1.5&ft=3")
lister.fetch()
stocks = lister.stocks
open("beta1_1_5.json","w").write(json.dumps({"stocks":stocks}))
print("Kentel - Done!")
