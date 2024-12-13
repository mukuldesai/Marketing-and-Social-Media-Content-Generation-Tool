# Setup Instructions

To set up the project on your local machine:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=<your-api-key>
   ```

4. To run the application:
   ```
   python manage.py runserver
   ```

5. For testing:
   ```
   pytest tests/
   ```
