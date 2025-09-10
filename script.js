document.getElementById("kuldes").addEventListener("click", function() {
    const hely = document.getElementById("hely").value.trim();

    if(hely === "") {
        alert("Kérjük, adja meg a lakóhelyét!");
    } else {
        alert("Köszönjük, hogy minket választott. A többit egy szakember a helyszínen megbeszéli Önnel.");
    }
});