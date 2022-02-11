


#-##
#-## Declare files to utilize
#-##
slcspFileName = 'slcsp.csv'
plansFileName = 'plans.csv'
zipsFileName = 'zips.csv'

planToConsider = 'silver'   # case insensitive value

origZipCodes = []
origRates = []

silverPlans = {}
rate_area_per_statezip = {}
zip_to_state = {}

#-##
#-## function to get unique values
#-##
#
# start --> 
# 
def unique(inList):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for x in inList:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
#
# end --> function to get unique values
#




#-##
#-## Read in the list of zip codes to search the rates for while maintaining its order by putting it into a list
#-##
with open(slcspFileName) as slcspInfile:
    slcspLines = slcspInfile.readlines()

debugCounter = 0

for line in slcspLines:
    debugCounter = debugCounter + 1
    zipcode,rate = line.rstrip().split(',')
    origZipCodes.append(zipcode)
    origRates.append(rate)

# print ('rates to find read in counter ' + str(debugCounter))





#-##
#-## Build a list of silver plan rates for each rate area and state
#-##

with open(plansFileName) as plansInfile:
    planLines = plansInfile.readlines()

debugCounter = 0

#-## skipping the header line and other types of plans
for line in planLines[1:]:
    plan_id,state,metal_level,rate,rate_area = line.rstrip().split(',')
    if planToConsider.lower() in metal_level.lower():
        rates = []
        debugCounter = debugCounter + 1
        if state not in silverPlans:
            silverPlans[state] = {}
        if rate_area in silverPlans[state]:
            rates = silverPlans[state][rate_area]
        rates.append(float(rate))
        silverPlans[state][rate_area] = rates

# print ('silver plans read in counter ' + str(debugCounter))

## Reduce silver plan's rates to unique rates by first sorting and then removing duplicates
for state in silverPlans.keys():
    for rate_area in silverPlans[state].keys():
        rates = silverPlans[state][rate_area]
        rates.sort()
        silverPlans[state][rate_area] = unique(rates)

        ## If there are more than two plans in a rate area, we set it to 2nd lowest else to nothing since no plan available
        if len(silverPlans[state][rate_area]) > 2:
            silverPlans[state][rate_area] = silverPlans[state][rate_area][1]
        else:
            silverPlans[state][rate_area] = ''

#        print('2nd lowest silverPlans --> {}-{}-{}'.format(state, rate_area, silverPlans[state][rate_area]))





#-##
#-## Build the list of rate areas per zipcode and state
#-##

with open(zipsFileName) as zipsInfile:
    zipLines = zipsInfile.readlines()

debugCounter = 0

#-## while skipping the header line
for line in zipLines[1:]:
    zipcode,state,county_code,name,rate_area = line.rstrip().split(',')
    newList = []
    zip_to_state[zipcode] = state
    debugCounter = debugCounter + 1
    if state not in rate_area_per_statezip:
        rate_area_per_statezip[state] = {}
    if zipcode in rate_area_per_statezip[state]:
        newList = rate_area_per_statezip[state][zipcode]
    newList.append(int(rate_area))
    rate_area_per_statezip[state][zipcode] = unique(newList)

# print ('zips read in counter ' + str(debugCounter))
# print ('rate_area_per_statezip -> {} {} {}'.format(state, zipcode, rate_area_per_statezip))

#-## If state and zip has more than one rate area then eliminate since ambiguous
for state in rate_area_per_statezip.keys():
    for zipcode in rate_area_per_statezip[state].keys():
        if len(rate_area_per_statezip[state][zipcode]) > 1:
            rate_area_per_statezip[state][zipcode] = ''







#-##
#-## Now that we have list of single rates for SLCSP based on state, zip code and rate area, we look it up and assign it to the original list elements if found.
#-## while skipping the header line
#-##    
for index in range(1, len(origZipCodes)):
    zipToLookup = origZipCodes[index]
    stateToLookup = zip_to_state[zipToLookup]

    if len(rate_area_per_statezip[stateToLookup][zipToLookup]) > 0:
        rateToLookup = str(rate_area_per_statezip[stateToLookup][zipToLookup][0])

        if stateToLookup in silverPlans:
            if rateToLookup in silverPlans[stateToLookup]:
                origRates[index] = silverPlans[stateToLookup][rateToLookup]

        




#-##
#-## Now 'stdout' our list which has a SLCSP filled in if rate was available
#-##
for index in range(len(origZipCodes)):
    # we started out with blank string list for pricing and updated with float value if SLCSP rate was available
    if type (origRates[index]) == 'float':
        print('{},{:.2f}'.format(origZipCodes[index], origRates[index])) # limit output to at most two decimals
    else:
        print('{},{}'.format(origZipCodes[index], origRates[index]))
    
#    print('{},{}-->{}'.format(origZipCodes[index], origRates[index], type (origRates[index]) ))
