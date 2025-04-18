# 🎭 OnChain Confession Wall 🎭

Welcome to the **OnChain Confession Wall**, the place where your secrets stay safe, forever, on the Ethereum blockchain. Don't worry—this wall won't judge you. But it will **immortalize** your deepest confessions. 🔥

## 🚨 What is it?

**OnChain Confession Wall** is a decentralized application (DApp) that allows users to confess their secrets **anonymously** on the Ethereum blockchain. No one can delete or change your confession, and it stays there **forever**. Because who wouldn’t want their embarrassing moments written in the stars (or at least on the blockchain)?

## ⚡ Features

- **Submit Confessions**: Confess your deepest secrets to the blockchain.
- **Immutable**: Once on the blockchain, your confession stays there. Forever.
- **Anonymity**: No one can trace your confession back to you.
- **Confession History**: View and retrieve old confessions using their ID.

## 📜 How It Works

1. **Confess** your secret with the `confess` function.
2. **Immutable** storage: Once a confession is made, it cannot be removed or altered.
3. **Check** the confession with the `getConfession` function by using its ID.

## 💻 Requirements

- Python 3.x
- Web3.py library
- An Ethereum node access (Infura)
- A deployed **Confession Wall contract** on Ethereum (or deploy your own)
  
## 📥 How to Deploy & Interact

1. **Deploy the Contract**: Deploy the `ConfessionWall` contract using tools like Remix or Truffle.
2. **Set Up Python**: Install Web3.py (`pip install web3`) and set up your Ethereum access in `config.py`.
3. **Start Confessing**: Use the provided Python scripts to confess or retrieve your secrets.

### Run the Scripts:

- **To confess**:
  ```bash
  python confession_wall.py
