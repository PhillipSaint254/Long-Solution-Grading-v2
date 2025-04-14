import fitz  # PyMuPDF

# Step 1: Load PDF
pdf_path = r'C:\Users\phill\Downloads\bjophthalmol-2019-314336-inline-supplementary-material-1 (1).pdf'
doc = fitz.open(pdf_path)

# Step 2: Extract all text from the PDF
full_text = ""
for page in doc:
    full_text += page.get_text()

# Step 3: Define European countries
europe_countries = [
    'Albania', 'Andorra', 'Armenia', 'Austria', 'Azerbaijan', 'Belarus', 'Belgium',
    'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 
    'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece',
    'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein', 'Lithuania',
    'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands',
    'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russia', 'San Marino',
    'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 
    'Ukraine', 'United Kingdom', 'Vatican City'
]

# Step 4: Check presence of each country
results = {}
for country in europe_countries:
    if country in full_text:
        results[country] = "✅ Present"
    else:
        results[country] = "❌ Missing"

# Step 5: Print or export the results
for country, status in results.items():
    print(f"{country}: {status}")
