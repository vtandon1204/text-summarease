document.addEventListener("DOMContentLoaded", () => {
    const summarizeBtn = document.getElementById("summarizeBtn");
    const clearBtn = document.getElementById("clearBtn");
    const textInput = document.getElementById("textInput");
    const summaryText = document.getElementById("summaryText");
    const resultDiv = document.getElementById("result");
    const charCount = document.getElementById("charCount");
    const errorMessage = document.getElementById("errorMessage");
    
    // Update character count
    textInput.addEventListener("input", () => {
        const inputLength = textInput.value.length;
        charCount.textContent = `${inputLength} / 5000`;
        if (inputLength > 5000) {
            charCount.classList.add("exceeded");
        } else {
            charCount.classList.remove("exceeded");
        }
    });

    // Generate summary on button click
    summarizeBtn.addEventListener("click", async () => {
        const text = textInput.value.trim();
        if (text === "") {
            errorMessage.textContent = "Please enter some text to summarize.";
            errorMessage.classList.remove("hidden");
            return;
        }

        errorMessage.classList.add("hidden");
        resultDiv.classList.add("hidden"); // Hide result initially

        // Show loading spinner
        const spinner = summarizeBtn.querySelector(".spinner");
        spinner.classList.remove("hidden");

        try {
            const response = await fetch("/summarize", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ text }),
            });

            const data = await response.json();
            if (response.ok) {
                summaryText.textContent = data.summary || "No summary available.";
                resultDiv.classList.remove("hidden");
            } else {
                errorMessage.textContent = data.error || "An error occurred.";
                errorMessage.classList.remove("hidden");
            }
        } catch (error) {
            errorMessage.textContent = "Failed to fetch summary.";
            errorMessage.classList.remove("hidden");
        } finally {
            spinner.classList.add("hidden"); // Hide spinner
        }
    });

    // Clear input and output on button click
    clearBtn.addEventListener("click", () => {
        textInput.value = ""; // Clear input field
        summaryText.textContent = ""; // Clear summary text
        resultDiv.classList.add("hidden"); // Hide the result area
        charCount.textContent = "0 / 5000"; // Reset character count
        charCount.classList.remove("exceeded"); // Remove exceeded class
        errorMessage.classList.add("hidden"); // Hide any error message
    });
});
