# Real-Time Stock Market Auction

A real-time stock market auction system built with Python, using WebSocket for client-server communication and peer-to-peer (P2P) interactions. This application allows users to participate in live stock auctions, placing bids and tracking stock prices in real-time.

![main image](https://github.com/sahanHansaja026/Real-Time-Stock-Market-Auction---Python-Web-Socket-/blob/main/image1.png)

## Features

- **Real-Time Bidding**: Users can place bids on stocks in real-time.
- **Live Price Updates**: Stock prices are updated live as bids are placed.
- **P2P Communication**: Supports peer-to-peer communication for enhanced scalability.
- **User Authentication**: Simple user authentication using CSV files.
- **CSV Data Storage**: User data and stock information are stored in CSV files.

## Tech Stack

- **Backend**: Python, WebSocket
- **Data Storage**: CSV files

## Dependencies

- socket
- threading
- csv
- random
- pandas

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/real-time-stock-market-auction.git
```

2. **Navigate to the project directory:**

```bash
cd real-time-stock-market-auction
```

3. **Install dependencies:**

```bash
pip install pandas
```

4. **Start the server:**

```bash
python server.py
```
The backend server should now be running and listening for client connections on port 2022.

4. **Start the client:**

```bash
python client.py
```

## Usage

Once the application is running, you can perform the following actions:

- **Register/Login**: Users must register or log in to participate in auctions.
- **Place Bids**: Users can place bids on available stocks.
- **Track Prices**: Users can see real-time updates of stock prices.
- **P2P Communication**: Peer-to-peer communication ensures efficient handling of bids and updates.

## Server Code Overview

### server.py

The `server.py` script is the main server-side code that handles client connections, user authentication, and real-time stock bidding. Below is a summary of the key parts of the server code:

- **Import Modules**: The script imports necessary modules such as `socket`, `threading`, `csv`, `random`, and `pandas`.

- **Handle Client Function**: This function handles individual client connections. It performs the following tasks:
  - Receives user ID and validates it.
  - Sends 10 random stock details to the client from `stocks.csv`.
  - Receives and processes bids from the client, updating `client.csv` with new bid information.
  - Continuously updates and sends the maximum bid to the client for a specified duration (300 seconds).

- **Start Server Function**: This function sets up the server socket, binds it to a port (2022), and listens for incoming client connections. For each new connection, it starts a new thread to handle the client.


## Data Files

- **stocks.csv**: Contains stock data with columns `Security`, `Symbol`, `Price`, and `Profit`.
- **client.csv**: Records client bids with columns `name`, `symbol`, and `bit`.

## Images

### Server Listening

![Server Listening](https://github.com/sahanHansaja026/Real-Time-Stock-Market-Auction---Python-Web-Socket-/blob/main/image3.png)

### Show Security, Symbol, Price and Profit in Clinet side

![Client Connection](https://github.com/sahanHansaja026/Real-Time-Stock-Market-Auction---Python-Web-Socket-/blob/main/image4.png)

### Finaly Output In Server Side

![Final OutPut](https://github.com/sahanHansaja026/Real-Time-Stock-Market-Auction---Python-Web-Socket-/blob/main/image2.png)

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests.
