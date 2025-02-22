

# Telex Currency Converter Integration

## Overview

The **Telex Currency Converter Integration** is a Modifier Integration designed to enhance communication within Telex channels by enabling real-time currency conversion. When a user sends a command in the Telex channel—such as:

```
/convert 100 USD to EUR
```

—the integration automatically:
- Parses the command to extract the amount and currency codes.
- Fetches the latest exchange rate from an external currency conversion API (e.g., ExchangeRate-API).
- Calculates the converted amount.
- Returns a formatted message with the conversion result back into the Telex channel.

This integration helps users quickly obtain conversion results without leaving the chat, making financial discussions more efficient and informed.

---

## Features

- **Command Parsing:** Detects and processes commands in the format `/convert <amount> <source_currency> to <target_currency>`.
- **Real-Time Data:** Retrieves live exchange rates from a trusted external API.
- **User-Friendly Response:** Returns a formatted message indicating the conversion result.
- **Robust Error Handling:** Provides clear error messages for malformed commands or API failures.
- **Extensible:** Can be easily extended to support more currencies or additional command variations.

---

## Prerequisites

Before setting up the integration, ensure you have the following:

- **Python 3.9+** installed.
- **Django** and **Django REST Framework** (if using DRF) installed.
- A valid API key for a currency conversion service (e.g., [ExchangeRate-API](https://www.exchangerate-api.com/)).
- Basic knowledge of Django views, URLs, and management commands.
- (Optional) A Telex account for testing the integration within a channel.

---

## Project Structure

The integration is organized as a Django project. An example structure might be:

```
telex_currency_converter/
├── currency/                       # Django app for currency conversion logic
│   ├── __init__.py
│   ├── views.py                    # Contains the convert_currency_view function
│   ├── urls.py                     # URL routes for the integration
│   ├── tests.py                    # Unit tests for the integration
│   └── utils.py                    # Utility functions: get_exchange_rate, conversion, formatting, etc.
├── manage.py
├── requirements.txt                # Project dependencies
├── README.md                       # This file
└── settings.py                     # Django settings
```

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/telex-currency-converter.git
   cd telex-currency-converter
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   Create a `.env` file in the project root (or set these variables in your deployment environment):

   ```ini
   # .env file
   DEBUG=False
   SECRET_KEY=your-secret-key
   EXCHANGE_RATE_API_KEY=your_currency_api_key
   ```

   Ensure you load these environment variables in your Django settings (using `python-dotenv` or another method).

---

## Configuration

### Django Settings

- **Static Files:**  
  Ensure your `STATIC_ROOT` is set (for production) as follows:

  ```python
  STATIC_URL = '/static/'
  STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
  STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
  STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
  ```

- **Currency API Key:**  
  In your Django settings, load the currency API key from your environment:

  ```python
  import os
  EXCHANGE_RATE_API_KEY = os.environ.get('EXCHANGE_RATE_API_KEY')
  ```

---

## Usage

### Running the Server

To run the integration locally, execute:

```bash
python manage.py runserver
```

You can then test the integration endpoint by sending a POST request to the conversion endpoint (e.g., `http://127.0.0.1:8000/telex/convert/`) with a JSON payload:

```json
{
  "message": "/convert 100 USD to EUR"
}
```

The response should return:

```json
{
  "message": "100 USD is equivalent to 85.50 EUR"
}
```

### Command Format

- **Format:** `/convert <amount> <source_currency> to <target_currency>`
- **Example:** `/convert 250 GBP to USD`

---

## API Reference

### Conversion Endpoint

- **URL:** `/telex/convert/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "message": "/convert 100 USD to EUR"
  }
  ```

- **Response:**

  - **Success (200):**

    ```json
    {
      "message": "100 USD is equivalent to 85.50 EUR"
    }
    ```

  - **Error (400/500):**

    ```json
    {
      "error": "Invalid command format."
    }
    ```

---

## Testing

Run the unit tests using:

```bash
pytest
```

Tests should cover:
- Command parsing.
- Exchange rate retrieval (you may need to mock external API calls).
- Correct conversion calculation.
- Error handling for invalid input or API failures.

---

## Deployment

### Deploying to Production

1. **Prepare your production environment:**  
   Ensure that your production server has Python, required packages, and environment variables configured.

2. **Collect Static Files:**

   ```bash
   python manage.py collectstatic
   ```

3. **Deploy your Django application:**  
   Use your preferred method (e.g., Render, AWS, Heroku) to deploy your app.  
   Ensure that your production environment uses a real currency API key and that `DEBUG=False`.

4. **Integration JSON:**  
   Host your integration settings JSON on a public URL as required by Telex. The JSON should include the necessary configuration for your integration (name, type, endpoints, etc.).

5. **Testing on Telex:**  
   Once deployed, install the integration in your designated test Telex organization and verify that it functions as expected.

---

## Screenshots

*(Include screenshots here showing the integration in action in a Telex channel, if available.)*

---

## Contribution Guidelines

- **Conventional Commits:**  
  Please follow conventional commit messages for any pull requests. For example, `feat: add currency conversion endpoint`.

- **Code Quality:**  
  Ensure your code is clean, well-documented, and properly tested before submission.

- **Issues and Enhancements:**  
  Feel free to submit issues or feature requests via GitHub.

---

## License

*(Specify your license here, if applicable.)*

---

## Contact

For any questions or support regarding this integration, please contact [your-email@example.com](mailto:your-email@example.com).

