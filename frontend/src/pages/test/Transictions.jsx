import { useState, useEffect } from "react";
import api from "../../utils/api";

export default function Transactions() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    api.get("/transactions/list/").then(res => setTransactions(res.data));
  }, []);

  return (
    <div>
      <h2>Your Transactions</h2>
      {transactions.length === 0 ? (
        <p>No transactions yet.</p>
      ) : (
        <ul>
          {transactions.map(tx => (
            <li key={tx.id}>
              {tx.title} — {tx.amount}$ at {tx.place} ({tx.category})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
