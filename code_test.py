import streamlit as st

TEST_CODE = """
import json
import random
import streamlit as st

# Load the JSON file containing the sponsor company data.
with open("notebooks/company_full.json", "r") as file:
    sponsor_companies = json.load(file)

# Generate a random number between 0 and the number of sponsor companies.
random_index = random.randint(0, len(sponsor_companies) - 1)

print(sponsor_companies)
# Use the random number to index the sponsor company data and retrieve the name of the company.
company_name = sponsor_companies[str(random_index)]["name"]

# Display the name of the randomly selected sponsor company to the user.
st.write(f"A randomly selected sponsor company is: {company_name}")
"""

def main():

    st.code(TEST_CODE, language="python")
    exec(TEST_CODE, globals())

main()