import pandas as pd

# MITOMASTER RESULT for input Sequence output in CSV (all VARIABLES IN CAPS)
MITOMASTER_RESULT_DATAFRAME = pd.read_csv(input("Enter the result of Query sequence from Mitomaster in CSV format:"))
  # print(MITOMASTER_RESULT_DATAFRAME)
rCRS_POSITION = MITOMASTER_RESULT_DATAFRAME["rCRS Position"]
rCRS_BASE = MITOMASTER_RESULT_DATAFRAME["rCRS NT"]
QUERY_BASE = MITOMASTER_RESULT_DATAFRAME["Query NT"]
MITOMASTER_RESULT_QUERY_SNPs = list()
for I in range(len(rCRS_POSITION)):
	MITOMASTER_RESULT_QUERY_SNPs.append(str(rCRS_POSITION[I])+rCRS_BASE[I]+'>'+QUERY_BASE[I])
 # print(MITOMASTER_RESULT_QUERY_SNPs)

# SNPs List from CLINVAR in CSV ( All varibales in small)
clinvar_dataframe = pd.read_csv("MELAS_genes_split.csv")
 # print(clinvar_dataframe)
clinvar_SNPs_rCRS = clinvar_dataframe["Name"]
dummy_list = list()
clinvar_SNPs_wrt_rCRS = list()
for i in range(len(clinvar_SNPs_rCRS)):
	dummy_list.append(clinvar_SNPs_rCRS[i].split(':')[-1])
	clinvar_SNPs_wrt_rCRS.append(dummy_list[i].split('.')[-1])	
 # print(clinvar_SNPs_wrt_rCRS) 

#print('MITOMASTER_RESULT_DATAFRAME', range(len(MITOMASTER_RESULT_DATAFRAME)), range(len(MITOMASTER_RESULT_QUERY_SNPs)))
#print('clinvar_dataframe', range(len(clinvar_dataframe)), range(len(clinvar_SNPs_wrt_rCRS)))

#SNP SEARCH
for M in range(len(MITOMASTER_RESULT_QUERY_SNPs)):
	for m in range(len(clinvar_SNPs_wrt_rCRS)):
		if MITOMASTER_RESULT_QUERY_SNPs[M]!= clinvar_SNPs_wrt_rCRS[m]: continue
		else :
			print(clinvar_SNPs_wrt_rCRS[m],"Mutation present in the Querry Sequence")
			print(MITOMASTER_RESULT_DATAFRAME.loc[M])
			print(clinvar_dataframe.loc[m])
