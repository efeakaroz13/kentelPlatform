import json 

string = """
Code,Company,Link,"Market Cap","Last trade",Change,%Change,Sector
ASX:BHP,"BHP Group Limited (ASX:BHP)",https://www.listcorp.com/asx/bhp/bhp-group-limited,"	217932000000",43.02,0.00,0,Materials
ASX:CBA,"Commonwealth Bank (ASX:CBA)",https://www.listcorp.com/asx/cba/commonwealth-bank,"	166896000000",99.57,0.00,0,Financials
ASX:CSL,"CSL Limited (ASX:CSL)",https://www.listcorp.com/asx/csl/csl-limited,"	127066000000",263.42,0.00,0,"Health Care"
ASX:NAB,"National Australia Bank (ASX:NAB)",https://www.listcorp.com/asx/nab/nab,"	87561000000",27.89,0.00,0,Financials
ASX:WBC,"Westpac Banking Corp (ASX:WBC)",https://www.listcorp.com/asx/wbc/westpac,"	74813500000",21.32,0.00,0,Financials
ASX:ANZ,"ANZ Group Holdings Limited (ASX:ANZ)",https://www.listcorp.com/asx/anz/anz-group-holdings-limited,"	73148700000",24.34,0.00,0,Financials
ASX:WDS,"Woodside Energy Group Ltd (ASX:WDS)",https://www.listcorp.com/asx/wds/woodside-energy-group,"	71525900000",37.67,0.00,0,Energy
ASX:MQG,"Macquarie Group Limited (ASX:MQG)",https://www.listcorp.com/asx/mqg/macquarie-group-limited,"	66392800000",171.79,0.00,0,Financials
ASX:FMG,"Fortescue Metals Group (ASX:FMG)",https://www.listcorp.com/asx/fmg/fortescue-metals,"	64442700000",20.93,0.00,0,Materials
ASX:WES,"Wesfarmers Limited (ASX:WES)",https://www.listcorp.com/asx/wes/wesfarmers-limited,"	57833600000",51,0.00,0,"Consumer Discretionary"
ASX:TLS,"Telstra Group Limited (ASX:TLS)",https://www.listcorp.com/asx/tls/telstra-group-limited,"	46333300000",4.01,0.00,0,"Communication Services"
ASX:WOW,"Woolworths Group Limited (ASX:WOW)",https://www.listcorp.com/asx/wow/woolworths-group,"	45591600000",37.41,0.00,0,"Consumer Staples"
ASX:GMG,"Goodman Group (ASX:GMG)",https://www.listcorp.com/asx/gmg/goodman-group,"	42536700000",22.58,0.00,0,"Real Estate"
ASX:TCL,"Transurban Group (ASX:TCL)",https://www.listcorp.com/asx/tcl/transurban,"	40388300000",13.08,0.00,0,Industrials
ASX:RIO,"Rio Tinto (ASX:RIO)",https://www.listcorp.com/asx/rio/rio-tinto,"	40054200000",107.9,0.00,0,Materials
ASX:ALL,"Aristocrat Leisure Limited (ASX:ALL)",https://www.listcorp.com/asx/all/aristocrat-leisure-limited,"	25916800000",39.96,0.00,0,"Consumer Discretionary"
ASX:STO,"Santos Limited (ASX:STO)",https://www.listcorp.com/asx/sto/santos-limited,"	25072800000",7.72,0.00,0,Energy
ASX:WTC,"WiseTech Global Limited (ASX:WTC)",https://www.listcorp.com/asx/wtc/wisetech-global-limited,"	23777800000",71.65,0.00,0,"Information Technology"
ASX:NCM,"Newcrest Mining Limited (ASX:NCM)",https://www.listcorp.com/asx/ncm/newcrest-mining-limited,"	22767100000",25.46,0.00,0,Materials
ASX:QBE,"QBE Insurance Group Limited (ASX:QBE)",https://www.listcorp.com/asx/qbe/qbe-insurance-group-limited,"	21620300000",14.49,0.00,0,Financials
ASX:REA,"REA Group Ltd (ASX:REA)",https://www.listcorp.com/asx/rea/rea-group,"	21321100000",161.38,0.00,0,"Communication Services"
ASX:COL,"Coles Group Limited (ASX:COL)",https://www.listcorp.com/asx/col/coles-group-limited,"	21293800000",15.91,0.00,0,"Consumer Staples"
ASX:BXB,"Brambles Limited (ASX:BXB)",https://www.listcorp.com/asx/bxb/brambles-limited,"	19533700000",14.06,0.00,0,Industrials
ASX:JHX,"James Hardie Industries plc (ASX:JHX)",https://www.listcorp.com/asx/jhx/james-hardie-industries-plc,"	19435900000",44.15,0.00,0,Materials
ASX:XRO,"Xero Limited (ASX:XRO)",https://www.listcorp.com/asx/xro/xero-limited,"	17969500000",118.67,0.00,0,"Information Technology"
ASX:COH,"Cochlear Limited (ASX:COH)",https://www.listcorp.com/asx/coh/cochlear-limited,"	17398300000",264.98,0.00,0,"Health Care"
ASX:SUN,"Suncorp Group Limited (ASX:SUN)",https://www.listcorp.com/asx/sun/suncorp-group-limited,"	16528400000",13.05,0.00,0,Financials
ASX:S32,"South32 Limited (ASX:S32)",https://www.listcorp.com/asx/s32/south32-limited,"	15818000000",3.48,0.00,0,Materials
ASX:SHL,"Sonic Healthcare Limited (ASX:SHL)",https://www.listcorp.com/asx/shl/sonic-healthcare,"	15063900000",31.88,0.00,0,"Health Care"
ASX:ORG,"Origin Energy Limited (ASX:ORG)",https://www.listcorp.com/asx/org/origin-energy-limited,"	14901800000",8.65,0.00,0,Utilities
ASX:CPU,"Computershare Limited (ASX:CPU)",https://www.listcorp.com/asx/cpu/computershare-limited,"	14894000000",24.67,0.00,0,Industrials
ASX:PLS,"Pilbara Minerals Limited (ASX:PLS)",https://www.listcorp.com/asx/pls/pilbara-minerals-limited,"	14116700000",4.7,0.00,0,Materials
ASX:SCG,"Scentre Group Limited (ASX:SCG)",https://www.listcorp.com/asx/scg/scentre-group-limited,"	14065900000",2.71,0.00,0,"Real Estate"
ASX:IAG,"Insurance Australia Group Limited (ASX:IAG)",https://www.listcorp.com/asx/iag/insurance-australia-group-limited,"	13862300000",5.68,0.00,0,Financials
ASX:NST,"Northern Star Resources Limited (ASX:NST)",https://www.listcorp.com/asx/nst/northern-star-resources-limited,"	12864500000",11.17,0.00,0,Materials
ASX:MIN,"Mineral Resources Limited (ASX:MIN)",https://www.listcorp.com/asx/min/mineral-resources-limited,"	12752100000",65.57,0.00,0,Materials
ASX:REH,"Reece Limited (ASX:REH)",https://www.listcorp.com/asx/reh/reece-limited,"	12654800000",19.59,0.00,0,Industrials
ASX:VAS,"Vanguard Australian Shares Index ETF (ASX:VAS)",https://www.listcorp.com/asx/vas/vanguard-australian-shares-index-etf,"	12031600000",88.47,0.00,0,Financials
ASX:FPH,"Fisher & Paykel Healthcare Corporation Limited (ASX:FPH)",https://www.listcorp.com/asx/fph/fisher-and-paykel-healthcare-corporation-limited,"	11930800000",20.51,0.00,0,"Health Care"
ASX:SOL,"Washington H. Soul Pattinson and Company Limited (ASX:SOL)",https://www.listcorp.com/asx/sol/washington-h.-soul-pattinson-and-company-limited,"	11525700000",31.93,0.00,0,Financials
ASX:TLC,"The Lottery Corporation Limited (ASX:TLC)",https://www.listcorp.com/asx/tlc/the-lottery-corporation-limited,"	11173400000",5.02,0.00,0,"Consumer Discretionary"
ASX:RHC,"Ramsay Health Care Limited (ASX:RHC)",https://www.listcorp.com/asx/rhc/ramsay-health-care-limited,"	11096500000",48.42,0.00,0,"Health Care"
ASX:ASX,"ASX Limited (ASX:ASX)",https://www.listcorp.com/asx/asx/asx-limited,"	11089100000",57.28,0.00,0,Financials
ASX:QAN,"Qantas Airways Limited (ASX:QAN)",https://www.listcorp.com/asx/qan/qantas-airways-limited,"	10760600000",6.24,0.00,0,Industrials
ASX:RMD,"ResMed Inc (ASX:RMD)",https://www.listcorp.com/asx/rmd/resmed-inc,"	10732400000",25.15,0.00,0,"Health Care"
ASX:AIA,"Auckland International Airport Limited (ASX:AIA)",https://www.listcorp.com/asx/aia/auckland-international-airport-limited,"	10676000000",7.25,0.00,0,Industrials
ASX:CAR,"Carsales.com Ltd (ASX:CAR)",https://www.listcorp.com/asx/car/carsales.com-ltd,"	10440900000",27.7,0.00,0,"Communication Services"
ASX:APA,"APA Group (ASX:APA)",https://www.listcorp.com/asx/apa/apa-group,"	10276900000",8.71,0.00,0,Utilities
ASX:TPG,"TPG Telecom Limited (ASX:TPG)",https://www.listcorp.com/asx/tpg/tpg-telecom-limited,"	10170600000",5.47,0.00,0,"Communication Services"
ASX:SGP,"Stockland (ASX:SGP)",https://www.listcorp.com/asx/sgp/stockland,"	9954510000",4.17,0.00,0,"Real Estate"
ASX:EDV,"Endeavour Group Limited (ASX:EDV)",https://www.listcorp.com/asx/edv/endeavour-group-limited,"	9850390000",5.5,0.00,0,"Consumer Staples"
ASX:SVW,"Seven Group Holdings Limited (ASX:SVW)",https://www.listcorp.com/asx/svw/seven-group-holdings-limited,"	9843980000",27.08,0.00,0,Industrials
ASX:MPL,"Medibank Private Limited (ASX:MPL)",https://www.listcorp.com/asx/mpl/medibank-private-limited,"	9831790000",3.57,0.00,0,Financials
ASX:IGO,"IGO Limited (ASX:IGO)",https://www.listcorp.com/asx/igo/igo-limited,"	9814190000",12.96,0.00,0,Materials
ASX:AMC,"Amcor Limited (ASX:AMC)",https://www.listcorp.com/asx/amc/amcor-limited,"	9389340000",14.59,0.00,0,Materials
ASX:BSL,"BlueScope Steel Limited (ASX:BSL)",https://www.listcorp.com/asx/bsl/bluescope-steel-limited,"	9320880000",20.46,0.00,0,Materials
ASX:MGR,"Mirvac Group (ASX:MGR)",https://www.listcorp.com/asx/mgr/mirvac-group,"	9233310000",2.34,0.00,0,"Real Estate"
ASX:AKE,"Allkem Limited (ASX:AKE)",https://www.listcorp.com/asx/ake/allkem-limited,"	8850690000",13.88,0.00,0,Materials
ASX:WOR,"Worley Limited (ASX:WOR)",https://www.listcorp.com/asx/wor/worley-limited,"	8842530000",16.84,0.00,0,Industrials
ASX:ALX,"Atlas Arteria (ASX:ALX)",https://www.listcorp.com/asx/alx/atlas-arteria,"	8792050000",6.06,0.00,0,Industrials
ASX:TWE,"Treasury Wine Estates Limited (ASX:TWE)",https://www.listcorp.com/asx/twe/treasury-wine-estates-limited,"	8568340000",11.87,0.00,0,"Consumer Staples"
ASX:SPK,"Spark New Zealand Limited (ASX:SPK)",https://www.listcorp.com/asx/spk/spark-new-zealand-limited,"	8542350000",4.63,0.00,0,"Communication Services"
ASX:AFI,"Australian Foundation Investment Company Limited (ASX:AFI)",https://www.listcorp.com/asx/afi/australian-foundation-investment-company-limited,"	8508790000",6.86,0.00,0,Financials
ASX:VCX,"Vicinity Centres (ASX:VCX)",https://www.listcorp.com/asx/vcx/vicinity-centres,"	8262380000",1.815,0.00,0,"Real Estate"
ASX:SEK,"SEEK Limited (ASX:SEK)",https://www.listcorp.com/asx/sek/seek-limited,"	8260750000",23.19,0.00,0,"Communication Services"
ASX:DXS,"Dexus (ASX:DXS)",https://www.listcorp.com/asx/dxs/dexus,"	8174300000",7.6,0.00,0,"Real Estate"
ASX:MCY,"Mercury NZ Limited (ASX:MCY)",https://www.listcorp.com/asx/mcy/mercury-nz-limited,"	8059450000",5.81,0.00,0,Utilities
ASX:ALD,"Ampol Limited (ASX:ALD)",https://www.listcorp.com/asx/ald/ampol-limited,"	8033160000",33.71,0.00,0,Energy
ASX:GPT,"The GPT Group (ASX:GPT)",https://www.listcorp.com/asx/gpt/gpt-group,"	7834710000",4.09,0.00,0,"Real Estate"
ASX:IFT,"Infratil Limited (ASX:IFT)",https://www.listcorp.com/asx/ift/infratil-limited,"	7703300000",9.26,0.00,0,Industrials
ASX:PME,"Pro Medicus Limited (ASX:PME)",https://www.listcorp.com/asx/pme/pro-medicus,"	7573430000",72.52,0.00,0,"Health Care"
ASX:AGL,"AGL Energy Limited (ASX:AGL)",https://www.listcorp.com/asx/agl/agl-energy-limited,"	7373310000",10.96,0.00,0,Utilities
ASX:IEL,"IDP Education Limited (ASX:IEL)",https://www.listcorp.com/asx/iel/idp-education-limited,"	7231170000",25.98,0.00,0,"Consumer Discretionary"
ASX:NXT,"NEXTDC Limited (ASX:NXT)",https://www.listcorp.com/asx/nxt/nextdc-limited,"	7009490000",13.62,0.00,0,"Information Technology"
ASX:MGOC,"Magellan Global Fund (Open Class)(Managed Fund) (ASX:MGOC)",https://www.listcorp.com/asx/mgoc/magellan-global-fund-open-class-managed-fund,"	6872260000",2.65,0.00,0,Financials
ASX:ORI,"Orica Limited (ASX:ORI)",https://www.listcorp.com/asx/ori/orica-limited,"	6818710000",14.97,0.00,0,Materials
ASX:YAL,"Yancoal Australia Ltd (ASX:YAL)",https://www.listcorp.com/asx/yal/yancoal-australia-ltd,"	6787060000",5.14,0.00,0,Energy
ASX:AZJ,"Aurizon Holdings Limited (ASX:AZJ)",https://www.listcorp.com/asx/azj/aurizon-holdings-limited,"	6773790000",3.68,0.00,0,Industrials
ASX:ARG,"Argo Investments Limited (ASX:ARG)",https://www.listcorp.com/asx/arg/argo-investments-limited,"	6543190000",8.66,0.00,0,Financials
ASX:LYC,"Lynas Rare Earths Limited (ASX:LYC)",https://www.listcorp.com/asx/lyc/lynas-rare-earths-limited,"	6508690000",6.97,0.00,0,Materials
ASX:EVN,"Evolution Mining Limited (ASX:EVN)",https://www.listcorp.com/asx/evn/evolution-mining-limited,"	6373470000",3.47,0.00,0,Materials
ASX:EBO,"EBOS Group Limited (ASX:EBO)",https://www.listcorp.com/asx/ebo/ebos-group-limited,"	6342390000",33.1,0.00,0,"Health Care"
ASX:ALU,"Altium Limited (ASX:ALU)",https://www.listcorp.com/asx/alu/altium-limited,"	6299310000",47.85,0.00,0,"Information Technology"
ASX:MEZ,"Meridian Energy Limited (ASX:MEZ)",https://www.listcorp.com/asx/mez/meridian-energy-limited,"	6233960000",4.93,0.00,0,Utilities
ASX:VGS,"Vanguard MSCI Index International Shares ETF (ASX:VGS)",https://www.listcorp.com/asx/vgs/vanguard-msci-index-international-shares-etf,"	6218930000",107.99,0.00,0,Financials
ASX:LTR,"Liontown Resources Limited (ASX:LTR)",https://www.listcorp.com/asx/ltr/liontown-resources-limited,"	6078230000",2.76,0.00,0,Materials
ASX:IVV,"iShares S&P 500 ETF (ASX:IVV)",https://www.listcorp.com/asx/ivv/ishares-s-and-p-500-etf,"	6005030000",45.55,0.00,0,Financials
ASX:SDF,"Steadfast Group Limited (ASX:SDF)",https://www.listcorp.com/asx/sdf/steadfast-group,"	5784790000",5.57,0.00,0,Financials
ASX:CWY,"Cleanaway Waste Management Limited (ASX:CWY)",https://www.listcorp.com/asx/cwy/cleanaway-waste-management-limited,"	5699180000",2.56,0.00,0,Industrials
ASX:IPL,"Incitec Pivot Limited (ASX:IPL)",https://www.listcorp.com/asx/ipl/incitec-pivot-limited,"	5632450000",2.9,0.00,0,Materials
ASX:BLD,"Boral Limited (ASX:BLD)",https://www.listcorp.com/asx/bld/boral-limited,"	5548530000",5.03,0.00,0,Materials
ASX:WHC,"Whitehaven Coal Limited (ASX:WHC)",https://www.listcorp.com/asx/whc/whitehaven-coal,"	5421170000",6.48,0.00,0,Energy
ASX:ALQ,"ALS Limited (ASX:ALQ)",https://www.listcorp.com/asx/alq/als-limited,"	5350050000",11.05,0.00,0,Industrials
ASX:QUB,"Qube Holdings Limited (ASX:QUB)",https://www.listcorp.com/asx/qub/qube-holdings-limited,"	5332600000",3.02,0.00,0,Industrials
ASX:BEN,"Bendigo and Adelaide Bank Limited (ASX:BEN)",https://www.listcorp.com/asx/ben/bendigo-and-adelaide-bank-limited,"	5279970000",9.3,0.00,0,Financials
ASX:LLC,"Lendlease Group (ASX:LLC)",https://www.listcorp.com/asx/llc/lendlease-group,"	5225060000",7.58,0.00,0,"Real Estate"
ASX:CHC,"Charter Hall Group (ASX:CHC)",https://www.listcorp.com/asx/chc/charter-hall-group,"	4975930000",10.52,0.00,0,"Real Estate"
ASX:TNE,"Technology One Limited (ASX:TNE)",https://www.listcorp.com/asx/tne/technology-one-limited,"	4863630000",14.98,0.00,0,"Information Technology"
ASX:JBH,"JB Hi-Fi Limited (ASX:JBH)",https://www.listcorp.com/asx/jbh/jb-hi-fi-limited,"	4863180000",44.48,0.00,0,"Consumer Discretionary"
ASX:VEA,"Viva Energy Group Limited (ASX:VEA)",https://www.listcorp.com/asx/vea/viva-energy-group-limited,"	4740590000",3.07,0.00,0,Energy
ASX:FLT,"Flight Centre Travel Group Limited (ASX:FLT)",https://www.listcorp.com/asx/flt/flight-centre-travel-group-limited,"	4737210000",21.72,0.00,0,"Consumer Discretionary"
ASX:HVN,"Harvey Norman Holdings Limited (ASX:HVN)",https://www.listcorp.com/asx/hvn/harvey-norman-holdings-limited,"	4684980000",3.76,0.00,0,"Consumer Discretionary"
ASX:STW,"SPDR S&P/ASX 200 Fund (ASX:STW)",https://www.listcorp.com/asx/stw/spdr-s-and-p-asx-200-fund,"	4672030000",64.34,0.00,0,Financials
ASX:CGF,"Challenger Limited (ASX:CGF)",https://www.listcorp.com/asx/cgf/challenger-limited,"	4634520000",6.74,0.00,0,Financials
ASX:NHC,"New Hope Corporation Limited (ASX:NHC)",https://www.listcorp.com/asx/nhc/new-hope-corporation-limited,"	4632440000",5.48,0.00,0,Energy
ASX:DMP,"Domino's Pizza Enterprises Limited (ASX:DMP)",https://www.listcorp.com/asx/dmp/dominos-pizza-enterprises-limited,"	4608650000",51.73,0.00,0,"Consumer Discretionary"
ASX:GQG,"GQG Partners Inc. (ASX:GQG)",https://www.listcorp.com/asx/gqg/gqg-partners,"	4473500000",1.515,0.00,0,Financials
ASX:IOZ,"iShares Core S&P/ASX 200 ETF (ASX:IOZ)",https://www.listcorp.com/asx/ioz/ishares-core-s-and-p-asx-200-etf,"	4062930000",28.77,0.00,0,Financials
ASX:PMV,"Premier Investments Limited (ASX:PMV)",https://www.listcorp.com/asx/pmv/premier-investments-limited,"	4020420000",25.25,0.00,0,"Consumer Discretionary"
ASX:BKW,"Brickworks Limited (ASX:BKW)",https://www.listcorp.com/asx/bkw/brickworks-limited,"	3984240000",26.17,0.00,0,Materials
ASX:QUAL,"VanEck MSCI International Quality ETF (ASX:QUAL)",https://www.listcorp.com/asx/qual/vaneck-msci-international-quality-etf,"	3963840000",45.57,0.00,0,Financials
ASX:NHF,"NIB Holdings Limited (ASX:NHF)",https://www.listcorp.com/asx/nhf/nib-holdings-limited,"	3881980000",8.03,0.00,0,Financials
ASX:BOQ,"Bank of Queensland Limited (ASX:BOQ)",https://www.listcorp.com/asx/boq/bank-of-queensland-limited,"	3871010000",5.89,0.00,0,Financials
ASX:NWL,"Netwealth Group Limited (ASX:NWL)",https://www.listcorp.com/asx/nwl/netwealth-group-limited,"	3714460000",15.23,0.00,0,Financials
ASX:APE,"Eagers Automotive Limited (ASX:APE)",https://www.listcorp.com/asx/ape/eagers-automotive-limited,"	3665970000",14.27,0.00,0,"Consumer Discretionary"
ASX:MTS,"Metcash Limited (ASX:MTS)",https://www.listcorp.com/asx/mts/metcash-limited,"	3566270000",3.65,0.00,0,"Consumer Staples"
ASX:VTS,"Vanguard US Total Market Shares Index ETF (ASX:VTS)",https://www.listcorp.com/asx/vts/vanguard-us-total-market-shares-index-etf,"	3564390000",338.76,0.00,0,Financials
ASX:BRG,"Breville Group Limited (ASX:BRG)",https://www.listcorp.com/asx/brg/breville-group-limited,"	3522420000",24.67,0.00,0,"Consumer Discretionary"
ASX:FBU,"Fletcher Building Limited (ASX:FBU)",https://www.listcorp.com/asx/fbu/fletcher-building-limited,"	3484540000",4.45,0.00,0,Industrials
ASX:BPT,"Beach Energy Limited (ASX:BPT)",https://www.listcorp.com/asx/bpt/beach-energy-limited,"	3456220000",1.515,0.00,0,Energy
ASX:AMP,"AMP Limited (ASX:AMP)",https://www.listcorp.com/asx/amp/amp-limited,"	3442280000",1.23,0.00,0,Financials
ASX:ILU,"Iluka Resources Limited (ASX:ILU)",https://www.listcorp.com/asx/ilu/iluka-resources-limited,"	3391060000",7.96,0.00,0,Materials
ASX:A2M,"The A2 Milk Company Limited (ASX:A2M)",https://www.listcorp.com/asx/a2m/the-a2-milk-company,"	3386070000",4.69,0.00,0,"Consumer Staples"
ASX:NDQ,"BetaShares NASDAQ 100 ETF (ASX:NDQ)",https://www.listcorp.com/asx/ndq/betashares-nasdaq-100-etf,"	3337430000",35.01,0.00,0,Financials
ASX:TLX,"Telix Pharmaceuticals Limited (ASX:TLX)",https://www.listcorp.com/asx/tlx/telix-pharmaceuticals-limited,"	3328620000",10.44,0.00,0,"Health Care"
ASX:AWC,"Alumina Limited (ASX:AWC)",https://www.listcorp.com/asx/awc/alumina-limited,"	3249880000",1.12,0.00,0,Materials
ASX:NEC,"Nine Entertainment Co. Holdings Limited (ASX:NEC)",https://www.listcorp.com/asx/nec/nine-entertainment-co-holdings-limited,"	3247280000",1.995,0.00,0,"Communication Services"
ASX:AUB,"AUB Group Limited (ASX:AUB)",https://www.listcorp.com/asx/aub/aub-group-limited,"	3230490000",29.8,0.00,0,Financials
ASX:RWC,"Reliance Worldwide Corporation Limited (ASX:RWC)",https://www.listcorp.com/asx/rwc/reliance-worldwide-corporation-limited,"	3152480000",3.99,0.00,0,Industrials
ASX:CNU,"Chorus Limited (ASX:CNU)",https://www.listcorp.com/asx/cnu/chorus-limited,"	3147470000",7.23,0.00,0,"Communication Services"
ASX:A200,"BetaShares Australia 200 ETF (ASX:A200)",https://www.listcorp.com/asx/a200/betashares-australia-200-etf,"	3094930000",118.66,0.00,0,Financials
ASX:AAA,"BetaShares Australian High Interest Cash ETF (ASX:AAA)",https://www.listcorp.com/asx/aaa/betashares-australian-high-interest-cash-etf,"	3069340000",50.215,0.00,0,Financials
ASX:NSR,"National Storage REIT (ASX:NSR)",https://www.listcorp.com/asx/nsr/national-storage-reit,"	3047340000",2.26,0.00,0,"Real Estate"
ASX:GOLD,"Global X Physical Gold (ASX:GOLD)",https://www.listcorp.com/asx/gold/global-x-physical-gold,"	3019870000",27.66,0.00,0,Financials
ASX:CIA,"Champion Iron Limited (ASX:CIA)",https://www.listcorp.com/asx/cia/champion-iron-limited,"	3010660000",5.82,0.00,0,Materials
ASX:ORA,"Orora Group Limited (ASX:ORA)",https://www.listcorp.com/asx/ora/orora-group-limited,"	2975640000",3.52,0.00,0,Materials
ASX:VHY,"Vanguard Australian Shares High Yield ETF (ASX:VHY)",https://www.listcorp.com/asx/vhy/vanguard-australian-shares-high-yield-etf,"	2939940000",66.19,0.00,0,Financials
ASX:ANN,"Ansell Limited (ASX:ANN)",https://www.listcorp.com/asx/ann/ansell-limited,"	2914260000",22.98,0.00,0,"Health Care"
ASX:SFR,"Sandfire Resources Limited (ASX:SFR)",https://www.listcorp.com/asx/sfr/sandfire-resources-limited,"	2864710000",6.27,0.00,0,Materials
ASX:WEB,"Webjet Limited (ASX:WEB)",https://www.listcorp.com/asx/web/webjet-limited,"	2863720000",7.43,0.00,0,"Consumer Discretionary"
ASX:SGM,"Sims Limited (ASX:SGM)",https://www.listcorp.com/asx/sgm/sims-limited,"	2861020000",14.81,0.00,0,Materials
ASX:SUL,"Super Retail Group Limited (ASX:SUL)",https://www.listcorp.com/asx/sul/super-retail-group-limited,"	2858960000",12.66,0.00,0,"Consumer Discretionary"
ASX:IOO,"iShares Global 100 ETF (ASX:IOO)",https://www.listcorp.com/asx/ioo/ishares-global-100-etf,"	2857980000",115.3,0.00,0,Financials
ASX:CSR,"CSR Limited (ASX:CSR)",https://www.listcorp.com/asx/csr/csr-limited,"	2773600000",5.81,0.00,0,Materials
ASX:ARB,"ARB Corporation Limited (ASX:ARB)",https://www.listcorp.com/asx/arb/arb-corporation-limited,"	2765930000",33.69,0.00,0,"Consumer Discretionary"
ASX:AVZ,"AVZ Minerals Limited (ASX:AVZ)",https://www.listcorp.com/asx/avz/avz-minerals-limited,"	2752410000",0.78,0.00,0,Materials
ASX:DOW,"Downer EDI Limited (ASX:DOW)",https://www.listcorp.com/asx/dow/downer-edi-limited,"	2746740000",4.09,0.00,0,Industrials
ASX:CTD,"Corporate Travel Management Limited (ASX:CTD)",https://www.listcorp.com/asx/ctd/corporate-travel-management,"	2728980000",18.65,0.00,0,"Consumer Discretionary"
ASX:SQ2,"Block Inc. (ASX:SQ2)",https://www.listcorp.com/asx/sq2/block-inc,"	2685190000",87.01,0.00,0,Financials
ASX:CRN,"Coronado Global Resources Inc. (ASX:CRN)",https://www.listcorp.com/asx/crn/coronado-global-resources-inc.,"	2665560000",1.59,0.00,0,Materials
ASX:ZIM,"Zimplats Holdings Limited (ASX:ZIM)",https://www.listcorp.com/asx/zim/zimplats-holdings-limited,"	2638200000",24.51,0.00,0,Materials
ASX:VEU,"Vanguard All-World Ex-US Shares Index ETF (ASX:VEU)",https://www.listcorp.com/asx/veu/vanguard-all-world-ex-us-shares-index-etf,"	2604720000",82.54,0.00,0,Financials
ASX:ETHI,"BetaShares Global Sustainability Leaders ETF (ASX:ETHI)",https://www.listcorp.com/asx/ethi/betashares-global-sustainability-leaders-etf,"	2587270000",12.53,0.00,0,Financials
ASX:NIC,"Nickel Industries Limited (ASX:NIC)",https://www.listcorp.com/asx/nic/nickel-industries-limited,"	2571610000",0.75,0.00,0,Materials
ASX:HUB,"HUB24 Limited (ASX:HUB)",https://www.listcorp.com/asx/hub/hub24-limited,"	2550210000",31.29,0.00,0,Financials
ASX:SMR,"Stanmore Resources Limited (ASX:SMR)",https://www.listcorp.com/asx/smr/stanmore-resources-limited,"	2532910000",2.81,0.00,0,Materials
ASX:PDN,"Paladin Energy Limited (ASX:PDN)",https://www.listcorp.com/asx/pdn/paladin-energy,"	2504150000",0.84,0.00,0,Energy
ASX:CLW,"Charter Hall Long WALE REIT (ASX:CLW)",https://www.listcorp.com/asx/clw/charter-hall-long-wale-reit,"	2501430000",3.46,0.00,0,"Real Estate"
ASX:BFL,"BSP Financial Group Limited (ASX:BFL)",https://www.listcorp.com/asx/bfl/bsp-financial-group-limited,"	2499630000",5.35,0.00,0,Financials
ASX:PPT,"Perpetual Limited (ASX:PPT)",https://www.listcorp.com/asx/ppt/perpetual-limited,"	2479890000",22.04,0.00,0,Financials
ASX:HDN,"HomeCo Daily Needs REIT (ASX:HDN)",https://www.listcorp.com/asx/hdn/homeco-daily-needs-reit,"	2478870000",1.195,0.00,0,"Real Estate"
ASX:MGF,"Magellan Global Fund (ASX:MGF)",https://www.listcorp.com/asx/mgf/magellan-global-fund,"	2467400000",1.715,0.00,0,Financials
ASX:RGN,"Region Group (ASX:RGN)",https://www.listcorp.com/asx/rgn/region-group,"	2458630000",2.14,0.00,0,"Real Estate"
ASX:LOV,"Lovisa Holdings Limited (ASX:LOV)",https://www.listcorp.com/asx/lov/lovisa-holdings-limited,"	2432690000",22.56,0.00,0,"Consumer Discretionary"
ASX:AIZ,"Air New Zealand Limited (ASX:AIZ)",https://www.listcorp.com/asx/aiz/air-new-zealand-limited,"	2425290000",0.72,0.00,0,Industrials
ASX:GNE,"Genesis Energy Limited (ASX:GNE)",https://www.listcorp.com/asx/gne/genesis-energy-limited,"	2418170000",2.27,0.00,0,Utilities
ASX:PRU,"Perseus Mining Limited (ASX:PRU)",https://www.listcorp.com/asx/pru/perseus-mining-limited,"	2411190000",1.76,0.00,0,Materials
ASX:VAP,"Vanguard Australian Property Securities Index ETF (ASX:VAP)",https://www.listcorp.com/asx/vap/vanguard-australian-property-securities-index-etf,"	2389760000",78.87,0.00,0,Financials
ASX:VGAD,"Vanguard MSCI Index International Shares (Hedged) ETF (ASX:VGAD)",https://www.listcorp.com/asx/vgad/vanguard-msci-index-international-shares-hedged-etf,"	2374300000",85.25,0.00,0,Financials
ASX:DHG,"Domain Holdings Australia Limited (ASX:DHG)",https://www.listcorp.com/asx/dhg/domain-holdings-australia,"	2349760000",3.72,0.00,0,"Communication Services"
ASX:TAH,"Tabcorp Holdings Limited (ASX:TAH)",https://www.listcorp.com/asx/tah/tabcorp-holdings-limited,"	2304390000",1.01,0.00,0,"Consumer Discretionary"
ASX:BWP,"BWP Trust (ASX:BWP)",https://www.listcorp.com/asx/bwp/bwp-trust,"	2293310000",3.57,0.00,0,"Real Estate"
ASX:VNT,"Ventia Services Group Limited (ASX:VNT)",https://www.listcorp.com/asx/vnt/ventia-services-group-limited,"	2275590000",2.66,0.00,0,Industrials
ASX:DRR,"Deterra Royalties Limited (ASX:DRR)",https://www.listcorp.com/asx/drr/deterra-royalties-limited,"	2273190000",4.3,0.00,0,Materials
ASX:BAP,"Bapcor Limited (ASX:BAP)",https://www.listcorp.com/asx/bap/bapcor-limited,"	2229940000",6.57,0.00,0,"Consumer Discretionary"
ASX:HYGG,"Hyperion Global Growth Companies Fund (Managed Fund) (ASX:HYGG)",https://www.listcorp.com/asx/hygg/hyperion-global-growth-companies-fund-managed-fund,"	2202820000",3.95,0.00,0,Financials
ASX:VUK,"Virgin Money UK PLC (ASX:VUK)",https://www.listcorp.com/asx/vuk/virgin-money-uk-plc,"	2184700000",3.15,0.00,0,Financials
ASX:DEG,"De Grey Mining Limited (ASX:DEG)",https://www.listcorp.com/asx/deg/de-grey-mining,"	2178710000",1.395,0.00,0,Materials
ASX:SNZ,"Summerset Group Holdings Limited (ASX:SNZ)",https://www.listcorp.com/asx/snz/summerset-group-holdings-limited,"	2098450000",9,0.00,0,"Health Care"
ASX:PXA,"PEXA Group Limited (ASX:PXA)",https://www.listcorp.com/asx/pxa/pexa-group-limited,"	2097760000",11.83,0.00,0,"Real Estate"
ASX:IAF,"iShares Core Composite Bond ETF (ASX:IAF)",https://www.listcorp.com/asx/iaf/ishares-core-composite-bond-etf,"	2031030000",99.51,0.00,0,Financials
ASX:VDHG,"Vanguard Diversified High Growth Index ETF (ASX:VDHG)",https://www.listcorp.com/asx/vdhg/vanguard-diversified-high-growth-index-etf,"	2021250000",57.76,0.00,0,Financials
ASX:HBRD,"BetaShares Active Australian Hybrids Fund (managed fund) (ASX:HBRD)",https://www.listcorp.com/asx/hbrd/betashares-active-australian-hybrids-fund,"	2019320000",10.04,0.00,0,Financials
ASX:CQR,"Charter Hall Retail REIT (ASX:CQR)",https://www.listcorp.com/asx/cqr/charter-hall-retail-reit,"	1981990000",3.41,0.00,0,"Real Estate"
ASX:EVT,"EVT Limited (ASX:EVT)",https://www.listcorp.com/asx/evt/evt-limited,"	1940770000",12.03,0.00,0,"Communication Services"
ASX:CIP,"Centuria Industrial REIT (ASX:CIP)",https://www.listcorp.com/asx/cip/centuria-industrial-reit,"	1923840000",3.03,0.00,0,"Real Estate"
ASX:CEN,"Contact Energy Limited (ASX:CEN)",https://www.listcorp.com/asx/cen/contact-energy-limited,"	1912890000",7.59,0.00,0,Utilities
ASX:MP1,"Megaport Limited (ASX:MP1)",https://www.listcorp.com/asx/mp1/megaport-limited,"	1912140000",12.04,0.00,0,"Information Technology"
ASX:CHN,"Chalice Mining Limited (ASX:CHN)",https://www.listcorp.com/asx/chn/chalice-mining-limited,"	1911470000",4.93,0.00,0,Materials
ASX:NUF,"Nufarm Limited (ASX:NUF)",https://www.listcorp.com/asx/nuf/nufarm-limited,"	1879820000",4.94,0.00,0,Materials
ASX:PNI,"Pinnacle Investment Management Group Limited (ASX:PNI)",https://www.listcorp.com/asx/pni/pinnacle-investment-management-group-limited,"	1868540000",9.3,0.00,0,Financials
ASX:MVW,"Vaneck Vectors Australian Equal Weight ETF (ASX:MVW)",https://www.listcorp.com/asx/mvw/vaneck-vectors-australian-equal-weight-etf,"	1863770000",34.19,0.00,0,Financials
ASX:WLE,"WAM Leaders Limited (ASX:WLE)",https://www.listcorp.com/asx/wle/wam-leaders-limited,"	1829420000",1.455,0.00,0,Financials
ASX:HMC,"HMC Capital Limited (ASX:HMC)",https://www.listcorp.com/asx/hmc/hmc-capital-limited,"	1823020000",5.23,0.00,0,"Real Estate"
ASX:WAM,"WAM Capital Limited (ASX:WAM)",https://www.listcorp.com/asx/wam/wam-capital-limited,"	1821500000",1.655,0.00,0,Financials
ASX:IVC,"InvoCare Limited (ASX:IVC)",https://www.listcorp.com/asx/ivc/invocare-limited,"	1803640000",12.52,0.00,0,"Consumer Discretionary"
ASX:GOZ,"Growthpoint Properties Australia (ASX:GOZ)",https://www.listcorp.com/asx/goz/growthpoint-properties,"	1794170000",2.38,0.00,0,"Real Estate"
ASX:IPH,"IPH Limited (ASX:IPH)",https://www.listcorp.com/asx/iph/iph-limited,"	1792510000",7.61,0.00,0,Industrials
ASX:LSF,"L1 Long Short Fund Limited (ASX:LSF)",https://www.listcorp.com/asx/lsf/l1-long-short-fund-limited,"	1775860000",2.88,0.00,0,Financials
ASX:PSI,"PSC Insurance Group Limited (ASX:PSI)",https://www.listcorp.com/asx/psi/psc-insurance-group-limited,"	1774860000",4.99,0.00,0,Financials
ASX:360,"Life360, Inc. (ASX:360)",https://www.listcorp.com/asx/360/life360-inc.,"	1770360000",8.83,0.00,0,"Information Technology"
ASX:MXT,"Metrics Master Income Trust (ASX:MXT)",https://www.listcorp.com/asx/mxt/metrics-master-income-trust,"	1764960000",2,0.00,0,Financials
ASX:GOR,"Gold Road Resources Limited (ASX:GOR)",https://www.listcorp.com/asx/gor/gold-road-resources,"	1763220000",1.635,0.00,0,Materials
ASX:GNC,"GrainCorp Limited (ASX:GNC)",https://www.listcorp.com/asx/gnc/graincorp-limited,"	1752070000",7.81,0.00,0,"Consumer Staples"
ASX:ABC,"Adbri Limited (ASX:ABC)",https://www.listcorp.com/asx/abc/adbri-limited,"	1750920000",2.68,0.00,0,Materials
ASX:KLS,"Kelsian Group Limited (ASX:KLS)",https://www.listcorp.com/asx/kls/kelsian-group-limited,"	1749920000",6.5,0.00,0,Industrials
ASX:BGL,"Bellevue Gold Limited (ASX:BGL)",https://www.listcorp.com/asx/bgl/bellevue-gold-limited,"	1725930000",1.525,0.00,0,Materials
ASX:LIC,"Lifestyle Communities Limited (ASX:LIC)",https://www.listcorp.com/asx/lic/lifestyle-communities-limited,"	1699900000",16.26,0.00,0,"Real Estate"
ASX:WPR,"Waypoint REIT (ASX:WPR)",https://www.listcorp.com/asx/wpr/waypoint-reit,"	1692980000",2.52,0.00,0,"Real Estate"
ASX:MFF,"MFF Capital Investments Limited (ASX:MFF)",https://www.listcorp.com/asx/mff/mff-capital-investments,"	1679140000",2.9,0.00,0,Financials
ASX:IFL,"Insignia Financial Ltd (ASX:IFL)",https://www.listcorp.com/asx/ifl/insignia-financial-ltd,"	1669750000",2.52,0.00,0,Financials
ASX:GUD,"GUD Holdings Limited (ASX:GUD)",https://www.listcorp.com/asx/gud/gud-holdings-limited,"	1656920000",11.76,0.00,0,"Consumer Discretionary"
ASX:VAF,"Vanguard Australian Fixed Interest Index ETF (ASX:VAF)",https://www.listcorp.com/asx/vaf/vanguard-australian-fixed-interest-index-etf,"	1655820000",44.62,0.00,0,Financials
ASX:MFG,"Magellan Financial Group Limited (ASX:MFG)",https://www.listcorp.com/asx/mfg/magellan-financial-group-limited,"	1654660000",9.12,0.00,0,Financials
ASX:INA,"Ingenia Communities Group (ASX:INA)",https://www.listcorp.com/asx/ina/ingenia-communities-group,"	1618110000",3.97,0.00,0,"Real Estate"
ASX:APM,"APM Human Services International Limited (ASX:APM)",https://www.listcorp.com/asx/apm/apm-human-services-international,"	1614240000",1.76,0.00,0,Industrials
ASX:CMM,"Capricorn Metals Ltd (ASX:CMM)",https://www.listcorp.com/asx/cmm/capricorn-metals-ltd,"	1586540000",4.22,0.00,0,Materials
ASX:NEU,"Neuren Pharmaceuticals Limited (ASX:NEU)",https://www.listcorp.com/asx/neu/neuren-pharmaceuticals-limited,"	1582070000",12.5,0.00,0,"Health Care"
ASX:SKC,"SkyCity Entertainment Group Limited (ASX:SKC)",https://www.listcorp.com/asx/skc/skycity-entertainment-group,"	1573620000",2.07,0.00,0,"Consumer Discretionary"
ASX:ASK,"Abacus Storage King (ASX:ASK)",https://www.listcorp.com/asx/ask/abacus-storage-king,"	1570350000",1.195,0.00,0,Unclassified
ASX:MAQ,"Macquarie Technology Group Limited (ASX:MAQ)",https://www.listcorp.com/asx/maq/macquarie-technology-group-limited,"	1562170000",64.17,0.00,0,"Information Technology"
ASX:SGR,"The Star Entertainment Group Limited (ASX:SGR)",https://www.listcorp.com/asx/sgr/star-entertainment-group,"	1529650000",0.945,0.00,0,"Consumer Discretionary"
ASX:JLG,"Johns Lyng Group Limited (ASX:JLG)",https://www.listcorp.com/asx/jlg/johns-lyng-group-limited,"	1528020000",5.53,0.00,0,Industrials
ASX:GMD,"Genesis Minerals Limited (ASX:GMD)",https://www.listcorp.com/asx/gmd/genesis-minerals-limited,"	1522930000",1.47,0.00,0,Materials
ASX:MAD,"Mader Group Limited (ASX:MAD)",https://www.listcorp.com/asx/mad/mader-group-limited,"	1500000000",7.5,0.00,0,Industrials
ASX:DDR,"Dicker Data Limited (ASX:DDR)",https://www.listcorp.com/asx/ddr/dicker-data-limited,"	1491760000",8.28,0.00,0,"Information Technology"
ASX:HLS,"Healius Limited (ASX:HLS)",https://www.listcorp.com/asx/hls/healius-limited,"	1486910000",2.61,0.00,0,"Health Care"
ASX:UMG,"United Malt Group Limited (ASX:UMG)",https://www.listcorp.com/asx/umg/united-malt-group-limited,"	1474950000",4.93,0.00,0,"Consumer Staples"
ASX:CDA,"Codan Limited (ASX:CDA)",https://www.listcorp.com/asx/cda/codan-limited,"	1414920000",7.81,0.00,0,"Information Technology"
ASX:MND,"Monadelphous Group Limited (ASX:MND)",https://www.listcorp.com/asx/mnd/monadelphous-group-limited,"	1385810000",14.36,0.00,0,Industrials
ASX:BKI,"BKI Investment Company Limited (ASX:BKI)",https://www.listcorp.com/asx/bki/bki-investment-company-limited,"	1377700000",1.74,0.00,0,Financials
ASX:CGC,"Costa Group Holdings Limited (ASX:CGC)",https://www.listcorp.com/asx/cgc/costa-group-holdings-limited,"	1375540000",2.96,0.00,0,"Consumer Staples"
ASX:CCP,"Credit Corp Group Limited (ASX:CCP)",https://www.listcorp.com/asx/ccp/credit-corp-group-limited,"	1368140000",20.1,0.00,0,Financials
ASX:EMR,"Emerald Resources NL (ASX:EMR)",https://www.listcorp.com/asx/emr/emerald-resources-nl,"	1358940000",2.28,0.00,0,Materials
ASX:DBI,"Dalrymple Bay Infrastructure Limited (ASX:DBI)",https://www.listcorp.com/asx/dbi/dalrymple-bay-infrastructure-limited,"	1343510000",2.71,0.00,0,Industrials
ASX:LNW,"Light & Wonder Inc (ASX:LNW)",https://www.listcorp.com/asx/lnw/light-and-wonder-inc,"	1343190000",117.75,0.00,0,"Consumer Discretionary"
ASX:RDX,"Redox Limited (ASX:RDX)",https://www.listcorp.com/asx/rdx/redox-limited,"	1338960000",2.55,0.00,0,Unclassified
ASX:MMS,"McMillan Shakespeare Limited (ASX:MMS)",https://www.listcorp.com/asx/mms/mcmillan-shakespeare-limited,"	1326000000",19.04,0.00,0,Industrials
ASX:IXJ,"iShares Global Healthcare ETF (ASX:IXJ)",https://www.listcorp.com/asx/ixj/ishares-global-healthcare-etf,"	1323280000",131.48,0.00,0,Financials
ASX:ING,"Inghams Group Limited (ASX:ING)",https://www.listcorp.com/asx/ing/inghams-group,"	1289730000",3.47,0.00,0,"Consumer Staples"
ASX:SYA,"Sayona Mining Limited (ASX:SYA)",https://www.listcorp.com/asx/sya/sayona-mining,"	1286660000",0.125,0.00,0,Materials
ASX:ARF,"Arena REIT (ASX:ARF)",https://www.listcorp.com/asx/arf/arena-reit,"	1284660000",3.65,0.00,0,"Real Estate"
ASX:CMW,"Cromwell Property Group (ASX:CMW)",https://www.listcorp.com/asx/cmw/cromwell-property-group,"	1283240000",0.49,0.00,0,"Real Estate"
ASX:KAR,"Karoon Energy Ltd (ASX:KAR)",https://www.listcorp.com/asx/kar/karoon-energy-ltd,"	1278690000",2.26,0.00,0,Energy
ASX:NAN,"Nanosonics Limited (ASX:NAN)",https://www.listcorp.com/asx/nan/nanosonics,"	1269900000",4.2,0.00,0,"Health Care"
ASX:IRE,"Iress Limited (ASX:IRE)",https://www.listcorp.com/asx/ire/iress-limited,"	1266430000",6.78,0.00,0,"Information Technology"
ASX:RMS,"Ramelius Resources Limited (ASX:RMS)",https://www.listcorp.com/asx/rms/ramelius-resources,"	1263910000",1.275,0.00,0,Materials
ASX:AUI,"Australian United Investment Company Limited (ASX:AUI)",https://www.listcorp.com/asx/aui/australian-united-investment-company-limited,"	1249360000",9.89,0.00,0,Financials
ASX:SDR,"SiteMinder Limited (ASX:SDR)",https://www.listcorp.com/asx/sdr/siteminder-limited,"	1237800000",4.5,0.00,0,"Information Technology"
ASX:LFS,"Latitude Financial Services Group Limited (ASX:LFS)",https://www.listcorp.com/asx/lfs/latitude-financial-services-group-limited,"	1232020000",1.185,0.00,0,Financials
ASX:NWH,"NRW Holdings Limited (ASX:NWH)",https://www.listcorp.com/asx/nwh/nrw-holdings-limited,"	1203840000",2.68,0.00,0,Industrials
ASX:LFG,"Liberty Financial Group Limited (ASX:LFG)",https://www.listcorp.com/asx/lfg/liberty-financial-group-limited,"	1196990000",3.94,0.00,0,Financials
ASX:AX1,"Accent Group Limited (ASX:AX1)",https://www.listcorp.com/asx/ax1/accent-group-limited,"	1193310000",2.16,0.00,0,"Consumer Discretionary"
ASX:HLI,"Helia Group Limited (ASX:HLI)",https://www.listcorp.com/asx/hli/helia-group-limited,"	1184820000",3.75,0.00,0,Financials
ASX:BOE,"Boss Energy Ltd (ASX:BOE)",https://www.listcorp.com/asx/boe/boss-energy-ltd,"	1171580000",3.32,0.00,0,Energy
ASX:HSN,"Hansen Technologies Limited (ASX:HSN)",https://www.listcorp.com/asx/hsn/hansen-technologies-limited,"	1167600000",5.75,0.00,0,"Information Technology"
ASX:CNI,"Centuria Capital Group (ASX:CNI)",https://www.listcorp.com/asx/cni/centuria-capital,"	1159300000",1.44,0.00,0,"Real Estate"
ASX:CKF,"Collins Foods Limited (ASX:CKF)",https://www.listcorp.com/asx/ckf/collins-foods-limited,"	1150230000",9.79,0.00,0,"Consumer Discretionary"
ASX:RRL,"Regis Resources Limited (ASX:RRL)",https://www.listcorp.com/asx/rrl/regis-resources-limited,"	1147730000",1.52,0.00,0,Materials
ASX:SIQ,"Smartgroup Corporation Ltd (ASX:SIQ)",https://www.listcorp.com/asx/siq/smartgroup-corporation-ltd,"	1146900000",8.58,0.00,0,Industrials
ASX:OCL,"Objective Corporation Limited (ASX:OCL)",https://www.listcorp.com/asx/ocl/objective-corporation-limited,"	1142130000",12,0.00,0,"Information Technology"
ASX:HGH,"Heartland Group Holdings Limited (ASX:HGH)",https://www.listcorp.com/asx/hgh/heartland-group-holdings-limited,"	1135450000",1.6,0.00,0,Financials
ASX:QPON,"BetaShares Australian Bank Senior Floating Rate Bond ETF (ASX:QPON)",https://www.listcorp.com/asx/qpon/betashares-australian-bank-senior-floating-rate-bond-etf,"	1125870000",25.98,0.00,0,Financials
ASX:LLL,"Leo Lithium Limited (ASX:LLL)",https://www.listcorp.com/asx/lll/leo-lithium-limited,"	1125450000",1.14,0.00,0,Materials
ASX:IHVV,"iShares S&P 500 (AUD Hedged) ETF (ASX:IHVV)",https://www.listcorp.com/asx/ihvv/ishares-s-and-p-500-aud-hedged-etf,"	1124350000",40.79,0.00,0,Financials
ASX:DTL,"Data#3 Limited (ASX:DTL)",https://www.listcorp.com/asx/dtl/data-3-limited,"	1094560000",7.08,0.00,0,"Information Technology"
ASX:AD8,"Audinate Group Limited (ASX:AD8)",https://www.listcorp.com/asx/ad8/audinate-group-limited,"	1078730000",13.88,0.00,0,"Information Technology"
ASX:DUI,"Diversified United Investment Limited (ASX:DUI)",https://www.listcorp.com/asx/dui/diversified-united-investment-limited,"	1061910000",4.89,0.00,0,Financials
ASX:CUV,"Clinuvel Pharmaceuticals Limited (ASX:CUV)",https://www.listcorp.com/asx/cuv/clinuvel-pharmaceuticals-limited,"	1052440000",21.3,0.00,0,"Health Care"
ASX:PWH,"PWR Holdings Limited (ASX:PWH)",https://www.listcorp.com/asx/pwh/pwr-holdings-limited,"	1035930000",10.32,0.00,0,"Consumer Discretionary"
ASX:ABG,"Abacus Group (ASX:ABG)",https://www.listcorp.com/asx/abg/abacus-group,"	1032170000",1.155,0.00,0,"Real Estate"
ASX:PNV,"Polynovo Limited (ASX:PNV)",https://www.listcorp.com/asx/pnv/polynovo-limited,"	1031900000",1.495,0.00,0,"Health Care"
ASX:CQE,"Charter Hall Social Infrastructure REIT (ASX:CQE)",https://www.listcorp.com/asx/cqe/charter-hall-social-infrastructure-reit,"	1027270000",2.78,0.00,0,"Real Estate"
ASX:MGH,"MAAS Group Holdings Limited (ASX:MGH)",https://www.listcorp.com/asx/mgh/maas-group-holdings-limited,"	1024730000",3.12,0.00,0,Industrials
ASX:JDO,"Judo Capital Holdings Limited (ASX:JDO)",https://www.listcorp.com/asx/jdo/judo-capital-holdings-limited,"	1022610000",0.925,0.00,0,Financials
ASX:VSL,"Vulcan Steel Limited (ASX:VSL)",https://www.listcorp.com/asx/vsl/vulcan-steel-limited,"	1017100000",7.74,0.00,0,Materials
ASX:ELD,"Elders Limited (ASX:ELD)",https://www.listcorp.com/asx/eld/elders-limited,"	1013970000",6.48,0.00,0,"Consumer Staples"
ASX:NCK,"Nick Scali Limited (ASX:NCK)",https://www.listcorp.com/asx/nck/nick-scali-limited,"	993060000",12.26,0.00,0,"Consumer Discretionary"
ASX:BGP,"Briscoe Group Limited (ASX:BGP)",https://www.listcorp.com/asx/bgp/briscoe-group-limited,"	980169000",4.4,0.00,0,"Consumer Discretionary"
ASX:STX,"Strike Energy Limited (ASX:STX)",https://www.listcorp.com/asx/stx/strike-energy,"	976230000",0.385,0.00,0,Energy
ASX:AZS,"Azure Minerals Limited (ASX:AZS)",https://www.listcorp.com/asx/azs/azure-minerals-limited,"	976215000",2.5,0.00,0,Materials
ASX:JIN,"Jumbo Interactive Limited (ASX:JIN)",https://www.listcorp.com/asx/jin/jumbo-interactive-limited,"	972409000",15.46,0.00,0,"Consumer Discretionary"
ASX:A4N,"Alpha HPA Limited (ASX:A4N)",https://www.listcorp.com/asx/a4n/alpha-hpa-limited,"	966905000",1.1,0.00,0,Materials
ASX:CTT,"Cettire Limited (ASX:CTT)",https://www.listcorp.com/asx/ctt/cettire-limited,"	964533000",2.53,0.00,0,"Consumer Discretionary"
ASX:BGA,"Bega Cheese Limited (ASX:BGA)",https://www.listcorp.com/asx/bga/bega-cheese-limited,"	964466000",3.17,0.00,0,"Consumer Staples"
ASX:SGF,"SG Fleet Group Limited (ASX:SGF)",https://www.listcorp.com/asx/sgf/sg-fleet-group,"	940459000",2.75,0.00,0,Industrials
ASX:VGB,"Vanguard Australian Government Bond Index ETF (ASX:VGB)",https://www.listcorp.com/asx/vgb/vanguard-australian-government-bond-index-etf,"	938833000",45.46,0.00,0,Financials
ASX:LRS,"Latin Resources Limited (ASX:LRS)",https://www.listcorp.com/asx/lrs/latin-resources-limited,"	919693000",0.35,0.00,0,Materials
ASX:NWS,"News Corporation (ASX:NWS)",https://www.listcorp.com/asx/nws/news-corp,"	913950000",32.9,0.00,0,"Communication Services"
ASX:IMD,"IMDEX Limited (ASX:IMD)",https://www.listcorp.com/asx/imd/imdex-limited,"	912958000",1.8,0.00,0,Materials
ASX:TUA,"Tuas Limited (ASX:TUA)",https://www.listcorp.com/asx/tua/tuas-limited,"	904347000",1.945,0.00,0,"Communication Services"
ASX:GEM,"G8 Education Limited (ASX:GEM)",https://www.listcorp.com/asx/gem/g8-education-limited,"	894504000",1.105,0.00,0,"Consumer Discretionary"
ASX:WBT,"Weebit Nano Limited (ASX:WBT)",https://www.listcorp.com/asx/wbt/weebit-nano-limited,"	894186000",4.77,0.00,0,"Information Technology"
ASX:PTM,"Platinum Asset Management Limited (ASX:PTM)",https://www.listcorp.com/asx/ptm/platinum-asset-management-limited,"	888819000",1.515,0.00,0,Financials
ASX:AAC,"Australian Agricultural Company Limited (ASX:AAC)",https://www.listcorp.com/asx/aac/australian-agricultural-company-limited,"	886067000",1.47,0.00,0,"Consumer Staples"
ASX:ERA,"Energy Resources of Australia Ltd (ASX:ERA)",https://www.listcorp.com/asx/era/energy-resources-of-australia,"	885932000",0.04,0.00,0,Energy
ASX:IEM,"iShares MSCI Emerging Markets ETF (ASX:IEM)",https://www.listcorp.com/asx/iem/ishares-msci-emerging-markets-etf,"	876797000",60.59,0.00,0,Financials
ASX:WAF,"West African Resources Limited (ASX:WAF)",https://www.listcorp.com/asx/waf/west-african-resources,"	872196000",0.85,0.00,0,Materials
ASX:ADT,"Adriatic Metals Plc (ASX:ADT)",https://www.listcorp.com/asx/adt/adriatic-metals-plc,"	869723000",3.66,0.00,0,Materials
ASX:DXI,"Dexus Industria REIT (ASX:DXI)",https://www.listcorp.com/asx/dxi/dexus-industria-reit,"	866147000",2.73,0.00,0,"Real Estate"
ASX:CXO,"Core Lithium Ltd (ASX:CXO)",https://www.listcorp.com/asx/cxo/core-lithium-ltd,"	864492000",0.41,0.00,0,Materials
ASX:VIF,"Vanguard International Fixed Interest Index (Hedged) ETF (ASX:VIF)",https://www.listcorp.com/asx/vif/vanguard-international-fixed-interest-index-hedged-etf,"	851850000",37.82,0.00,0,Financials
ASX:SUBD,"VanEck Australian Subordinated Debt ETF (ASX:SUBD)",https://www.listcorp.com/asx/subd/vaneck-australian-subordinated-debt-etf,"	848678000",24.98,0.00,0,Financials
ASX:HCW,"HealthCo Healthcare and Wellness REIT (ASX:HCW)",https://www.listcorp.com/asx/hcw/healthco-healthcare-and-wellness-reit,"	830150000",1.475,0.00,0,"Real Estate"
ASX:MAF,"MA Financial Group Limited (ASX:MAF)",https://www.listcorp.com/asx/maf/ma-financial-group-limited,"	820175000",4.6,0.00,0,Financials
ASX:ABB,"Aussie Broadband Limited (ASX:ABB)",https://www.listcorp.com/asx/abb/aussie-broadband-limited,"	817628000",3.44,0.00,0,"Communication Services"
ASX:TPW,"Temple & Webster Group Limited (ASX:TPW)",https://www.listcorp.com/asx/tpw/temple-and-webster-group-limited,"	816386000",6.64,0.00,0,"Consumer Discretionary"
ASX:SIG,"Sigma Healthcare Limited (ASX:SIG)",https://www.listcorp.com/asx/sig/sigma-healthcare-limited,"	815643000",0.77,0.00,0,"Health Care"
ASX:SLR,"Silver Lake Resources Limited (ASX:SLR)",https://www.listcorp.com/asx/slr/silver-lake-resources-limited,"	813526000",0.875,0.00,0,Materials
ASX:OML,"oOh!media Limited (ASX:OML)",https://www.listcorp.com/asx/oml/ooh-media-limited,"	805478000",1.495,0.00,0,"Communication Services"
ASX:SFY,"SPDR S&P/ASX 50 Fund (ASX:SFY)",https://www.listcorp.com/asx/sfy/spdr-s-and-p-asx-50-fund,"	801656000",63.16,0.00,0,Financials
ASX:PL8,"Plato Income Maximiser Limited (ASX:PL8)",https://www.listcorp.com/asx/pl8/plato-income-maximiser-limited,"	796147000",1.26,0.00,0,Financials
ASX:VBND,"Vanguard Global Aggregate Bond Index (Hedged) ETF (ASX:VBND)",https://www.listcorp.com/asx/vbnd/vanguard-global-aggregate-bond-index-hedged-etf,"	793971000",40.51,0.00,0,Financials
ASX:IFRA,"VanEck FTSE Global Infrastructure (Hedged) ETF (ASX:IFRA)",https://www.listcorp.com/asx/ifra/vaneck-ftse-global-infrastructure-hedged-etf,"	789205000",19.23,0.00,0,Financials
ASX:EHE,"Estia Health Limited (ASX:EHE)",https://www.listcorp.com/asx/ehe/estia-health-limited,"	787370000",3.03,0.00,0,"Health Care"
ASX:SLX,"Silex Systems Limited (ASX:SLX)",https://www.listcorp.com/asx/slx/silex-systems-limited,"	782919000",3.32,0.00,0,Industrials
ASX:RFF,"Rural Funds Group (ASX:RFF)",https://www.listcorp.com/asx/rff/rural-funds-group,"	780000000",2.02,0.00,0,"Real Estate"
ASX:VSO,"Vanguard MSCI Australian Small Companies Index ETF (ASX:VSO)",https://www.listcorp.com/asx/vso/vanguard-msci-australian-small-companies-index-etf,"	773336000",61.69,0.00,0,Financials
ASX:IEU,"iShares Europe ETF (ASX:IEU)",https://www.listcorp.com/asx/ieu/ishares-europe-etf,"	772983000",75.9,0.00,0,Financials
ASX:PGF,"PM Capital Global Opportunities Fund (ASX:PGF)",https://www.listcorp.com/asx/pgf/pm-capital-global-opportunities-fund,"	772090000",1.89,0.00,0,Financials
ASX:CXL,"Calix Limited (ASX:CXL)",https://www.listcorp.com/asx/cxl/calix-limited,"	768427000",4.24,0.00,0,Materials
ASX:CIN,"Carlton Investments Limited (ASX:CIN)",https://www.listcorp.com/asx/cin/carlton-investments-limited,"	767766000",29,0.00,0,Financials
ASX:COF,"Centuria Office Reit (ASX:COF)",https://www.listcorp.com/asx/cof/centuria-office-reit,"	764591000",1.28,0.00,0,"Real Estate"
ASX:XARO,"Activex Ardea Real Outcome Bond Fund (Managed Fund) (ASX:XARO)",https://www.listcorp.com/asx/xaro/activex-ardea-real-outcome-bond-fund-managed-fund,"	762836000",24.59,0.00,0,Financials
ASX:RSG,"Resolute Mining Limited (ASX:RSG)",https://www.listcorp.com/asx/rsg/resolute-mining,"	755797000",0.355,0.00,0,Materials
ASX:FPR,"FleetPartners Group Limited (ASX:FPR)",https://www.listcorp.com/asx/fpr/fleetpartners-group-limited,"	755494000",2.86,0.00,0,Financials
ASX:HACK,"BetaShares Global Cybersecurity ETF (ASX:HACK)",https://www.listcorp.com/asx/hack/betashares-global-cybersecurity-etf,"	752261000",9.59,0.00,0,Financials
ASX:DJW,"Djerriwarrh Investments Limited (ASX:DJW)",https://www.listcorp.com/asx/djw/djerriwarrh-investments-limited,"	744847000",2.84,0.00,0,Financials
ASX:RED,"Red 5 Limited (ASX:RED)",https://www.listcorp.com/asx/red/red-5-limited,"	743789000",0.215,0.00,0,Materials
ASX:QAL,"Qualitas Limited (ASX:QAL)",https://www.listcorp.com/asx/qal/qualitas-limited,"	737080000",2.49,0.00,0,"Real Estate"
ASX:VGE,"Vanguard FTSE Emerging Markets Shares ETF (ASX:VGE)",https://www.listcorp.com/asx/vge/vanguard-ftse-emerging-markets-shares-etf,"	731564000",69.5,0.00,0,Financials
ASX:IDX,"Integral Diagnostics Limited (ASX:IDX)",https://www.listcorp.com/asx/idx/integral-diagnostics-limited,"	727052000",3.12,0.00,0,"Health Care"
ASX:PRN,"Perenti Limited (ASX:PRN)",https://www.listcorp.com/asx/prn/perenti-limited,"	723103000",1.06,0.00,0,Materials
ASX:REG,"Regis Healthcare Limited (ASX:REG)",https://www.listcorp.com/asx/reg/regis-healthcare-limited,"	722180000",2.4,0.00,0,"Health Care"
ASX:IAA,"iShares Asia 50 ETF (ASX:IAA)",https://www.listcorp.com/asx/iaa/ishares-asia-50-etf,"	719302000",89.9,0.00,0,Financials
ASX:WTN,"Winton Land Limited (ASX:WTN)",https://www.listcorp.com/asx/wtn/winton-land-limited,"	717805000",2.42,0.00,0,"Real Estate"
ASX:NNUK,"Nanuk New World Fund (ASX:NNUK)",https://www.listcorp.com/asx/nnuk/nanuk-new-world-fund,"	715443000",1.72,0.00,0,Financials
ASX:VESG,"Vanguard Ethically Conscious International Shares Index ETF (ASX:VESG)",https://www.listcorp.com/asx/vesg/vanguard-ethically-conscious-international-shares-index-etf,"	715318000",75.72,0.00,0,Financials
ASX:THL,"Tourism Holdings Rentals Limited (ASX:THL)",https://www.listcorp.com/asx/thl/tourism-holdings-rentals-limited,"	711856000",3.32,0.00,0,Industrials
ASX:QHAL,"VanEck MSCI International Quality (Hedged) ETF (ASX:QHAL)",https://www.listcorp.com/asx/qhal/vaneck-msci-international-quality-hedged-etf,"	705615000",38.66,0.00,0,Financials
ASX:WGB,"WAM Global Limited (ASX:WGB)",https://www.listcorp.com/asx/wgb/wam-global-limited,"	697762000",1.975,0.00,0,Financials
ASX:LNK,"Link Administration Holdings Limited (ASX:LNK)",https://www.listcorp.com/asx/lnk/link-administration-holdings,"	697663000",1.36,0.00,0,Industrials
ASX:WGX,"Westgold Resources Limited (ASX:WGX)",https://www.listcorp.com/asx/wgx/westgold-resources-limited,"	696225000",1.47,0.00,0,Materials
ASX:VDGR,"Vanguard Diversified Growth Index ETF (ASX:VDGR)",https://www.listcorp.com/asx/vdgr/vanguard-diversified-growth-index-etf,"	695631000",54.16,0.00,0,Financials
ASX:ASB,"Austal Limited (ASX:ASB)",https://www.listcorp.com/asx/asb/austal-limited,"	692264000",1.91,0.00,0,Industrials
ASX:BILL,"iShares Core Cash ETF (ASX:BILL)",https://www.listcorp.com/asx/bill/ishares-core-cash-etf,"	685462000",100.65,0.00,0,Financials
ASX:FCL,"Fineos Corporation Holdings Plc (ASX:FCL)",https://www.listcorp.com/asx/fcl/fineos-corporation-holdings-plc,"	685442000",2.04,0.00,0,"Information Technology"
ASX:DYL,"Deep Yellow Limited (ASX:DYL)",https://www.listcorp.com/asx/dyl/deep-yellow-limited,"	682053000",0.9,0.00,0,Energy
ASX:EQT,"EQT Holdings Limited (ASX:EQT)",https://www.listcorp.com/asx/eqt/eqt-holdings-limited,"	678563000",25.6,0.00,0,Financials
ASX:MICH,"Magellan Infrastructure Fund (Currency Hedged)(Managed Fund) (ASX:MICH)",https://www.listcorp.com/asx/mich/magellan-infrastructure-fund-currency-hedged-managed-fund,"	674393000",2.61,0.00,0,Financials
ASX:RIC,"Ridley Corporation Limited (ASX:RIC)",https://www.listcorp.com/asx/ric/ridley-corporation-limited,"	672724000",2.13,0.00,0,"Consumer Staples"
ASX:KKC,"KKR Credit Income Fund (ASX:KKC)",https://www.listcorp.com/asx/kkc/kkr-credit-income-fund,"	664420000",2.06,0.00,0,Financials
ASX:OBL,"Omni Bridgeway Limited (ASX:OBL)",https://www.listcorp.com/asx/obl/omni-bridgeway-limited,"	652134000",2.34,0.00,0,Financials
ASX:URW,"Unibail-Rodamco-Westfield (ASX:URW)",https://www.listcorp.com/asx/urw/unibail-rodamco-westfield,"	641436000",3.97,0.00,0,"Real Estate"
ASX:VACF,"Vanguard Australian Corp Fixed Interest Index ETF (ASX:VACF)",https://www.listcorp.com/asx/vacf/vanguard-australian-corp-fixed-interest-index-etf,"	635860000",49.36,0.00,0,Financials
ASX:MOAT,"VanEck Morningstar Wide Moat ETF (ASX:MOAT)",https://www.listcorp.com/asx/moat/vaneck-morningstar-wide-moat-etf,"	635431000",113.73,0.00,0,Financials
ASX:RPL,"Regal Partners Limited (ASX:RPL)",https://www.listcorp.com/asx/rpl/regal-partners-limited,"	634125000",2.49,0.00,0,Financials
ASX:FLOT,"VanEck Australian Floating Rate ETF (ASX:FLOT)",https://www.listcorp.com/asx/flot/vaneck-australian-floating-rate-etf,"	626816000",24.9,0.00,0,Financials
ASX:VDBA,"Vanguard Diversified Balanced Index ETF (ASX:VDBA)",https://www.listcorp.com/asx/vdba/vanguard-diversified-balanced-index-etf,"	624337000",50.74,0.00,0,Financials
ASX:IFM,"Infomedia Ltd (ASX:IFM)",https://www.listcorp.com/asx/ifm/infomedia,"	616291000",1.64,0.00,0,"Information Technology"
ASX:SNL,"Supply Network Limited (ASX:SNL)",https://www.listcorp.com/asx/snl/supply-network,"	608371000",14.64,0.00,0,"Consumer Discretionary"
ASX:MVA,"Vaneck Australian Property ETF (ASX:MVA)",https://www.listcorp.com/asx/mva/vaneck-australian-property-etf,"	607195000",20.41,0.00,0,Financials
ASX:NBI,"NB Global Corporate Income Trust (ASX:NBI)",https://www.listcorp.com/asx/nbi/nb-global-corporate-income-trust,"	606264000",1.405,0.00,0,Unclassified
ASX:ILB,"iShares Government Inflation ETF (ASX:ILB)",https://www.listcorp.com/asx/ilb/ishares-government-inflation-etf,"	604926000",123.07,0.00,0,Financials
ASX:TYR,"Tyro Payments Limited (ASX:TYR)",https://www.listcorp.com/asx/tyr/tyro-payments-limited,"	601591000",1.155,0.00,0,Financials
ASX:ACDC,"Global X Battery Tech & Lithium ETF (ASX:ACDC)",https://www.listcorp.com/asx/acdc/global-x-battery-tech-and-lithium-etf,"	597912000",96.12,0.00,0,Financials
ASX:WHF,"Whitefield Industrials Limited (ASX:WHF)",https://www.listcorp.com/asx/whf/whitefield-industrials-limited,"	594685000",5.1,0.00,0,Financials
ASX:HPI,"Hotel Property Investments Limited (ASX:HPI)",https://www.listcorp.com/asx/hpi/hotel-property-investments-limited,"	592606000",3.05,0.00,0,"Real Estate"
ASX:QRI,"Qualitas Real Estate Income Fund (ASX:QRI)",https://www.listcorp.com/asx/qri/qualitas-real-estate-income-fund,"	585791000",1.56,0.00,0,Financials
ASX:ACL,"Australian Clinical Labs Limited (ASX:ACL)",https://www.listcorp.com/asx/acl/australian-clinical-labs-limited,"	577245000",2.86,0.00,0,"Health Care"
ASX:BRN,"Brainchip Holdings Ltd (ASX:BRN)",https://www.listcorp.com/asx/brn/brainchip-holdings,"	576894000",0.325,0.00,0,"Information Technology"
ASX:RF1,"Regal Investment Fund (ASX:RF1)",https://www.listcorp.com/asx/rf1/regal-investment-fund,"	576658000",2.83,0.00,0,Financials
ASX:GRR,"Grange Resources Limited (ASX:GRR)",https://www.listcorp.com/asx/grr/grange-resources,"	572883000",0.495,0.00,0,Materials
ASX:PPC,"Peet Limited (ASX:PPC)",https://www.listcorp.com/asx/ppc/peet-limited,"	572649000",1.215,0.00,0,"Real Estate"
ASX:VVLU,"Vanguard Global Value Equity Active ETF (Managed Fund) (ASX:VVLU)",https://www.listcorp.com/asx/vvlu/vanguard-global-value-equity-active-etf-managed-fund,"	572211000",64.73,0.00,0,Financials
ASX:PPM,"Pepper Money Limited (ASX:PPM)",https://www.listcorp.com/asx/ppm/pepper-money-limited,"	571696000",1.3,0.00,0,Financials
ASX:HTA,"Hutchison Telecommunications (Australia) Limited (ASX:HTA)",https://www.listcorp.com/asx/hta/hutchison-telecommunications-australia-limited,"	570045000",0.042,0.00,0,"Communication Services"
ASX:INR,"Ioneer Ltd (ASX:INR)",https://www.listcorp.com/asx/inr/ioneer-ltd,"	569541000",0.27,0.00,0,Materials
ASX:TIE,"Tietto Minerals Limited (ASX:TIE)",https://www.listcorp.com/asx/tie/tietto-minerals-limited,"	560077000",0.515,0.00,0,Materials
ASX:VUL,"Vulcan Energy Resources Limited (ASX:VUL)",https://www.listcorp.com/asx/vul/vulcan-energy-resources-limited,"	555553000",3.32,0.00,0,Materials
ASX:SSM,"Service Stream Limited (ASX:SSM)",https://www.listcorp.com/asx/ssm/service-stream-limited,"	554358000",0.9,0.00,0,Industrials
ASX:MIR,"Mirrabooka Investments Limited (ASX:MIR)",https://www.listcorp.com/asx/mir/mirrabooka-investments-limited,"	553563000",2.87,0.00,0,Financials
ASX:KMD,"KMD Brands Limited (ASX:KMD)",https://www.listcorp.com/asx/kmd/kmd-brands-limited,"	551294000",0.775,0.00,0,"Consumer Discretionary"
ASX:PAC,"Pacific Current Group Limited (ASX:PAC)",https://www.listcorp.com/asx/pac/pacific-current-group,"	546166000",10.59,0.00,0,Financials
ASX:OPH,"Ophir High Conviction Fund (ASX:OPH)",https://www.listcorp.com/asx/oph/ophir-high-conviction-fund,"	540915000",2.43,0.00,0,Financials
ASX:CRED,"BetaShares Australian Investment Grade Corporate Bond ETF (ASX:CRED)",https://www.listcorp.com/asx/cred/betashares-australian-investment-grade-corporate-bond-etf,"	540822000",21.96,0.00,0,Financials
ASX:CBO,"Cobram Estate Olives Limited (ASX:CBO)",https://www.listcorp.com/asx/cbo/cobram-estate-olives-limited,"	540505000",1.3,0.00,0,"Consumer Staples"
ASX:RBD,"Restaurant Brands New Zealand Limited (ASX:RBD)",https://www.listcorp.com/asx/rbd/restaurant-brands-new-zealand-limited,"	535214000",4.29,0.00,0,"Consumer Discretionary"
ASX:MOT,"Metrics Income Opportunities Trust (ASX:MOT)",https://www.listcorp.com/asx/mot/metrics-income-opportunities-trust,"	534820000",2.01,0.00,0,Financials
ASX:DVP,"Develop Global Limited (ASX:DVP)",https://www.listcorp.com/asx/dvp/develop-global-limited,"	533486000",2.71,0.00,0,Materials
ASX:HM1,"Hearts and Minds Investments Limited (ASX:HM1)",https://www.listcorp.com/asx/hm1/hearts-and-minds-investments-limited,"	533110000",2.33,0.00,0,Financials
ASX:VG1,"VGI Partners Global Investments Limited (ASX:VG1)",https://www.listcorp.com/asx/vg1/vgi-partners-global-investments-limited,"	533000000",1.59,0.00,0,Financials
ASX:NVX,"Novonix Limited (ASX:NVX)",https://www.listcorp.com/asx/nvx/novonix-limited,"	531127000",1.09,0.00,0,"Information Technology"
ASX:KGN,"Kogan.com Limited (ASX:KGN)",https://www.listcorp.com/asx/kgn/kogan.com-limited,"	530618000",5.06,0.00,0,"Consumer Discretionary"
ASX:MYR,"Myer Holdings Limited (ASX:MYR)",https://www.listcorp.com/asx/myr/myer-holdings-limited,"	529725000",0.645,0.00,0,"Consumer Discretionary"
ASX:AQZ,"Alliance Aviation Services Limited (ASX:AQZ)",https://www.listcorp.com/asx/aqz/alliance-aviation-services-limited,"	519173000",3.23,0.00,0,Industrials
ASX:USTB,"Global X US Treasury Bond ETF (Currency Hedged) (ASX:USTB)",https://www.listcorp.com/asx/ustb/global-x-us-treasury-bond-etf-currency-hedged,"	519166000",9.18,0.00,0,Financials
ASX:MRM,"MMA Offshore Limited (ASX:MRM)",https://www.listcorp.com/asx/mrm/mma-offshore-limited,"	518536000",1.385,0.00,0,Energy
ASX:ARU,"Arafura Rare Earths Limited (ASX:ARU)",https://www.listcorp.com/asx/aru/arafura-rare-earths-limited,"	517774000",0.245,0.00,0,Materials
ASX:OCA,"Oceania Healthcare Limited (ASX:OCA)",https://www.listcorp.com/asx/oca/oceania-healthcare-limited,"	516359000",0.71,0.00,0,"Health Care"
ASX:MGX,"Mount Gibson Iron Limited (ASX:MGX)",https://www.listcorp.com/asx/mgx/mount-gibson-iron-limited,"	516128000",0.425,0.00,0,Materials
ASX:PFP,"Propel Funeral Partners Limited (ASX:PFP)",https://www.listcorp.com/asx/pfp/propel-funeral-partners,"	514346000",4.35,0.00,0,"Consumer Discretionary"
ASX:ASG,"Autosports Group Limited (ASX:ASG)",https://www.listcorp.com/asx/asg/autosports-group-limited,"	512550000",2.55,0.00,0,"Consumer Discretionary"
ASX:SHV,"Select Harvests Limited (ASX:SHV)",https://www.listcorp.com/asx/shv/select-harvests-limited,"	512078000",4.23,0.00,0,"Consumer Staples"
ASX:ILC,"iShares S&P/ASX 20 ETF (ASX:ILC)",https://www.listcorp.com/asx/ilc/ishares-s-and-p-asx-20-etf,"	509971000",27.34,0.00,0,Financials
ASX:GWA,"GWA Group Limited (ASX:GWA)",https://www.listcorp.com/asx/gwa/gwa-group,"	499912000",1.885,0.00,0,Industrials
ASX:PBH,"Pointsbet Holdings Limited (ASX:PBH)",https://www.listcorp.com/asx/pbh/pointsbet-holdings-limited,"	497018000",1.595,0.00,0,"Consumer Discretionary"
ASX:BNDS,"BetaShares Western Asset Australian Bond Fund (managed fund) (ASX:BNDS)",https://www.listcorp.com/asx/bnds/betashares-western-asset-australian-bond-fund-managed-fund,"	495562000",23.31,0.00,0,Financials
ASX:GCI,"Gryphon Capital Income Trust (ASX:GCI)",https://www.listcorp.com/asx/gci/gryphon-capital-income-trust,"	482676000",1.985,0.00,0,Financials
ASX:IJP,"iShares MSCI Japan ETF (ASX:IJP)",https://www.listcorp.com/asx/ijp/ishares-msci-japan-etf,"	481686000",92.84,0.00,0,Financials
ASX:SWM,"Seven West Media Limited (ASX:SWM)",https://www.listcorp.com/asx/swm/seven-west-media-limited,"	481607000",0.31,0.00,0,"Communication Services"
ASX:NXL,"Nuix Limited (ASX:NXL)",https://www.listcorp.com/asx/nxl/nuix-limited,"	476800000",1.485,0.00,0,"Information Technology"
ASX:HLO,"Helloworld Travel Limited (ASX:HLO)",https://www.listcorp.com/asx/hlo/helloworld-travel-limited,"	476028000",3,0.00,0,"Consumer Discretionary"
ASX:AGVT,"BetaShares Australian Government Bond ETF (ASX:AGVT)",https://www.listcorp.com/asx/agvt/betashares-australian-government-bond-etf,"	475341000",41.2,0.00,0,Financials
ASX:SLF,"SPDR S&P/ASX 200 Listed Property Fund (ASX:SLF)",https://www.listcorp.com/asx/slf/spdr-s-and-p-asx-200-listed-property-fund,"	475100000",10.81,0.00,0,Financials
ASX:PGG,"Partners Group Global Income Fund (ASX:PGG)",https://www.listcorp.com/asx/pgg/partners-group-global-income-fund,"	473226000",1.72,0.00,0,Financials
ASX:IMU,"Imugene Limited (ASX:IMU)",https://www.listcorp.com/asx/imu/imugene,"	471564000",0.069,0.00,0,"Health Care"
ASX:ASIA,"BetaShares Asia Technology Tigers ETF (ASX:ASIA)",https://www.listcorp.com/asx/asia/betashares-asia-technology-tigers-etf,"	469613000",7.49,0.00,0,Financials
ASX:FGG,"Future Generation Global Limited (ASX:FGG)",https://www.listcorp.com/asx/fgg/future-generation-global-limited,"	469608000",1.185,0.00,0,Financials
ASX:PIC,"Perpetual Equity Investment Company Limited (ASX:PIC)",https://www.listcorp.com/asx/pic/perpetual-equity-investment-company-limited,"	469202000",1.24,0.00,0,Financials
ASX:AEF,"Australian Ethical Investment Ltd (ASX:AEF)",https://www.listcorp.com/asx/aef/australian-ethical-investment,"	466918000",4.14,0.00,0,Financials
ASX:IJR,"iShares S&P Small-Cap ETF (ASX:IJR)",https://www.listcorp.com/asx/ijr/ishares-s-and-p-small-cap-etf,"	463193000",153.41,0.00,0,Financials
ASX:MVF,"Monash IVF Group Limited (ASX:MVF)",https://www.listcorp.com/asx/mvf/monash-ivf-group-limited,"	459769000",1.18,0.00,0,"Health Care"
ASX:FGX,"Future Generation Australia Limited (ASX:FGX)",https://www.listcorp.com/asx/fgx/future-generation-australia-limited,"	458853000",1.13,0.00,0,Financials
ASX:MHHT,"Magellan High Conviction Trust (Managed Fund) (ASX:MHHT)",https://www.listcorp.com/asx/mhht/magellan-high-conviction-trust-managed-fund,"	453535000",1.58,0.00,0,Financials
ASX:OFX,"OFX Group Limited (ASX:OFX)",https://www.listcorp.com/asx/ofx/ofx-group-limited,"	448941000",1.83,0.00,0,Financials
ASX:PMT,"Patriot Battery Metals Inc (ASX:PMT)",https://www.listcorp.com/asx/pmt/patriot-battery-metals-inc,"	445901000",1.28,0.00,0,Materials
ASX:PWR,"Peter Warren Automotive Holdings Limited (ASX:PWR)",https://www.listcorp.com/asx/pwr/peter-warren-automotive-holdings-limited,"	445274000",2.59,0.00,0,"Consumer Discretionary"
ASX:BLY,"Boart Longyear Group Ltd (ASX:BLY)",https://www.listcorp.com/asx/bly/boart-longyear-group-ltd,"	442401000",1.495,0.00,0,Materials
ASX:AFG,"Australian Finance Group Ltd (ASX:AFG)",https://www.listcorp.com/asx/afg/australian-finance-group-ltd,"	435116000",1.61,0.00,0,Financials
ASX:TLG,"Talga Group Ltd (ASX:TLG)",https://www.listcorp.com/asx/tlg/talga-group,"	434709000",1.205,0.00,0,Materials
ASX:DLI,"Delta Lithium Limited (ASX:DLI)",https://www.listcorp.com/asx/dli/delta-lithium-limited,"	431334000",0.81,0.00,0,Materials
ASX:CWP,"Cedar Woods Properties Limited (ASX:CWP)",https://www.listcorp.com/asx/cwp/cedar-woods-properties-limited,"	428314000",5.21,0.00,0,"Real Estate"
ASX:SGLLV,"Ricegrowers Limited (ASX:SGLLV)",https://www.listcorp.com/asx/sgllv/ricegrowers-limited,"	428000000",6.65,0.00,0,"Consumer Staples"
ASX:SKO,"Serko Limited (ASX:SKO)",https://www.listcorp.com/asx/sko/serko-limited,"	426273000",3.5,0.00,0,"Information Technology"
ASX:GDX,"Vaneck Vectors Gold Miners ETF (ASX:GDX)",https://www.listcorp.com/asx/gdx/vaneck-vectors-gold-miners-etf,"	426143000",44.42,0.00,0,Financials
ASX:BLX,"Beacon Lighting Group Limited (ASX:BLX)",https://www.listcorp.com/asx/blx/beacon-lighting-group-limited,"	424487000",1.89,0.00,0,"Consumer Discretionary"
ASX:PDI,"Predictive Discovery Limited (ASX:PDI)",https://www.listcorp.com/asx/pdi/predictive-discovery-limited,"	423990000",0.205,0.00,0,Materials
ASX:XALG,"Alphinity  Global  Equity  Fund  (Managed Fund) (ASX:XALG)",https://www.listcorp.com/asx/xalg/alphinity-global-equity-fund-managed-fund,"	423575000",9.45,0.00,0,Financials
ASX:SSR,"SSR Mining Inc (ASX:SSR)",https://www.listcorp.com/asx/ssr/ssr-mining-inc,"	423436000",23.08,0.00,0,Materials
ASX:PE1,"Pengana Private Equity Trust (ASX:PE1)",https://www.listcorp.com/asx/pe1/pengana-private-equity-trust,"	419525000",1.5,0.00,0,Financials
ASX:IGB,"iShares Treasury ETF (ASX:IGB)",https://www.listcorp.com/asx/igb/ishares-treasury-etf,"	418713000",96.3,0.00,0,Financials
ASX:DJRE,"SPDR Dow Jones Global Real Estate ESG Fund (ASX:DJRE)",https://www.listcorp.com/asx/djre/spdr-dow-jones-global-real-estate-esg-fund,"	417151000",19.58,0.00,0,Financials
ASX:PCI,"Perpetual Credit Income Trust (ASX:PCI)",https://www.listcorp.com/asx/pci/perpetual-credit-income-trust,"	415002000",1.035,0.00,0,Unclassified
ASX:IVE,"iShares MSCI EAFE ETF (ASX:IVE)",https://www.listcorp.com/asx/ive/ishares-msci-eafe-etf,"	414113000",108.29,0.00,0,Financials
ASX:LYL,"Lycopodium Limited (ASX:LYL)",https://www.listcorp.com/asx/lyl/lycopodium-limited,"	409324000",10.3,0.00,0,Industrials
ASX:GTK,"Gentrack Group Limited (ASX:GTK)",https://www.listcorp.com/asx/gtk/gentrack-group-limited,"	407938000",4.01,0.00,0,"Information Technology"
ASX:VGL,"Vista Group International Limited (ASX:VGL)",https://www.listcorp.com/asx/vgl/vista-group-international-limited,"	406338000",1.72,0.00,0,"Information Technology"
ASX:ALK,"Alkane Resources Limited (ASX:ALK)",https://www.listcorp.com/asx/alk/alkane-resources-limited,"	406062000",0.675,0.00,0,Materials
ASX:C79,"Chrysos Corporation Limited (ASX:C79)",https://www.listcorp.com/asx/c79/chrysos-corporation-limited,"	402927000",6.27,0.00,0,Industrials
ASX:GL1,"Global Lithium Resources Limited (ASX:GL1)",https://www.listcorp.com/asx/gl1/global-lithium-resources-limited,"	402707000",1.55,0.00,0,Materials
ASX:OMH,"OM Holdings Limited (ASX:OMH)",https://www.listcorp.com/asx/omh/om-holdings-limited,"	402550000",0.545,0.00,0,Materials
ASX:JMS,"Jupiter Mines Limited (ASX:JMS)",https://www.listcorp.com/asx/jms/jupiter-mines-limited,"	401593000",0.205,0.00,0,Materials
ASX:MSB,"Mesoblast Limited (ASX:MSB)",https://www.listcorp.com/asx/msb/mesoblast-limited,"	394889000",0.485,0.00,0,"Health Care"
ASX:YMAX,"BetaShares Australian Top 20 Equity Yield Maximiser Fund (managed fund) (ASX:YMAX)",https://www.listcorp.com/asx/ymax/betashares-australian-top-20-equity-yield-maximiser-fund-managed-fund,"	394716000",7.36,0.00,0,Financials
ASX:MYX,"Mayne Pharma Group Limited (ASX:MYX)",https://www.listcorp.com/asx/myx/mayne-pharma-group-limited,"	392192000",4.61,0.00,0,"Health Care"
ASX:SYI,"SPDR MSCI Australia Select High Dividend Yield Fund (ASX:SYI)",https://www.listcorp.com/asx/syi/spdr-msci-australia-select-high-dividend-yield-fund,"	389371000",26.52,0.00,0,Financials
ASX:RDY,"ReadyTech Holdings Limited (ASX:RDY)",https://www.listcorp.com/asx/rdy/readytech-holdings-limited,"	386765000",3.33,0.00,0,"Information Technology"
ASX:ALI,"Argo Global Listed Infrastructure Limited (ASX:ALI)",https://www.listcorp.com/asx/ali/argo-global-listed-infrastructure-limited,"	386032000",2.18,0.00,0,Financials
ASX:PMC,"Platinum Capital Limited (ASX:PMC)",https://www.listcorp.com/asx/pmc/platinum-capital-limited,"	382701000",1.295,0.00,0,Financials
ASX:JHG,"Janus Henderson Group plc (ASX:JHG)",https://www.listcorp.com/asx/jhg/janus-henderson-group-plc,"	381724000",41.58,0.00,0,Financials
ASX:RMC,"Resimac Group Limited (ASX:RMC)",https://www.listcorp.com/asx/rmc/resimac-group-limited,"	381541000",0.95,0.00,0,Financials
ASX:TER,"TerraCom Limited (ASX:TER)",https://www.listcorp.com/asx/ter/terracom-limited,"	380459000",0.475,0.00,0,Energy
ASX:AASF,"Airlie Australian Share Fund (Managed Fund) (ASX:AASF)",https://www.listcorp.com/asx/aasf/airlie-australian-share-fund-managed-fund,"	379381000",3.41,0.00,0,Financials
ASX:IPG,"IPD Group Ltd (ASX:IPG)",https://www.listcorp.com/asx/ipg/ipd-group-ltd,"	379251000",4.38,0.00,0,Industrials
ASX:VETH,"Vanguard Ethically Conscious Australian Shares ETF (ASX:VETH)",https://www.listcorp.com/asx/veth/vanguard-ethically-conscious-australian-shares-etf,"	375329000",54.91,0.00,0,Financials
ASX:MVR,"Vaneck Vectors Australian Resources ETF (ASX:MVR)",https://www.listcorp.com/asx/mvr/vaneck-vectors-australian-resources-etf,"	375322000",36.64,0.00,0,Financials
ASX:SYR,"Syrah Resources Limited (ASX:SYR)",https://www.listcorp.com/asx/syr/syrah-resources-limited,"	375123000",0.555,0.00,0,Materials
ASX:RUL,"RPMGlobal Holdings Limited (ASX:RUL)",https://www.listcorp.com/asx/rul/rpmglobal-holdings-limited,"	373346000",1.64,0.00,0,"Information Technology"
ASX:GNG,"GR Engineering Services Limited (ASX:GNG)",https://www.listcorp.com/asx/gng/gr-engineering-services-limited,"	371605000",2.3,0.00,0,Materials
ASX:REP,"RAM Essential Services Property Fund (ASX:REP)",https://www.listcorp.com/asx/rep/ram-essential-services-property-fund,"	369970000",0.71,0.00,0,"Real Estate"
ASX:RNU,"Renascor Resources Limited (ASX:RNU)",https://www.listcorp.com/asx/rnu/renascor-resources,"	368214000",0.145,0.00,0,Materials
ASX:RG8,"Regal Asian Investments Limited (ASX:RG8)",https://www.listcorp.com/asx/rg8/regal-asian-investments-limited,"	367807000",1.85,0.00,0,Financials
ASX:HETH,"BetaShares Global Sustainability Leaders ETF  Currency Hedged (ASX:HETH)",https://www.listcorp.com/asx/heth/betashares-global-sustainability-leaders-etf-currency-hedged,"	366090000",11.83,0.00,0,Financials
ASX:SMP,"Smartpay Holdings Limited (ASX:SMP)",https://www.listcorp.com/asx/smp/smartpay-holdings-limited,"	364576000",1.53,0.00,0,Financials
ASX:CVW,"Clearview Wealth Limited (ASX:CVW)",https://www.listcorp.com/asx/cvw/clearview-wealth-limited,"	363571000",0.55,0.00,0,Financials
ASX:IPD,"ImpediMed Limited (ASX:IPD)",https://www.listcorp.com/asx/ipd/impedimed-limited,"	363381000",0.18,0.00,0,"Health Care"
ASX:SST,"Steamships Trading Company Limited (ASX:SST)",https://www.listcorp.com/asx/sst/steamships-trading-company,"	362796000",11.7,0.00,0,Industrials
ASX:LAU,"Lindsay Australia Limited (ASX:LAU)",https://www.listcorp.com/asx/lau/lindsay-australia-limited,"	362581000",1.17,0.00,0,Industrials
ASX:29M,"29Metals Limited (ASX:29M)",https://www.listcorp.com/asx/29m/29metals-limited,"	361561000",0.75,0.00,0,Materials
ASX:VBLD,"Vanguard Global Infrastructure Index ETF (ASX:VBLD)",https://www.listcorp.com/asx/vbld/vanguard-global-infrastructure-index-etf,"	360172000",61.79,0.00,0,Financials
ASX:CTM,"Centaurus Metals Limited (ASX:CTM)",https://www.listcorp.com/asx/ctm/centaurus-metals-limited,"	359829000",0.73,0.00,0,Materials
ASX:MEI,"Meteoric Resources NL (ASX:MEI)",https://www.listcorp.com/asx/mei/meteoric-resources,"	358929000",0.185,0.00,0,Materials
ASX:MYS,"MyState Limited (ASX:MYS)",https://www.listcorp.com/asx/mys/mystate-limited,"	358523000",3.27,0.00,0,Financials
ASX:AGY,"Argosy Minerals Limited (ASX:AGY)",https://www.listcorp.com/asx/agy/argosy-minerals-limited,"	358124000",0.255,0.00,0,Materials
ASX:WDIV,"SPDR S&P Global Dividend Fund (ASX:WDIV)",https://www.listcorp.com/asx/wdiv/spdr-s-and-p-global-dividend-fund,"	357926000",17.48,0.00,0,Financials
ASX:SRG,"SRG Global Limited (ASX:SRG)",https://www.listcorp.com/asx/srg/srg-global-limited,"	355837000",0.685,0.00,0,Industrials
ASX:AFP,"AFT Pharmaceuticals Limited (ASX:AFP)",https://www.listcorp.com/asx/afp/aft-pharmaceuticals-limited,"	353399000",3.37,0.00,0,"Health Care"
ASX:MHJ,"Michael Hill International Limited (ASX:MHJ)",https://www.listcorp.com/asx/mhj/michael-hill-international-limited,"	353111000",0.93,0.00,0,"Consumer Discretionary"
ASX:APX,"Appen Limited (ASX:APX)",https://www.listcorp.com/asx/apx/appen-limited,"	351504000",2.24,0.00,0,"Information Technology"
ASX:VAE,"Vanguard FTSE Asia Ex Japan Shares Index ETF (ASX:VAE)",https://www.listcorp.com/asx/vae/vanguard-ftse-asia-ex-japan-shares-index-etf,"	350539000",68.78,0.00,0,Financials
ASX:DXC,"Dexus Convenience Retail Reit (ASX:DXC)",https://www.listcorp.com/asx/dxc/dexus-convenience-retail-reit,"	348524000",2.53,0.00,0,"Real Estate"
ASX:NGI,"Navigator Global Investments Limited (ASX:NGI)",https://www.listcorp.com/asx/ngi/navigator-global-investments-limited,"	346043000",1.42,0.00,0,Financials
ASX:DDH,"DDH1 Limited (ASX:DDH)",https://www.listcorp.com/asx/ddh/ddh1-limited,"	344940000",0.86,0.00,0,Materials
ASX:AGX1,"Antipodes Global Shares (Quoted Managed Fund) (ASX:AGX1)",https://www.listcorp.com/asx/agx1/antipodes-global-shares,"	344365000",5.38,0.00,0,Financials
ASX:EHL,"Emeco Holdings Limited (ASX:EHL)",https://www.listcorp.com/asx/ehl/emeco-holdings-limited,"	342542000",0.66,0.00,0,Industrials
ASX:KSC,"K&S Corporation Limited (ASX:KSC)",https://www.listcorp.com/asx/ksc/k-and-s-corporation-limited,"	342122000",2.5,0.00,0,Industrials
ASX:SLC,"Superloop Limited (ASX:SLC)",https://www.listcorp.com/asx/slc/superloop-limited,"	341366000",0.695,0.00,0,"Communication Services"
ASX:BFG,"Bell Financial Group Limited (ASX:BFG)",https://www.listcorp.com/asx/bfg/bell-financial-group-limited,"	339989000",1.06,0.00,0,Financials
ASX:AGI,"Ainsworth Game Technology Limited (ASX:AGI)",https://www.listcorp.com/asx/agi/ainsworth-game-technology-limited,"	336794000",1,0.00,0,"Consumer Discretionary"
ASX:AKP,"Audio Pixels Limited (ASX:AKP)",https://www.listcorp.com/asx/akp/audio-pixels-limited,"	335332000",11.48,0.00,0,"Consumer Discretionary"
ASX:GDI,"GDI Property Group (ASX:GDI)",https://www.listcorp.com/asx/gdi/gdi-property-group,"	334903000",0.63,0.00,0,"Real Estate"
ASX:MAH,"Macmahon Holdings Limited (ASX:MAH)",https://www.listcorp.com/asx/mah/macmahon-holdings-limited,"	334023000",0.155,0.00,0,Materials
ASX:WXOZ,"SPDR S&P World ex Australia Carbon Control Fund (ASX:WXOZ)",https://www.listcorp.com/asx/wxoz/spdr-s-and-p-world-ex-australia-carbon-control-fund,"	333868000",38.77,0.00,0,Financials
ASX:WMI,"WAM Microcap Limited (ASX:WMI)",https://www.listcorp.com/asx/wmi/wam-microcap-limited,"	333348000",1.58,0.00,0,Financials
ASX:IGL,"IVE Group Limited (ASX:IGL)",https://www.listcorp.com/asx/igl/ive-group-limited,"	330048000",2.17,0.00,0,"Communication Services"
ASX:DUR,"Duratec Limited (ASX:DUR)",https://www.listcorp.com/asx/dur/duratec-limited,"	329428000",1.35,0.00,0,Industrials
ASX:KCN,"Kingsgate Consolidated Limited (ASX:KCN)",https://www.listcorp.com/asx/kcn/kingsgate-consolidated-limited,"	328633000",1.275,0.00,0,Materials
ASX:LKE,"Lake Resources NL (ASX:LKE)",https://www.listcorp.com/asx/lke/lake-resources,"	327162000",0.23,0.00,0,Materials
ASX:IMM,"Immutep Limited (ASX:IMM)",https://www.listcorp.com/asx/imm/immutep-limited,"	326509000",0.275,0.00,0,"Health Care"
ASX:PPS,"Praemium Limited (ASX:PPS)",https://www.listcorp.com/asx/pps/praemium-limited,"	326180000",0.65,0.00,0,"Information Technology"
ASX:TECH,"Global X Morningstar Global Technology ETF (ASX:TECH)",https://www.listcorp.com/asx/tech/global-x-morningstar-global-technology-etf,"	325954000",93.14,0.00,0,Financials
ASX:SKT,"Sky Network Television Limited (ASX:SKT)",https://www.listcorp.com/asx/skt/sky-network-television-limited,"	323668000",2.25,0.00,0,"Communication Services"
ASX:FANG,"Global X FANG+ ETF (ASX:FANG)",https://www.listcorp.com/asx/fang/global-x-fang-etf,"	322976000",18.91,0.00,0,Financials
ASX:BVS,"Bravura Solutions Limited (ASX:BVS)",https://www.listcorp.com/asx/bvs/bravura-solutions-limited,"	322815000",0.72,0.00,0,"Information Technology"
ASX:PIXX,"Platinum International Fund (Quoted Managed Hedge Fund) (ASX:PIXX)",https://www.listcorp.com/asx/pixx/platinum-international-fund-quoted-managed-hedge-fund,"	319754000",4.74,0.00,0,Financials
ASX:AVR,"Anteris Technologies Ltd (ASX:AVR)",https://www.listcorp.com/asx/avr/anteris-technologies-ltd,"	319728000",20.5,0.00,0,"Health Care"
ASX:FSF,"Fonterra Shareholders Fund (ASX:FSF)",https://www.listcorp.com/asx/fsf/fonterra-shareholders,"	316862000",2.95,0.00,0,"Consumer Staples"
ASX:COE,"Cooper Energy Limited (ASX:COE)",https://www.listcorp.com/asx/coe/cooper-energy-limited,"	315784000",0.12,0.00,0,Energy
ASX:BCI,"BCI Minerals Limited (ASX:BCI)",https://www.listcorp.com/asx/bci/bci-minerals-limited,"	315520000",0.26,0.00,0,Materials
ASX:WCMQ,"WCM Quality Global Growth Fund (Quoted Managed Fund) (ASX:WCMQ)",https://www.listcorp.com/asx/wcmq/wcm-quality-global-growth-fund-quoted-managed-fund,"	315373000",7.33,0.00,0,Financials
ASX:APZ,"Aspen Group (ASX:APZ)",https://www.listcorp.com/asx/apz/aspen-group,"	314377000",1.745,0.00,0,"Real Estate"
ASX:BDM,"Burgundy Diamond Mines Limited (ASX:BDM)",https://www.listcorp.com/asx/bdm/burgundy-diamond-mines-limited,"	312665000",0.22,0.00,0,Materials
ASX:AVH,"AVITA Medical, Inc. (ASX:AVH)",https://www.listcorp.com/asx/avh/avita-medical-inc.,"	312456000",5.03,0.00,0,"Health Care"
ASX:IZZ,"iShares China Large-Cap ETF (ASX:IZZ)",https://www.listcorp.com/asx/izz/ishares-china-large-cap-etf,"	311753000",42.07,0.00,0,Financials
ASX:RARI,"Russell Investments Australian Responsible Investment ETF (ASX:RARI)",https://www.listcorp.com/asx/rari/russell-investments-australian-responsible-investment-etf,"	310618000",24.32,0.00,0,Financials
ASX:3PL,"3P Learning Limited (ASX:3PL)",https://www.listcorp.com/asx/3pl/3p-learning-limited,"	309662000",1.12,0.00,0,"Consumer Discretionary"
ASX:IHOO,"iShares Global 100 (AUD Hedged) ETF (ASX:IHOO)",https://www.listcorp.com/asx/ihoo/ishares-global-100-aud-hedged-etf,"	308317000",137.02,0.00,0,Financials
ASX:PAI,"Platinum Asia Investments Limited (ASX:PAI)",https://www.listcorp.com/asx/pai/platinum-asia-investments-limited,"	307137000",0.83,0.00,0,Financials
ASX:AMH,"AMCIL Limited (ASX:AMH)",https://www.listcorp.com/asx/amh/amcil,"	304946000",0.97,0.00,0,Financials
ASX:CDP,"Carindale Property Trust (ASX:CDP)",https://www.listcorp.com/asx/cdp/carindale-property-trust,"	304394000",4.02,0.00,0,"Real Estate"
ASX:NMT,"Neometals Limited (ASX:NMT)",https://www.listcorp.com/asx/nmt/neometals-limited,"	304008000",0.55,0.00,0,Materials
ASX:PNR,"Pantoro Limited (ASX:PNR)",https://www.listcorp.com/asx/pnr/pantoro-limited,"	301834000",0.058,0.00,0,Materials
ASX:BMN,"Bannerman Energy Limited (ASX:BMN)",https://www.listcorp.com/asx/bmn/bannerman-energy-limited,"	301021000",2,0.00,0,Energy
ASX:LGL,"Lynch Group Holdings Limited (ASX:LGL)",https://www.listcorp.com/asx/lgl/lynch-group-holdings-limited,"	300283000",2.46,0.00,0,"Consumer Staples"
ASX:ARX,"Aroa Biosurgery Limited (ASX:ARX)",https://www.listcorp.com/asx/arx/aroa-biosurgery-limited,"	298505000",0.87,0.00,0,"Health Care"
ASX:LOT,"Lotus Resources Limited (ASX:LOT)",https://www.listcorp.com/asx/lot/lotus-resources-limited,"	295676000",0.22,0.00,0,Materials
ASX:BBOZ,"BetaShares Australian Equities Strong Bear Hedge Fund (ASX:BBOZ)",https://www.listcorp.com/asx/bboz/betashares-australian-equities-strong-bear-hedge-fund,"	295421000",3.6,0.00,0,Financials
ASX:UOS,"United Overseas Australia Limited (ASX:UOS)",https://www.listcorp.com/asx/uos/united-overseas-australia,"	292253000",0.56,0.00,0,"Real Estate"
ASX:SRV,"Servcorp Limited (ASX:SRV)",https://www.listcorp.com/asx/srv/servcorp-limited,"	291422000",3.01,0.00,0,"Real Estate"
ASX:EML,"EML Payments Limited (ASX:EML)",https://www.listcorp.com/asx/eml/eml-payments-limited,"	289838000",0.775,0.00,0,Financials
ASX:CAT,"Catapult Group International Limited (ASX:CAT)",https://www.listcorp.com/asx/cat/catapult-group-international-limited,"	288961000",1.145,0.00,0,"Information Technology"
ASX:ASM,"Australian Strategic Materials Limited (ASX:ASM)",https://www.listcorp.com/asx/asm/australian-strategic-materials-limited,"	286843000",1.72,0.00,0,Materials
ASX:IHD,"iShares S&P/ASX Dividend Opportunities ETF (ASX:IHD)",https://www.listcorp.com/asx/ihd/ishares-s-and-p-asx-dividend-opportunities-etf,"	284427000",12.83,0.00,0,Financials
ASX:LIN,"Lindian Resources Limited (ASX:LIN)",https://www.listcorp.com/asx/lin/lindian-resources-limited,"	283863000",0.25,0.00,0,Materials
ASX:TRA,"Turners Automotive Group Limited (ASX:TRA)",https://www.listcorp.com/asx/tra/turners-automotive-group-limited,"	283067000",3.24,0.00,0,"Consumer Discretionary"
ASX:SM1,"Synlait Milk Limited (ASX:SM1)",https://www.listcorp.com/asx/sm1/synlait-milk,"	281970000",1.29,0.00,0,"Consumer Staples"
ASX:CVC,"CVC Limited (ASX:CVC)",https://www.listcorp.com/asx/cvc/cvc-limited,"	280378000",2.4,0.00,0,Financials
ASX:GBND,"BetaShares Sustainability Leaders Diversified Bond ETF - Currency Hedged (ASX:GBND)",https://www.listcorp.com/asx/gbnd/betashares-sustainability-leaders-diversified-bond-etf-currency-hedged,"	279016000",20.38,0.00,0,Financials
ASX:UNI,"Universal Store Holdings Limited (ASX:UNI)",https://www.listcorp.com/asx/uni/universal-store-holdings-limited,"	276195000",3.6,0.00,0,"Consumer Discretionary"
ASX:WVOL,"iShares Edge MSCI World Minimum Volatility ETF (ASX:WVOL)",https://www.listcorp.com/asx/wvol/ishares-edge-msci-world-minimum-volatility-etf,"	273835000",36.51,0.00,0,Financials
ASX:A1N,"ARN Media Limited (ASX:A1N)",https://www.listcorp.com/asx/a1n/arn-media-limited,"	272607000",0.89,0.00,0,"Communication Services"
ASX:RHI,"Red Hill Minerals Limited (ASX:RHI)",https://www.listcorp.com/asx/rhi/red-hill-minerals-limited,"	272546000",4.27,0.00,0,Materials
ASX:BBN,"Baby Bunting Group Limited (ASX:BBN)",https://www.listcorp.com/asx/bbn/baby-bunting-group-limited,"	272511000",2.02,0.00,0,"Consumer Discretionary"
ASX:ZIP,"Zip Co Limited (ASX:ZIP)",https://www.listcorp.com/asx/zip/zip-co-limited,"	272133000",0.33,0.00,0,Financials
ASX:ALG,"Ardent Leisure Group Limited (ASX:ALG)",https://www.listcorp.com/asx/alg/ardent-leisure-group-limited,"	271034000",0.565,0.00,0,"Consumer Discretionary"
ASX:BHYB,"BetaShares Australian Major Bank Hybrids Index ETF (ASX:BHYB)",https://www.listcorp.com/asx/bhyb/betashares-australian-major-bank-hybrids-index-etf,"	269356000",9.78,0.00,0,Financials
ASX:PIA,"Pengana International Equities Limited (ASX:PIA)",https://www.listcorp.com/asx/pia/pengana-international-equities-limited,"	267117000",1.04,0.00,0,Financials
ASX:PLL,"Piedmont Lithium Limited (ASX:PLL)",https://www.listcorp.com/asx/pll/piedmont-lithium-limited,"	266082000",0.695,0.00,0,Materials
ASX:GDF,"Garda Property Group (ASX:GDF)",https://www.listcorp.com/asx/gdf/garda-property-group,"	265866000",1.17,0.00,0,"Real Estate"
ASX:PLUS,"VanEck Australian Corporate Bond Plus ETF (ASX:PLUS)",https://www.listcorp.com/asx/plus/vaneck-australian-corporate-bond-plus-etf,"	264702000",16.17,0.00,0,Financials
ASX:BBUS,"BetaShares U.S. Equities Strong Bear Hedge Fund - Currency Hedged (ASX:BBUS)",https://www.listcorp.com/asx/bbus/betashares-u.s.-equities-strong-bear-hedge-fund-currency-hedged,"	264691000",8.31,0.00,0,Financials
ASX:HNDQ,"BetaShares NASDAQ 100 ETF  Currency Hedged (ASX:HNDQ)",https://www.listcorp.com/asx/hndq/betashares-nasdaq-100-etf-currency-hedged,"	264470000",31.09,0.00,0,Financials
ASX:OPT,"Opthea Limited (ASX:OPT)",https://www.listcorp.com/asx/opt/opthea-limited,"	264235000",0.56562,0.00,0,"Health Care"
ASX:BOT,"Botanix Pharmaceuticals Limited (ASX:BOT)",https://www.listcorp.com/asx/bot/botanix-pharmaceuticals-limited,"	262921000",0.185,0.00,0,"Health Care"
ASX:QOR,"Qoria Limited (ASX:QOR)",https://www.listcorp.com/asx/qor/qoria-limited,"	262816000",0.245,0.00,0,"Information Technology"
ASX:RCB,"Russell Investments Australian Select Corporate Bond ETF (ASX:RCB)",https://www.listcorp.com/asx/rcb/russell-investments-australian-select-corporate-bond-etf,"	262151000",19.68,0.00,0,Financials
ASX:CVN,"Carnarvon Energy Limited (ASX:CVN)",https://www.listcorp.com/asx/cvn/carnarvon-energy-limited,"	261027000",0.145,0.00,0,Energy
ASX:GRX,"GreenX Metals Limited (ASX:GRX)",https://www.listcorp.com/asx/grx/greenx-metals-limited,"	260599000",0.955,0.00,0,Materials
ASX:VISM,"Vanguard MSCI International Small Companies Index ETF (ASX:VISM)",https://www.listcorp.com/asx/vism/vanguard-msci-international-small-companies-index-etf,"	260022000",58.41,0.00,0,Financials
ASX:PGH,"Pact Group Holdings Ltd (ASX:PGH)",https://www.listcorp.com/asx/pgh/pact-group-holdings-ltd,"	259939000",0.755,0.00,0,Materials
ASX:GCY,"Gascoyne Resources Limited (ASX:GCY)",https://www.listcorp.com/asx/gcy/gascoyne-resources,"	258886000",0.295,0.00,0,Materials
ASX:TRJ,"Trajan Group Holdings Limited (ASX:TRJ)",https://www.listcorp.com/asx/trj/trajan-group-holdings-limited,"	258543000",1.7,0.00,0,"Health Care"
ASX:SVR,"Solvar Limited (ASX:SVR)",https://www.listcorp.com/asx/svr/solvar-limited,"	257914000",1.24,0.00,0,Financials
ASX:COG,"Consolidated Financial Services Limited (ASX:COG)",https://www.listcorp.com/asx/cog/consolidated-financial-services-limited,"	257394000",1.35,0.00,0,Financials
ASX:GDG,"Generation Development Group Limited (ASX:GDG)",https://www.listcorp.com/asx/gdg/generation-development-group,"	257241000",1.35,0.00,0,Financials
ASX:ISEC,"iShares Enhanced Cash ETF (ASX:ISEC)",https://www.listcorp.com/asx/isec/ishares-enhanced-cash-etf,"	256695000",100.77,0.00,0,Financials
ASX:EBR,"EBR Systems Inc. (ASX:EBR)",https://www.listcorp.com/asx/ebr/ebr-systems-inc,"	255804000",0.85,0.00,0,"Health Care"
ASX:DHHF,"BetaShares Diversified All Growth ETF (ASX:DHHF)",https://www.listcorp.com/asx/dhhf/betashares-diversified-all-growth-etf,"	255798000",29.55,0.00,0,Financials
ASX:BTH,"Bigtincan Holdings Limited (ASX:BTH)",https://www.listcorp.com/asx/bth/bigtincan-holdings-limited,"	255046000",0.42,0.00,0,"Information Technology"
ASX:MLX,"Metals X Limited (ASX:MLX)",https://www.listcorp.com/asx/mlx/metals-x,"	254034000",0.28,0.00,0,Materials
ASX:STA,"Strandline Resources Limited (ASX:STA)",https://www.listcorp.com/asx/sta/strandline-resources-limited,"	253282000",0.175,0.00,0,Materials
ASX:ECF,"Elanor Commercial Property Fund (ASX:ECF)",https://www.listcorp.com/asx/ecf/elanor-commercial-property-fund,"	253245000",0.8,0.00,0,"Real Estate"
ASX:ABA,"Auswide Bank Ltd (ASX:ABA)",https://www.listcorp.com/asx/aba/auswide-bank,"	252945000",5.51,0.00,0,Financials
ASX:SVL,"Silver Mines Limited (ASX:SVL)",https://www.listcorp.com/asx/svl/silver-mines-limited,"	252780000",0.18,0.00,0,Materials
ASX:SVM,"Sovereign Metals Limited (ASX:SVM)",https://www.listcorp.com/asx/svm/sovereign-metals-limited,"	252057000",0.455,0.00,0,Materials
ASX:WR1,"Winsome Resources Limited (ASX:WR1)",https://www.listcorp.com/asx/wr1/winsome-resources-limited,"	250799000",1.54,0.00,0,Materials
ASX:D2O,"Duxton Water Limited (ASX:D2O)",https://www.listcorp.com/asx/d2o/duxton-water-limited,"	250483000",1.645,0.00,0,Utilities
ASX:HZN,"Horizon Oil Limited (ASX:HZN)",https://www.listcorp.com/asx/hzn/horizon-oil-limited,"	248224000",0.155,0.00,0,Energy
ASX:A11,"Atlantic Lithium Limited (ASX:A11)",https://www.listcorp.com/asx/a11/atlantic-lithium-limited,"	247958000",0.405,0.00,0,Materials
ASX:CGS,"Cogstate Limited (ASX:CGS)",https://www.listcorp.com/asx/cgs/cogstate-limited,"	245924000",1.42,0.00,0,"Health Care"
ASX:BCB,"Bowen Coking Coal Limited (ASX:BCB)",https://www.listcorp.com/asx/bcb/bowen-coking-coal-limited,"	245638000",0.115,0.00,0,Materials
ASX:IJH,"iShares S&P Mid-Cap ETF (ASX:IJH)",https://www.listcorp.com/asx/ijh/ishares-s-and-p-mid-cap-etf,"	245619000",40.08,0.00,0,Financials
ASX:CAJ,"Capitol Health Limited (ASX:CAJ)",https://www.listcorp.com/asx/caj/capitol-health-limited,"	244610000",0.23,0.00,0,"Health Care"
ASX:PYC,"PYC Therapeutics Limited (ASX:PYC)",https://www.listcorp.com/asx/pyc/pyc-therapeutics-limited,"	242636000",0.065,0.00,0,"Health Care"
ASX:RDV,"Russell Investments High Dividend Australian Shares ETF (ASX:RDV)",https://www.listcorp.com/asx/rdv/russell-investments-high-dividend-australian-shares-etf,"	240828000",27.59,0.00,0,Financials
ASX:IHCB,"iShares Core Global Corporate Bond (AUD Hedged) ETF (ASX:IHCB)",https://www.listcorp.com/asx/ihcb/ishares-core-global-corporate-bond-aud-hedged-etf,"	240322000",90.11,0.00,0,Financials
ASX:ADH,"Adairs Limited (ASX:ADH)",https://www.listcorp.com/asx/adh/adairs-limited,"	239676000",1.385,0.00,0,"Consumer Discretionary"
ASX:ACF,"Acrow Formwork and Construction Services Limited (ASX:ACF)",https://www.listcorp.com/asx/acf/acrow-formwork-and-construction-services-limited,"	238373000",0.895,0.00,0,Industrials
ASX:SFC,"Schaffer Corporation Limited (ASX:SFC)",https://www.listcorp.com/asx/sfc/schaffer-corporation-limited,"	237467000",17.5,0.00,0,"Consumer Discretionary"
ASX:OZBD,"BetaShares Australian Composite Bond ETF (ASX:OZBD)",https://www.listcorp.com/asx/ozbd/betashares-australian-composite-bond-etf,"	237031000",43.47,0.00,0,Financials
ASX:EX20,"BetaShares Australian Ex-20 Portfolio Diversifier ETF (ASX:EX20)",https://www.listcorp.com/asx/ex20/betashares-australian-ex-20-portfolio-diversifier-etf,"	237013000",19.25,0.00,0,Financials
ASX:FFX,"Firefinch Limited (ASX:FFX)",https://www.listcorp.com/asx/ffx/firefinch-limited,"	236569000",0.2,0.00,0,Materials
ASX:LPGD,"Loftus Peak Global Disruption Fund (Managed Fund) (ASX:LPGD)",https://www.listcorp.com/asx/lpgd/loftus-peak-global-disruption-fund-managed-fund,"	236428000",3.31,0.00,0,Financials
ASX:REIT,"VanEck FTSE International Property (Hedged) ETF (ASX:REIT)",https://www.listcorp.com/asx/reit/vaneck-ftse-international-property-hedged-etf,"	235551000",14.91,0.00,0,Financials
ASX:VEQ,"Vanguard FTSE Europe Shares ETF (ASX:VEQ)",https://www.listcorp.com/asx/veq/vanguard-ftse-europe-shares-etf,"	235318000",66.3,0.00,0,Financials
ASX:CDM,"Cadence Capital Limited (ASX:CDM)",https://www.listcorp.com/asx/cdm/cadence-capital,"	235248000",0.79,0.00,0,Financials
ASX:ORR,"OreCorp Limited (ASX:ORR)",https://www.listcorp.com/asx/orr/orecorp-limited,"	234704000",0.5,0.00,0,Materials
ASX:ROBO,"Global X ROBO Global Robotics & Automation ETF (ASX:ROBO)",https://www.listcorp.com/asx/robo/global-x-robo-global-robotics-and-automation-etf,"	234149000",71.36,0.00,0,Financials
ASX:GLN,"Galan Lithium Limited (ASX:GLN)",https://www.listcorp.com/asx/gln/galan-lithium-limited,"	232605000",0.67,0.00,0,Materials
ASX:WQG,"WCM Global Growth Limited (ASX:WQG)",https://www.listcorp.com/asx/wqg/wcm-global-growth-limited,"	232465000",1.25,0.00,0,Financials
ASX:BCK,"Brockman Mining Ltd (ASX:BCK)",https://www.listcorp.com/asx/bck/brockman-mining,"	232006000",0.025,0.00,0,Materials
ASX:TBN,"Tamboran Resources Limited (ASX:TBN)",https://www.listcorp.com/asx/tbn/tamboran-resources-limited,"	231751000",0.135,0.00,0,Energy
ASX:BSE,"Base Resources Limited (ASX:BSE)",https://www.listcorp.com/asx/bse/base-resources-limited,"	229712000",0.195,0.00,0,Materials
ASX:ENN,"Elanor Investors Group (ASX:ENN)",https://www.listcorp.com/asx/enn/elanor-investors,"	229188000",1.54,0.00,0,"Consumer Discretionary"
ASX:WAX,"WAM Research Limited (ASX:WAX)",https://www.listcorp.com/asx/wax/wam-research,"	229009000",1.14,0.00,0,Financials
ASX:DGL,"DGL Group Limited (ASX:DGL)",https://www.listcorp.com/asx/dgl/dgl-group-limited,"	228125000",0.8,0.00,0,Materials
ASX:IHWL,"iShares Core MSCI World Ex Australia ESG Leaders (AUD Hedged) ETF (ASX:IHWL)",https://www.listcorp.com/asx/ihwl/ishares-core-msci-world-ex-australia-esg-leaders-aud-hedged-etf,"	227846000",41.04,0.00,0,Financials
ASX:HUM,"Humm Group Limited (ASX:HUM)",https://www.listcorp.com/asx/hum/humm-group-limited,"	226888000",0.45,0.00,0,Financials
ASX:KSL,"Kina Securities Limited (ASX:KSL)",https://www.listcorp.com/asx/ksl/kina-securities-limited,"	226679000",0.79,0.00,0,Financials
ASX:CLG,"Close the Loop Limited (ASX:CLG)",https://www.listcorp.com/asx/clg/close-the-loop-limited,"	226075000",0.435,0.00,0,Industrials
ASX:SYM,"Symbio Holdings Limited (ASX:SYM)",https://www.listcorp.com/asx/sym/symbio-holdings-limited,"	225936000",2.65,0.00,0,"Information Technology"
ASX:QUS,"BetaShares S&P 500 Equal Weight ETF (ASX:QUS)",https://www.listcorp.com/asx/qus/betashares-s-and-p-500-equal-weight-etf,"	225182000",43.53,0.00,0,Financials
ASX:MAU,"Magnetic Resources NL (ASX:MAU)",https://www.listcorp.com/asx/mau/magnetic-resources,"	225106000",0.95,0.00,0,Materials
ASX:WC8,"Wildcat Resources Limited (ASX:WC8)",https://www.listcorp.com/asx/wc8/wildcat-resources-limited,"	222966000",0.335,0.00,0,Materials
ASX:PPE,"Peoplein Limited (ASX:PPE)",https://www.listcorp.com/asx/ppe/peoplein-limited,"	221438000",2.18,0.00,0,Industrials
ASX:VIT,"Vitura Health Limited (ASX:VIT)",https://www.listcorp.com/asx/vit/vitura-health-limited,"	220423000",0.395,0.00,0,"Health Care"
ASX:4DS,"4DS Memory Limited (ASX:4DS)",https://www.listcorp.com/asx/4ds/4ds-memory-limited,"	220393000",0.135,0.00,0,"Information Technology"
ASX:PBP,"Probiotec Limited (ASX:PBP)",https://www.listcorp.com/asx/pbp/probiotec-limited,"	219573000",2.7,0.00,0,"Health Care"
ASX:URF,"US Masters Residential Property Fund (ASX:URF)",https://www.listcorp.com/asx/urf/us-masters-residential-property,"	217977000",0.295,0.00,0,"Real Estate"
ASX:TRS,"The Reject Shop Limited (ASX:TRS)",https://www.listcorp.com/asx/trs/the-reject-shop-limited,"	217049000",5.66,0.00,0,"Consumer Discretionary"
ASX:AOF,"Australian Unity Office Fund (ASX:AOF)",https://www.listcorp.com/asx/aof/australian-unity-office-fund,"	216986000",1.32,0.00,0,"Real Estate"
ASX:TWR,"Tower Limited (ASX:TWR)",https://www.listcorp.com/asx/twr/tower-limited,"	216306000",0.57,0.00,0,Financials
ASX:CYC,"Cyclopharm Limited (ASX:CYC)",https://www.listcorp.com/asx/cyc/cyclopharm-limited,"	215732000",2.3,0.00,0,"Health Care"
ASX:CVL,"Civmec Limited (ASX:CVL)",https://www.listcorp.com/asx/cvl/civmec-limited,"	214748000",0.9,0.00,0,Industrials
ASX:4DX,"4DMedical Limited (ASX:4DX)",https://www.listcorp.com/asx/4dx/4dmedical-limited,"	213982000",0.62,0.00,0,"Health Care"
ASX:FEMX,"Fidelity Global Emerging Markets Fund (ASX:FEMX)",https://www.listcorp.com/asx/femx/fidelity-global-emerging-markets-fund,"	213703000",6.06,0.00,0,Financials
ASX:IXI,"iShares Global Consumer Staples ETF (ASX:IXI)",https://www.listcorp.com/asx/ixi/ishares-global-consumer-staples-etf,"	210685000",92.06,0.00,0,Financials
ASX:PSQ,"Pacific Smiles Group Limited (ASX:PSQ)",https://www.listcorp.com/asx/psq/pacific-smiles-group,"	209052000",1.31,0.00,0,"Health Care"
ASX:MAY,"Melbana Energy Limited (ASX:MAY)",https://www.listcorp.com/asx/may/melbana-energy-limited,"	208953000",0.062,0.00,0,Energy
ASX:VDCO,"Vanguard Diversified Conservative Index ETF (ASX:VDCO)",https://www.listcorp.com/asx/vdco/vanguard-diversified-conservative-index-etf,"	208452000",48.97,0.00,0,Financials
ASX:QVE,"QV Equities Limited (ASX:QVE)",https://www.listcorp.com/asx/qve/qv-equities-limited,"	207171000",0.91,0.00,0,Financials
ASX:KPG,"Kelly Partners Group Holdings Limited (ASX:KPG)",https://www.listcorp.com/asx/kpg/kelly-partners-group-holdings-limited,"	206100000",4.58,0.00,0,Industrials
ASX:VHT,"Volpara Health Technologies Limited (ASX:VHT)",https://www.listcorp.com/asx/vht/volpara-health-technologies,"	206030000",0.81,0.00,0,"Health Care"
ASX:FEX,"Fenix Resources Ltd (ASX:FEX)",https://www.listcorp.com/asx/fex/fenix-resources-ltd,"	204778000",0.295,0.00,0,Materials
ASX:ATA,"Atturra Limited (ASX:ATA)",https://www.listcorp.com/asx/ata/atturra-limited,"	204622000",0.88,0.00,0,"Information Technology"
ASX:IPX,"IperionX Limited (ASX:IPX)",https://www.listcorp.com/asx/ipx/iperionx-limited,"	204455000",1.05,0.00,0,Materials
ASX:NPR,"Newmark Property REIT (ASX:NPR)",https://www.listcorp.com/asx/npr/newmark-property-reit,"	204354000",1.125,0.00,0,"Real Estate"
ASX:WA1,"WA1 Resources Ltd (ASX:WA1)",https://www.listcorp.com/asx/wa1/wa1-resources-ltd,"	203947000",5.16,0.00,0,Materials
ASX:WMA,"WAM Alternative Assets Limited (ASX:WMA)",https://www.listcorp.com/asx/wma/wam-alternative-assets-limited,"	203018000",1.04,0.00,0,Financials
ASX:WOT,"WOTSO Property (ASX:WOT)",https://www.listcorp.com/asx/wot/wotso-property,"	201945000",1.24,0.00,0,"Real Estate"
ASX:WXHG,"SPDR S&P World ex Australia Carbon Control (Hedged) Fund (ASX:WXHG)",https://www.listcorp.com/asx/wxhg/spdr-s-and-p-world-ex-australia-carbon-control-hedged-fund,"	201709000",20.93,0.00,0,Financials
ASX:FUEL,"BetaShares Global Energy Companies ETF - Currency Hedged (ASX:FUEL)",https://www.listcorp.com/asx/fuel/betashares-global-energy-companies-etf-currency-hedged,"	201704000",6.21,0.00,0,Financials
ASX:CU6,"Clarity Pharmaceuticals Ltd (ASX:CU6)",https://www.listcorp.com/asx/cu6/clarity-pharmaceuticals,"	201428000",1.1,0.00,0,"Health Care"
ASX:PAR,"Paradigm Biopharmaceuticals Limited (ASX:PAR)",https://www.listcorp.com/asx/par/paradigm-biopharmaceuticals-limited,"	198677000",0.71,0.00,0,"Health Care"
ASX:GVF,"Global Value Fund Limited (ASX:GVF)",https://www.listcorp.com/asx/gvf/global-value-fund-limited,"	198492000",1.135,0.00,0,Financials
ASX:QGL,"Quantum Graphite Limited (ASX:QGL)",https://www.listcorp.com/asx/qgl/quantum-graphite-limited,"	197361000",0.585,0.00,0,Materials
ASX:GNP,"GenusPlus Group Ltd (ASX:GNP)",https://www.listcorp.com/asx/gnp/genusplus-group-ltd,"	197275000",1.11,0.00,0,Industrials
ASX:BRI,"Big River Industries Limited (ASX:BRI)",https://www.listcorp.com/asx/bri/big-river-industries-limited,"	196745000",2.37,0.00,0,Materials
ASX:VLUE,"VanEck MSCI International Value ETF (ASX:VLUE)",https://www.listcorp.com/asx/vlue/vaneck-msci-international-value-etf,"	196418000",23.92,0.00,0,Financials
ASX:VLC,"Vanguard MSCI Australian Large Companies Index ETF (ASX:VLC)",https://www.listcorp.com/asx/vlc/vanguard-msci-australian-large-companies-index-etf,"	196292000",70.89,0.00,0,Financials
ASX:ATEC,"BetaShares S&P/ASX Australian Technology ETF (ASX:ATEC)",https://www.listcorp.com/asx/atec/betashares-s-and-p-asx-australian-technology-etf,"	195355000",19.8,0.00,0,Financials
ASX:BRL,"Bathurst Resources Limited (ASX:BRL)",https://www.listcorp.com/asx/brl/bathurst-resources,"	195187000",1.02,0.00,0,Materials
ASX:MGV,"Musgrave Minerals Ltd (ASX:MGV)",https://www.listcorp.com/asx/mgv/musgrave-minerals,"	195099000",0.33,0.00,0,Materials
ASX:LGI,"LGI Limited (ASX:LGI)",https://www.listcorp.com/asx/lgi/lgi-limited,"	194246000",2.2,0.00,0,Utilities
ASX:A2B,"A2B Australia Limited (ASX:A2B)",https://www.listcorp.com/asx/a2b/a2b-australia-limited,"	193969000",1.6,0.00,0,Industrials
ASX:BKY,"Berkeley Energia Limited (ASX:BKY)",https://www.listcorp.com/asx/bky/berkeley-energia-limited,"	193922000",0.435,0.00,0,Energy
ASX:SXE,"Southern Cross Electrical Engineering Limited (ASX:SXE)",https://www.listcorp.com/asx/sxe/southern-cross-electrical-engineering-limited,"	192202000",0.735,0.00,0,Industrials
ASX:QSML,"Vaneck Vectors MSCI Inter Small Companies Qual ETF (ASX:QSML)",https://www.listcorp.com/asx/qsml/vaneck-vectors-msci-inter-small-companies-qual-etf,"	191935000",24.6,0.00,0,Financials
ASX:GLOB,"Barrow Hanley Global Share Fund (Managed Fund) (ASX:GLOB)",https://www.listcorp.com/asx/glob/barrow-hanley-global-share-fund-managed-fund,"	191764000",4.35,0.00,0,Financials
ASX:IVZ,"Invictus Energy Limited (ASX:IVZ)",https://www.listcorp.com/asx/ivz/invictus-energy-limited,"	190400000",0.16,0.00,0,Energy
ASX:MVE,"Vaneck Vectors S&P/ASX Midcap ETF (ASX:MVE)",https://www.listcorp.com/asx/mve/vaneck-vectors-s-and-p-asx-midcap-etf,"	190200000",36.18,0.00,0,Financials
ASX:FID,"Fiducian Group Limited (ASX:FID)",https://www.listcorp.com/asx/fid/fiducian-group-limited,"	187607000",5.96,0.00,0,Financials
ASX:DSE,"Dropsuite Limited (ASX:DSE)",https://www.listcorp.com/asx/dse/dropsuite-limited,"	187039000",0.27,0.00,0,"Information Technology"
ASX:GNX,"Genex Power Limited (ASX:GNX)",https://www.listcorp.com/asx/gnx/genex-power-limited,"	186999000",0.135,0.00,0,Utilities
ASX:WAR,"WAM Strategic Value Limited (ASX:WAR)",https://www.listcorp.com/asx/war/wam-strategic-value-limited,"	185530000",1.03,0.00,0,Financials
ASX:ASN,"Anson Resources Limited (ASX:ASN)",https://www.listcorp.com/asx/asn/anson-resources-limited,"	184248000",0.145,0.00,0,Materials
ASX:PLY,"PlaySide Studios Limited (ASX:PLY)",https://www.listcorp.com/asx/ply/playside-studios-limited,"	182972000",0.45,0.00,0,"Communication Services"
ASX:M7T,"Mach7 Technologies Limited (ASX:M7T)",https://www.listcorp.com/asx/m7t/mach7-technologies-limited,"	182601000",0.76,0.00,0,"Health Care"
ASX:DRO,"Droneshield Limited (ASX:DRO)",https://www.listcorp.com/asx/dro/droneshield-limited,"	181940000",0.31,0.00,0,Industrials
ASX:EXP,"Experience Co Limited (ASX:EXP)",https://www.listcorp.com/asx/exp/experience-co-limited,"	181249000",0.24,0.00,0,"Consumer Discretionary"
ASX:MVB,"Vaneck Vectors Australian Banks ETF (ASX:MVB)",https://www.listcorp.com/asx/mvb/vaneck-vectors-australian-banks-etf,"	181208000",28.3,0.00,0,Financials
ASX:BTI,"Bailador Technology Investments Limited (ASX:BTI)",https://www.listcorp.com/asx/bti/bailador-technology-investments-limited,"	180362000",1.245,0.00,0,Financials
ASX:DUG,"DUG Technology Ltd (ASX:DUG)",https://www.listcorp.com/asx/dug/dug-technology-ltd,"	180138000",1.525,0.00,0,"Information Technology"
ASX:SXL,"Southern Cross Media Group Limited (ASX:SXL)",https://www.listcorp.com/asx/sxl/southern-cross-media-group-limited,"	179924000",0.75,0.00,0,"Communication Services"
ASX:AIS,"Aeris Resources Limited (ASX:AIS)",https://www.listcorp.com/asx/ais/aeris-resources-limited,"	179646000",0.26,0.00,0,Materials
ASX:IOD,"IODM Limited (ASX:IOD)",https://www.listcorp.com/asx/iod/iodm-limited,"	179001000",0.3,0.00,0,"Information Technology"
ASX:HFR,"Highfield Resources Limited (ASX:HFR)",https://www.listcorp.com/asx/hfr/highfield-resources,"	178444000",0.455,0.00,0,Materials
ASX:HVST,"BetaShares Australian Dividend Harvester Fund (managed fund) (ASX:HVST)",https://www.listcorp.com/asx/hvst/betashares-australian-dividend-harvester-fund,"	176996000",12.01,0.00,0,Financials
ASX:SFX,"Sheffield Resources Limited (ASX:SFX)",https://www.listcorp.com/asx/sfx/sheffield-resources,"	176772000",0.45,0.00,0,Materials
ASX:FWD,"Fleetwood Limited (ASX:FWD)",https://www.listcorp.com/asx/fwd/fleetwood-limited,"	175841000",1.865,0.00,0,"Consumer Discretionary"
ASX:SLA,"SILK Laser Australia Limited (ASX:SLA)",https://www.listcorp.com/asx/sla/silk-laser-australia-limited,"	174769000",3.29,0.00,0,"Health Care"
ASX:ZER,"Zeta Resources Limited (ASX:ZER)",https://www.listcorp.com/asx/zer/zeta-resources-limited,"	174675000",0.31,0.00,0,Materials
ASX:FRI,"Finbar Group Limited (ASX:FRI)",https://www.listcorp.com/asx/fri/finbar-group-limited,"	174159000",0.64,0.00,0,"Real Estate"
ASX:TBR,"Tribune Resources Ltd (ASX:TBR)",https://www.listcorp.com/asx/tbr/tribune-resources,"	173145000",3.3,0.00,0,Materials
ASX:CLV,"Clover Corporation Limited (ASX:CLV)",https://www.listcorp.com/asx/clv/clover-corporation-limited,"	172844000",1.035,0.00,0,Materials
ASX:QRE,"BetaShares Australian Resources Sector ETF (ASX:QRE)",https://www.listcorp.com/asx/qre/betashares-australian-resources-sector-etf,"	172753000",7.44,0.00,0,Financials
ASX:MAET,"Munro Global Growth Fund (ASX:MAET)",https://www.listcorp.com/asx/maet/munro-global-growth-fund,"	172710000",4.71,0.00,0,Financials
ASX:WGN,"Wagners Holding Company Limited (ASX:WGN)",https://www.listcorp.com/asx/wgn/wagners-holding-company-limited,"	172609000",0.92,0.00,0,Materials
ASX:EZL,"Euroz Hartleys Group Limited (ASX:EZL)",https://www.listcorp.com/asx/ezl/euroz-hartleys-group-limited,"	171770000",1.045,0.00,0,Financials
ASX:COI,"Comet Ridge Limited (ASX:COI)",https://www.listcorp.com/asx/coi/comet-ridge-limited,"	171763000",0.17,0.00,0,Energy
ASX:CNB,"Carnaby Resources Limited (ASX:CNB)",https://www.listcorp.com/asx/cnb/carnaby-resources-limited,"	170078000",1.045,0.00,0,Materials
ASX:TNT,"Tesserent Limited (ASX:TNT)",https://www.listcorp.com/asx/tnt/tesserent-limited,"	169273000",0.125,0.00,0,"Information Technology"
ASX:AVJ,"AVJennings Limited (ASX:AVJ)",https://www.listcorp.com/asx/avj/avjennings-limited,"	168554000",0.415,0.00,0,"Consumer Discretionary"
ASX:OOO,"BetaShares Crude Oil Index ETF-Currency Hedged Synthetic (ASX:OOO)",https://www.listcorp.com/asx/ooo/betashares-crude-oil-index-etf-currency-hedged-synthetic,"	168490000",5.59,0.00,0,Financials
ASX:NTU,"Northern Minerals Limited (ASX:NTU)",https://www.listcorp.com/asx/ntu/northern-minerals-limited,"	167562000",0.033,0.00,0,Materials
ASX:VIA,"ViaGold Rare Earth Resources Holdings Limited (ASX:VIA)",https://www.listcorp.com/asx/via/viagold-rare-earth-resources-holdings-limited,"	166625000",2,0.00,0,Materials
ASX:XAM,"Xanadu Mines (ASX:XAM)",https://www.listcorp.com/asx/xam/xanadu-mines,"	163782000",0.1,0.00,0,Materials
ASX:ANG,"Austin Engineering Ltd (ASX:ANG)",https://www.listcorp.com/asx/ang/austin-engineering,"	163335000",0.28,0.00,0,Industrials
ASX:EOS,"Electro Optic Systems Holdings Limited (ASX:EOS)",https://www.listcorp.com/asx/eos/electro-optic-systems-holdings-limited,"	160962000",0.94,0.00,0,Industrials
ASX:XRF,"XRF Scientific Limited (ASX:XRF)",https://www.listcorp.com/asx/xrf/xrf-scientific-limited,"	160348000",1.17,0.00,0,Industrials
ASX:ERTH,"BetaShares Climate Change Innovation ETF (ASX:ERTH)",https://www.listcorp.com/asx/erth/betashares-climate-change-innovation-etf,"	160105000",10.1,0.00,0,Financials
ASX:TSK,"TASK Group Holdings Limited (ASX:TSK)",https://www.listcorp.com/asx/tsk/task-group-holdings-limited,"	159722000",0.45,0.00,0,"Information Technology"
ASX:HE8,"Helios Energy Limited (ASX:HE8)",https://www.listcorp.com/asx/he8/helios-energy-limited,"	158847000",0.061,0.00,0,Energy
ASX:ESGI,"VanEck MSCI International Sustainable Equity ETF (ASX:ESGI)",https://www.listcorp.com/asx/esgi/vaneck-msci-international-sustainable-equity-etf,"	158692000",30.34,0.00,0,Financials
ASX:ALC,"Alcidion Group Limited (ASX:ALC)",https://www.listcorp.com/asx/alc/alcidion-group-limited,"	158509000",0.125,0.00,0,"Health Care"
ASX:NZM,"NZME Limited (ASX:NZM)",https://www.listcorp.com/asx/nzm/nzme-limited,"	158166000",0.86,0.00,0,"Communication Services"
ASX:NXD,"NextEd Group Limited (ASX:NXD)",https://www.listcorp.com/asx/nxd/nexted-group-limited,"	157178000",0.71,0.00,0,"Consumer Discretionary"
ASX:DRUG,"BetaShares Global Healthcare ETF - Currency Hedged (ASX:DRUG)",https://www.listcorp.com/asx/drug/betashares-global-healthcare-etf-currency-hedged,"	157132000",7.86,0.00,0,Financials
ASX:ENR,"Encounter Resources Limited (ASX:ENR)",https://www.listcorp.com/asx/enr/encounter-resources-limited,"	156233000",0.395,0.00,0,Materials
ASX:CHL,"Camplify Holdings Limited (ASX:CHL)",https://www.listcorp.com/asx/chl/camplify-holdings-limited,"	155871000",2.18,0.00,0,Industrials
ASX:LM8,"Lunnon Metals Limited (ASX:LM8)",https://www.listcorp.com/asx/lm8/lunnon-metals-limited,"	155711000",0.89,0.00,0,Materials
ASX:NOL,"NobleOak Life Limited (ASX:NOL)",https://www.listcorp.com/asx/nol/nobleoak-life-limited,"	155587000",1.81,0.00,0,Financials
ASX:AEE,"Aura Energy Limited (ASX:AEE)",https://www.listcorp.com/asx/aee/aura-energy-limited,"	155287000",0.27,0.00,0,Energy
ASX:HCH,"Hot Chili Limited (ASX:HCH)",https://www.listcorp.com/asx/hch/hot-chili-limited,"	155279000",1.3,0.00,0,Materials
ASX:MSTR,"Morningstar International Shares Active ETF (Managed Fund) (ASX:MSTR)",https://www.listcorp.com/asx/mstr/morningstar-international-shares-active-etf-managed-fund,"	154790000",8.57,0.00,0,Financials
ASX:LPI,"Lithium Power International Limited (ASX:LPI)",https://www.listcorp.com/asx/lpi/lithium-power-international-limited,"	154163000",0.245,0.00,0,Materials
ASX:SSG,"Shaver Shop Group Limited (ASX:SSG)",https://www.listcorp.com/asx/ssg/shaver-shop-group-limited,"	152630000",1.165,0.00,0,"Consumer Discretionary"
ASX:FDV,"Frontier Digital Ventures Limited (ASX:FDV)",https://www.listcorp.com/asx/fdv/frontier-digital-ventures-limited,"	151616000",0.35,0.00,0,"Communication Services"
ASX:RCT,"Reef Casino Trust (ASX:RCT)",https://www.listcorp.com/asx/rct/reef-casino,"	151108000",3.08,0.00,0,"Consumer Discretionary"
ASX:DNK,"Danakali Limited (ASX:DNK)",https://www.listcorp.com/asx/dnk/danakali-limited,"	151017000",0.41,0.00,0,Materials
ASX:PEN,"Peninsula Energy Limited (ASX:PEN)",https://www.listcorp.com/asx/pen/peninsula-energy-limited,"	150846000",0.12,0.00,0,Energy
ASX:VCF,"Vanguard International Credit Securities Index (Hedged) ETF (ASX:VCF)",https://www.listcorp.com/asx/vcf/vanguard-international-credit-securities-index-hedged-etf,"	149861000",36.99,0.00,0,Financials
ASX:EBND,"VanEck Emerging Income Opportunities Active ETF (Managed Fund) (ASX:EBND)",https://www.listcorp.com/asx/ebnd/vaneck-emerging-income-opportunities-active-etf-managed-fund,"	149751000",10.02,0.00,0,Financials
ASX:WDMF,"iShares Edge MSCI World Multifactor ETF (ASX:WDMF)",https://www.listcorp.com/asx/wdmf/ishares-edge-msci-world-multifactor-etf,"	149360000",38.16,0.00,0,Financials
ASX:SPY,"SPDR S&P 500 ETF Trust (ASX:SPY)",https://www.listcorp.com/asx/spy/spdr-s-and-p-500-etf-trust,"	148378000",682.49,0.00,0,Financials
ASX:IR1,"Iris Metals Limited (ASX:IR1)",https://www.listcorp.com/asx/ir1/iris-metals-limited,"	148172000",1.78,0.00,0,Materials
ASX:TGP,"360 Capital Group (ASX:TGP)",https://www.listcorp.com/asx/tgp/360-capital-group,"	148059000",0.61,0.00,0,Financials
ASX:SDG,"Sunland Group Limited (ASX:SDG)",https://www.listcorp.com/asx/sdg/sunland-group-limited,"	147862000",1.08,0.00,0,"Real Estate"
ASX:WAT,"Waterco Limited (ASX:WAT)",https://www.listcorp.com/asx/wat/waterco,"	147424000",4.19,0.00,0,"Consumer Discretionary"
ASX:SBM,"St Barbara Limited (ASX:SBM)",https://www.listcorp.com/asx/sbm/st-barbara-limited,"	147235000",0.18,0.00,0,Materials
ASX:RBL,"Redbubble Limited (ASX:RBL)",https://www.listcorp.com/asx/rbl/redbubble-limited,"	147192000",0.53,0.00,0,"Consumer Discretionary"
ASX:UMAX,"BetaShares S&P 500 Yield Maximiser Fund (managed fund) (ASX:UMAX)",https://www.listcorp.com/asx/umax/betashares-s-and-p-500-yield-maximiser-fund-managed-fund,"	146662000",21.72,0.00,0,Financials
ASX:NWF,"Newfield Resources Limited (ASX:NWF)",https://www.listcorp.com/asx/nwf/newfield-resources-limited,"	146085000",0.19,0.00,0,Materials
ASX:IKO,"iShares MSCI South Korea Capped ETF (ASX:IKO)",https://www.listcorp.com/asx/iko/ishares-msci-south-korea-capped-etf,"	145953000",98.14,0.00,0,Financials
ASX:A1M,"AIC Mines Limited (ASX:A1M)",https://www.listcorp.com/asx/a1m/aic-mines-limited,"	145678000",0.315,0.00,0,Materials
ASX:RGB,"Russell Investments Australian Government Bond ETF (ASX:RGB)",https://www.listcorp.com/asx/rgb/russell-investments-australian-government-bond-etf,"	145643000",18.61,0.00,0,Financials
ASX:GRNV,"VanEck MSCI Australian Sustainable Equity ETF (ASX:GRNV)",https://www.listcorp.com/asx/grnv/vaneck-msci-australian-sustainable-equity-etf,"	145308000",26.98,0.00,0,Financials
ASX:PCL,"Pancontinental Energy NL (ASX:PCL)",https://www.listcorp.com/asx/pcl/pancontinental-energy-nl,"	145084000",0.018,0.00,0,Energy
ASX:PGC,"Paragon Care Limited (ASX:PGC)",https://www.listcorp.com/asx/pgc/paragon-care,"	145056000",0.22,0.00,0,"Health Care"
ASX:GGOV,"BetaShares U.S. Treasury Bond 20+ Year ETF  Currency Hedged (ASX:GGOV)",https://www.listcorp.com/asx/ggov/betashares-u.s.-treasury-bond-20-year-etf-currency-hedged,"	143935000",14.39,0.00,0,Financials
ASX:ERD,"EROAD Limited (ASX:ERD)",https://www.listcorp.com/asx/erd/eroad-limited,"	143687000",1.27,0.00,0,"Information Technology"
ASX:RAC,"Race Oncology Limited (ASX:RAC)",https://www.listcorp.com/asx/rac/race-oncology-limited,"	142685000",0.875,0.00,0,"Health Care"
ASX:CAA,"Capral Limited (ASX:CAA)",https://www.listcorp.com/asx/caa/capral-limited,"	142420000",7.89,0.00,0,Materials
ASX:OZR,"SPDR S&P/ASX 200 Resources Fund (ASX:OZR)",https://www.listcorp.com/asx/ozr/spdr-s-and-p-asx-200-resources-fund,"	141843000",13.09,0.00,0,Financials
ASX:MIH,"MNC Media Investment Ltd (ASX:MIH)",https://www.listcorp.com/asx/mih/mnc-media,"	141092000",3.6,0.00,0,"Communication Services"
ASX:HLA,"Healthia Limited (ASX:HLA)",https://www.listcorp.com/asx/hla/healthia-limited,"	140893000",1.005,0.00,0,"Health Care"
ASX:DRE,"Dreadnought Resources Limited (ASX:DRE)",https://www.listcorp.com/asx/dre/dreadnought-resources-limited,"	140481000",0.042,0.00,0,Materials
ASX:CKA,"Cokal Limited (ASX:CKA)",https://www.listcorp.com/asx/cka/cokal,"	140263000",0.13,0.00,0,Materials
ASX:DCN,"Dacian Gold Limited (ASX:DCN)",https://www.listcorp.com/asx/dcn/dacian-gold-limited,"	139932000",0.115,0.00,0,Materials
ASX:ETPMAG,"Global X Physical Silver (ASX:ETPMAG)",https://www.listcorp.com/asx/etpmag/global-x-physical-silver,"	139833000",34.9,0.00,0,Financials
ASX:IHL,"Incannex Healthcare Limited (ASX:IHL)",https://www.listcorp.com/asx/ihl/incannex-healthcare-limited,"	139657000",0.088,0.00,0,"Health Care"
ASX:NXG,"NexGen Energy (Canada) Ltd (ASX:NXG)",https://www.listcorp.com/asx/nxg/nexgen-energy-canada-ltd,"	139423000",7.93,0.00,0,Energy
ASX:SLH,"Silk Logistics Holdings Limited (ASX:SLH)",https://www.listcorp.com/asx/slh/silk-logistics-holdings-limited,"	139041000",1.76,0.00,0,Industrials
ASX:AGE,"Alligator Energy Limited (ASX:AGE)",https://www.listcorp.com/asx/age/alligator-energy,"	138849000",0.042,0.00,0,Energy
ASX:ONE,"Oneview Healthcare Plc (ASX:ONE)",https://www.listcorp.com/asx/one/oneview-healthcare-plc,"	138683000",0.215,0.00,0,"Health Care"
ASX:RDG,"Resource Development Group Limited (ASX:RDG)",https://www.listcorp.com/asx/rdg/resource-development-group-limited,"	138486000",0.048,0.00,0,Industrials
ASX:CCV,"Cash Converters International Limited (ASX:CCV)",https://www.listcorp.com/asx/ccv/cash-converters-international-limited,"	138060000",0.22,0.00,0,Financials
ASX:MXI,"MaxiPARTS Limited (ASX:MXI)",https://www.listcorp.com/asx/mxi/maxiparts-limited,"	137848000",2.89,0.00,0,Industrials
ASX:KIL,"Kiland Limited (ASX:KIL)",https://www.listcorp.com/asx/kil/kiland-limited,"	137292000",1.91,0.00,0,Materials
ASX:IHHY,"iShares Global High Yield Bond (AUD Hedged) ETF (ASX:IHHY)",https://www.listcorp.com/asx/ihhy/ishares-global-high-yield-bond-aud-hedged-etf,"	136989000",90.34,0.00,0,Financials
ASX:OBM,"Ora Banda Mining Ltd (ASX:OBM)",https://www.listcorp.com/asx/obm/ora-banda-mining,"	135595000",0.08,0.00,0,Materials
ASX:EGG,"Enero Group Limited (ASX:EGG)",https://www.listcorp.com/asx/egg/enero-group-limited,"	135538000",1.47,0.00,0,"Communication Services"
ASX:EGH,"Eureka Group Holdings Limited (ASX:EGH)",https://www.listcorp.com/asx/egh/eureka-group-holdings-limited,"	135479000",0.45,0.00,0,"Real Estate"
ASX:BUB,"Bubs Australia Limited (ASX:BUB)",https://www.listcorp.com/asx/bub/bubs-australia-limited,"	135244000",0.18,0.00,0,"Consumer Staples"
ASX:COS,"COSOL Limited (ASX:COS)",https://www.listcorp.com/asx/cos/cosol-limited,"	135192000",0.815,0.00,0,"Information Technology"
ASX:CRD,"Conrad Asia Energy Ltd (ASX:CRD)",https://www.listcorp.com/asx/crd/conrad-asia-energy-ltd,"	135078000",1.395,0.00,0,Energy
ASX:AMI,"Aurelia Metals Limited (ASX:AMI)",https://www.listcorp.com/asx/ami/aurelia-metals-limited,"	134783000",0.08,0.00,0,Materials
ASX:QIP,"Qantm Intellectual Property Limited (ASX:QIP)",https://www.listcorp.com/asx/qip/qantm-intellectual-property-limited,"	134539000",0.97,0.00,0,Industrials
ASX:AMA,"AMA Group Limited (ASX:AMA)",https://www.listcorp.com/asx/ama/ama-group-limited,"	134134000",0.125,0.00,0,Industrials
ASX:TGF,"Tribeca Global Natural Resources Limited (ASX:TGF)",https://www.listcorp.com/asx/tgf/tribeca-global-natural-resources-limited,"	132799000",1.69,0.00,0,Financials
ASX:RHK,"Red Hawk Mining Limited (ASX:RHK)",https://www.listcorp.com/asx/rhk/red-hawk-mining-limited,"	132546000",0.785,0.00,0,Materials
ASX:BOC,"Bougainville Copper Limited (ASX:BOC)",https://www.listcorp.com/asx/boc/bougainville-copper-limited,"	132351000",0.33,0.00,0,Materials
ASX:NXS,"Next Science Limited (ASX:NXS)",https://www.listcorp.com/asx/nxs/next-science-limited,"	132096000",0.615,0.00,0,"Health Care"
ASX:SHA,"SHAPE Australia Corporation Limited (ASX:SHA)",https://www.listcorp.com/asx/sha/shape-australia-corporation-limited,"	131078000",1.57,0.00,0,Industrials
ASX:X64,"Ten Sixty Four Limited (ASX:X64)",https://www.listcorp.com/asx/x64/ten-sixty-four-limited,"	130184000",0.57,0.00,0,Materials
ASX:MCA,"Murray Cod Australia Limited (ASX:MCA)",https://www.listcorp.com/asx/mca/murray-cod-australia-limited,"	130178000",0.17,0.00,0,"Consumer Staples"
ASX:EMV,"Emvision Medical Devices Limited (ASX:EMV)",https://www.listcorp.com/asx/emv/emvision-medical-devices-limited,"	130118000",1.67,0.00,0,"Health Care"
ASX:FOR,"Forager Australian Shares Fund (ASX:FOR)",https://www.listcorp.com/asx/for/forager-australian-shares-fund,"	129935000",1.29,0.00,0,Financials
ASX:JRV,"Jervois Global Limited (ASX:JRV)",https://www.listcorp.com/asx/jrv/jervois-global-limited,"	129721000",0.048,0.00,0,Materials
ASX:PEK,"Peak Rare Earths Limited (ASX:PEK)",https://www.listcorp.com/asx/pek/peak-rare-earths-limited,"	129674000",0.49,0.00,0,Materials
ASX:AND,"Ansarada Group Limited (ASX:AND)",https://www.listcorp.com/asx/and/ansarada-group-limited,"	129537000",1.45,0.00,0,"Information Technology"
ASX:GOW,"Gowing Brothers Limited (ASX:GOW)",https://www.listcorp.com/asx/gow/gowing-brothers-limited,"	129013000",2.42,0.00,0,Financials
ASX:AVL,"Australian Vanadium Limited (ASX:AVL)",https://www.listcorp.com/asx/avl/australian-vanadium-limited,"	128793000",0.0295,0.00,0,Materials
ASX:VVA,"Viva Leisure Limited (ASX:VVA)",https://www.listcorp.com/asx/vva/viva-leisure-limited,"	128206000",1.42,0.00,0,"Consumer Discretionary"
ASX:DEV,"DevEx Resources Limited (ASX:DEV)",https://www.listcorp.com/asx/dev/devex-resources-limited,"	127919000",0.345,0.00,0,Materials
ASX:GDC,"Global Data Centre Group (ASX:GDC)",https://www.listcorp.com/asx/gdc/global-data-centre-group,"	127886000",1.655,0.00,0,Financials
ASX:BET,"Betmakers Technology Group (ASX:BET)",https://www.listcorp.com/asx/bet/betmakers-technology-group,"	127378000",0.135,0.00,0,"Consumer Discretionary"
ASX:MTO,"MotorCycle Holdings Limited (ASX:MTO)",https://www.listcorp.com/asx/mto/motorcycle-holdings-limited,"	127277000",1.7275,0.00,0,"Consumer Discretionary"
ASX:ARL,"Ardea Resources Limited (ASX:ARL)",https://www.listcorp.com/asx/arl/ardea-resources-limited,"	127202000",0.74,0.00,0,Materials
ASX:CII,"CI Resources Limited (ASX:CII)",https://www.listcorp.com/asx/cii/ci-resources-limited,"	127139000",1.1,0.00,0,Materials
ASX:MDR,"MedAdvisor Limited (ASX:MDR)",https://www.listcorp.com/asx/mdr/medadvisor-limited,"	125607000",0.23,0.00,0,"Health Care"
ASX:HAS,"Hastings Technology Metals Limited (ASX:HAS)",https://www.listcorp.com/asx/has/hastings-technology-metals,"	125486000",0.97,0.00,0,Materials
ASX:RFG,"Retail Food Group Limited (ASX:RFG)",https://www.listcorp.com/asx/rfg/retail-food-group-limited,"	124776000",0.051,0.00,0,"Consumer Discretionary"
ASX:PCG,"Pengana Capital Group (ASX:PCG)",https://www.listcorp.com/asx/pcg/pengana-capital-group,"	124321000",1.13,0.00,0,Financials
ASX:HGO,"Hillgrove Resources Limited (ASX:HGO)",https://www.listcorp.com/asx/hgo/hillgrove-resources-limited,"	124278000",0.065,0.00,0,Materials
ASX:COB,"Cobalt Blue Holdings Limited (ASX:COB)",https://www.listcorp.com/asx/cob/cobalt-blue-holdings-limited,"	123969000",0.335,0.00,0,Materials
ASX:TPD,"Talon Energy Ltd (ASX:TPD)",https://www.listcorp.com/asx/tpd/talon-energy-ltd,"	123715000",0.195,0.00,0,Energy
ASX:CLX,"CTI Logistics Limited (ASX:CLX)",https://www.listcorp.com/asx/clx/cti-logistics-limited,"	123672000",1.555,0.00,0,Industrials
ASX:5EA,"5E Advanced Materials, Inc (ASX:5EA)",https://www.listcorp.com/asx/5ea/5e-advanced-materials-inc,"	123426000",0.41,0.00,0,Materials
ASX:RCE,"Recce Pharmaceuticals Limited (ASX:RCE)",https://www.listcorp.com/asx/rce/recce-pharmaceuticals-limited,"	122995000",0.69,0.00,0,"Health Care"
ASX:FSA,"FSA Group Limited (ASX:FSA)",https://www.listcorp.com/asx/fsa/fsa-group-limited,"	121346000",1,0.00,0,Financials
ASX:EOL,"Energy One Limited (ASX:EOL)",https://www.listcorp.com/asx/eol/energy-one-limited,"	121285000",4.05,0.00,0,"Information Technology"
ASX:ISO,"iShares S&P/ASX Small Ordinaries ETF (ASX:ISO)",https://www.listcorp.com/asx/iso/ishares-s-and-p-asx-small-ordinaries-etf,"	120888000",4.29,0.00,0,Financials
ASX:88E,"88 Energy Limited (ASX:88E)",https://www.listcorp.com/asx/88e/88-energy-limited,"	120647000",0.006,0.00,0,Energy
ASX:RXM,"Rex Minerals Ltd (ASX:RXM)",https://www.listcorp.com/asx/rxm/rex-minerals,"	120230000",0.19,0.00,0,Materials
ASX:ICOR,"iShares Core Corporate Bond ETF (ASX:ICOR)",https://www.listcorp.com/asx/icor/ishares-core-corporate-bond-etf,"	119818000",92.78,0.00,0,Financials
ASX:EMMG,"BetaShares Martin Currie Emerging Markets Fund (managed fund) (ASX:EMMG)",https://www.listcorp.com/asx/emmg/betashares-martin-currie-emerging-markets-fund-managed-fund,"	119654000",5.78,0.00,0,Financials
ASX:FOOD,"BetaShares Global Agriculture Companies ETF - Currency Hedged (ASX:FOOD)",https://www.listcorp.com/asx/food/betashares-global-agriculture-companies-etf-currency-hedged,"	118749000",6.86,0.00,0,Financials
ASX:USD,"BetaShares U.S. Dollar ETF (ASX:USD)",https://www.listcorp.com/asx/usd/betashares-u.s.-dollar-etf,"	118630000",15.05,0.00,0,Financials
ASX:IESG,"iShares Core MSCI Australia ESG Leaders ETF (ASX:IESG)",https://www.listcorp.com/asx/iesg/ishares-core-msci-australia-esg-leaders-etf,"	117795000",25.72,0.00,0,Financials
ASX:QPM,"Queensland Pacific Metals Limited (ASX:QPM)",https://www.listcorp.com/asx/qpm/queensland-pacific-metals-limited,"	117005000",0.067,0.00,0,Materials
ASX:REX,"Regional Express Holdings Limited (ASX:REX)",https://www.listcorp.com/asx/rex/regional-express-holdings-limited,"	116605000",1.045,0.00,0,Industrials
ASX:ARA,"Ariadne Australia Limited (ASX:ARA)",https://www.listcorp.com/asx/ara/ariadne-australia-limited,"	116602000",0.595,0.00,0,Industrials
ASX:EEG,"Empire Energy Group Limited (ASX:EEG)",https://www.listcorp.com/asx/eeg/empire-energy-group-limited,"	115968000",0.15,0.00,0,Energy
ASX:AXE,"Archer Materials Limited (ASX:AXE)",https://www.listcorp.com/asx/axe/archer-materials-limited,"	115955000",0.455,0.00,0,"Information Technology"
ASX:MI6,"Minerals 260 Limited (ASX:MI6)",https://www.listcorp.com/asx/mi6/minerals-260-limited,"	115830000",0.495,0.00,0,Materials
ASX:HPG,"Hipages Group Holdings Limited (ASX:HPG)",https://www.listcorp.com/asx/hpg/hipages-group-holdings-limited,"	115806000",0.87,0.00,0,"Communication Services"
ASX:CAM,"Clime Capital Limited (ASX:CAM)",https://www.listcorp.com/asx/cam/clime-capital-limited,"	115630000",0.825,0.00,0,Financials
ASX:SPZ,"Smart Parking Ltd (ASX:SPZ)",https://www.listcorp.com/asx/spz/smart-parking,"	115616000",0.33,0.00,0,"Information Technology"
ASX:SND,"Saunders International Limited (ASX:SND)",https://www.listcorp.com/asx/snd/saunders-international-limited,"	115454000",1.06,0.00,0,Industrials
ASX:G6M,"Group 6 Metals Limited (ASX:G6M)",https://www.listcorp.com/asx/g6m/group-6-metals-limited,"	115394000",0.115,0.00,0,Materials
ASX:SEC,"Spheria Emerging Companies (ASX:SEC)",https://www.listcorp.com/asx/sec/spheria-emerging-companies,"	115188000",1.915,0.00,0,Financials
ASX:PPK,"PPK Group Limited (ASX:PPK)",https://www.listcorp.com/asx/ppk/ppk-group,"	114290000",1.28,0.00,0,Materials
ASX:EQR,"EQ Resources Limited (ASX:EQR)",https://www.listcorp.com/asx/eqr/eq-resources-limited,"	113971000",0.077,0.00,0,Materials
ASX:ATC,"Altech Batteries Ltd (ASX:ATC)",https://www.listcorp.com/asx/atc/altech-batteries-ltd,"	113587000",0.069,0.00,0,Materials
ASX:CYL,"Catalyst Metals Limited (ASX:CYL)",https://www.listcorp.com/asx/cyl/catalyst-metals-limited,"	113345000",0.515,0.00,0,Materials
ASX:PAN,"Panoramic Resources Limited (ASX:PAN)",https://www.listcorp.com/asx/pan/panoramic-resources,"	113210000",0.048,0.00,0,Materials
ASX:LEG,"Legend Mining Limited (ASX:LEG)",https://www.listcorp.com/asx/leg/legend-mining-limited,"	113158000",0.039,0.00,0,Materials
ASX:OZF,"SPDR S&P/ASX 200 Financials EX A-REIT Fund (ASX:OZF)",https://www.listcorp.com/asx/ozf/spdr-s-and-p-asx-200-financials-ex-a-reit-fund,"	112476000",20.46,0.00,0,Financials
ASX:GT1,"Green Technology Metals Limited (ASX:GT1)",https://www.listcorp.com/asx/gt1/green-technology-metals-limited,"	111813000",0.525,0.00,0,Materials
ASX:RWL,"Rubicon Water Limited (ASX:RWL)",https://www.listcorp.com/asx/rwl/rubicon-water-limited,"	111725000",0.65,0.00,0,"Information Technology"
ASX:MHG,"Magellan Global Equities Fund (Currency Hedged) (ASX:MHG)",https://www.listcorp.com/asx/mhg/magellan-global-equities-fund-currency-hedged,"	111338000",3.19,0.00,0,Financials
ASX:CNEW,"VanEck China New Economy ETF (ASX:CNEW)",https://www.listcorp.com/asx/cnew/vaneck-china-new-economy-etf,"	111179000",6.6,0.00,0,Financials
ASX:SEMI,"Global X Semiconductor ETF (ASX:SEMI)",https://www.listcorp.com/asx/semi/global-x-semiconductor-etf,"	111027000",11.67,0.00,0,Financials
ASX:LRK,"Lark Distilling Co. Ltd (ASX:LRK)",https://www.listcorp.com/asx/lrk/lark-distilling-co,"	110882000",1.47,0.00,0,"Consumer Staples"
ASX:CLB,"Candy Club Holdings Limited (ASX:CLB)",https://www.listcorp.com/asx/clb/candy-club-holdings-limited,"	110400000",1.104,0.00,0,"Consumer Staples"
ASX:ESS,"Essential Metals Limited (ASX:ESS)",https://www.listcorp.com/asx/ess/essential-metals-limited,"	110233000",0.41,0.00,0,Materials
ASX:CCX,"City Chic Collective Limited (ASX:CCX)",https://www.listcorp.com/asx/ccx/city-chic-collective-limited,"	110162000",0.475,0.00,0,"Consumer Discretionary"
ASX:EL8,"Elevate Uranium Limited (ASX:EL8)",https://www.listcorp.com/asx/el8/elevate-uranium-limited,"	109756000",0.395,0.00,0,Energy
ASX:CD3,"Cordish Dixon Private Equity Fund III (ASX:CD3)",https://www.listcorp.com/asx/cd3/cordish-dixon-private-equity-fund-iii,"	109483000",1.52,0.00,0,Financials
ASX:JAN,"Janison Education Group Limited (ASX:JAN)",https://www.listcorp.com/asx/jan/janison-education-group,"	108676000",0.455,0.00,0,"Information Technology"
ASX:ORN,"Orion Minerals Limited (ASX:ORN)",https://www.listcorp.com/asx/orn/orion-minerals-limited,"	108047000",0.019,0.00,0,Materials
ASX:CLNE,"VanEck Global Clean Energy ETF (ASX:CLNE)",https://www.listcorp.com/asx/clne/vaneck-global-clean-energy-etf,"	107993000",7.81,0.00,0,Financials
ASX:EWC,"Energy World Corporation Limited (ASX:EWC)",https://www.listcorp.com/asx/ewc/energy-world-corporation-limited,"	107762000",0.035,0.00,0,Utilities
ASX:EVO,"Embark Early Education Limited (ASX:EVO)",https://www.listcorp.com/asx/evo/embark-early-education-limited,"	107696000",0.675,0.00,0,"Consumer Discretionary"
ASX:SMI,"Santana Minerals (ASX:SMI)",https://www.listcorp.com/asx/smi/santana-minerals,"	106898000",0.605,0.00,0,Materials
ASX:WIRE,"Global X Copper Miners ETF (ASX:WIRE)",https://www.listcorp.com/asx/wire/global-x-copper-miners-etf,"	106469000",11.51,0.00,0,Financials
ASX:IIGF,"Intelligent Investor Australian Equity Growth Fund (ASX:IIGF)",https://www.listcorp.com/asx/iigf/intelligent-investor-australian-equity-growth-fund,"	106419000",2.72,0.00,0,Financials
ASX:IMA,"Image Resources NL (ASX:IMA)",https://www.listcorp.com/asx/ima/image-resources,"	106166000",0.098,0.00,0,Materials
ASX:FDEM,"Fidelity Global Demographics Fund (Managed Fund) (ASX:FDEM)",https://www.listcorp.com/asx/fdem/fidelity-global-demographics-fund-managed-fund,"	105739000",26.48,0.00,0,Financials
ASX:EMH,"European Metals Holdings Limited (ASX:EMH)",https://www.listcorp.com/asx/emh/european-metals-holdings,"	105699000",0.77,0.00,0,Materials
ASX:SDI,"SDI Limited (ASX:SDI)",https://www.listcorp.com/asx/sdi/sdi-limited,"	105196000",0.885,0.00,0,"Health Care"
ASX:CAI,"Calidus Resources Limited (ASX:CAI)",https://www.listcorp.com/asx/cai/calidus-resources-limited,"	104859000",0.1725,0.00,0,Materials
ASX:SHJ,"Shine Justice Ltd (ASX:SHJ)",https://www.listcorp.com/asx/shj/shine-justice-ltd,"	104823000",0.605,0.00,0,"Consumer Discretionary"
ASX:EUR,"European Lithium Limited (ASX:EUR)",https://www.listcorp.com/asx/eur/european-lithium-limited,"	104568000",0.075,0.00,0,Materials
ASX:MAP,"Microba Life Sciences Limited (ASX:MAP)",https://www.listcorp.com/asx/map/microba-life-sciences-limited,"	103637000",0.35,0.00,0,"Health Care"
ASX:AVG,"Australian Vintage Limited (ASX:AVG)",https://www.listcorp.com/asx/avg/australian-vintage-limited,"	103582000",0.41,0.00,0,"Consumer Staples"
ASX:JRL,"Jindalee Resources Limited (ASX:JRL)",https://www.listcorp.com/asx/jrl/jindalee-resources-limited,"	103282000",1.8,0.00,0,Materials
ASX:IMR,"Imricor Medical Systems, Inc. (ASX:IMR)",https://www.listcorp.com/asx/imr/imricor-medical-systems-inc,"	102828000",0.645,0.00,0,"Health Care"
ASX:LCY,"Legacy Iron Ore Limited (ASX:LCY)",https://www.listcorp.com/asx/lcy/legacy-iron-ore-limited,"	102509000",0.016,0.00,0,Materials
ASX:MDX,"Mindax Limited (ASX:MDX)",https://www.listcorp.com/asx/mdx/mindax-limited,"	102278000",0.05,0.00,0,Materials
ASX:EP1,"E&P Financial Group Limited (ASX:EP1)",https://www.listcorp.com/asx/ep1/e-and-p-financial-group-limited,"	102202000",0.43,0.00,0,Financials
ASX:TVN,"Tivan Limited (ASX:TVN)",https://www.listcorp.com/asx/tvn/tivan-limited,"	102101000",0.065,0.00,0,Materials
ASX:BKT,"Black Rock Mining Limited (ASX:BKT)",https://www.listcorp.com/asx/bkt/black-rock-mining-limited,"	102009000",0.093,0.00,0,Materials
ASX:EGN,"Engenco Limited (ASX:EGN)",https://www.listcorp.com/asx/egn/engenco,"	101008000",0.32,0.00,0,Industrials
ASX:EVS,"EnviroSuite Limited (ASX:EVS)",https://www.listcorp.com/asx/evs/envirosuite-limited,"	100944000",0.08,0.00,0,"Information Technology"
ASX:ASH,"Ashley Services Group Limited (ASX:ASH)",https://www.listcorp.com/asx/ash/ashley-services-group,"	100783000",0.7,0.00,0,Industrials
ASX:SMN,"Structural Monitoring Systems Plc (ASX:SMN)",https://www.listcorp.com/asx/smn/structural-monitoring-systems,"	99292900",0.74,0.00,0,"Information Technology"
ASX:AW1,"American West Metals Limited (ASX:AW1)",https://www.listcorp.com/asx/aw1/american-west-metals-limited,"	99146300",0.275,0.00,0,Materials
ASX:PIQ,"Proteomics International Laboratories Ltd (ASX:PIQ)",https://www.listcorp.com/asx/piq/proteomics-international-laboratories,"	98479400",0.805,0.00,0,"Health Care"
ASX:BBL,"Brisbane Broncos Limited (ASX:BBL)",https://www.listcorp.com/asx/bbl/brisbane-broncos-limited,"	98040600",1,0.00,0,"Communication Services"
ASX:SNAS,"Global X Ultra Short Nasdaq 100 Hedge Fund (ASX:SNAS)",https://www.listcorp.com/asx/snas/global-x-ultra-short-nasdaq-100-hedge-fund,"	97753000",2.68,0.00,0,Financials
ASX:BCN,"Beacon Minerals Limited (ASX:BCN)",https://www.listcorp.com/asx/bcn/beacon-minerals-limited,"	97676000",0.026,0.00,0,Materials
ASX:IKE,"ikeGPS Group Limited (ASX:IKE)",https://www.listcorp.com/asx/ike/ikegps-group-limited,"	97614800",0.61,0.00,0,"Information Technology"
ASX:SZL,"Sezzle Inc (ASX:SZL)",https://www.listcorp.com/asx/szl/sezzle-inc,"	97077900",17.79,0.00,0,Financials
ASX:FLN,"Freelancer Limited (ASX:FLN)",https://www.listcorp.com/asx/fln/freelancer-limited,"	96946700",0.215,0.00,0,Industrials
ASX:DTZ,"Dotz Nano Limited (ASX:DTZ)",https://www.listcorp.com/asx/dtz/dotz-nano-limited,"	96747800",0.195,0.00,0,"Information Technology"
ASX:ADN,"Andromeda Metals Limited (ASX:ADN)",https://www.listcorp.com/asx/adn/andromeda-metals-limited,"	96410300",0.031,0.00,0,Materials
ASX:CVV,"Caravel Minerals (ASX:CVV)",https://www.listcorp.com/asx/cvv/caravel-minerals,"	96217300",0.185,0.00,0,Materials
ASX:NSC,"NAOS Small Cap Opportunities Company (ASX:NSC)",https://www.listcorp.com/asx/nsc/naos-small-cap-opportunities-company,"	95922200",0.7,0.00,0,Financials
ASX:KOV,"Korvest Ltd (ASX:KOV)",https://www.listcorp.com/asx/kov/korvest,"	95737700",8.21,0.00,0,Industrials
ASX:CEL,"Challenger Gold Limited (ASX:CEL)",https://www.listcorp.com/asx/cel/challenger-gold-limited,"	95349200",0.08,0.00,0,Materials
ASX:CYG,"Coventry Group Ltd (ASX:CYG)",https://www.listcorp.com/asx/cyg/coventry-group,"	95126600",1.03,0.00,0,Industrials
ASX:BIS,"Bisalloy Steel Group Limited (ASX:BIS)",https://www.listcorp.com/asx/bis/bisalloy-steel-group-limited,"	94900100",2,0.00,0,Materials
ASX:ABY,"Adore Beauty Group Limited (ASX:ABY)",https://www.listcorp.com/asx/aby/adore-beauty-group,"	94846400",1.01,0.00,0,"Consumer Discretionary"
ASX:HZR,"Hazer Group Limited (ASX:HZR)",https://www.listcorp.com/asx/hzr/hazer-group-limited,"	94835000",0.475,0.00,0,Materials
ASX:NZK,"New Zealand King Salmon Investments (ASX:NZK)",https://www.listcorp.com/asx/nzk/new-zealand-king-salmon-investments,"	94754600",0.175,0.00,0,"Consumer Staples"
ASX:TMH,"The Market Herald Limited (ASX:TMH)",https://www.listcorp.com/asx/tmh/the-market-herald-limited,"	94686900",0.295,0.00,0,"Communication Services"
ASX:E25,"Element 25 Limited (ASX:E25)",https://www.listcorp.com/asx/e25/element-25-limited,"	94625700",0.435,0.00,0,Materials
ASX:MNS,"Magnis Energy Technologies Limited (ASX:MNS)",https://www.listcorp.com/asx/mns/magnis-energy-technologies-limited,"	94359900",0.08,0.00,0,Materials
ASX:FLC,"Fluence Corporation Limited (ASX:FLC)",https://www.listcorp.com/asx/flc/fluence-corporation-limited,"	94330300",0.145,0.00,0,Industrials
ASX:KED,"Keypath Education International Inc (ASX:KED)",https://www.listcorp.com/asx/ked/keypath-education-international-inc,"	94147300",0.44,0.00,0,"Consumer Discretionary"
ASX:TOP,"Thorney Opportunities Limited (ASX:TOP)",https://www.listcorp.com/asx/top/thorney-opportunities-limited,"	94007800",0.495,0.00,0,"Real Estate"
ASX:FHE,"Frontier Energy Limited (ASX:FHE)",https://www.listcorp.com/asx/fhe/frontier-energy-limited,"	93925800",0.365,0.00,0,Materials
ASX:HIT,"Hitech Group Australia Limited (ASX:HIT)",https://www.listcorp.com/asx/hit/hitech-group-australia-limited,"	93684000",2.22,0.00,0,Industrials
ASX:MVP,"Medical Developments International Limited (ASX:MVP)",https://www.listcorp.com/asx/mvp/medical-developments-international-limited,"	93641200",1.085,0.00,0,"Health Care"
ASX:LBL,"Laserbond Limited (ASX:LBL)",https://www.listcorp.com/asx/lbl/laserbond-limited,"	93476200",0.85,0.00,0,Industrials
ASX:ANO,"Advance Zinctek Limited (ASX:ANO)",https://www.listcorp.com/asx/ano/advance-zinctek-limited,"	93023300",1.49,0.00,0,Materials
ASX:SRL,"Sunrise Energy Metals Limited (ASX:SRL)",https://www.listcorp.com/asx/srl/sunrise-energy-metals-limited,"	92934300",1.03,0.00,0,Materials
ASX:PH2DD,"ASX:PH2DD (ASX:PH2DD)",https://www.listcorp.com/asx/ph2dd/profile,"	92374300",0.27,0.00,0,Energy
ASX:ACE,"Acusensus Limited (ASX:ACE)",https://www.listcorp.com/asx/ace/acusensus-limited,"	92089500",0.73,0.00,0,"Information Technology"
ASX:ISLM,"Hejaz Equities Fund (Managed Fund) (ASX:ISLM)",https://www.listcorp.com/asx/islm/hejaz-equities-fund-managed-fund,"	91932100",0.935,0.00,0,Financials
ASX:GAL,"Galileo Mining Limited (ASX:GAL)",https://www.listcorp.com/asx/gal/galileo-mining-limited,"	91895600",0.465,0.00,0,Materials
ASX:STP,"Step One Clothing Limited (ASX:STP)",https://www.listcorp.com/asx/stp/step-one-clothing-limited,"	91743400",0.495,0.00,0,"Consumer Discretionary"
ASX:MMI,"Metro Mining Limited (ASX:MMI)",https://www.listcorp.com/asx/mmi/metro-mining-limited,"	91670500",0.021,0.00,0,Materials
ASX:OEL,"Otto Energy Limited (ASX:OEL)",https://www.listcorp.com/asx/oel/otto-energy-limited,"	91105200",0.019,0.00,0,Energy
ASX:NTD,"National Tyre & Wheel Limited (ASX:NTD)",https://www.listcorp.com/asx/ntd/national-tyre-and-wheel-limited,"	90624500",0.68,0.00,0,"Consumer Discretionary"
ASX:ART,"Airtasker Limited (ASX:ART)",https://www.listcorp.com/asx/art/airtasker-limited,"	90245400",0.2,0.00,0,"Communication Services"
ASX:RTR,"Rumble Resources Limited (ASX:RTR)",https://www.listcorp.com/asx/rtr/rumble-resources-limited,"	89877800",0.13,0.00,0,Materials
ASX:KKO,"Kinetiko Energy Ltd (ASX:KKO)",https://www.listcorp.com/asx/kko/kinetiko-energy,"	89764800",0.115,0.00,0,Energy
ASX:LMG,"Latrobe Magnesium Limited (ASX:LMG)",https://www.listcorp.com/asx/lmg/latrobe-magnesium-limited,"	89762300",0.052,0.00,0,Materials
ASX:GLB,"Globe International Limited (ASX:GLB)",https://www.listcorp.com/asx/glb/globe-international-limited,"	89147200",2.15,0.00,0,"Consumer Discretionary"
ASX:SNC,"Sandon Capital Investments Limited (ASX:SNC)",https://www.listcorp.com/asx/snc/sandon-capital-investments-limited,"	89046100",0.64,0.00,0,Financials
ASX:BYE,"Byron Energy Limited (ASX:BYE)",https://www.listcorp.com/asx/bye/byron-energy-limited,"	88674400",0.082,0.00,0,Energy
ASX:NAM,"Namoi Cotton Limited (ASX:NAM)",https://www.listcorp.com/asx/nam/namoi-cotton-limited,"	88104600",0.43,0.00,0,Industrials
ASX:MSV,"Mitchell Services Limited (ASX:MSV)",https://www.listcorp.com/asx/msv/mitchell-services-limited,"	87985400",0.405,0.00,0,Materials
ASX:ESTX,"Global X EURO STOXX 50 ETF (ASX:ESTX)",https://www.listcorp.com/asx/estx/global-x-euro-stoxx-50-etf,"	87887700",79.89,0.00,0,Financials
ASX:SHM,"Shriro Holdings Limited (ASX:SHM)",https://www.listcorp.com/asx/shm/shriro-holdings-limited,"	87256200",0.905,0.00,0,"Consumer Discretionary"
ASX:MNB,"Minbos Resources Limited (ASX:MNB)",https://www.listcorp.com/asx/mnb/minbos-resources,"	87036000",0.11,0.00,0,Materials
ASX:VEE,"Veem Limited (ASX:VEE)",https://www.listcorp.com/asx/vee/veem-limited,"	86860400",0.64,0.00,0,Industrials
ASX:CCR,"Credit Clear Limited (ASX:CCR)",https://www.listcorp.com/asx/ccr/credit-clear-limited,"	86633900",0.21,0.00,0,"Information Technology"
ASX:SOP,"Synertec Corporation Limited (ASX:SOP)",https://www.listcorp.com/asx/sop/synertec-corporation-limited,"	86299200",0.2,0.00,0,Industrials
ASX:AESG,"iShares Global Aggregate Bond ESG (AUD Hedged) ETF (ASX:AESG)",https://www.listcorp.com/asx/aesg/ishares-global-aggregate-bond-esg-aud-hedged-etf,"	86140600",94.66,0.00,0,Financials
ASX:TOT,"360 Capital Total Return Fund (ASX:TOT)",https://www.listcorp.com/asx/tot/360-capital-total-return-fund,"	85939700",0.595,0.00,0,"Real Estate"
ASX:SRX,"Sierra Rutile Holdings Limited (ASX:SRX)",https://www.listcorp.com/asx/srx/sierra-rutile-holdings-limited,"	85907900",0.2025,0.00,0,Materials
ASX:MLG,"MLG Oz Limited (ASX:MLG)",https://www.listcorp.com/asx/mlg/mlg-oz-limited,"	85874600",0.585,0.00,0,Materials
ASX:DRX,"Diatreme Resources Limited (ASX:DRX)",https://www.listcorp.com/asx/drx/diatreme-resources-limited,"	85784500",0.023,0.00,0,Materials
ASX:HAV,"Havilah Resources Limited (ASX:HAV)",https://www.listcorp.com/asx/hav/havilah-resources-limited,"	85492600",0.27,0.00,0,Materials
ASX:FCT,"Firstwave Cloud Technology Limited (ASX:FCT)",https://www.listcorp.com/asx/fct/firstwave-cloud-technology,"	84805200",0.051,0.00,0,"Information Technology"
ASX:CSS,"Clean Seas Tuna (ASX:CSS)",https://www.listcorp.com/asx/css/clean-seas-tuna,"	84399600",0.51,0.00,0,"Consumer Staples"
ASX:ACQ,"Acorn Capital Investment Fund (ASX:ACQ)",https://www.listcorp.com/asx/acq/acorn-capital-investment-fund,"	84294300",0.965,0.00,0,Financials
ASX:LPD,"Lepidico Ltd (ASX:LPD)",https://www.listcorp.com/asx/lpd/lepidico,"	84021400",0.011,0.00,0,Materials
ASX:TGM,"Theta Gold Mines Limited (ASX:TGM)",https://www.listcorp.com/asx/tgm/theta-gold-mines-limited,"	84009000",0.12,0.00,0,Materials
ASX:RHY,"Rhythm Biosciences Limited (ASX:RHY)",https://www.listcorp.com/asx/rhy/rhythm-biosciences-limited,"	82844100",0.375,0.00,0,"Health Care"
ASX:RYD,"Ryder Capital Limited (ASX:RYD)",https://www.listcorp.com/asx/ryd/ryder-capital-limited,"	82015100",0.98,0.00,0,Financials
ASX:FBR,"FBR Limited (ASX:FBR)",https://www.listcorp.com/asx/fbr/fbr-limited,"	81860700",0.022,0.00,0,Industrials
ASX:GTN,"GTN Limited (ASX:GTN)",https://www.listcorp.com/asx/gtn/gtn-limited,"	81658800",0.4,0.00,0,"Communication Services"
ASX:MOV,"MOVE Logistics Group Limited (ASX:MOV)",https://www.listcorp.com/asx/mov/move-logistics-group-limited,"	81469600",0.7,0.00,0,Industrials
ASX:POS,"Poseidon Nickel Limited (ASX:POS)",https://www.listcorp.com/asx/pos/poseidon-nickel-limited,"	81433700",0.022,0.00,0,Materials
ASX:GEN,"Genmin Limited (ASX:GEN)",https://www.listcorp.com/asx/gen/genmin-limited,"	81276000",0.18,0.00,0,Materials
ASX:VRX,"VRX Silica Ltd (ASX:VRX)",https://www.listcorp.com/asx/vrx/vrx-silica-ltd,"	81258400",0.145,0.00,0,Materials
ASX:HJPN,"BetaShares Japan ETF - Currency Hedged (ASX:HJPN)",https://www.listcorp.com/asx/hjpn/betashares-japan-etf-currency-hedged,"	80694800",16.21,0.00,0,Financials
ASX:VEFI,"Vanguard Ethically Conscious Global Aggregate Bond Index Hedged ETF (ASX:VEFI)",https://www.listcorp.com/asx/vefi/vanguard-ethically-conscious-global-aggregate-bond-index-hedged-etf,"	80650100",41.26,0.00,0,Financials
ASX:ATR,"Astron Corporation Limited (ASX:ATR)",https://www.listcorp.com/asx/atr/astron-corporation,"	80598100",0.55,0.00,0,Materials
ASX:RND,"Rand Mining Limited (ASX:RND)",https://www.listcorp.com/asx/rnd/rand-mining,"	79342000",1.395,0.00,0,Materials
ASX:VYS,"Vysarn Limited (ASX:VYS)",https://www.listcorp.com/asx/vys/vysarn-limited,"	79031400",0.195,0.00,0,Materials
ASX:EGL,"The Environmental Group Limited (ASX:EGL)",https://www.listcorp.com/asx/egl/environmental-group-limited,"	78762900",0.215,0.00,0,Industrials
ASX:TIG,"Tigers Realm Coal Limited (ASX:TIG)",https://www.listcorp.com/asx/tig/tigers-realm-coal-limited,"	78400200",0.006,0.00,0,Materials
ASX:NZO,"New Zealand Oil & Gas Ltd (ASX:NZO)",https://www.listcorp.com/asx/nzo/new-zealand-oil-and-gas-ltd,"	78382800",0.35,0.00,0,Energy
ASX:VLS,"Vita Life Sciences (ASX:VLS)",https://www.listcorp.com/asx/vls/vita-life-sciences,"	77424900",1.435,0.00,0,"Health Care"
ASX:STM,"Sunstone Metals Limited (ASX:STM)",https://www.listcorp.com/asx/stm/sunstone-metals-limited,"	77049600",0.025,0.00,0,Materials
ASX:PEB,"Pacific Edge Limited (ASX:PEB)",https://www.listcorp.com/asx/peb/pacific-edge-limited,"	76984700",0.095,0.00,0,"Health Care"
ASX:NWC,"New World Resources Limited (ASX:NWC)",https://www.listcorp.com/asx/nwc/new-world-resources-limited,"	76899200",0.034,0.00,0,Materials
ASX:EXR,"Elixir Energy Limited (ASX:EXR)",https://www.listcorp.com/asx/exr/elixir-energy-limited,"	76410700",0.082,0.00,0,Energy
ASX:INIF,"Intelligent Investor Australian Equity Income Fund (Managed Fund) (ASX:INIF)",https://www.listcorp.com/asx/inif/intelligent-investor-australian-equity-income-fund-managed-fund,"	76144200",2.61,0.00,0,Financials
ASX:CVB,"CurveBeam AI Limited (ASX:CVB)",https://www.listcorp.com/asx/cvb/curvebeam-ai-limited,"	75888600",0.415,0.00,0,Unclassified
ASX:MAM,"Microequities Asset Management Group (ASX:MAM)",https://www.listcorp.com/asx/mam/microequities-asset-management-group,"	75854700",0.57,0.00,0,Financials
ASX:TWD,"Tamawood Limited (ASX:TWD)",https://www.listcorp.com/asx/twd/tamawood-limited,"	75834600",2.14,0.00,0,"Consumer Discretionary"
ASX:DVDY,"VanEck Morningstar Australian Moat Income ETF (ASX:DVDY)",https://www.listcorp.com/asx/dvdy/vaneck-morningstar-australian-moat-income-etf,"	75823400",20.4,0.00,0,Financials
ASX:AUC,"Ausgold Limited (ASX:AUC)",https://www.listcorp.com/asx/auc/ausgold-limited,"	75772700",0.033,0.00,0,Materials
ASX:TTM,"Titan Minerals Limited (ASX:TTM)",https://www.listcorp.com/asx/ttm/titan-minerals-limited,"	75703400",0.05,0.00,0,Materials
ASX:VHM,"VHM Limited (ASX:VHM)",https://www.listcorp.com/asx/vhm/vhm-limited,"	75315700",0.49,0.00,0,Materials
ASX:DRA,"DRA Global Limited (ASX:DRA)",https://www.listcorp.com/asx/dra/dra-global-limited,"	74865000",1.37,0.00,0,Industrials
ASX:TEK,"Thorney Technologies Limited (ASX:TEK)",https://www.listcorp.com/asx/tek/thorney-technologies-limited,"	74856000",0.18,0.00,0,Energy
ASX:SEQ,"Sequoia Financial Group Ltd (ASX:SEQ)",https://www.listcorp.com/asx/seq/sequoia-financial-group-ltd,"	74611500",0.545,0.00,0,Financials
ASX:CPV,"ClearVue Technologies Limited (ASX:CPV)",https://www.listcorp.com/asx/cpv/clearvue-technologies-limited,"	74331400",0.34,0.00,0,Industrials
ASX:WMC,"Wiluna Mining Corporation Limited (ASX:WMC)",https://www.listcorp.com/asx/wmc/wiluna-mining-corporation-limited,"	74238000",0.205,0.00,0,Materials
ASX:EIQ,"Echo IQ Limited (ASX:EIQ)",https://www.listcorp.com/asx/eiq/echo-iq-limited,"	73973200",0.15,0.00,0,"Information Technology"
ASX:AHX,"Apiam Animal Health Limited (ASX:AHX)",https://www.listcorp.com/asx/ahx/apiam-animal-health-limited,"	73802200",0.41,0.00,0,"Health Care"
ASX:G1A,"Galena Mining Limited (ASX:G1A)",https://www.listcorp.com/asx/g1a/galena-mining-limited,"	73751700",0.098,0.00,0,Materials
ASX:MRL,"Mayur Resources Limited (ASX:MRL)",https://www.listcorp.com/asx/mrl/mayur-resources-limited,"	73667900",0.225,0.00,0,Materials
ASX:ECL,"Excelsior Capital Limited (ASX:ECL)",https://www.listcorp.com/asx/ecl/excelsior-capital-limited,"	73356000",2.53,0.00,0,Industrials
ASX:JYC,"Joyce Corporation Ltd (ASX:JYC)",https://www.listcorp.com/asx/jyc/joyce-corporation,"	73281300",2.58,0.00,0,"Consumer Discretionary"
ASX:OCC,"Orthocell Limited (ASX:OCC)",https://www.listcorp.com/asx/occ/orthocell-limited,"	73002100",0.37,0.00,0,"Health Care"
ASX:WKT,"Walkabout Resources Limited (ASX:WKT)",https://www.listcorp.com/asx/wkt/walkabout-resources-limited,"	72877900",0.11,0.00,0,Materials
ASX:CRR,"Critical Resources Limited (ASX:CRR)",https://www.listcorp.com/asx/crr/critical-resources-limited,"	72871400",0.041,0.00,0,Materials
ASX:CYM,"Cyprium Metals Limited (ASX:CYM)",https://www.listcorp.com/asx/cym/cyprium-metals-limited,"	72851900",0.09977,0.00,0,Materials
ASX:IRD,"Iron Road Limited (ASX:IRD)",https://www.listcorp.com/asx/ird/iron-road-limited,"	72620200",0.09,0.00,0,Materials
ASX:RFT,"Rectifier Technologies Ltd (ASX:RFT)",https://www.listcorp.com/asx/rft/rectifier-technologies-ltd,"	71703000",0.052,0.00,0,Industrials
ASX:ZEO,"Zeotech Limited (ASX:ZEO)",https://www.listcorp.com/asx/zeo/zeotech-limited,"	71648800",0.042,0.00,0,Materials
ASX:SSL,"Sietel Limited (ASX:SSL)",https://www.listcorp.com/asx/ssl/sietel-limited,"	71266600",8.9,0.00,0,"Real Estate"
ASX:MCP,"McPherson's Limited (ASX:MCP)",https://www.listcorp.com/asx/mcp/mcphersons-limited,"	71254800",0.495,0.00,0,"Consumer Staples"
ASX:IXR,"Ionic Rare Earths Limited (ASX:IXR)",https://www.listcorp.com/asx/ixr/ionic-rare-earths-limited,"	71029900",0.018,0.00,0,Materials
ASX:AHL,"Adrad Holdings Limited (ASX:AHL)",https://www.listcorp.com/asx/ahl/adrad-holdings-limited,"	70975100",0.88,0.00,0,"Consumer Discretionary"
ASX:KGL,"KGL Resources Limited (ASX:KGL)",https://www.listcorp.com/asx/kgl/kgl-resources-limited,"	70911500",0.125,0.00,0,Materials
ASX:ACB,"A-Cap Energy Limited (ASX:ACB)",https://www.listcorp.com/asx/acb/a-cap-energy-limited,"	70796900",0.057,0.00,0,Energy
ASX:S2R,"S2 Resources Ltd (ASX:S2R)",https://www.listcorp.com/asx/s2r/s2-resources-ltd,"	70740800",0.1725,0.00,0,Materials
ASX:BC8,"Black Cat Syndicate Limited (ASX:BC8)",https://www.listcorp.com/asx/bc8/black-cat-syndicate-limited,"	70722300",0.265,0.00,0,Materials
ASX:TMK,"TMK Energy Limited (ASX:TMK)",https://www.listcorp.com/asx/tmk/tmk-energy-limited,"	70428100",0.014,0.00,0,Energy
ASX:CRYP,"BetaShares Crypto Innovators ETF (ASX:CRYP)",https://www.listcorp.com/asx/cryp/betashares-crypto-innovators-etf,"	70356000",2.86,0.00,0,Financials
ASX:SOM,"SomnoMed Limited (ASX:SOM)",https://www.listcorp.com/asx/som/somnomed,"	70345400",0.85,0.00,0,"Health Care"
ASX:BLG,"BluGlass Limited (ASX:BLG)",https://www.listcorp.com/asx/blg/bluglass,"	70290100",0.046,0.00,0,"Information Technology"
ASX:CAE,"Cannindah Resources Limited (ASX:CAE)",https://www.listcorp.com/asx/cae/cannindah-resources-limited,"	70247500",0.125,0.00,0,Materials
ASX:HHR,"Hartshead Resources NL (ASX:HHR)",https://www.listcorp.com/asx/hhr/hartshead-resources-nl,"	70217100",0.025,0.00,0,Energy
ASX:IRI,"Integrated Research Limited (ASX:IRI)",https://www.listcorp.com/asx/iri/integrated-research-limited,"	70097700",0.405,0.00,0,"Information Technology"
ASX:INES,"Intelligent Investor Ethical Share Fund (Managed Fund) (ASX:INES)",https://www.listcorp.com/asx/ines/intelligent-investor-ethical-share-fund-managed-fund,"	70084100",3.04,0.00,0,Financials
ASX:MOGL,"Montaka Global Long Only Equites Fund (Managed Fund) (ASX:MOGL)",https://www.listcorp.com/asx/mogl/montaka-global-long-only-equites-fund-managed-fund,"	69959300",3.3,0.00,0,Financials
ASX:3DP,"Pointerra Limited (ASX:3DP)",https://www.listcorp.com/asx/3dp/pointerra-limited,"	69756500",0.098,0.00,0,"Information Technology"
ASX:DSK,"Dusk Group Limited (ASX:DSK)",https://www.listcorp.com/asx/dsk/dusk-group-limited,"	69740000",1.12,0.00,0,"Consumer Discretionary"
ASX:AUT,"Auteco Minerals Ltd (ASX:AUT)",https://www.listcorp.com/asx/aut/auteco-minerals-ltd,"	69385100",0.03,0.00,0,Materials
ASX:ESPO,"VanEck Video Gaming and Esports ETF (ASX:ESPO)",https://www.listcorp.com/asx/espo/vaneck-video-gaming-and-esports-etf,"	69087900",10.13,0.00,0,Financials
ASX:ZYUS,"Global X S&P 500 High Yield Low Volatility ETF (ASX:ZYUS)",https://www.listcorp.com/asx/zyus/global-x-s-and-p-500-high-yield-low-volatility-etf,"	68545300",13.04,0.00,0,Financials
ASX:RXL,"Rox Resources Limited (ASX:RXL)",https://www.listcorp.com/asx/rxl/rox-resources,"	68542600",0.205,0.00,0,Materials
ASX:MEA,"McGrath Limited (ASX:MEA)",https://www.listcorp.com/asx/mea/mcgrath-limited,"	68027300",0.425,0.00,0,"Real Estate"
ASX:EGR,"EcoGraf Limited (ASX:EGR)",https://www.listcorp.com/asx/egr/ecograf-limited,"	67888800",0.15,0.00,0,Materials
ASX:STK,"Strickland Metals Limited (ASX:STK)",https://www.listcorp.com/asx/stk/strickland-metals-limited,"	67210100",0.042,0.00,0,Materials
ASX:HLTH,"VanEck Global Healthcare Leaders ETF (ASX:HLTH)",https://www.listcorp.com/asx/hlth/vaneck-global-healthcare-leaders-etf,"	66222500",10.34,0.00,0,Financials
ASX:CHZ,"Chesser Resources Limited (ASX:CHZ)",https://www.listcorp.com/asx/chz/chesser-resources-limited,"	66217700",0.1125,0.00,0,Materials
ASX:IVR,"Investigator Resources Limited (ASX:IVR)",https://www.listcorp.com/asx/ivr/investigator-resources-limited,"	66109800",0.046,0.00,0,Materials
ASX:GSS,"Genetic Signatures Limited (ASX:GSS)",https://www.listcorp.com/asx/gss/genetic-signatures-limited,"	65966800",0.46,0.00,0,"Health Care"
ASX:TYX,"Tyranna Resources Limited (ASX:TYX)",https://www.listcorp.com/asx/tyx/tyranna-resources-limited,"	65728500",0.02,0.00,0,Materials
ASX:RKN,"Reckon Limited (ASX:RKN)",https://www.listcorp.com/asx/rkn/reckon-limited,"	65711000",0.58,0.00,0,"Information Technology"
ASX:PTL,"Pental Limited (ASX:PTL)",https://www.listcorp.com/asx/ptl/pental-limited,"	65626900",0.385,0.00,0,"Consumer Staples"
ASX:KAI,"Kairos Minerals Limited (ASX:KAI)",https://www.listcorp.com/asx/kai/kairos-minerals-limited,"	65522800",0.025,0.00,0,Materials
ASX:HNG,"Hancock & Gore Ltd (ASX:HNG)",https://www.listcorp.com/asx/hng/hancock-and-gore-ltd,"	65355100",0.29,0.00,0,Industrials
ASX:DME,"Dome Gold Mines (ASX:DME)",https://www.listcorp.com/asx/dme/dome-gold-mines,"	65344600",0.185,0.00,0,Materials
ASX:MFD,"Mayfield Childcare Limited (ASX:MFD)",https://www.listcorp.com/asx/mfd/mayfield-childcare-limited,"	65312700",1,0.00,0,"Consumer Discretionary"
ASX:ADO,"AnteoTech Ltd (ASX:ADO)",https://www.listcorp.com/asx/ado/anteotech,"	65248200",0.03,0.00,0,"Health Care"
ASX:ETM,"Energy Transition Minerals Ltd (ASX:ETM)",https://www.listcorp.com/asx/etm/energy-transition-minerals-ltd,"	65075700",0.048,0.00,0,Materials
ASX:BGBL,"Betashares Global Shares ETF (ASX:BGBL)",https://www.listcorp.com/asx/bgbl/betashares-global-shares-etf,"	65046200",54.66,0.00,0,Financials
ASX:CAY,"Canyon Resources Limited (ASX:CAY)",https://www.listcorp.com/asx/cay/canyon-resources,"	65009100",0.064,0.00,0,Materials
ASX:IIQ,"INOVIQ Ltd (ASX:IIQ)",https://www.listcorp.com/asx/iiq/inoviq-ltd,"	64873200",0.705,0.00,0,"Health Care"
ASX:TMT,"Technology Metals Australia Limited (ASX:TMT)",https://www.listcorp.com/asx/tmt/technology-metals-australia-limited,"	64842900",0.255,0.00,0,Materials
ASX:SPQ,"Superior Resources Limited (ASX:SPQ)",https://www.listcorp.com/asx/spq/superior-resources-limited,"	64209400",0.035,0.00,0,Materials
ASX:PEX,"Peel Mining Limited (ASX:PEX)",https://www.listcorp.com/asx/pex/peel-mining,"	63884500",0.11,0.00,0,Materials
ASX:BEZ,"Besra Gold Inc (ASX:BEZ)",https://www.listcorp.com/asx/bez/besra-gold,"	63870300",0.175,0.00,0,Materials
ASX:ZYAU,"Global X S&P/ASX 300 High Yield Plus ETF (ASX:ZYAU)",https://www.listcorp.com/asx/zyau/global-x-s-and-p-asx-300-high-yield-plus-etf,"	63813300",8.05,0.00,0,Financials
ASX:GAP,"Gale Pacific Limited (ASX:GAP)",https://www.listcorp.com/asx/gap/gale-pacific-limited,"	63570400",0.23,0.00,0,"Consumer Discretionary"
ASX:AMN,"Agrimin Limited (ASX:AMN)",https://www.listcorp.com/asx/amn/agrimin-limited,"	63437500",0.22,0.00,0,Materials
ASX:TRY,"Troy Resources Limited (ASX:TRY)",https://www.listcorp.com/asx/try/troy-resources-limited,"	62921000",0.0295001,0.00,0,Materials
ASX:TGN,"Tungsten Mining NL (ASX:TGN)",https://www.listcorp.com/asx/tgn/tungsten-mining,"	62913100",0.08,0.00,0,Materials
ASX:EOF,"Ecofibre Limited (ASX:EOF)",https://www.listcorp.com/asx/eof/ecofibre-limited,"	62858600",0.18,0.00,0,"Health Care"
ASX:ARR,"American Rare Earths Limited (ASX:ARR)",https://www.listcorp.com/asx/arr/american-rare-earths-limited,"	62499300",0.14,0.00,0,Materials
ASX:LSX,"Lion Selection Group Limited (ASX:LSX)",https://www.listcorp.com/asx/lsx/lion-selection-group-limited,"	62106300",0.44,0.00,0,Financials
ASX:TVL,"Touch Ventures Limited (ASX:TVL)",https://www.listcorp.com/asx/tvl/touch-ventures-limited,"	62086100",0.088,0.00,0,Financials
ASX:IXU,"IXUP Limited (ASX:IXU)",https://www.listcorp.com/asx/ixu/ixup-limited,"	61991900",0.058,0.00,0,"Information Technology"
ASX:PLT,"Plenti Group Limited (ASX:PLT)",https://www.listcorp.com/asx/plt/plenti-group-limited,"	61977700",0.36,0.00,0,Financials
ASX:MX1,"Micro-X Limited (ASX:MX1)",https://www.listcorp.com/asx/mx1/micro-x-limited,"	61971000",0.12,0.00,0,"Health Care"
ASX:DZZF,"BetaShares Ethical Diversified High Growth ETF (ASX:DZZF)",https://www.listcorp.com/asx/dzzf/betashares-ethical-diversified-high-growth-etf,"	61748600",25.95,0.00,0,Financials
ASX:ASO,"Aston Minerals Limited (ASX:ASO)",https://www.listcorp.com/asx/aso/aston-minerals-limited,"	61223100",0.048,0.00,0,Materials
ASX:PTX,"Prescient Therapeutics Limited (ASX:PTX)",https://www.listcorp.com/asx/ptx/prescient-therapeutics-limited,"	61200500",0.076,0.00,0,"Health Care"
ASX:NVA,"Nova Minerals Limited (ASX:NVA)",https://www.listcorp.com/asx/nva/nova-minerals-limited,"	61158100",0.29,0.00,0,Materials
ASX:DBF,"Duxton Farms Ltd (ASX:DBF)",https://www.listcorp.com/asx/dbf/duxton-farms-ltd,"	61072100",1.465,0.00,0,"Consumer Staples"
ASX:AVD,"AVADA Group Limited (ASX:AVD)",https://www.listcorp.com/asx/avd/avada-group-limited,"	60812700",0.83,0.00,0,Industrials
ASX:PH2,"Pure Hydrogen Corporation Limited (ASX:PH2)",https://www.listcorp.com/asx/ph2/pure-hydrogen-corporation-limited,"	60377600",0.17,0.00,0,Energy
ASX:BRK,"Brookside Energy Limited (ASX:BRK)",https://www.listcorp.com/asx/brk/brookside-energy-limited,"	60174500",0.012,0.00,0,Energy
ASX:OIL,"Optiscan Imaging Limited (ASX:OIL)",https://www.listcorp.com/asx/oil/optiscan-imaging-limited,"	60122900",0.072,0.00,0,"Health Care"
ASX:AZL,"Arizona Lithium Limited (ASX:AZL)",https://www.listcorp.com/asx/azl/arizona-lithium-limited,"	60096800",0.019,0.00,0,Materials
ASX:NRZ,"NeuRizer Ltd (ASX:NRZ)",https://www.listcorp.com/asx/nrz/neurizer-ltd,"	59933100",0.048,0.00,0,Materials
ASX:GDA,"Good Drinks Australia Ltd (ASX:GDA)",https://www.listcorp.com/asx/gda/good-drinks-australia-ltd,"	59677300",0.465,0.00,0,"Consumer Staples"
ASX:CD2,"Cordish Dixon Private Equity Fund II (ASX:CD2)",https://www.listcorp.com/asx/cd2/cordish-dixon-private-equity-fund-ii,"	59563800",1.135,0.00,0,Financials
ASX:AIM,"Ai-Media Technologies Limited (ASX:AIM)",https://www.listcorp.com/asx/aim/ai-media-technologies-limited,"	59351000",0.285,0.00,0,Industrials
ASX:LEL,"Lithium Energy Limited (ASX:LEL)",https://www.listcorp.com/asx/lel/lithium-energy-limited,"	59230800",0.575,0.00,0,Materials
ASX:PRT,"PRT Company Limited (ASX:PRT)",https://www.listcorp.com/asx/prt/prt-company-limited,"	58938900",0.16089,0.00,0,"Communication Services"
ASX:AVC,"Auctus Investment Group Limited (ASX:AVC)",https://www.listcorp.com/asx/avc/auctus-investment-group-limited,"	58914800",0.78,0.00,0,Financials
ASX:MCE,"Matrix Composites & Engineering Ltd (ASX:MCE)",https://www.listcorp.com/asx/mce/matrix-composites-and-engineering-ltd,"	58899500",0.27,0.00,0,Energy
ASX:BMT,"Beamtree Holdings Limited (ASX:BMT)",https://www.listcorp.com/asx/bmt/beamtree-holdings-limited,"	58603900",0.22,0.00,0,"Health Care"
ASX:3DA,"Amaero International Ltd (ASX:3DA)",https://www.listcorp.com/asx/3da/amaero-international-ltd,"	58358300",0.14,0.00,0,Industrials
ASX:XASG,"Alphinity Global Sustainable Equity Fund (Managed Fund) (ASX:XASG)",https://www.listcorp.com/asx/xasg/alphinity-global-sustainable-equity-fund-managed-fund,"	58073300",5.85,0.00,0,Financials
ASX:VMT,"VMoto Limited (ASX:VMT)",https://www.listcorp.com/asx/vmt/vmoto,"	58048100",0.2,0.00,0,"Consumer Discretionary"
ASX:WIN,"Widgie Nickel Limited (ASX:WIN)",https://www.listcorp.com/asx/win/widgie-nickel-limited,"	58015800",0.195,0.00,0,Materials
ASX:CUP,"Count Limited (ASX:CUP)",https://www.listcorp.com/asx/cup/count-limited,"	57995000",0.52,0.00,0,Industrials
ASX:MCM,"MC Mining Limited (ASX:MCM)",https://www.listcorp.com/asx/mcm/mc-mining-limited,"	57951500",0.145,0.00,0,Energy
ASX:LKO,"Lakes Blue Energy NL (ASX:LKO)",https://www.listcorp.com/asx/lko/lakes-blue-energy,"	57825100",0.001,0.00,0,Energy
ASX:AXN,"Alliance Nickel Limited (ASX:AXN)",https://www.listcorp.com/asx/axn/alliance-nickel-limited,"	57761600",0.081,0.00,0,Materials
ASX:NDIA,"Global X India Nifty 50 ETF (ASX:NDIA)",https://www.listcorp.com/asx/ndia/global-x-india-nifty-50-etf,"	57731800",66.01,0.00,0,Financials
ASX:AZY,"Antipa Minerals Limited (ASX:AZY)",https://www.listcorp.com/asx/azy/antipa-minerals,"	57552800",0.016,0.00,0,Materials
ASX:SPL,"Starpharma Holdings Limited (ASX:SPL)",https://www.listcorp.com/asx/spl/starpharma-holdings,"	57469000",0.14,0.00,0,"Health Care"
ASX:PVE,"Po Valley Energy Limited (ASX:PVE)",https://www.listcorp.com/asx/pve/po-valley-energy,"	57368600",0.0495,0.00,0,Energy
ASX:FML,"Focus Minerals Limited (ASX:FML)",https://www.listcorp.com/asx/fml/focus-minerals-limited,"	57311700",0.2,0.00,0,Materials
ASX:TNC,"True North Copper Limited (ASX:TNC)",https://www.listcorp.com/asx/tnc/true-north-copper-limited,"	57165100",0.22,0.00,0,Materials
ASX:GROW,"Schroder Real Return (Managed Fund) (ASX:GROW)",https://www.listcorp.com/asx/grow/schroder-real-return-managed-fund,"	57150700",3.48,0.00,0,Financials
ASX:SWP,"Swoop Holdings Limited (ASX:SWP)",https://www.listcorp.com/asx/swp/swoop-holdings-limited,"	56959100",0.275,0.00,0,"Communication Services"
ASX:SB2,"Salter Brothers Emerging Companies Limited (ASX:SB2)",https://www.listcorp.com/asx/sb2/salter-brothers-emerging-companies-limited,"	56864200",0.615,0.00,0,Financials
ASX:BSX,"Blackstone Minerals Limited (ASX:BSX)",https://www.listcorp.com/asx/bsx/blackstone-minerals-limited,"	56842700",0.12,0.00,0,Materials
ASX:WAK,"WA Kaolin Limited (ASX:WAK)",https://www.listcorp.com/asx/wak/wa-kaolin-limited,"	56553300",0.145,0.00,0,Materials
ASX:ICI,"iCandy Interactive Limited (ASX:ICI)",https://www.listcorp.com/asx/ici/icandy-interactive-limited,"	56372600",0.042,0.00,0,"Communication Services"
ASX:PPG,"Pro-Pac Packaging Limited (ASX:PPG)",https://www.listcorp.com/asx/ppg/pro-pac-packaging-limited,"	56323200",0.31,0.00,0,Materials
ASX:NGY,"NuEnergy Gas Limited (ASX:NGY)",https://www.listcorp.com/asx/ngy/nuenergy-gas-limited,"	56276300",0.038,0.00,0,Energy
ASX:MEK,"Meeka Metals Limited (ASX:MEK)",https://www.listcorp.com/asx/mek/meeka-metals-limited,"	56212700",0.051,0.00,0,Materials
ASX:LOM,"Lucapa Diamond Company (ASX:LOM)",https://www.listcorp.com/asx/lom/lucapa-diamond,"	56142800",0.039,0.00,0,Materials
ASX:BRU,"Buru Energy Limited (ASX:BRU)",https://www.listcorp.com/asx/bru/buru-energy,"	56028000",0.094,0.00,0,Energy
ASX:SIO,"Simonds Group Limited (ASX:SIO)",https://www.listcorp.com/asx/sio/simonds-group-limited,"	55785500",0.155,0.00,0,"Consumer Discretionary"
ASX:APW,"AIMS Property Securities Fund (ASX:APW)",https://www.listcorp.com/asx/apw/aims-property-securities-fund,"	55648900",1.25,0.00,0,"Real Estate"
ASX:RINC,"BetaShares Martin Currie Real Income Fund (managed fund) (ASX:RINC)",https://www.listcorp.com/asx/rinc/betashares-martin-currie-real-income-fund-managed-fund,"	55482700",8.36,0.00,0,Financials
ASX:EMKT,"VanEck MSCI Multifactor Emerging Markets Equity ETF (ASX:EMKT)",https://www.listcorp.com/asx/emkt/vaneck-msci-multifactor-emerging-markets-equity-etf,"	55319400",21.2,0.00,0,Financials
ASX:EPY,"Earlypay Ltd (ASX:EPY)",https://www.listcorp.com/asx/epy/earlypay-ltd,"	55086500",0.19,0.00,0,Financials
ASX:TZN,"Terramin Australia Limited (ASX:TZN)",https://www.listcorp.com/asx/tzn/terramin-australia-limited,"	55030600",0.026,0.00,0,Materials
ASX:MNRS,"BetaShares Global Gold Miners ETF - Currency Hedged (ASX:MNRS)",https://www.listcorp.com/asx/mnrs/betashares-global-gold-miners-etf-currency-hedged,"	54734100",5.1,0.00,0,Financials
ASX:LLI,"Loyal Lithium Limited (ASX:LLI)",https://www.listcorp.com/asx/lli/loyal-lithium-limited,"	54715800",0.75,0.00,0,Materials
ASX:MEC,"Morphic Ethical Equities Fund (ASX:MEC)",https://www.listcorp.com/asx/mec/morphic-ethical-equities-fund,"	54397500",1.065,0.00,0,Financials
ASX:PGL,"Prospa Group Limited (ASX:PGL)",https://www.listcorp.com/asx/pgl/prospa-group-limited,"	53913900",0.33,0.00,0,Financials
ASX:GLIN,"AMP Cap Global Infrastructure Securities Fund (ASX:GLIN)",https://www.listcorp.com/asx/glin/amp-cap-global-infrastructure-securities-fund,"	53912000",23.44,0.00,0,Financials
ASX:MWY,"Midway Limited (ASX:MWY)",https://www.listcorp.com/asx/mwy/midway-limited,"	53711800",0.615,0.00,0,Materials
ASX:TGA,"Thorn Group Limited (ASX:TGA)",https://www.listcorp.com/asx/tga/thorn-group,"	53536600",1.54,0.00,0,"Consumer Discretionary"
ASX:WAA,"WAM Active Limited (ASX:WAA)",https://www.listcorp.com/asx/waa/wam-active,"	53298500",0.71,0.00,0,Financials
ASX:AUMF,"iShares Edge MSCI Australia Multifactor ETF (ASX:AUMF)",https://www.listcorp.com/asx/aumf/ishares-edge-msci-australia-multifactor-etf,"	53291300",29.23,0.00,0,Financials
ASX:EAFZ,"Ellerston Asia Growth Fund (Hedge Fund) (ASX:EAFZ)",https://www.listcorp.com/asx/eafz/ellerston-asia-growth-fund-hedge-fund,"	53287000",6.21,0.00,0,Financials
ASX:CAN,"Cann Group Limited (ASX:CAN)",https://www.listcorp.com/asx/can/cann-group-limited,"	53225500",0.125,0.00,0,"Health Care"
ASX:SDV,"SciDev Limited (ASX:SDV)",https://www.listcorp.com/asx/sdv/scidev-limited,"	53145000",0.28,0.00,0,Materials
ASX:UBI,"Universal Biosensors Inc (ASX:UBI)",https://www.listcorp.com/asx/ubi/universal-biosensors,"	53092400",0.25,0.00,0,"Health Care"
ASX:VML,"Vital Metals Limited (ASX:VML)",https://www.listcorp.com/asx/vml/vital-metals-limited,"	53061500",0.01,0.00,0,Materials
ASX:MBH,"Maggie Beer Holdings Limited (ASX:MBH)",https://www.listcorp.com/asx/mbh/maggie-beer-holdings-limited,"	52866000",0.15,0.00,0,"Consumer Staples"
ASX:IBC,"Ironbark Capital Limited (ASX:IBC)",https://www.listcorp.com/asx/ibc/ironbark-capital-limited,"	52597500",0.48,0.00,0,Financials
ASX:CE1,"Calima Energy Limited (ASX:CE1)",https://www.listcorp.com/asx/ce1/calima-energy-limited,"	52560500",0.084,0.00,0,Energy
ASX:ODA,"Orcoda Limited (ASX:ODA)",https://www.listcorp.com/asx/oda/orcoda-limited,"	52438700",0.31,0.00,0,"Information Technology"
ASX:AVA,"Ava Risk Group Limited (ASX:AVA)",https://www.listcorp.com/asx/ava/ava-risk-group-limited,"	52360000",0.205,0.00,0,"Information Technology"
ASX:AFA,"ASF Group Limited (ASX:AFA)",https://www.listcorp.com/asx/afa/asf-group-limited,"	52298200",0.066,0.00,0,Financials
ASX:CXM,"Centrex Limited (ASX:CXM)",https://www.listcorp.com/asx/cxm/centrex-limited,"	52235000",0.085,0.00,0,Materials
ASX:CLDD,"BetaShares Cloud Computing ETF (ASX:CLDD)",https://www.listcorp.com/asx/cldd/betashares-cloud-computing-etf,"	52193700",11.79,0.00,0,Financials
ASX:WSP,"Whispir Limited (ASX:WSP)",https://www.listcorp.com/asx/wsp/whispir-limited,"	52006100",0.44,0.00,0,"Information Technology"
ASX:3MF,"3D Metalforge Limited (ASX:3MF)",https://www.listcorp.com/asx/3mf/3d-metalforge-limited,"	52000000",0.26,0.00,0,Industrials
ASX:KRM,"Kingsrose Mining (ASX:KRM)",https://www.listcorp.com/asx/krm/kingsrose-mining,"	51924300",0.069,0.00,0,Materials
ASX:BEAR,"BetaShares Australian Equities Bear Hedge Fund (ASX:BEAR)",https://www.listcorp.com/asx/bear/betashares-australian-equities-bear-hedge-fund,"	51863900",8.65,0.00,0,Financials
ASX:AR1,"Austral Resources Australia Ltd (ASX:AR1)",https://www.listcorp.com/asx/ar1/austral-resources-australia,"	51785500",0.16,0.00,0,Materials
ASX:NHE,"Noble Helium Limited (ASX:NHE)",https://www.listcorp.com/asx/nhe/noble-helium-limited,"	51675900",0.2,0.00,0,Energy
ASX:FFI,"FFI Holdings Limited (ASX:FFI)",https://www.listcorp.com/asx/ffi/ffi-holdings-limited,"	51649800",4.8,0.00,0,"Consumer Staples"
ASX:CAF,"Centrepoint Alliance Limited (ASX:CAF)",https://www.listcorp.com/asx/caf/centrepoint-alliance-limited,"	51449300",0.26,0.00,0,Financials
ASX:RDN,"Raiden Resources Limited (ASX:RDN)",https://www.listcorp.com/asx/rdn/raiden-resources-limited,"	51381700",0.025,0.00,0,Materials
ASX:EBG,"Eumundi Group Limited (ASX:EBG)",https://www.listcorp.com/asx/ebg/eumundi-group-limited,"	51376500",1.13,0.00,0,"Consumer Discretionary"
ASX:MME,"MoneyMe Limited (ASX:MME)",https://www.listcorp.com/asx/mme/moneyme-limited,"	51205000",0.064,0.00,0,Financials
ASX:LGP,"Little Green Pharma Ltd (ASX:LGP)",https://www.listcorp.com/asx/lgp/little-green-pharma,"	50930000",0.17,0.00,0,"Health Care"
ASX:CY5,"Cygnus Metals Limited (ASX:CY5)",https://www.listcorp.com/asx/cy5/cygnus-metals-limited,"	50863000",0.21,0.00,0,Materials
ASX:PSC,"Prospect Resources Limited (ASX:PSC)",https://www.listcorp.com/asx/psc/prospect-resources-limited,"	50848500",0.11,0.00,0,Materials
ASX:KLL,"Kalium Lakes Limited (ASX:KLL)",https://www.listcorp.com/asx/kll/kalium-lakes-limited,"	50792800",0.025,0.00,0,Materials
ASX:NCC,"NAOS Emerging Opportunities Company (ASX:NCC)",https://www.listcorp.com/asx/ncc/naos-emerging-opportunities-company,"	50702200",0.695,0.00,0,Financials
ASX:WRLD,"BetaShares Managed Risk Global Share Fund (managed fund) (ASX:WRLD)",https://www.listcorp.com/asx/wrld/betashares-managed-risk-global-share-fund-managed-fund,"	50684100",15.52,0.00,0,Financials
ASX:AAR,"Astral Resources NL (ASX:AAR)",https://www.listcorp.com/asx/aar/astral-resources-nl,"	50553200",0.066,0.00,0,Materials
ASX:FBM,"Future Battery Minerals Limited (ASX:FBM)",https://www.listcorp.com/asx/fbm/future-battery-minerals-limited,"	50088600",0.11,0.00,0,Materials
ASX:EMN,"Euro Manganese Inc (ASX:EMN)",https://www.listcorp.com/asx/emn/euro-manganese-inc,"	49793000",0.2,0.00,0,Materials
ASX:IMB,"Intelligent Monitoring Group Limited (ASX:IMB)",https://www.listcorp.com/asx/imb/intelligent-monitoring-group-limited,"	49496800",0.205,0.00,0,Industrials
ASX:AHC,"Austco Healthcare Limited (ASX:AHC)",https://www.listcorp.com/asx/ahc/austco-healthcare-limited,"	49434300",0.17,0.00,0,"Health Care"
ASX:DNA,"Donaco International Limited (ASX:DNA)",https://www.listcorp.com/asx/dna/donaco-international-limited,"	49415600",0.04,0.00,0,"Consumer Discretionary"
ASX:BOL,"Boom Logistics Limited (ASX:BOL)",https://www.listcorp.com/asx/bol/boom-logistics-limited,"	49194000",0.115,0.00,0,Industrials
ASX:BBT,"BlueBet Holdings Limited (ASX:BBT)",https://www.listcorp.com/asx/bbt/bluebet-holdings-limited,"	49064000",0.245,0.00,0,"Consumer Discretionary"
ASX:IHEB,"iShares JP Morgan USD Emerging Mkt Bnd AUD Hdg ETF (ASX:IHEB)",https://www.listcorp.com/asx/iheb/ishares-jp-morgan-usd-emerging-mkt-bnd-aud-hdg-etf,"	49039600",72.97,0.00,0,Financials
ASX:ACW,"Actinogen Medical Limited (ASX:ACW)",https://www.listcorp.com/asx/acw/actinogen-medical-limited,"	49038800",0.027,0.00,0,"Health Care"
ASX:LIT,"Lithium Australia Limited (ASX:LIT)",https://www.listcorp.com/asx/lit/lithium-australia-limited,"	48887700",0.04,0.00,0,Industrials
ASX:MVS,"Vaneck Vectors Small Companies Masters ETF (ASX:MVS)",https://www.listcorp.com/asx/mvs/vaneck-vectors-small-companies-masters-etf,"	48882400",18.17,0.00,0,Financials
ASX:TPC,"TPC Consolidated Limited (ASX:TPC)",https://www.listcorp.com/asx/tpc/tpc-consolidated-limited,"	48774300",4.3,0.00,0,Utilities
ASX:BBC,"BNK Banking Corporation Limited (ASX:BBC)",https://www.listcorp.com/asx/bbc/bnk-banking-corporation,"	48675000",0.41,0.00,0,Financials
ASX:RSM,"Russell Investments Australian Semi-Government Bond ETF (ASX:RSM)",https://www.listcorp.com/asx/rsm/russell-investments-australian-semi-government-bond-etf,"	48636300",19.17,0.00,0,Financials
ASX:AQC,"Australian Pacific Coal Limited (ASX:AQC)",https://www.listcorp.com/asx/aqc/australian-pacific-coal-limited,"	48623500",0.14,0.00,0,Materials
ASX:USQ,"US Student Housing REIT (ASX:USQ)",https://www.listcorp.com/asx/usq/us-student-housing-reit,"	48598600",0.875,0.00,0,"Real Estate"
ASX:PRL,"Province Resources Limited (ASX:PRL)",https://www.listcorp.com/asx/prl/province-resources-limited,"	48441200",0.041,0.00,0,Materials
ASX:SEG,"Sports Entertainment Group Limited (ASX:SEG)",https://www.listcorp.com/asx/seg/sports-entertainment-group-limited,"	48305700",0.185,0.00,0,"Communication Services"
ASX:TOE,"Toro Energy Limited (ASX:TOE)",https://www.listcorp.com/asx/toe/toro-energy-limited,"	47947800",0.011,0.00,0,Energy
ASX:ANP,"Antisense Therapeutics Limited (ASX:ANP)",https://www.listcorp.com/asx/anp/antisense-therapeutics-limited,"	47781900",0.053,0.00,0,"Health Care"
ASX:AKM,"Aspire Mining Limited (ASX:AKM)",https://www.listcorp.com/asx/akm/aspire-mining-limited,"	47717900",0.094,0.00,0,Materials
ASX:TI1,"Tombador Iron Limited (ASX:TI1)",https://www.listcorp.com/asx/ti1/tombador-iron-limited,"	47459100",0.022,0.00,0,Materials
ASX:HGEN,"Global X Hydrogen ETF (ASX:HGEN)",https://www.listcorp.com/asx/hgen/global-x-hydrogen-etf,"	47347900",6.38,0.00,0,Financials
ASX:PFG,"Prime Financial (ASX:PFG)",https://www.listcorp.com/asx/pfg/prime-financial,"	47236800",0.23,0.00,0,Financials
ASX:KIN,"Kin Mining NL (ASX:KIN)",https://www.listcorp.com/asx/kin/kin-mining,"	47126000",0.04,0.00,0,Materials
ASX:ARV,"Artemis Resources Limited (ASX:ARV)",https://www.listcorp.com/asx/arv/artemis-resources-limited,"	47097600",0.03,0.00,0,Materials
ASX:KYP,"Kinatico Limited (ASX:KYP)",https://www.listcorp.com/asx/kyp/kinatico-limited,"	47091600",0.1125,0.00,0,"Information Technology"
ASX:NC1,"NiCo Resources Limited (ASX:NC1)",https://www.listcorp.com/asx/nc1/nico-resources-limited,"	47039900",0.535,0.00,0,Materials
ASX:RLT,"Renergen Limited (ASX:RLT)",https://www.listcorp.com/asx/rlt/renergen-limited,"	47005300",1.55,0.00,0,Energy
ASX:HMX,"Hammer Metals Limited (ASX:HMX)",https://www.listcorp.com/asx/hmx/hammer-metals-limited,"	46979600",0.053,0.00,0,Materials
ASX:FSI,"Flagship Investments (ASX:FSI)",https://www.listcorp.com/asx/fsi/flagship-investments,"	46801600",1.81,0.00,0,Financials
ASX:CUE,"Cue Energy Resources Limited (ASX:CUE)",https://www.listcorp.com/asx/cue/cue-energy-resources-limited,"	46774000",0.067,0.00,0,Energy
ASX:WOA,"Wide Open Agriculture Ltd (ASX:WOA)",https://www.listcorp.com/asx/woa/wide-open-agriculture-ltd,"	46566600",0.325,0.00,0,"Consumer Staples"
ASX:LDX,"Lumos Diagnostics Holdings Limited (ASX:LDX)",https://www.listcorp.com/asx/ldx/lumos-diagnostics-holdings-limited,"	46561500",0.105,0.00,0,"Health Care"
ASX:WZR,"Wisr Limited (ASX:WZR)",https://www.listcorp.com/asx/wzr/wisr-limited,"	46305400",0.034,0.00,0,Financials
ASX:WCG,"Webcentral Limited (ASX:WCG)",https://www.listcorp.com/asx/wcg/webcentral-limited,"	46077700",0.14,0.00,0,"Information Technology"
ASX:FEG,"Far East Gold Ltd (ASX:FEG)",https://www.listcorp.com/asx/feg/far-east-gold-ltd,"	46054600",0.255,0.00,0,Materials
ASX:RZI,"Raiz Invest Limited (ASX:RZI)",https://www.listcorp.com/asx/rzi/raiz-invest-limited,"	45788300",0.49,0.00,0,Financials
ASX:EYE,"Nova Eye Medical Limited (ASX:EYE)",https://www.listcorp.com/asx/eye/nova-eye-medical-limited,"	45747600",0.24,0.00,0,"Health Care"
ASX:AHI,"Advanced Health Intelligence Ltd (ASX:AHI)",https://www.listcorp.com/asx/ahi/advanced-health-intelligence-ltd,"	45717800",0.21,0.00,0,"Health Care"
ASX:TIP,"Teaminvest Private Group Limited (ASX:TIP)",https://www.listcorp.com/asx/tip/teaminvest-private-group-limited,"	45471600",0.335,0.00,0,Financials
ASX:OPY,"Openpay Group Ltd (ASX:OPY)",https://www.listcorp.com/asx/opy/openpay-group-ltd,"	45403900",0.195,0.00,0,Financials
ASX:PAM,"Pan Asia Metals Limited (ASX:PAM)",https://www.listcorp.com/asx/pam/pan-asia-metals-limited,"	45264100",0.285,0.00,0,Materials
ASX:EDC,"Eildon Capital Limited (ASX:EDC)",https://www.listcorp.com/asx/edc/eildon-capital-limited,"	45248300",0.925,0.00,0,Financials
ASX:BGD,"Barton Gold Holdings Limited (ASX:BGD)",https://www.listcorp.com/asx/bgd/barton-gold-holdings-limited,"	44915900",0.23,0.00,0,Materials
ASX:PRO,"Prophecy International (ASX:PRO)",https://www.listcorp.com/asx/pro/prophecy-international,"	44905700",0.61,0.00,0,"Information Technology"
ASX:FGR,"First Graphene Limited (ASX:FGR)",https://www.listcorp.com/asx/fgr/first-graphene-limited,"	44855600",0.076,0.00,0,Materials
ASX:RR1,"Reach Resources Limited (ASX:RR1)",https://www.listcorp.com/asx/rr1/reach-resources-limited,"	44170700",0.014,0.00,0,Materials
ASX:AIQ,"Alternative Investment Trust (ASX:AIQ)",https://www.listcorp.com/asx/aiq/alternative-investment-trust,"	44010100",1.39,0.00,0,Financials
ASX:LIS,"Li-S Energy Limited (ASX:LIS)",https://www.listcorp.com/asx/lis/li-s-energy-limited,"	43967300",0.265,0.00,0,Industrials
ASX:CCA,"Change Financial Limited (ASX:CCA)",https://www.listcorp.com/asx/cca/change-financial-limited,"	43936300",0.07,0.00,0,Financials
ASX:ADA,"Adacel Technologies Limited (ASX:ADA)",https://www.listcorp.com/asx/ada/adacel-technologies-limited,"	43829400",0.575,0.00,0,"Information Technology"
ASX:HMY,"Harmoney Corp Limited (ASX:HMY)",https://www.listcorp.com/asx/hmy/harmoney-corp-limited,"	43668900",0.43,0.00,0,Financials
ASX:MYE,"Metarock Group Limited (ASX:MYE)",https://www.listcorp.com/asx/mye/metarock-group-limited,"	43643700",0.145,0.00,0,Materials
ASX:TAM,"Tanami Gold NL (ASX:TAM)",https://www.listcorp.com/asx/tam/tanami-gold,"	43478600",0.037,0.00,0,Materials
ASX:QMIX,"SPDR MSCI World Quality Mix Fund (ASX:QMIX)",https://www.listcorp.com/asx/qmix/spdr-msci-world-quality-mix-fund,"	43458100",26.75,0.00,0,Financials
ASX:POL,"Polymetals Resources Ltd (ASX:POL)",https://www.listcorp.com/asx/pol/polymetals-resources,"	43113800",0.29,0.00,0,Materials
ASX:CTP,"Central Petroleum Limited (ASX:CTP)",https://www.listcorp.com/asx/ctp/central-petroleum-limited,"	43034900",0.059,0.00,0,Energy
ASX:DUB,"Dubber Corporation Limited (ASX:DUB)",https://www.listcorp.com/asx/dub/dubber-corporation,"	42900800",0.12,0.00,0,"Information Technology"
ASX:VR1,"Vection Technologies Ltd (ASX:VR1)",https://www.listcorp.com/asx/vr1/vection-technologies,"	42810400",0.038,0.00,0,"Information Technology"
ASX:BNKS,"BetaShares Global Banks  ETF  Currency Hedged (ASX:BNKS)",https://www.listcorp.com/asx/bnks/betashares-global-banks-etf-currency-hedged,"	42653100",5.97,0.00,0,Financials
ASX:ALA,"Arovella Therapeutics Limited (ASX:ALA)",https://www.listcorp.com/asx/ala/arovella-therapeutics-limited,"	42392300",0.047,0.00,0,"Health Care"
ASX:SXG,"Southern Cross Gold Ltd (ASX:SXG)",https://www.listcorp.com/asx/sxg/southern-cross-gold-ltd,"	42326100",0.47,0.00,0,Materials
ASX:MGL,"Magontec Limited (ASX:MGL)",https://www.listcorp.com/asx/mgl/magontec-limited,"	42287700",0.54,0.00,0,Materials
ASX:BNZ,"Benz Mining Corp (ASX:BNZ)",https://www.listcorp.com/asx/bnz/benz-mining-corp,"	42128900",0.38,0.00,0,Materials
ASX:LRT,"Lowell Resources Fund (ASX:LRT)",https://www.listcorp.com/asx/lrt/lowell-resources-fund,"	42123700",1.3,0.00,0,Financials
ASX:ELS,"Elsight Limited (ASX:ELS)",https://www.listcorp.com/asx/els/elsight-limited,"	42089500",0.28,0.00,0,"Information Technology"
ASX:SOR,"Strategic Elements Ltd (ASX:SOR)",https://www.listcorp.com/asx/sor/strategic-elements,"	42011700",0.094,0.00,0,Financials
ASX:INF,"Infinity Lithium Corporation Limited (ASX:INF)",https://www.listcorp.com/asx/inf/infinity-lithium-corporation-limited,"	41633300",0.09,0.00,0,Materials
ASX:BSA,"BSA Limited (ASX:BSA)",https://www.listcorp.com/asx/bsa/bsa-limited,"	41475200",0.58,0.00,0,Industrials
ASX:IMPQ,"eInvest Future Impact Small Caps Fund (ASX:IMPQ)",https://www.listcorp.com/asx/impq/einvest-future-impact-small-caps-fund,"	41442200",4.79,0.00,0,Financials
ASX:STG,"Straker Limited (ASX:STG)",https://www.listcorp.com/asx/stg/straker-limited,"	41382000",0.61,0.00,0,Industrials
ASX:HRN,"Horizon Gold Limited (ASX:HRN)",https://www.listcorp.com/asx/hrn/horizon-gold-limited,"	41309900",0.33,0.00,0,Materials
ASX:BNL,"Blue Star Helium Limited (ASX:BNL)",https://www.listcorp.com/asx/bnl/blue-star-helium-limited,"	41240400",0.026,0.00,0,Energy
ASX:QFN,"BetaShares Australian Financials Sector ETF (ASX:QFN)",https://www.listcorp.com/asx/qfn/betashares-australian-financials-sector-etf,"	41056800",11.62,0.00,0,Financials
ASX:RFX,"RedFlow Limited (ASX:RFX)",https://www.listcorp.com/asx/rfx/redflow-limited,"	40607800",0.2,0.00,0,Industrials
ASX:E200,"SPDR S&P/ASX ESG 200 FUND (ASX:E200)",https://www.listcorp.com/asx/e200/spdr-s-and-p-asx-esg-200-fund,"	40604200",22.7,0.00,0,Financials
ASX:NAC,"NAOS Absolute Opportunities Company (ASX:NAC)",https://www.listcorp.com/asx/nac/naos-absolute-opportunities-company,"	40574100",0.935,0.00,0,Financials
ASX:MTC,"MetalsTech Limited (ASX:MTC)",https://www.listcorp.com/asx/mtc/metalstech-limited,"	40550000",0.215,0.00,0,Materials
ASX:HAW,"Hawthorn Resources Limited (ASX:HAW)",https://www.listcorp.com/asx/haw/hawthorn-resources,"	40201900",0.12,0.00,0,Materials
ASX:IPT,"Impact Minerals Limited (ASX:IPT)",https://www.listcorp.com/asx/ipt/impact-minerals-limited,"	40105900",0.014,0.00,0,Materials
ASX:BWX,"BWX Limited (ASX:BWX)",https://www.listcorp.com/asx/bwx/bwx-limited,"	39997500",0.2,0.00,0,"Consumer Staples"
ASX:VRS,"Veris Limited (ASX:VRS)",https://www.listcorp.com/asx/vrs/veris-limited,"	39996200",0.078,0.00,0,Industrials
ASX:CNW,"Cirrus Networks Holdings Limited (ASX:CNW)",https://www.listcorp.com/asx/cnw/cirrus-networks-holdings-limited,"	39990300",0.043,0.00,0,"Information Technology"
ASX:KSN,"Kingston Resources Limited (ASX:KSN)",https://www.listcorp.com/asx/ksn/kingston-resources,"	39836900",0.08,0.00,0,Materials
ASX:AGN,"Argenica Therapeutics Limited (ASX:AGN)",https://www.listcorp.com/asx/agn/argenica-therapeutics-limited,"	39660300",0.4,0.00,0,"Health Care"
ASX:1MC,"Morella Corporation Limited (ASX:1MC)",https://www.listcorp.com/asx/1mc/morella-corporation-limited,"	39640800",0.0065,0.00,0,Materials
ASX:ESK,"Etherstack Plc (ASX:ESK)",https://www.listcorp.com/asx/esk/etherstack-plc,"	39527100",0.3,0.00,0,"Information Technology"
ASX:TSI,"Top Shelf International Holdings Ltd (ASX:TSI)",https://www.listcorp.com/asx/tsi/top-shelf-international-holdings-ltd,"	39415200",0.2,0.00,0,"Consumer Staples"
ASX:DGH,"Desane Group Holdings Limited (ASX:DGH)",https://www.listcorp.com/asx/dgh/desane-group-holdings-limited,"	39273600",0.96,0.00,0,"Real Estate"
ASX:JGH,"Jade Gas Holdings Limited (ASX:JGH)",https://www.listcorp.com/asx/jgh/jade-gas-holdings-limited,"	39242000",0.039,0.00,0,Energy
ASX:XF1,"Xref Limited (ASX:XF1)",https://www.listcorp.com/asx/xf1/xref-limited,"	39097000",0.21,0.00,0,"Information Technology"
ASX:RMY,"RMA Global Limited (ASX:RMY)",https://www.listcorp.com/asx/rmy/rma-global-limited,"	39056000",0.07,0.00,0,"Communication Services"
ASX:NOV,"Novatti Group Limited (ASX:NOV)",https://www.listcorp.com/asx/nov/novatti-group-limited,"	38945500",0.115,0.00,0,"Information Technology"
ASX:PCK,"PainChek Ltd (ASX:PCK)",https://www.listcorp.com/asx/pck/painchek-ltd,"	38939700",0.03,0.00,0,"Health Care"
ASX:GAS,"State Gas Limited (ASX:GAS)",https://www.listcorp.com/asx/gas/state-gas-limited,"	38879000",0.155,0.00,0,Energy
ASX:NTI,"Neurotech International Limited (ASX:NTI)",https://www.listcorp.com/asx/nti/neurotech-international-limited,"	38452000",0.044,0.00,0,"Health Care"
ASX:MPX,"Mustera Property Group Limited (ASX:MPX)",https://www.listcorp.com/asx/mpx/mustera-property-group-limited,"	38222300",0.265,0.00,0,"Real Estate"
ASX:RTG,"RTG Mining (ASX:RTG)",https://www.listcorp.com/asx/rtg/rtg-mining,"	38194500",0.038,0.00,0,Materials
ASX:MYG,"Mayfield Group Holdings Limited (ASX:MYG)",https://www.listcorp.com/asx/myg/mayfield-group-holdings-limited,"	38038400",0.42,0.00,0,Industrials
ASX:DEM,"De.mem Limited (ASX:DEM)",https://www.listcorp.com/asx/dem/de.mem-limited,"	38002500",0.155,0.00,0,Utilities
ASX:FAR,"FAR Limited (ASX:FAR)",https://www.listcorp.com/asx/far/far,"	37888000",0.41,0.00,0,Energy
ASX:RVR,"Red River Resources Limited (ASX:RVR)",https://www.listcorp.com/asx/rvr/red-river-resources-limited,"	37847900",0.073,0.00,0,Materials
ASX:CURE,"Global X S&P Biotech ETF (ASX:CURE)",https://www.listcorp.com/asx/cure/global-x-s-and-p-biotech-etf,"	37706300",41.71,0.00,0,Financials
ASX:SWF,"SelfWealth Limited (ASX:SWF)",https://www.listcorp.com/asx/swf/selfwealth-limited,"	37681500",0.16,0.00,0,Financials
ASX:OAU,"Ora Gold Limited (ASX:OAU)",https://www.listcorp.com/asx/oau/ora-gold-limited,"	37518400",0.008,0.00,0,Materials
ASX:KAT,"Katana Capital (ASX:KAT)",https://www.listcorp.com/asx/kat/katana-capital,"	37438800",1.12,0.00,0,Financials
ASX:MMM,"Marley Spoon SE (ASX:MMM)",https://www.listcorp.com/asx/mmm/marley-spoon-se,"	37369200",0.095,0.00,0,"Consumer Staples"
ASX:SGQ,"St George Mining Limited (ASX:SGQ)",https://www.listcorp.com/asx/sgq/st-george-mining-limited,"	37249300",0.044,0.00,0,Materials
ASX:FAL,"Falcon Metals Limited (ASX:FAL)",https://www.listcorp.com/asx/fal/falcon-metals-limited,"	37170000",0.21,0.00,0,Materials
ASX:AME,"Alto Metals Limited (ASX:AME)",https://www.listcorp.com/asx/ame/alto-metals-limited,"	37138400",0.052,0.00,0,Materials
ASX:BWF,"Blackwall Limited (ASX:BWF)",https://www.listcorp.com/asx/bwf/blackwall-limited,"	37114100",0.55,0.00,0,Financials
ASX:REY,"Rey Resources Limited (ASX:REY)",https://www.listcorp.com/asx/rey/rey-resources-limited,"	37050600",0.175,0.00,0,Energy
ASX:BLU,"Blue Energy Limited (ASX:BLU)",https://www.listcorp.com/asx/blu/blue-energy,"	37019500",0.02,0.00,0,Energy
ASX:PNM,"Pacific Nickel Mines Limited (ASX:PNM)",https://www.listcorp.com/asx/pnm/pacific-nickel-mines-limited,"	36962600",0.09,0.00,0,Materials
ASX:VEN,"Vintage Energy Ltd (ASX:VEN)",https://www.listcorp.com/asx/ven/vintage-energy-ltd,"	36916300",0.043,0.00,0,Energy
ASX:BOND,"SPDR S&P/ASX Australian Bond Fund (ASX:BOND)",https://www.listcorp.com/asx/bond/spdr-s-and-p-asx-australian-bond-fund,"	36835600",24.11,0.00,0,Financials
ASX:SNS,"SenSen Networks Limited (ASX:SNS)",https://www.listcorp.com/asx/sns/sensen-networks-limited,"	36764000",0.054,0.00,0,"Information Technology"
ASX:XTE,"XTEK Limited (ASX:XTE)",https://www.listcorp.com/asx/xte/xtek,"	36634200",0.36,0.00,0,Industrials
ASX:DDB,"Dynamic Group Holdings Limited (ASX:DDB)",https://www.listcorp.com/asx/ddb/dynamic-group-holdings-limited,"	36633100",0.265,0.00,0,Industrials
ASX:DKM,"Duketon Mining Limited (ASX:DKM)",https://www.listcorp.com/asx/dkm/duketon-mining-limited,"	36627100",0.3,0.00,0,Materials
ASX:DGGF,"BetaShares Ethical Diversified Growth ETF (ASX:DGGF)",https://www.listcorp.com/asx/dggf/betashares-ethical-diversified-growth-etf,"	36557700",24.77,0.00,0,Financials
ASX:CZR,"CZR Resources Ltd (ASX:CZR)",https://www.listcorp.com/asx/czr/czr-resources-ltd,"	36538900",0.155,0.00,0,Materials
ASX:ERM,"Emmerson Resources Limited (ASX:ERM)",https://www.listcorp.com/asx/erm/emmerson-resources-limited,"	36495600",0.067,0.00,0,Materials
ASX:IAM,"Income Asset Management Group Limited (ASX:IAM)",https://www.listcorp.com/asx/iam/income-asset-management-group-limited,"	36402700",0.13,0.00,0,Financials
ASX:WA8,"Warriedar Resources Limited (ASX:WA8)",https://www.listcorp.com/asx/wa8/warriedar-resources-limited,"	36208900",0.084,0.00,0,Materials
ASX:PNC,"Pioneer Credit Limited (ASX:PNC)",https://www.listcorp.com/asx/pnc/pioneer-credit-limited,"	35822100",0.32,0.00,0,Financials
ASX:NUH,"Nuheara Limited (ASX:NUH)",https://www.listcorp.com/asx/nuh/nuheara-limited,"	35603800",0.175,0.00,0,"Information Technology"
ASX:TKM,"Trek Metals Limited (ASX:TKM)",https://www.listcorp.com/asx/tkm/trek-metals-limited,"	35504600",0.072,0.00,0,Materials
ASX:AR3,"Australian Rare Earths Limited (ASX:AR3)",https://www.listcorp.com/asx/ar3/australian-rare-earths-limited,"	35458200",0.23,0.00,0,Materials
ASX:VRC,"Volt Resources Limited (ASX:VRC)",https://www.listcorp.com/asx/vrc/volt-resources-limited,"	35454800",0.009,0.00,0,Materials
ASX:PUR,"Pursuit Minerals Limited (ASX:PUR)",https://www.listcorp.com/asx/pur/pursuit-minerals-limited,"	35327700",0.012,0.00,0,Materials
ASX:MRC,"Mineral Commodities Ltd (ASX:MRC)",https://www.listcorp.com/asx/mrc/mineral-commodities,"	35264300",0.051,0.00,0,Materials
ASX:MKAX,"Montaka Global Extension Fund (ASX:MKAX)",https://www.listcorp.com/asx/mkax/montaka-global-extension-fund,"	35258200",2.72,0.00,0,Financials
ASX:KME,"Kip McGrath Education Centres Limited (ASX:KME)",https://www.listcorp.com/asx/kme/kip-mcgrath-education,"	35131800",0.62,0.00,0,"Consumer Discretionary"
ASX:5GG,"Pentanet Limited (ASX:5GG)",https://www.listcorp.com/asx/5gg/pentanet-limited,"	35130400",0.094,0.00,0,"Communication Services"
ASX:WIA,"WIA Gold Limited (ASX:WIA)",https://www.listcorp.com/asx/wia/wia-gold-limited,"	34986000",0.038,0.00,0,Materials
ASX:WWI,"West Wits Mining Limited (ASX:WWI)",https://www.listcorp.com/asx/wwi/west-wits-mining,"	34819500",0.015,0.00,0,Materials
ASX:PV1,"Provaris Energy Ltd (ASX:PV1)",https://www.listcorp.com/asx/pv1/provaris-energy-ltd,"	34632900",0.063,0.00,0,Energy
ASX:GOAT,"VanEck Morningstar International Wide Moat ETF (ASX:GOAT)",https://www.listcorp.com/asx/goat/vaneck-morningstar-international-wide-moat-etf,"	34585300",25.53,0.00,0,Financials
ASX:92E,"92 Energy Limited (ASX:92E)",https://www.listcorp.com/asx/92e/92-energy-limited,"	34571900",0.325,0.00,0,Energy
ASX:RVT,"Richmond Vanadium Technology Limited (ASX:RVT)",https://www.listcorp.com/asx/rvt/richmond-vanadium-technology-limited,"	34483100",0.4,0.00,0,Materials
ASX:ADX,"ADX Energy Limited (ASX:ADX)",https://www.listcorp.com/asx/adx/adx-energy-limited,"	34403000",0.0095,0.00,0,Energy
ASX:TON,"Triton Minerals Limited (ASX:TON)",https://www.listcorp.com/asx/ton/triton-minerals-limited,"	34349800",0.022,0.00,0,Materials
ASX:KZA,"Kazia Therapeutics Limited (ASX:KZA)",https://www.listcorp.com/asx/kza/kazia-therapeutics-limited,"	34270700",0.145,0.00,0,"Health Care"
ASX:CBR,"Carbon Revolution Limited (ASX:CBR)",https://www.listcorp.com/asx/cbr/carbon-revolution-limited,"	33944400",0.16,0.00,0,"Consumer Discretionary"
ASX:SOV,"Sovereign Cloud Holdings Limited (ASX:SOV)",https://www.listcorp.com/asx/sov/sovereign-cloud-holdings,"	33940100",0.1,0.00,0,"Information Technology"
ASX:VR8,"Vanadium Resources Limited (ASX:VR8)",https://www.listcorp.com/asx/vr8/vanadium-resources-limited,"	33905100",0.063,0.00,0,Materials
ASX:WMG,"Western Mines Group Ltd (ASX:WMG)",https://www.listcorp.com/asx/wmg/western-mines-group-ltd,"	33769600",0.56,0.00,0,Materials
ASX:GRV,"Greenvale Energy Limited (ASX:GRV)",https://www.listcorp.com/asx/grv/greenvale-energy-limited,"	33755100",0.078,0.00,0,Energy
ASX:GW1,"Greenwing Resources Ltd (ASX:GW1)",https://www.listcorp.com/asx/gw1/greenwing-resources-ltd,"	33690300",0.195,0.00,0,Materials
ASX:DTC,"Damstra Holdings Limited (ASX:DTC)",https://www.listcorp.com/asx/dtc/damstra-holdings-limited,"	33511100",0.13,0.00,0,"Information Technology"
ASX:UBN,"Urbanise.com Limited (ASX:UBN)",https://www.listcorp.com/asx/ubn/urbanise.com-limited,"	33509400",0.525,0.00,0,"Information Technology"
ASX:MPA,"Mad Paws Holdings Limited (ASX:MPA)",https://www.listcorp.com/asx/mpa/mad-paws-holdings-limited,"	33407900",0.095,0.00,0,"Consumer Discretionary"
ASX:PWN,"Parkway Corporate Limited (ASX:PWN)",https://www.listcorp.com/asx/pwn/parkway-corporate-limited,"	33402300",0.015,0.00,0,Materials
ASX:DGR,"DGR Global Limited (ASX:DGR)",https://www.listcorp.com/asx/dgr/dgr-global-limited,"	33398200",0.032,0.00,0,Materials
ASX:GBR,"Great Boulder Resources Limited (ASX:GBR)",https://www.listcorp.com/asx/gbr/great-boulder-resources,"	33350400",0.066,0.00,0,Materials
ASX:AKG,"Academies Australasia (ASX:AKG)",https://www.listcorp.com/asx/akg/academies-australasia,"	33153600",0.25,0.00,0,"Consumer Discretionary"
ASX:DVR,"Diverger Limited (ASX:DVR)",https://www.listcorp.com/asx/dvr/diverger-limited,"	33153200",0.88,0.00,0,Financials
ASX:TBA,"Tombola Gold Ltd (ASX:TBA)",https://www.listcorp.com/asx/tba/tombola-gold-ltd,"	33129200",0.026,0.00,0,Materials
ASX:SOC,"SOCO Corporation Limited (ASX:SOC)",https://www.listcorp.com/asx/soc/soco-corporation-limited,"	33088200",0.26,0.00,0,"Information Technology"
ASX:HIO,"Hawsons Iron Limited (ASX:HIO)",https://www.listcorp.com/asx/hio/hawsons-iron-limited,"	33086600",0.036,0.00,0,Materials
ASX:PPL,"Pureprofile Limited (ASX:PPL)",https://www.listcorp.com/asx/ppl/pureprofile-limited,"	32866300",0.029,0.00,0,"Communication Services"
ASX:FSG,"Field Solutions Holdings Limited (ASX:FSG)",https://www.listcorp.com/asx/fsg/field-solutions-holdings-limited,"	32840900",0.043,0.00,0,"Communication Services"
ASX:AMX,"Aerometrex Limited (ASX:AMX)",https://www.listcorp.com/asx/amx/aerometrex-limited,"	32713500",0.345,0.00,0,Industrials
ASX:OMA,"Omega Oil and Gas Limited (ASX:OMA)",https://www.listcorp.com/asx/oma/omega-oil-and-gas-limited,"	32711800",0.185,0.00,0,Energy
ASX:RTE,"Retech Technology Co., Limited (ASX:RTE)",https://www.listcorp.com/asx/rte/retech-technology-co.-limited,"	32607800",0.14,0.00,0,"Consumer Discretionary"
ASX:USL,"Unico Silver Limited (ASX:USL)",https://www.listcorp.com/asx/usl/unico-silver-limited,"	32565700",0.11,0.00,0,Materials
ASX:FRE,"Firebrick Pharma Limited (ASX:FRE)",https://www.listcorp.com/asx/fre/firebrick-pharma-limited,"	32351500",0.285,0.00,0,"Health Care"
ASX:GCAP,"VanEck Bentham Global Capital Securities Active ETF (Managed Fund) (ASX:GCAP)",https://www.listcorp.com/asx/gcap/vaneck-bentham-global-capital-securities-active-etf-managed-fund,"	32347000",8.39,0.00,0,Financials
ASX:AE1,"Aerison Group Limited (ASX:AE1)",https://www.listcorp.com/asx/ae1/aerison-group-limited,"	32343700",0.1,0.00,0,Industrials
ASX:EIGA,"eInvest Income Generator Fund (Managed Fund) (ASX:EIGA)",https://www.listcorp.com/asx/eiga/einvest-income-generator-fund-managed-fund,"	32132200",3.63,0.00,0,Financials
ASX:IVX,"Invion Limited (ASX:IVX)",https://www.listcorp.com/asx/ivx/invion-limited,"	32108200",0.005,0.00,0,"Health Care"
ASX:LEX,"Lefroy Exploration Limited (ASX:LEX)",https://www.listcorp.com/asx/lex/lefroy-exploration-limited,"	32091600",0.2,0.00,0,Materials
ASX:CMP,"Compumedics Limited (ASX:CMP)",https://www.listcorp.com/asx/cmp/compumedics,"	31889300",0.18,0.00,0,"Health Care"
ASX:NOU,"Noumi Limited (ASX:NOU)",https://www.listcorp.com/asx/nou/noumi-limited,"	31867600",0.115,0.00,0,"Consumer Staples"
ASX:NET,"NetLinkz Limited (ASX:NET)",https://www.listcorp.com/asx/net/netlinkz-limited,"	31774800",0.009,0.00,0,"Information Technology"
ASX:TOU,"Tlou Energy Limited (ASX:TOU)",https://www.listcorp.com/asx/tou/tlou-energy,"	31762100",0.031,0.00,0,Energy
ASX:CTE,"Cryosite Limited (ASX:CTE)",https://www.listcorp.com/asx/cte/cryosite-limited,"	31726200",0.65,0.00,0,"Health Care"
ASX:ASP,"Aspermont Limited (ASX:ASP)",https://www.listcorp.com/asx/asp/aspermont-limited,"	31703900",0.013,0.00,0,"Communication Services"
ASX:EV1,"Evolution Energy Minerals Limited (ASX:EV1)",https://www.listcorp.com/asx/ev1/evolution-energy-minerals-limited,"	31631200",0.21,0.00,0,Materials
ASX:SEN,"Senetas Corp (ASX:SEN)",https://www.listcorp.com/asx/sen/senetas,"	31567700",0.026,0.00,0,"Information Technology"
ASX:SES,"SECOS Group Limited (ASX:SES)",https://www.listcorp.com/asx/ses/secos-group-limited,"	31454500",0.053,0.00,0,Materials
ASX:SLM,"Solis Minerals Limited (ASX:SLM)",https://www.listcorp.com/asx/slm/solis-minerals-limited,"	31382100",0.41,0.00,0,Materials
ASX:MGT,"Magnetite Mines Limited (ASX:MGT)",https://www.listcorp.com/asx/mgt/magnetite-mines-limited,"	31089800",0.405,0.00,0,Materials
ASX:IDA,"Indiana Resources Limited (ASX:IDA)",https://www.listcorp.com/asx/ida/indiana-resources-limited,"	31069200",0.058,0.00,0,Materials
ASX:FGH,"Foresta Group Holdings Limited (ASX:FGH)",https://www.listcorp.com/asx/fgh/foresta-group-holdings-limited,"	30930600",0.015,0.00,0,Materials
ASX:ATS,"Australis Oil & Gas Ltd (ASX:ATS)",https://www.listcorp.com/asx/ats/australis-oil-and-gas-ltd,"	30899300",0.0245,0.00,0,Energy
ASX:GOVT,"SPDR S&P/ASX Australian Government Bond Fund (ASX:GOVT)",https://www.listcorp.com/asx/govt/spdr-s-and-p-asx-australian-government-bond-fund,"	30874900",23.35,0.00,0,Financials
ASX:MCCL,"Munro Climate Change Leaders Fund (Managed Fund) (ASX:MCCL)",https://www.listcorp.com/asx/mccl/munro-climate-change-leaders-fund-managed-fund,"	30768800",10.28,0.00,0,Financials
ASX:MEU,"Marmota Limited (ASX:MEU)",https://www.listcorp.com/asx/meu/marmota-limited,"	30705200",0.029,0.00,0,Energy
ASX:SVY,"Stavely Minerals Limited (ASX:SVY)",https://www.listcorp.com/asx/svy/stavely-minerals-limited,"	30574500",0.081,0.00,0,Materials
ASX:COD,"Coda Minerals Ltd (ASX:COD)",https://www.listcorp.com/asx/cod/coda-minerals-ltd,"	30563800",0.215,0.00,0,Materials
ASX:WRK,"Wrkr Ltd (ASX:WRK)",https://www.listcorp.com/asx/wrk/wrkr-ltd,"	30518100",0.024,0.00,0,"Information Technology"
ASX:MOZ,"Mosaic Brands Limited (ASX:MOZ)",https://www.listcorp.com/asx/moz/mosaic-brands-limited,"	30346100",0.17,0.00,0,"Consumer Discretionary"
ASX:BTN,"Butn Limited (ASX:BTN)",https://www.listcorp.com/asx/btn/butn-limited,"	30198100",0.165,0.00,0,Financials
ASX:GWR,"GWR Group Limited (ASX:GWR)",https://www.listcorp.com/asx/gwr/gwr-group,"	30194400",0.094,0.00,0,Materials
ASX:ST1,"Spirit Technology Solutions Ltd (ASX:ST1)",https://www.listcorp.com/asx/st1/spirit-technology-solutions,"	30159800",0.041,0.00,0,"Communication Services"
ASX:CAV,"Carnavale Resources Ltd (ASX:CAV)",https://www.listcorp.com/asx/cav/carnavale-resources,"	30002000",0.009,0.00,0,Materials
ASX:BML,"Boab Metals Limited (ASX:BML)",https://www.listcorp.com/asx/bml/boab-metals-limited,"	29658700",0.17,0.00,0,Materials
ASX:PGY,"Pilot Energy Limited (ASX:PGY)",https://www.listcorp.com/asx/pgy/pilot-energy-limited,"	29614600",0.029,0.00,0,Energy
ASX:BAS,"Bass Oil Limited (ASX:BAS)",https://www.listcorp.com/asx/bas/bass-oil-limited,"	29523400",0.11,0.00,0,Energy
ASX:QEM,"QEM Limited (ASX:QEM)",https://www.listcorp.com/asx/qem/qem-limited,"	29378200",0.2,0.00,0,Materials
ASX:EM2,"Eagle Mountain Mining Limited (ASX:EM2)",https://www.listcorp.com/asx/em2/eagle-mountain-mining-limited,"	29276800",0.096,0.00,0,Materials
ASX:AR9,"archTIS Limited (ASX:AR9)",https://www.listcorp.com/asx/ar9/archtis-limited,"	29272000",0.1025,0.00,0,"Information Technology"
ASX:AV1,"Adveritas Limited (ASX:AV1)",https://www.listcorp.com/asx/av1/adveritas-limited,"	29128600",0.044,0.00,0,"Information Technology"
ASX:MIO,"Macarthur Minerals Limited (ASX:MIO)",https://www.listcorp.com/asx/mio/macarthur-minerals-limited,"	29059400",0.175,0.00,0,Materials
ASX:GFL,"Global Masters Fund Limited (ASX:GFL)",https://www.listcorp.com/asx/gfl/global-masters-fund-limited,"	28952500",2.7,0.00,0,Financials
ASX:CIW,"Clime Investment Management (ASX:CIW)",https://www.listcorp.com/asx/ciw/clime-investment-management,"	28924100",0.4,0.00,0,Financials
ASX:ECG,"Ecargo Holdings Limited (ASX:ECG)",https://www.listcorp.com/asx/ecg/ecargo-holdings-limited,"	28916800",0.047,0.00,0,Industrials
ASX:PXS,"Pharmaxis Ltd (ASX:PXS)",https://www.listcorp.com/asx/pxs/pharmaxis,"	28819500",0.04,0.00,0,"Health Care"
ASX:SRT,"Strata Investment Holdings Plc (ASX:SRT)",https://www.listcorp.com/asx/srt/strata-investment-holdings-plc,"	28802000",0.17,0.00,0,Materials
ASX:CDO,"Cadence Opportunities Fund Limited (ASX:CDO)",https://www.listcorp.com/asx/cdo/cadence-opportunities-fund-limited,"	28722000",1.84,0.00,0,Financials
ASX:TCG,"Turaco Gold Limited (ASX:TCG)",https://www.listcorp.com/asx/tcg/turaco-gold-limited,"	28654800",0.057,0.00,0,Materials
ASX:IND,"Industrial Minerals Ltd (ASX:IND)",https://www.listcorp.com/asx/ind/industrial-minerals-ltd,"	28649100",0.445,0.00,0,Materials
ASX:AZI,"Altamin Limited (ASX:AZI)",https://www.listcorp.com/asx/azi/altamin-limited,"	28595300",0.073,0.00,0,Materials
ASX:NML,"Navarre Minerals Limited (ASX:NML)",https://www.listcorp.com/asx/nml/navarre-minerals-limited,"	28555700",0.019,0.00,0,Materials
ASX:EPM,"Eclipse Metals Ltd (ASX:EPM)",https://www.listcorp.com/asx/epm/eclipse-metals-ltd,"	28392800",0.014,0.00,0,Energy
ASX:SUV,"Suvo Strategic Minerals Limited (ASX:SUV)",https://www.listcorp.com/asx/suv/suvo-strategic-minerals-limited,"	28368000",0.035,0.00,0,Materials
ASX:DCC,"DigitalX Limited (ASX:DCC)",https://www.listcorp.com/asx/dcc/digitalx-limited,"	28329700",0.038,0.00,0,"Information Technology"
ASX:CD1,"Cordish Dixon Private Equity Fund I (ASX:CD1)",https://www.listcorp.com/asx/cd1/cordish-dixon-private-equity-fund-i,"	28327200",0.775,0.00,0,Financials
ASX:RDM,"Red Metal Limited (ASX:RDM)",https://www.listcorp.com/asx/rdm/red-metal-limited,"	28243000",0.115,0.00,0,Materials
ASX:BIT,"Biotron Limited (ASX:BIT)",https://www.listcorp.com/asx/bit/biotron,"	27960300",0.031,0.00,0,"Health Care"
ASX:ANX,"Anax Metals Limited (ASX:ANX)",https://www.listcorp.com/asx/anx/anax-metals-limited,"	27943800",0.065,0.00,0,Materials
ASX:MKR,"Manuka Resources Limited (ASX:MKR)",https://www.listcorp.com/asx/mkr/manuka-resources-limited,"	27906000",0.05,0.00,0,Materials
ASX:CCG,"Comms Group Limited (ASX:CCG)",https://www.listcorp.com/asx/ccg/comms-group-limited,"	27872800",0.073,0.00,0,"Communication Services"
ASX:BM8,"Battery Age Minerals Limited (ASX:BM8)",https://www.listcorp.com/asx/bm8/battery-age-minerals-limited,"	27831800",0.375,0.00,0,Materials
ASX:ALO,"Alloggio Group Limited (ASX:ALO)",https://www.listcorp.com/asx/alo/alloggio-group-limited,"	27817000",0.235,0.00,0,"Consumer Discretionary"
ASX:BDT,"BirdDog Technology Limited (ASX:BDT)",https://www.listcorp.com/asx/bdt/birddog-technology-limited,"	27786100",0.14,0.00,0,"Information Technology"
ASX:RHT,"Resonance Health (ASX:RHT)",https://www.listcorp.com/asx/rht/resonance-health,"	27651100",0.06,0.00,0,"Health Care"
ASX:NGE,"NGE Capital Limited (ASX:NGE)",https://www.listcorp.com/asx/nge/nge-capital-limited,"	27602200",0.77,0.00,0,Financials
ASX:TEG,"Triangle Energy (Global) Limited (ASX:TEG)",https://www.listcorp.com/asx/teg/triangle-energy-global-limited,"	27518400",0.02,0.00,0,Energy
ASX:JAT,"Jatcorp Limited (ASX:JAT)",https://www.listcorp.com/asx/jat/jatcorp-limited,"	27477500",0.011,0.00,0,"Consumer Discretionary"
ASX:KAU,"Kaiser Reef Limited (ASX:KAU)",https://www.listcorp.com/asx/kau/kaiser-reef-limited,"	27357300",0.185,0.00,0,Materials
ASX:EZZ,"EZZ Life Science Holdings Limited (ASX:EZZ)",https://www.listcorp.com/asx/ezz/ezz-life-science-holdings-limited,"	27331200",0.64,0.00,0,"Health Care"
ASX:INCM,"BetaShares Global Income Leaders ETF (ASX:INCM)",https://www.listcorp.com/asx/incm/betashares-global-income-leaders-etf,"	27327000",15.37,0.00,0,Financials
ASX:TLM,"Talisman Mining Limited (ASX:TLM)",https://www.listcorp.com/asx/tlm/talisman-mining-limited,"	27306500",0.145,0.00,0,Materials
ASX:VMS,"Venture Minerals Limited (ASX:VMS)",https://www.listcorp.com/asx/vms/venture-minerals,"	27300200",0.014,0.00,0,Materials
ASX:RMI,"Resource Mining Corporation Limited (ASX:RMI)",https://www.listcorp.com/asx/rmi/resource-mining-corporation-limited,"	27285400",0.05,0.00,0,Materials
ASX:RTH,"RAS Technology Holdings Limited (ASX:RTH)",https://www.listcorp.com/asx/rth/ras-technology-holdings-limited,"	27275200",0.6,0.00,0,Industrials
ASX:ELT,"Elementos Limited (ASX:ELT)",https://www.listcorp.com/asx/elt/elementos-limited,"	27263600",0.14,0.00,0,Materials
ASX:RSH,"Respiri Limited (ASX:RSH)",https://www.listcorp.com/asx/rsh/respiri-limited,"	27263500",0.028,0.00,0,"Health Care"
ASX:HNR,"Hannans Ltd (ASX:HNR)",https://www.listcorp.com/asx/hnr/hannans-ltd,"	27246000",0.01,0.00,0,Materials
ASX:AUST,"BetaShares Managed Risk Australian Share Fund (managed fund) (ASX:AUST)",https://www.listcorp.com/asx/aust/betashares-managed-risk-australian-share-fund-managed-fund,"	27202500",15.63,0.00,0,Financials
ASX:TBIL,"VanEck 1-3 Month US Treasury Bond ETF (ASX:TBIL)",https://www.listcorp.com/asx/tbil/vaneck-1-3-month-us-treasury-bond-etf,"	27148100",52.2,0.00,0,Financials
ASX:WTL,"WT Financial Group Limited (ASX:WTL)",https://www.listcorp.com/asx/wtl/wt-financial-group-limited,"	27138700",0.08,0.00,0,Financials
ASX:CLA,"Celsius Resources Limited (ASX:CLA)",https://www.listcorp.com/asx/cla/celsius-resources-limited,"	26952600",0.012,0.00,0,Materials
ASX:QXR,"QX Resources Limited (ASX:QXR)",https://www.listcorp.com/asx/qxr/qx-resources-limited,"	26905900",0.03,0.00,0,Materials
ASX:COO,"Corum Group Limited (ASX:COO)",https://www.listcorp.com/asx/coo/corum-group-limited,"	26882200",0.045,0.00,0,"Information Technology"
ASX:DXB,"Dimerix Limited (ASX:DXB)",https://www.listcorp.com/asx/dxb/dimerix-limited,"	26862800",0.069,0.00,0,"Health Care"
ASX:SFG,"Seafarms Group Limited (ASX:SFG)",https://www.listcorp.com/asx/sfg/seafarms-group-limited,"	26601300",0.0055,0.00,0,"Consumer Staples"
ASX:CWX,"Carawine Resources Limited (ASX:CWX)",https://www.listcorp.com/asx/cwx/carawine-resources-limited,"	26570400",0.135,0.00,0,Materials
ASX:ROG,"Red Sky Energy Limited (ASX:ROG)",https://www.listcorp.com/asx/rog/red-sky-energy-limited,"	26511100",0.005,0.00,0,Energy
ASX:PAA,"PharmAust Limited (ASX:PAA)",https://www.listcorp.com/asx/paa/pharmaust,"	26506900",0.076,0.00,0,"Health Care"
ASX:SSO,"SPDR S&P/ASX Small Ordinaries Fund (ASX:SSO)",https://www.listcorp.com/asx/sso/spdr-s-and-p-asx-small-ordinaries-fund,"	26496700",12.9,0.00,0,Financials
ASX:DCG,"Decmil Group Limited (ASX:DCG)",https://www.listcorp.com/asx/dcg/decmil-group-limited,"	26443900",0.17,0.00,0,Industrials
ASX:MHC,"Manhattan Corporation Limited (ASX:MHC)",https://www.listcorp.com/asx/mhc/manhattan-corporation-limited,"	26432800",0.009,0.00,0,Materials
ASX:DHOF,"Daintree Hybrid Opportunities Fund (Managed Fund) (ASX:DHOF)",https://www.listcorp.com/asx/dhof/daintree-hybrid-opportunities-fund-managed-fund,"	26353900",9.13,0.00,0,Financials
ASX:IOU,"IOUpay Limited (ASX:IOU)",https://www.listcorp.com/asx/iou/ioupay-limited,"	26333300",0.041,0.00,0,"Communication Services"
ASX:AMS,"Atomos Limited (ASX:AMS)",https://www.listcorp.com/asx/ams/atomos-limited,"	26118400",0.065,0.00,0,"Consumer Discretionary"
ASX:IISV,"Intelligent Investor Select Value Share Fund (Managed Fund) (ASX:IISV)",https://www.listcorp.com/asx/iisv/intelligent-investor-select-value-share-fund-managed-fund,"	26087900",2.7,0.00,0,Financials
ASX:REE,"RareX Limited (ASX:REE)",https://www.listcorp.com/asx/ree/rarex-limited,"	25968700",0.038,0.00,0,Materials
ASX:MPP,"Metro Performance Glass (ASX:MPP)",https://www.listcorp.com/asx/mpp/metro-performance-glass,"	25952900",0.14,0.00,0,Industrials
ASX:GC1,"Glennon Small Companies Limited (ASX:GC1)",https://www.listcorp.com/asx/gc1/glennon-small-companies-limited,"	25906900",0.5,0.00,0,Financials
ASX:EMD,"Emyria Limited (ASX:EMD)",https://www.listcorp.com/asx/emd/emyria-limited,"	25901300",0.084,0.00,0,"Health Care"
ASX:STN,"Saturn Metals Limited (ASX:STN)",https://www.listcorp.com/asx/stn/saturn-metals-limited,"	25764900",0.16,0.00,0,Materials
ASX:SPX,"Spenda Limited (ASX:SPX)",https://www.listcorp.com/asx/spx/spenda-limited,"	25700000",0.007,0.00,0,"Information Technology"
ASX:KNI,"Kuniko Limited (ASX:KNI)",https://www.listcorp.com/asx/kni/kuniko-limited,"	25696700",0.38,0.00,0,Materials
ASX:GRE,"Greentech Metals Limited (ASX:GRE)",https://www.listcorp.com/asx/gre/greentech-metals-limited,"	25468000",0.45,0.00,0,Materials
ASX:ECS,"ECS Botanics Holdings Ltd (ASX:ECS)",https://www.listcorp.com/asx/ecs/ecs-botanics-holdings,"	25454800",0.023,0.00,0,"Health Care"
ASX:GLL,"Galilee Energy Limited (ASX:GLL)",https://www.listcorp.com/asx/gll/galilee-energy-limited,"	25390300",0.075,0.00,0,Energy
ASX:ZNC,"Zenith Minerals Limited (ASX:ZNC)",https://www.listcorp.com/asx/znc/zenith-minerals-limited,"	25371400",0.072,0.00,0,Materials
ASX:EME,"Energy Metals Limited (ASX:EME)",https://www.listcorp.com/asx/eme/energy-metals-limited,"	25162000",0.12,0.00,0,Energy
ASX:CYP,"Cynata Therapeutics Limited (ASX:CYP)",https://www.listcorp.com/asx/cyp/cynata-therapeutics,"	25148400",0.14,0.00,0,"Health Care"
ASX:ANL,"Amani Gold Limited (ASX:ANL)",https://www.listcorp.com/asx/anl/amani-gold-limited,"	25143400",0.001,0.00,0,Materials
ASX:IME,"ImExHS Limited (ASX:IME)",https://www.listcorp.com/asx/ime/imexhs-limited,"	25139100",0.605,0.00,0,"Health Care"
ASX:AUQ,"Alara Resources (ASX:AUQ)",https://www.listcorp.com/asx/auq/alara-resources,"	25133100",0.035,0.00,0,Materials
ASX:HRZ,"Horizon Minerals Limited (ASX:HRZ)",https://www.listcorp.com/asx/hrz/horizon-minerals-limited,"	25091400",0.036,0.00,0,Materials
ASX:MLS,"Metals Australia Limited (ASX:MLS)",https://www.listcorp.com/asx/mls/metals-australia-limited,"	24961400",0.04,0.00,0,Materials
ASX:C1X,"Cosmos Exploration Limited (ASX:C1X)",https://www.listcorp.com/asx/c1x/cosmos-exploration-limited,"	24906000",0.56,0.00,0,Materials
ASX:EDU,"EDU Holdings Limited (ASX:EDU)",https://www.listcorp.com/asx/edu/edu-holdings-limited,"	24782200",0.15,0.00,0,"Consumer Discretionary"
ASX:SRN,"Surefire Resources NL (ASX:SRN)",https://www.listcorp.com/asx/srn/surefire-resources-nl,"	24770500",0.015,0.00,0,Materials
ASX:LCL,"LCL Resources Limited (ASX:LCL)",https://www.listcorp.com/asx/lcl/lcl-resources-limited,"	24623400",0.031,0.00,0,Materials
ASX:MGU,"Magnum Mining & Exploration Limited (ASX:MGU)",https://www.listcorp.com/asx/mgu/magnum-mining-and-exploration-limited,"	24537900",0.034,0.00,0,Materials
ASX:BDX,"BCAL Diagnostics Limited (ASX:BDX)",https://www.listcorp.com/asx/bdx/bcal-diagnostics-limited,"	24521800",0.115,0.00,0,"Health Care"
ASX:FTZ,"Fertoz Ltd (ASX:FTZ)",https://www.listcorp.com/asx/ftz/fertoz,"	24494300",0.095,0.00,0,Materials
ASX:OJC,"The Original Juice Co. Limited (ASX:OJC)",https://www.listcorp.com/asx/ojc/the-original-juice-co-limited,"	24459100",0.1,0.00,0,"Consumer Staples"
ASX:JAY,"Jayride Group Limited (ASX:JAY)",https://www.listcorp.com/asx/jay/jayride-group-limited,"	24436500",0.12,0.00,0,Industrials
ASX:SIH,"Sihayo Gold (ASX:SIH)",https://www.listcorp.com/asx/sih/sihayo-gold,"	24408500",0.002,0.00,0,Materials
ASX:VBC,"Verbrec Limited (ASX:VBC)",https://www.listcorp.com/asx/vbc/verbrec-limited,"	24362400",0.11,0.00,0,Industrials
ASX:UNT,"Unith Ltd (ASX:UNT)",https://www.listcorp.com/asx/unt/unith-ltd,"	24292300",0.027,0.00,0,"Communication Services"
ASX:ASW,"Advanced Share Registry Ltd (ASX:ASW)",https://www.listcorp.com/asx/asw/advanced-share-registry,"	24176000",0.125,0.00,0,Financials
ASX:MLM,"Metallica Minerals Limited (ASX:MLM)",https://www.listcorp.com/asx/mlm/metallica-minerals-limited,"	23998100",0.025,0.00,0,Materials
ASX:BKG,"Booktopia Group Limited (ASX:BKG)",https://www.listcorp.com/asx/bkg/booktopia-group-limited,"	23961500",0.105,0.00,0,"Consumer Discretionary"
ASX:WLD,"Wellard Limited (ASX:WLD)",https://www.listcorp.com/asx/wld/wellard-limited,"	23906300",0.045,0.00,0,"Consumer Staples"
ASX:ENA,"Ensurance Ltd (ASX:ENA)",https://www.listcorp.com/asx/ena/ensurance-ltd,"	23891300",0.265,0.00,0,Financials
ASX:TIA,"Tian An Australia Limited (ASX:TIA)",https://www.listcorp.com/asx/tia/tian-an-australia-limited,"	23817400",0.275,0.00,0,"Real Estate"
ASX:WSI,"Weststar Industrial Limited (ASX:WSI)",https://www.listcorp.com/asx/wsi/weststar-industrial-limited,"	23814500",0.215,0.00,0,Materials
ASX:BRX,"Belararox Limited (ASX:BRX)",https://www.listcorp.com/asx/brx/belararox-limited,"	23811400",0.46,0.00,0,Materials
ASX:HCF,"H&G High Conviction Limited (ASX:HCF)",https://www.listcorp.com/asx/hcf/h-and-g-high-conviction-limited,"	23806500",0.95,0.00,0,Financials
ASX:SPT,"Splitit Payments Ltd (ASX:SPT)",https://www.listcorp.com/asx/spt/splitit-payments-ltd,"	23791200",0.043,0.00,0,Financials
ASX:REC,"Recharge Metals Limited (ASX:REC)",https://www.listcorp.com/asx/rec/recharge-metals-limited,"	23756500",0.225,0.00,0,Materials
ASX:VMC,"Venus Metals Corporation Limited (ASX:VMC)",https://www.listcorp.com/asx/vmc/venus-metals,"	23716100",0.125,0.00,0,Materials
ASX:HTG,"Harvest Technology Group Limited (ASX:HTG)",https://www.listcorp.com/asx/htg/harvest-technology-group-limited,"	23554000",0.034,0.00,0,"Information Technology"
ASX:TMS,"Tennant Minerals Limited (ASX:TMS)",https://www.listcorp.com/asx/tms/tennant-minerals-limited,"	23542400",0.031,0.00,0,Materials
ASX:MAN,"Mandrake Resources Limited (ASX:MAN)",https://www.listcorp.com/asx/man/mandrake-resources-limited,"	23351600",0.039,0.00,0,Materials
ASX:AQI,"Alicanto Minerals Limited (ASX:AQI)",https://www.listcorp.com/asx/aqi/alicanto-minerals,"	23287800",0.038,0.00,0,Materials
ASX:FPC,"Fat Prophets Global Contrarian Fund (ASX:FPC)",https://www.listcorp.com/asx/fpc/fat-prophets-global-contrarian-fund,"	23248000",0.77,0.00,0,Financials
ASX:IDT,"IDT Australia Limited (ASX:IDT)",https://www.listcorp.com/asx/idt/idt-australia-limited,"	23188300",0.066,0.00,0,"Health Care"
ASX:JXT,"Jaxsta Limited (ASX:JXT)",https://www.listcorp.com/asx/jxt/jaxsta-limited,"	23153000",0.054,0.00,0,"Information Technology"
ASX:CPH,"Creso Pharma Limited (ASX:CPH)",https://www.listcorp.com/asx/cph/creso-pharma-limited,"	23106100",0.009,0.00,0,"Health Care"
ASX:FYI,"FYI Resources Limited (ASX:FYI)",https://www.listcorp.com/asx/fyi/fyi-resources,"	23090600",0.063,0.00,0,Materials
ASX:GTG,"Genetic Technologies Limited (ASX:GTG)",https://www.listcorp.com/asx/gtg/genetic-technologies-limited,"	23083300",0.002,0.00,0,"Health Care"
ASX:TCO,"Transmetro Corporation Limited (ASX:TCO)",https://www.listcorp.com/asx/tco/transmetro-corporation,"	23018400",1.72,0.00,0,"Consumer Discretionary"
ASX:CDX,"CardieX Limited (ASX:CDX)",https://www.listcorp.com/asx/cdx/cardiex-limited,"	22989400",0.16,0.00,0,"Health Care"
ASX:LCT,"Living Cell Technologies (ASX:LCT)",https://www.listcorp.com/asx/lct/living-cell-technologies,"	22899000",0.014,0.00,0,"Health Care"
ASX:BXN,"Bioxyne Limited (ASX:BXN)",https://www.listcorp.com/asx/bxn/bioxyne-limited,"	22819700",0.012,0.00,0,"Consumer Staples"
ASX:WNX,"Wellnex Life Limited (ASX:WNX)",https://www.listcorp.com/asx/wnx/wellnex-life-limited,"	22704500",0.0524011,0.00,0,"Consumer Staples"
ASX:EMB,"Embelton Limited (ASX:EMB)",https://www.listcorp.com/asx/emb/embelton-limited,"	22657500",10.5,0.00,0,Industrials
ASX:AYA,"Artrya Limited (ASX:AYA)",https://www.listcorp.com/asx/aya/artrya-limited,"	22654300",0.36,0.00,0,"Health Care"
ASX:BTR,"Brightstar Resources Limited (ASX:BTR)",https://www.listcorp.com/asx/btr/brightstar-resources-limited,"	22608200",0.012,0.00,0,Materials
ASX:CNQ,"Clean TeQ Water Limited (ASX:CNQ)",https://www.listcorp.com/asx/cnq/clean-teq-water-limited,"	22427200",0.3875,0.00,0,Industrials
ASX:EINC,"BetaShares Martin Currie Equity Income Fund (managed fund) (ASX:EINC)",https://www.listcorp.com/asx/einc/betashares-martin-currie-equity-income-fund-managed-fund,"	22376900",8.1,0.00,0,Financials
ASX:JPR,"Jupiter Energy Limited (ASX:JPR)",https://www.listcorp.com/asx/jpr/jupiter-energy-limited,"	22362300",0.018,0.00,0,Energy
ASX:ABX,"ABx Group Limited (ASX:ABX)",https://www.listcorp.com/asx/abx/abx-group-limited,"	22359100",0.1,0.00,0,Materials
ASX:BUX,"Buxton Resources Limited (ASX:BUX)",https://www.listcorp.com/asx/bux/buxton-resources-limited,"	22266200",0.13,0.00,0,Materials
ASX:QML,"Qmines Limited (ASX:QML)",https://www.listcorp.com/asx/qml/qmines-limited,"	22153000",0.13,0.00,0,Materials
ASX:AL3,"AML3D Limited (ASX:AL3)",https://www.listcorp.com/asx/al3/aml3d-limited,"	22142000",0.094,0.00,0,Industrials
ASX:XMET,"BetaShares Energy Transition Metals ETF (ASX:XMET)",https://www.listcorp.com/asx/xmet/betashares-energy-transition-metals-etf,"	22095700",7.89,0.00,0,Financials
ASX:PNN,"Power Minerals Limited (ASX:PNN)",https://www.listcorp.com/asx/pnn/power-minerals-limited,"	21964900",0.3,0.00,0,Materials
ASX:AMO,"Ambertech Limited (ASX:AMO)",https://www.listcorp.com/asx/amo/ambertech,"	21912500",0.235,0.00,0,"Information Technology"
ASX:MM8,"Medallion Metals Limited (ASX:MM8)",https://www.listcorp.com/asx/mm8/medallion-metals-limited,"	21834500",0.071,0.00,0,Materials
ASX:CXZ,"Connexion Telematics Ltd (ASX:CXZ)",https://www.listcorp.com/asx/cxz/connexion-telematics-ltd,"	21780200",0.023,0.00,0,"Information Technology"
ASX:RAD,"Radiopharm Theranostics Limited (ASX:RAD)",https://www.listcorp.com/asx/rad/radiopharm-theranostics-limited,"	21777500",0.091,0.00,0,"Health Care"
ASX:SHP,"South Harz Potash Ltd (ASX:SHP)",https://www.listcorp.com/asx/shp/south-harz-potash-ltd,"	21776200",0.032,0.00,0,Materials
ASX:EQX,"Equatorial Resources Limited (ASX:EQX)",https://www.listcorp.com/asx/eqx/equatorial-resources-limited,"	21606000",0.165,0.00,0,Materials
ASX:TCF,"360 Capital Mortgage REIT (ASX:TCF)",https://www.listcorp.com/asx/tcf/360-capital-mortgage-reit,"	21524700",5.21,0.00,0,Financials
ASX:HMD,"HeraMED Limited (ASX:HMD)",https://www.listcorp.com/asx/hmd/heramed-limited,"	21522600",0.077,0.00,0,"Health Care"
ASX:RNO,"Rhinomed (ASX:RNO)",https://www.listcorp.com/asx/rno/rhinomed,"	21429000",0.075,0.00,0,"Health Care"
ASX:XRG,"xReality Group Ltd (ASX:XRG)",https://www.listcorp.com/asx/xrg/xreality-group-ltd,"	21424600",0.048,0.00,0,"Consumer Discretionary"
ASX:IYLD,"iShares Yield Plus ETF (ASX:IYLD)",https://www.listcorp.com/asx/iyld/ishares-yield-plus-etf,"	21410600",98.54,0.00,0,Financials
ASX:VBS,"Vectus Biosystems Limited (ASX:VBS)",https://www.listcorp.com/asx/vbs/vectus-biosystems-limited,"	21275800",0.4,0.00,0,"Health Care"
ASX:DBBF,"BetaShares Ethical Diversified Balanced ETF (ASX:DBBF)",https://www.listcorp.com/asx/dbbf/betashares-ethical-diversified-balanced-etf,"	21203000",23.46,0.00,0,Financials
ASX:BIO,"Biome Australia Limited (ASX:BIO)",https://www.listcorp.com/asx/bio/biome-australia-limited,"	21118900",0.13,0.00,0,"Consumer Staples"
ASX:ECP,"ECP Emerging Growth Limited (ASX:ECP)",https://www.listcorp.com/asx/ecp/ecp-emerging-growth-limited,"	21090000",1.15,0.00,0,Financials
ASX:BUD,"Buddy Technologies Limited (ASX:BUD)",https://www.listcorp.com/asx/bud/buddy-technologies,"	21075200",0.006,0.00,0,"Consumer Discretionary"
ASX:TSO,"Tesoro Gold Limited (ASX:TSO)",https://www.listcorp.com/asx/tso/tesoro-gold-limited,"	21072300",0.02,0.00,0,Materials
ASX:ITM,"iTech Minerals Ltd (ASX:ITM)",https://www.listcorp.com/asx/itm/itech-minerals,"	21048000",0.18,0.00,0,Materials
ASX:IBX,"Imagion Biosystems Limited (ASX:IBX)",https://www.listcorp.com/asx/ibx/imagion-biosystems-limited,"	20892300",0.016,0.00,0,"Health Care"
ASX:ASQ,"Australian Silica Quartz Group Ltd (ASX:ASQ)",https://www.listcorp.com/asx/asq/australian-silica-quartz-group-ltd,"	20842900",0.074,0.00,0,Materials
ASX:AML,"Aeon Metals (ASX:AML)",https://www.listcorp.com/asx/aml/aeon-metals,"	20831600",0.019,0.00,0,Materials
ASX:CSX,"CleanSpace Holdings Limited (ASX:CSX)",https://www.listcorp.com/asx/csx/cleanspace-holdings-limited,"	20808900",0.27,0.00,0,"Health Care"
ASX:AEV,"Avenira Limited (ASX:AEV)",https://www.listcorp.com/asx/aev/avenira-limited,"	20760100",0.012,0.00,0,Materials
ASX:CSE,"Copper Strike Limited (ASX:CSE)",https://www.listcorp.com/asx/cse/copper-strike,"	20705600",0.155,0.00,0,Materials
ASX:LVH,"Livehire Limited (ASX:LVH)",https://www.listcorp.com/asx/lvh/livehire-limited,"	20673700",0.059,0.00,0,"Information Technology"
ASX:CG1,"Carbonxt Group Limited (ASX:CG1)",https://www.listcorp.com/asx/cg1/carbonxt-group-limited,"	20647400",0.075,0.00,0,Materials
ASX:LU7,"Lithium Universe Limited (ASX:LU7)",https://www.listcorp.com/asx/lu7/lithium-universe-limited,"	20591700",0.053,0.00,0,Materials
ASX:SKF,"Skyfii Limited (ASX:SKF)",https://www.listcorp.com/asx/skf/skyfii-limited,"	20564700",0.049,0.00,0,"Information Technology"
ASX:TAL,"Talius Group Limited (ASX:TAL)",https://www.listcorp.com/asx/tal/talius-group-limited,"	20561800",0.009,0.00,0,"Information Technology"
ASX:AYI,"A1 Investments & Resources (ASX:AYI)",https://www.listcorp.com/asx/ayi/a1-investments-and-resources,"	20527400",0.001,0.00,0,Financials"""


lines = string.split("\n")
tickers = []
for l in lines:
    try:
        tickers.append(l.split(",")[0].split(":")[1]+".AX")
    except:
        pass 

open("../ASX/1.json","w").write(json.dumps({"list":tickers},indent=4))