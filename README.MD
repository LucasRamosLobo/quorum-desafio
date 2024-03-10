# Quorum Coding Challenge - Legislative Data

This project is a Django web application that provides insights into legislative data. The data includes information about legislators, bills, votes, and vote results.

## Setup and Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LucasRamosLobo/quorum-desafio.git
   cd quorum-desafio
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Django development server:

bash
Copy code
python manage.py runserver
Access the application in your web browser at http://localhost:8000/api/all_stats/.

Questions & Answers
1. Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used, and any other variable that you understand important in your development process.
Answer:

Strategy:

Utilized Django as the web framework due to its robustness and efficiency in handling database operations.
Employed Django models to represent legislators, bills, votes, and vote results.
Calculated statistics using Django queries to minimize time complexity.
Time Complexity:

Leveraged Django's ORM to optimize database queries, resulting in efficient data retrieval and processing.
Effort Cost:

Reduced effort by utilizing Django's built-in features for handling models, views, and templates.
Focused on code readability and maintainability.
Technologies Used:

Django: Web framework for building robust web applications.
Python: Language used for application logic.
HTML: Used for rendering templates.
2. How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
Answer:

Adding Future Columns:
For additional columns like "Bill Voted On Date" or "Co-Sponsors," I would extend the existing models.
Create new fields in the Bill model for the requested data.
Update data import processes to include the new columns.
Modify views to incorporate the new data into statistics calculations.
3. How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?
Answer:

CSV Generation:
Implement a Django management command to generate CSV files for given lists of legislators or bills.
Dynamically create CSV files based on input parameters.
Utilize Django's CSV module or Python's CSV writer for efficient file creation.
4. How long did you spend working on the assignment?
Answer:

I spent approximately 2 hours working on the assignment, including data modeling, implementation, testing, and documentation.