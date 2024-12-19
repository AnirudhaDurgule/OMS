from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from django.contrib import messages
from random import randrange
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt

def home(request):
    print(request.session) 
    if not request.session.get('is_logged_in'):
        return redirect('ulogin')

    return render(request, 'home.html')

def ulogin(request):
    if request.session.get('is_logged_in'):
        return redirect("home")

    if request.method == "POST":
        mobile_number = request.POST.get("un")

        url = 'http://192.168.50.35:5000/userRegistration/'
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "mobileNumber": mobile_number,
            "source": "web"
        }
        request.session["clientCode"]=mobile_number
        print("Client Code ", request.session["clientCode"])

        try:
            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                try:
                    response_data = response.json()
                    if response_data.get("type") == "success":
                        request.session["clientCode"]=mobile_number
                        reset_password_url = 'http://192.168.50.35:5000/resetPassword/'
                        reset_data = {
                            "clientCode": mobile_number,
                        }

                        reset_response = requests.get(reset_password_url, headers=headers, json=reset_data)
                        reset_data_response = reset_response.json()

                        if reset_data_response.get("type") == "success" and reset_data_response.get("resetPassword") == False:
                            return redirect('password')
                        else:
                            request.session['mobile_number'] = mobile_number
                            return redirect('verify_password')
                            # request.session['is_logged_in'] = True
                            # request.session['mobile_number'] = mobile_number
                            # return redirect("home")
                    else:
                        return render(request, "login.html", {
                            "login_msg": "We Are Unable To Find Entered User ID... Please Contact System Administrator",
                            "incorrect_attempt": True
                        })
                except ValueError:
                    print("Failed to parse JSON response")
                    return render(request, "login.html", {
                        "login_msg": "Unexpected response format. Please try again.",
                        "incorrect_attempt": True
                    })
            else:
                return render(request, "login.html", {
                    "login_msg": "We Are Unable To Find Entered User ID... Please Contact System Administrator",
                    "incorrect_attempt": True
                })

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return render(request, "login.html", {
                "login_msg": "An error occurred. Please try again later.",
                "incorrect_attempt": True
            })

    return render(request, "login.html")

def verify_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('oldPassword')
        new_password = request.POST.get('newPassword')
        client_code = request.session.get("mobile_number")

        url = 'http://192.168.50.35:5000/verifyOTP'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'sessionid={request.COOKIES.get("sessionid")}'
        }
        data = {
            "clientCode": client_code,
            "password": old_password,
            "newPasword": new_password
        }
        print("Payload sent to API:", data)

        try:
            response = requests.post(url, headers=headers, json=data)
            print(response.text)
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get("type") == "success":
                    messages.success(request, "Password successfully changed.")
                    return redirect('home')
                else:
                    messages.error(request, response_data.get("message", "Failed to change password. Please try again."))
            else:
                messages.error(request, "Failed to change password. Please try again.")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            messages.error(request, "An error occurred. Please try again later.")

    return render(request, 'verify_password.html')

def password(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)
            client_code = data.get('clientCode')
            password = data.get('password')
            new_password = data.get('newPasword', "")

            # Check if clientCode and password are provided
            if not client_code or not password:
                return JsonResponse({"status": "error", "message": "Client code or password is missing."}, status=400)

            # API URL for verifying the password
            url = 'http://192.168.50.35:5000/verifyOTP'

            # Headers for the API request
            headers = {
                'Content-Type': 'application/json',
                'Cookie': request.COOKIES.get('sessionid', ''),
            }

            # Payload for the API request
            payload = {
                "clientCode": client_code,
                "password": password,
                "newPasword": new_password  # Send as received or leave empty
            }

            # Make the API request using the requests library
            response = requests.post(url, headers=headers, json=payload)

            # Handle the API response
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get("type") == "success":
                    # Success: Return success response
                    request.session['is_logged_in'] = True
                    return JsonResponse({"status": "success", "message": "Password successfully verified."})
                else:
                    # API responded but with an error
                    return JsonResponse({"status": "error", "message": response_data.get("message", "Verification failed.")}, status=400)
            else:
                # Handle non-200 status codes
                return JsonResponse({"status": "error", "message": "Failed to verify password. API error."}, status=response.status_code)
        except Exception as e:
            # Handle exceptions
            print(f"Error during API call: {e}")
            return JsonResponse({"status": "error", "message": "An error occurred while processing your request."}, status=500)

    # Render the password page for GET requests
    return render(request, 'password.html')

