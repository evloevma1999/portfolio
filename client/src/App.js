import React, { useState } from 'react'
import LoginPage from "./authentication/LoginPage";
import CreateAccountPage from "./authentication/CreateAccountPage"
import CreatePortfolioPage from "./portfolio_manager/CreatePortfolioPage"
import PortfolioHomePage from "./portfolio_manager/PortfolioHomePage"

const App = () => {
  const [page, setPage] = useState("login");
  const [clientId, setClientId] = useState("")

  return (
    <div>
      {page == "login" ? (
        <LoginPage setPage={setPage} setClientId={setClientId}/>
      ) : page == "create_account" ? (
        <CreateAccountPage setPage={setPage} />
      ) : page == "portfolio_home" ? (
        <PortfolioHomePage setPage={setPage} clientId={clientId} />
      ): page == "create_portfolio" ? (
        <CreatePortfolioPage setPage={setPage} />
      ) : (
        <LoginPage setPage={setPage} />
      )}
    </div>
  );
}

export default App