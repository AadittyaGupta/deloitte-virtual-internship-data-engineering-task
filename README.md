# deloitte-virtual-internship-data-engineering-task (Forage)

This repository contains my solution to a simulation project completed during the **Deloitte Technology Consulting Virtual Internship** offered by [Forage](https://www.theforage.com/).

## Project Overview

As part of the internship, I acted as a junior technology consultant helping a new Deloitte client: **Daikibo Industrials**, a global manufacturing company headquartered in Tokyo. 

**Daikibo** is integrating Industrial IoT devices across its infrastructure, but their telemetry data is coming in **two different formats**. My task was to write a Python script to:

- Identify which data format is being used
- Convert it into a unified structure
- Validate the transformation using provided test cases

##  Technologies Used

- Python 3
- JSON
- datetime
- `unittest` for testing


## Data Conversion Logic

### Format 1:
- Flat JSON structure
- Location provided as a string (e.g. `"Japan/Tokyo/Area51/Plant12/SectionA"`)

**Converted to:** Nested location dictionary with keys like `country`, `city`, etc.

---

### Format 2:
- Structured JSON with `device`, `data`, and location fields as separate keys
- Timestamp in ISO 8601 format (e.g. `"2023-01-01T08:30:00.000Z"`)

**Converted to:**  
- Milliseconds since UNIX epoch
- Unified JSON structure like Format 1

---

## Tests

The script includes unit tests that check:
- Sanity of the expected result
- Correct transformation from both Format 1 and Format 2


##  Outcome

Successfully transformed both input formats into a single, consistent JSON structure. This project showcases my ability to:

- 🧠 Interpret client needs  
- 🧩 Work with semi-structured data  
- 🧪 Write clean, testable Python code  

---

##  About the Internship

- **Program:** Deloitte Technology Consulting Virtual Internship  
- **Platform:** [Forage](https://www.theforage.com/)  
- **Focus Area:** Digital transformation, data engineering, and systems integration  


