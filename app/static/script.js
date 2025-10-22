document.getElementById("research-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    const topic = formData.get("topic");
    const length = formData.get("length");
    const sections = Array.from(document.getElementById("sections").selectedOptions).map(option => option.value);
    const audience = formData.get("audience");

    const reportOutput = document.getElementById("report-output");
    reportOutput.innerHTML = "Generating report... Please wait.";

    const response = await fetch("/generate_report", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            topic: topic,
            length: length,
            sections: sections,
            audience: audience
        })
    });

    const data = await response.json();
    reportOutput.innerHTML = data.report;
});
