import React, { useState } from "react";
import axios from "axios";

const LoginPage = ({ setPage, setClientId }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        try {
            const response = await axios.post("http://localhost:5000/login", {
                username,
                password,
            });
            alert(response.data.message);
            if(response.status == 200) {
                setClientId(response.data.client_id);
                setPage("portfolio_home")
            }
        } catch (error) {
            alert(error.response?.data?.message || "An error occurred");
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form 
                onSubmit={(e) => {
                    e.preventDefault();
                    handleLogin()
                }}
            >
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <br />
                <input
                    type="password"
                    placeholder="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br />
                <button type="submit">Log In</button>
            </form>
            <p>
                Dont have an account? {" "}
                <span style={{ color: "blue", cursor: "pointer" }} onClick={() => setPage("create_account")}>
                    Create Account
                </span>
            </p>

        </div>
    )
}

export default LoginPage