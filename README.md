# AutomateInvesting
Welcome to AutomateInvesting, a dollar-cost averaging bot designed to operate seamlessly in the cloud. This tool is crafted to assist investors in executing consistent investment strategies with ease. By interfacing with the TD Ameritrade API, AutomateInvesting offers a user-friendly experience for managing investments across multiple stocks. Whether you're looking to run it on a local machine or deploy it on the cloud, this bot is equipped with functionality to send text alerts for trades, allowing users to stay informed on the go. It's customizable to fit various risk tolerances and investment preferences, making it a versatile tool for both new and seasoned investors.

## Features

- **Investment Automation:** Runs on the cloud or a local machine for convenient investing.
- **Multi-Stock Investment:** Allocates investments evenly across user-selected stocks.
- **Trade Alerts:** Sends text alerts for executed trades, keeping users informed.
- **TD Ameritrade Integration:** Seamlessly works with TD Ameritrade's API for reliable data and transactions.
- **Customizable Investment Strategy:** Users can specify the number of shares to purchase, allowing for tailored risk management and consistent dollar-cost averaging.
- **Automatic Token Refresh:** Automatically generates a new access token every 30 minutes to maintain API connectivity.
- **Account Balance Check:** Verifies user account balance before each trade to ensure sufficient funds are available. If funds are insufficient, the trade is skipped and reattempted the next day.



## Getting Started
To set up AutomateInvesting, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/arunrai3/AutomateInvesting.git

2. **Navigate to the Repository Directory:**
   ```bash
   cd AutomateInvesting

3. **Install Dependencies:**
   Run the following command from root directory to install the necessary dependencies:
   ```bash
   pip install -r requirements.txt

4. **Set Up Twilio Account:**
   Create an account on [Twilio](https://twilio.com/), and obtain an API key and a phone number.

5. **Get Refresh Token**
   This feature will only work if you currently have a TD Ameritrade API account setup. Visit this [link](https://developer.tdameritrade.com/authentication/apis/post/token-0) to get refresh token from TD Ameritrade.

6. **(Optional) Set Up Cloud Server:**
   Choose and set up a cloud server with your preferred provider.

7. **Run the Bot:**
   Execute the main script:
   ```bash
   python main.py


## Risk Disclosure

**Please Note:** AutomateInvesting is a tool intended solely for educational purposes. Users should be aware that investing in the stock market involves a degree of risk, and potential investors should do their own research or consult with a financial advisor before making any investment decisions. Not only does the stock market have risk, but so do algorithms like this one that are used to make trades. Please be aware of bugs and tailor your risk tolerance based on possiblity of computer errors. The creators and contributors of AutomateInvesting are not responsible for any financial losses that may result from using this tool. By using AutomateInvesting, you acknowledge and agree that you are solely responsible for your investment decisions and any resulting gains or losses.
