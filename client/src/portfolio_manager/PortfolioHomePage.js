import React, { useState, useEffect } from "react"
import axios from "axios"

const PortfolioHomePage = ({setPage, clientId}) => {
    const [portfolios, setPortfolios] = useState([]);

    useEffect(() => {
        if (!clientId) return;
        console.log(`http://localhost:5000/api/portfolios/${clientId}`)

        // Fetch portfolios for the logged-in client
        axios
            .get(`http://localhost:5000/api/portfolios/${clientId}`)
            .then((response) => {
                console.log(response.data)
                setPortfolios(response.data);
            })
            .catch((error) => {
                console.error("Error fetching portfolios:", error);
            });
    }, [clientId]);

    return(
        <div>
            <h2>
                Portfolios
            </h2>
            <p>
                Here:
            </p>
        </div>
    )

}

export default PortfolioHomePage;