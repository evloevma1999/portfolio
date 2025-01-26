import Reac, { useState } from "react"
import axios from "axios"

const CreatePortfolioPage = ({setPage}) => {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleCreatePortfolio = async () => {
        try {
            const response = await axios.post("http://localhost:5000/create-portfolio", {
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
            <h2>Create Portfolio</h2>
            <p>
                Hello
            </p>
            <span style={{ color: "blue", cursor: "pointer" }} onClick={() => setPage("login")}>
                    Log Out
            </span>
        </div>
    )

}

export default CreatePortfolioPage