def get_market_depth(request):
    if request.method == "GET":
        # Get tokenNumber from query parameters
        token_number = request.GET.get("tokenNumber")
        if not token_number:
            return JsonResponse({"status": "error", "message": "Token number is required"})

        url = "http://192.168.50.35:5000/api/getPriceSnapshot/"
        headers = {
            "Content-Type": "application/json",
            "Cookie": "sessionid=76zbtd0v107wz6id6hcc983ya0647ftf",  # Replace with dynamic sessionid if needed
        }
        payload = {"tokenNumber": int(token_number)}
        
        try:
            response = requests.get(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data.get("type") == "success":
                    return JsonResponse({"status": "success", "result": data["result"]})
                else:
                    return JsonResponse({"status": "error", "message": "Data Not Available for This Provided TokenNumber."})
            else:
                return JsonResponse({"status": "error", "message": "Failed to fetch data from API"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"})
# def password(request):
#     if request.method == 'POST':
#         try:
#             # Parse the incoming JSON data
#             data = json.loads(request.body)
#             client_code = data.get('clientCode')
#             password = data.get('password')
#             new_password = data.get('newPasword', "")

#             # Check if clientCode and password are provided
#             if not password or not client_code:
#                 return JsonResponse({"status": "error", "message": "Client code or password is missing."}, status=400)

#             # API URL for verifying the password
#             url = 'http://192.168.50.35:5000/verifyOTP'

#             # Headers for the API request
#             headers = {
#                 'Content-Type': 'application/json',
#                 'Cookie': f"sessionid={request.COOKIES.get('sessionid')}",
#             }

#             # Payload for the API request
#             payload = {
#                 "clientCode": client_code,
#                 "password": password,
#                 "newPasword": new_password  # You can update this if needed
#             }

#             # Make the API request using the requests library
#             response = requests.post(url, headers=headers, json=payload)

#             # Check the response status code
#             if response.status_code == 200:
#                 response_data = response.json()
#                 if response_data.get("type") == "success":
#                     # Success: Return success response
#                     request.session['is_logged_in'] = True
#                     return JsonResponse({"status": "success", "message": "Password successfully verified."})
#                 else:
#                     # API responded but with an error
#                     return JsonResponse({"status": "error", "message": response_data.get("message", "Verification failed.")}, status=400)
#             else:
#                 # Handle non-200 status codes
#                 return JsonResponse({"status": "error", "message": "Failed to verify password. API error."}, status=500)
#         except Exception as e:
#             # Handle exceptions such as network issues
#             print(f"Error during API call: {e}")
#             return JsonResponse({"status": "error", "message": "An error occurred while processing your request."}, status=500)

#     # Render the password page for GET requests
#     return render(request, 'password.html')
    
def home_view(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        response = requests.post('https://neuronsoft.in/api/new_ticker_search/', json={"ticker": "NIFTY"})
        stock_data = response.json()
        return JsonResponse(stock_data)

    return render(request, 'home.html')

def order_book_view(request):
    api_url = 'http://192.168.50.35:5000/api/orderBook/'  # Ensure this is the correct endpoint
    sessionid = request.COOKIES.get('sessionid')
    client_code = request.session.get("mobile_number")  # Assuming client_code is stored in session
    
    # Log session details
    print(f"Session ID: {sessionid}")
    print(f"Client Code: {client_code}")

    if not sessionid:
        return JsonResponse({'error': 'Session ID not found in cookies'}, status=400)

    # Prepare headers, cookies, and payload
    cookies = {'sessionid': sessionid}
    headers = {'Content-Type': 'application/json'}
    payload = {'clientCode': client_code}

    try:
        # Use POST request (adjust to GET if needed)
        response = requests.post(api_url, cookies=cookies, json=payload, headers=headers)
        
        # Log the API response details
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        if response.status_code == 200:
            data = response.json()
            if data.get("type") == "success":
                return JsonResponse({'order_book': data['order_book']})
            else:
                return JsonResponse({'error': 'Failed to fetch order book data'})
        else:
            return JsonResponse({'error': 'Error fetching data from API', 'details': response.text}, status=500)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'API request error: {str(e)}'}, status=500)

def trade_book_view(request):
    api_url = 'http://192.168.50.35:5000/api/strategyTradeBook/'
    sessionid = request.COOKIES.get('sessionid')
    client_code = request.session.get("mobile_number")  # Assuming clientCode is stored in session

    if not sessionid:
        return JsonResponse({'error': 'Session ID not found in cookies'}, status=400)

    cookies = {'sessionid': sessionid}
    headers = {'Content-Type': 'application/json'}
    payload = {'clientCode': client_code}

    try:
        response = requests.post(api_url, cookies=cookies, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("type") == "success":
                return JsonResponse({'trade_book': data['trade_book']})
            else:
                return JsonResponse({'error': 'Failed to fetch trade book data'})
        else:
            return JsonResponse({'error': 'Error fetching data from API', 'details': response.text}, status=500)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'API request error: {str(e)}'}, status=500)
    
def net_position_view(request):
    api_url = 'http://192.168.50.35:5000/api/strategyNetPosition/'
    sessionid = request.COOKIES.get('sessionid')
    client_code = request.session.get("mobile_number")  # Assuming clientCode is stored in session

    if not sessionid:
        return JsonResponse({'error': 'Session ID not found in cookies'}, status=400)

    cookies = {'sessionid': sessionid}
    headers = {'Content-Type': 'application/json'}
    payload = {'clientCode': client_code}

    try:
        response = requests.post(api_url, cookies=cookies, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("type") == "success":
                net_position = json.loads(data['net_position'])
                return JsonResponse({'net_position': net_position})
            else:
                return JsonResponse({'error': 'Failed to fetch net position data'})
        else:
            return JsonResponse({'error': 'Error fetching data from API', 'details': response.text}, status=500)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'API request error: {str(e)}'}, status=500)


