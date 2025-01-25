# SWIFT Connect Automation Case Study
This project is a case study for automating the onboarding and request processing of business customers for SWIFT Connect, replacing the existing manual process with an electronic one. The solution includes:

- A web module for collecting customer requests.
- A CRM module for processing those requests within the company's platform.

## Features
### Web Module
- User-friendly interface for business customers to submit requests.
- Form validation to ensure the accuracy of submitted data.
- Integration with the CRM module for seamless processing.
### CRM Module
- Admin interface for viewing and processing customer requests.
- Request management tools (approve, reject, or update requests).
- Dashboard for tracking request statuses and analytics.

## Technology Stack
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Backend:** Python (Django framework)
- **Database:** SQLite
- **Template Engine:** Django Templates

## Setup Instructions

`1.` **Clone the repository:**
```bash
git clone https://github.com/AsnakeMulu/SwiftConnect.git
cd SwiftConnect
```

`2.` **Install dependencies:**
```bash
pip install -r requirements.txt
```

`3.` **Start the application:**
```bash
python manage.py runserver
```

`4.` Open your browser and visit 
```bash
http://localhost:5000
```

## Contributing
Contributions are welcome! Please fork the repository, create a new branch for your feature or fix, and submit a pull request.
