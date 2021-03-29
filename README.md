# Election-Audit Analysis

## Overview of Project
The purpose of this project was to provide an audit of election results to the election commission. The audit was specifically looking at vote counts for each candidate as well as general voter turnout for each county.

## Election-Audit Results
### County Results
- Total Votes: 369,711
- Jefferson: 10.5% of the votes (38,855).
- Denver: 82.8% of the votes (306,055).
- Arapahoe: 6.7% of the votes (24,801).
- Largest County Turnout: Denver

### Candidate Results
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)
### Winning Candidate
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

### Election-Audit Summary
The great thing about this script is that it could be run for any other election as long as the data is provided in this same format. Since the script checks for candidate names and counties (instead of these items being hardcoded) the commmision could easily utilize it for future elections.
`# Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)`
`# 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in counties:
            # 4b: Add the existing county to the list of counties.
            counties.append(county_name)`

However, the script there are a couple areas where the script could be improved.
- One improvement would be to add have the script account for ties. Currently, the script is only able to declare one winner. In the event of a tie, the script would not be able to make this distinction and announce the need for a runoff vote.
- Another improvement would be to add in the margin a candidate needs to win by in order to avoid a runoff elections. Depending on county rules, this might be a necessary addition. Currently, the script is designed to announce a winner as long as they have one more vote than the next highest candidate.
I beleive these two additions will increase the value of the election audit script and make it more useful for the commission.