def strategy_net_position_view(request):
    api_url = 'http://192.168.50.35:5000/api/strategyNetPosition/'
    sessionid = request.COOKIES.get('sessionid')
    client_code = request.session.get("mobile_number")  # Assuming clientCode is stored in session

    if not sessionid:
        return JsonResponse({'error': 'Session ID not found in cookies'}, status=400)

    cookies = {'sessionid': sessionid}
    headers = {'Content-Type': 'application/json'}
    payload = {'clientCode': client_code}

    try:
        response = requests.post(api_url, cookies=cookies, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("type") == "success":
                net_position = json.loads(data['net_position'])
                return JsonResponse({'net_position': net_position})
            else:
                return JsonResponse({'error': 'Failed to fetch net position data'})
        else:
            return JsonResponse({'error': 'Error fetching data from API', 'details': response.text}, status=500)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'API request error: {str(e)}'}, status=500)  

    
TOKEN = '0XaWQVoOO16sug0Mpj970rYQXjfVg0sY'

def get_symbols(request):
    try:
        response = requests.get('http://192.168.112.81:8010/v1/symbol', headers={
            'auth-token': TOKEN,
            'Content-Type': 'application/json'
        })
        response.raise_for_status()
        symbols = response.json()
        return JsonResponse(symbols['data'], safe=False)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_expiry(request):
    symbol = request.GET.get('symbol')
    try:
        response = requests.get(f'http://192.168.112.81:8010/v1/expiry?sym={symbol}&opt_type=opt', headers={
            'auth-token': TOKEN,
            'Content-Type': 'application/json'
        })
        response.raise_for_status()
        expiry_data = response.json()
        return JsonResponse(expiry_data['data'], safe=False)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_strikes(request):
    symbol = request.GET.get('symbol')
    expiry = request.GET.get('expiry')
    try:
        response = requests.get(f'http://192.168.112.81:8010/v1/strikes?sym={symbol}&exp={expiry}', headers={
            'auth-token': TOKEN,
            'Content-Type': 'application/json'
        })
        response.raise_for_status()
        strikes_data = response.json()
        return JsonResponse(strikes_data['data'], safe=False)
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def add_strategy(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)


            payload = {
                "portfolio": data.get("portfolio", ""),
                "client_id": data.get("client_id", ""),
                "underlying": data.get("underlying", ""),
                "strategy_code": data.get("strategy_code", ""),
                "bidding_mode": data.get("bidding_mode", ""),
                "spread_type": data.get("spread_type", ""),
                "legs_info": {
                    "leg1": {
                        "type": data.get("legs_info", {}).get("leg1", {}).get("type", ""),
                        "strike": data.get("legs_info", {}).get("leg1", {}).get("strike", 0),
                        "quantity": data.get("legs_info", {}).get("leg1", {}).get("quantity", 0),
                        "executionType": data.get("legs_info", {}).get("leg1", {}).get("executionType", ""),
                        "ratio": data.get("legs_info", {}).get("leg1", {}).get("ratio", 1),
                        "expiry": data.get("legs_info", {}).get("leg1", {}).get("expiry", "")
                    },
                    "leg2": {
                        "type": data.get("legs_info", {}).get("leg2", {}).get("type", ""),
                        "strike": data.get("legs_info", {}).get("leg2", {}).get("strike", 0),
                        "quantity": data.get("legs_info", {}).get("leg2", {}).get("quantity", 0),
                        "executionType": data.get("legs_info", {}).get("leg2", {}).get("executionType", ""),
                        "ratio": data.get("legs_info", {}).get("leg2", {}).get("ratio", 1),
                        "expiry": data.get("legs_info", {}).get("leg2", {}).get("expiry", "")
                    },
                    
                },
                "active": data.get("active", True),
                "expiry": data.get("expiry", "")
            }


            url = 'http://192.168.112.81:8010/v1/strategy-watchlist'
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json',
                'auth-token': '0XaWQVoOO16sug0Mpj970rYQXjfVg0sY'
            }

            response = requests.post(url, headers=headers, json=payload)


            if response.status_code == 200:
                return JsonResponse({"message": "Strategy added successfully", "data": response.json()}, status=200)
            else:
                return JsonResponse({"error": "Failed to send data", "status_code": response.status_code, "response": response.text}, status=response.status_code)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Method not allowed"}, status=405)

