from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import re
import requests
from django.conf import settings  

def get_exchange_rate(source_currency, target_currency):
    api_key = settings.EXCHANGE_RATE_API_KEY  
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency}"
    response = requests.get(url)
    data = response.json()
    if data.get('result') != 'success':
        raise Exception("Error fetching exchange rate.")
    try:
        rate = data['conversion_rates'][target_currency]
    except KeyError:
        raise Exception("Unsupported target currency.")
    return rate

def convert_currency(amount, rate):
    return amount * rate

def format_conversion_message(amount, source, target, converted_amount):
    return f"{amount} {source} is equivalent to {converted_amount:.2f} {target}"

@csrf_exempt
def convert_currency_view(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON.'}, status=400)
        
        message = payload.get('message', '')
       
        match = re.match(r'/convert\s+([\d.]+)\s+(\w{3})\s+to\s+(\w{3})', message, re.IGNORECASE)
        if not match:
            return JsonResponse({'error': 'Invalid command format. Use: /convert <amount> <source_currency> to <target_currency>'}, status=400)

        amount = float(match.group(1))
        source_currency = match.group(2).upper()
        target_currency = match.group(3).upper()

        try:
            rate = get_exchange_rate(source_currency, target_currency)
            converted = convert_currency(amount, rate)
            result_message = format_conversion_message(amount, source_currency, target_currency, converted)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        return JsonResponse({'message': result_message}, status=200)

    return JsonResponse({'error': 'Invalid method'}, status=405)
