const input = document.getElementById("accountID");
const resultDiv = document.getElementById("result");

// Press Enter to search
input.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        loadProfile();
    }
});

async function loadProfile() {
    const id = input.value.trim();

    if (!id) {
        resultDiv.innerHTML = `<div class="error">Please enter an Account ID.</div>`;
        return;
    }

    resultDiv.innerHTML = `<div class="loading">Fetching profile...</div>`;

    try {
        const response = await fetch(`http://127.0.0.1:5000/api/profile/${id}`);
        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `<div class="error">${data.error}</div>`;
            return;
        }

        resultDiv.innerHTML = `
            <div class="card">
                <h2>${data.username}</h2>

                <div class="stat-grid">
                    <div class="stat">⭐ Stars: ${data.stars}</div>
                    <div class="stat">😈 Demons: ${data.demons}</div>
                    <div class="stat">💎 Diamonds: ${data.diamonds}</div>
                    <div class="stat">🏆 CP: ${data.cp}</div>
                    <div class="stat">🪙 Coins: ${data.coins}</div>
                    <div class="stat">🎨 Glow: ${data.glow ? "Yes" : "No"}</div>
                </div>
            </div>
        `;
    } catch (error) {
        resultDiv.innerHTML = `<div class="error">Cannot connect to backend.</div>`;
    }
}
