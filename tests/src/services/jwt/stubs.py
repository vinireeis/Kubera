from src.domain.models.user.model import UserModel


user_data = {
  "username": "vini",
  "id": "0149fcd5-fa2f-4648-b14c-0a59864dc906",
  "password": "$2b$12$t91S8c6oJEkmd3Gej3Lrpu0IjUXSt9LHGg8AdNpkKbV6noZDaRlIW",
  "credit_card": [
    {
      "exp_date": "2027-05-31",
      "holder": "Vinicius",
      "number": {
        "$binary": {
          "base64": "Z0FBQUFBQmtFZHVYeXVtNU5xRVMyNFVZTkNjSksyRlFwS2UySWZGVS1mYTB6S1VZTEg2QVNwZzJKQmlpT0k1cFdWUlFqLWwzRHQ1UWlnWElDRWtPMnBwSWVsTFRJZVN2UU9sRTZGeUstNHY5Q3RQd19kMEw5bE09",
          "subType": "00"
        }
      },
      "cvv": 956
    },
    {
      "exp_date": "2027-05-31",
      "holder": "Vinicius",
      "number": {
        "$binary": {
          "base64": "Z0FBQUFBQmtFZHdFdnZpQ1F1bGpJbENTQ2RPTDF6bFVVbXY4ZGZNWTFGX2tOTjhiNWtrbi12S0tnQlFyTjRlWldnWWhkTTVnZTk1SVhfaUFaRUhMcXZjNU9YQWp5ckt3QWQ2ekJGakwxYjBRNUpiZV83MzNPNk09",
          "subType": "00"
        }
      },
      "cvv": 956
    }
  ]
}

stub_user_model = UserModel(user_data=user_data)
