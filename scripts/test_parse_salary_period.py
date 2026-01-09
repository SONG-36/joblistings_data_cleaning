from src.salary.parse_salary_period import extract_salary_period, extract_currency

samples = [
    "USD 3000 per month",
    "$25 per hour",
    "Annual salary: 60000 USD",
    "RM 8000",
    "Negotiable",
    "",
    None,
]

for s in samples:
    print("INPUT:", repr(s))
    print("PERIOD:", extract_salary_period(s))
    print("CURRENCY:", extract_currency(s))
    print("-" * 50)
