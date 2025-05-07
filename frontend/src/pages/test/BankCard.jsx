import { useState, useEffect } from "react";
import api from "../../utils/api";

export default function BankCard() {
  const [card, setCard] = useState(null);
  const [amount, setAmount] = useState("");

  useEffect(() => {
    api.get("/users/bank-card/").then(res => setCard(res.data));
  }, []);

  const topUp = async () => {
    const res = await api.post("/users/top-up/", { amount });
    alert(res.data.detail);
    window.location.reload();
  };

  if (!card) return <div>Loading...</div>;

  return (
    <div>
      <h3>Card: {card.card_number}</h3>
      <p>CVV: {card.cvv}</p>
      <p>Balance: ${card.balance}</p>
      <input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount" />
      <button onClick={topUp}>Top Up</button>
    </div>
  );
}
