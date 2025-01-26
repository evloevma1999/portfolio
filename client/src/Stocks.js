import React, { useState, useEffect } from 'react'

function Stocks() {

  const [data, setData] = useState([{}])

  useEffect(() => {
      fetch("/stocks").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
        }
      )
  }, [])

  return (
    <div>
        {(typeof data.stocks === 'undefined') ? (
          <p>Loading...</p>
        ) : (
          data.stocks.map((stock, i) => (
            <p key={i}>{stock.symbol}</p>
          ))
        )}
    </div>
  )
}

export default Stocks