def strategy_watchlist(request):
    api_url = 'http://192.168.112.81:8010/v1/strategy-watchlist-gp'

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'http://172.16.47.87:5173',
        'Referer': 'http://172.16.47.87:5173/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
        'auth-token': '0XaWQVoOO16sug0Mpj970rYQXjfVg0sY'
    }

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()


        data = response.json().get('data', {})

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        data = {}

    # Pass data to the template
    return render(request, 'strategy_table.html', {'userStrategy': data})

@csrf_exempt
def modify_order(request):
    if request.method == 'POST':
        try:
           
            response_data = {
                "type": "success",
                "desc": "Order modified successfully."
            }
            return JsonResponse(response_data, status=200)
 
        except json.JSONDecodeError:
            return JsonResponse({"type": "failure", "desc": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"type": "failure", "desc": str(e)}, status=500)
    else:
        return JsonResponse({"type": "failure", "desc": "Method not allowed."}, status=405)
   
@csrf_exempt
def cancel_order(request):
    if request.method == 'POST':
        try:
            response_data = {
                "type": "success",
                "desc": "Order cancelled successfully."
            }
            return JsonResponse(response_data, status=200)
 
        except json.JSONDecodeError:
            return JsonResponse({"type": "failure", "desc": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"type": "failure", "desc": str(e)}, status=500)
    else:
        return JsonResponse({"type": "failure", "desc": "Method not allowed."}, status=405)


def get_ltpPrice(sym, expiry, strike, opt_type):
    url = "http://192.168.112.81:8010/v1/ltp"

    # payload = json.dumps({
    # "symbol": "NIFTY",
    # "expiry": "03OCT2024",
    # "strike": "26000",
    # "opt_type": "CE"
    # })
    headers = {
    'accept': 'application/json',
    'auth-token': 'hq9CgjUSAyouc6kKfGzowKo7J5orVaLB',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps({
    "symbol": sym,
    "expiry": expiry,
    "strike": strike,
    "opt_type": opt_type
    }))

    return response
 
@csrf_exempt
def place_order(request):
    
    if request.method == 'POST':

        try:
            url = 'http://192.168.50.35:5000/api/placeOrder/'
            headers = {
                'Content-Type': 'application/json',
            }
            sessionid = request.COOKIES.get('sessionid')
            if not sessionid:
                return JsonResponse({'error': 'Session ID not found in cookies'}, status=400)

            cookies = {'sessionid': sessionid}

           
            data = json.loads(request.body)

            
            response = requests.post(url, headers=headers, cookies=cookies, json=data)

            print("Response data =>", response)

            if response.status_code == 200:
                return JsonResponse({"message": "Order placed successfully", "data": response.json()}, status=200)
            else:
                return JsonResponse({"error": "Failed to send data", "status_code": response.status_code, "response": response.text}, status=response.status_code)

        except json.JSONDecodeError:
            return JsonResponse({"type": "failure", "desc": "Invalid JSON."}, status=400)
        except Exception as e:
            return JsonResponse({"type": "failure", "desc": str(e)}, status=500)
    else:
        return JsonResponse({"type": "failure", "desc": "Method not allowed."}, status=405)
    
def strategy_list(request):
    return render(request, 'strategy.html')

def ulogout(request):
    request.session.flush()
    return redirect('ulogin')