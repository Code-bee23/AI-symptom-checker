// -----------------------------
// Search Symptoms
// -----------------------------

const search = document.getElementById("search");
const symptomItems = document.querySelectorAll(".symptom-item");

// Use "input" instead of "keyup" — also catches paste, cut,
// autofill, and mobile keyboard events that don't always fire keyup.
search.addEventListener("input", function () {

    const value = this.value.toLowerCase();

    symptomItems.forEach(item => {

        const text = item.textContent.toLowerCase();

        // Reset to "" instead of hardcoding "block" so it falls back
        // to whatever display value your CSS actually uses (flex, etc).
        item.style.display = text.includes(value) ? "" : "none";

    });

});

// -----------------------------
// Select All
// -----------------------------

document.getElementById("selectAll").addEventListener("click", () => {

    document.querySelectorAll("input[name='selected_symptoms']").forEach(cb => {
        cb.checked = true;
    });

    document.querySelectorAll(".chip").forEach(chip => {
        chip.classList.add("active");
    });

});

// -----------------------------
// Clear All
// -----------------------------

document.getElementById("clearAll").addEventListener("click", () => {

    document.querySelectorAll("input[name='selected_symptoms']").forEach(cb => {
        cb.checked = false;
    });

    document.querySelectorAll(".chip").forEach(chip => {
        chip.classList.remove("active");
    });

});

// -----------------------------
// Common Symptoms (chips)
// -----------------------------

document.querySelectorAll(".chip").forEach(chip => {

    chip.addEventListener("click", () => {

        const symptom = chip.dataset.symptom;

        const checkbox = document.querySelector(
            `input[name="selected_symptoms"][value="${symptom}"]`
        );

        if (checkbox) {

            checkbox.checked = !checkbox.checked;
            checkbox.dispatchEvent(new Event("change"));
            checkbox.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        }

    });

});

const checkboxes = document.querySelectorAll(
'input[name="selected_symptoms"]'
);

const selectedBox = document.getElementById("selectedSymptoms");

function updateSelected(){

    let html = "";

    checkboxes.forEach(cb=>{

        if(cb.checked){

            html += `<span class="selected-chip">
                        ${cb.value.replaceAll("_"," ")}
                    </span>`;

        }

        const chip = document.querySelector(
            `.chip[data-symptom="${cb.value}"]`
        );

        if(chip){

            chip.classList.toggle("active",cb.checked);

        }

    });

    selectedBox.innerHTML = html || "<p>No symptoms selected.</p>";

}

checkboxes.forEach(cb=>{

    cb.addEventListener("change",updateSelected);

});

updateSelected();