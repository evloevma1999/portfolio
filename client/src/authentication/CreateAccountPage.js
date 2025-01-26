import React, { useState } from "react";
import axios from "axios";

const CreateAccountPage = ({ setPage }) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleCreateAccount = async () => {
        try {
            const response = await axios.post("http://localhost:5000/create-account", {
                username,
                password,
            });
            alert(response.data.message);
            setPage("login");
        } catch(error) {
            alert(error.response?.data?.message || "An error occurred");
        }
    };

    return (
        <div>
            <h2>Create Account</h2>
            <form
                onSubmit={(e) => {
                    e.preventDefault();
                    handleCreateAccount();
                }}
            >
                <input
                    type = "text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <br />
                <input
                    type = "password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br />
                <button type="submit">Create Account</button>
            </form>
            <p>
                Already have an account? {" "}
                <span style={{ color: "blue", cursor: "pointer" }} onClick={() => setPage("login")}>
                    Log In
                </span>
            </p>
        </div>
    )
}

export default CreateAccountPage