document.addEventListener('DOMContentLoaded', function () {
    const noButton = document.querySelector('.no');
    const yesButton = document.querySelector('.yes');
    const mainDiv = document.querySelector('.main');
    const part2Div = document.querySelector('.part2');
    let clickCount = 0;

    if (noButton && yesButton && mainDiv && part2Div) {
        noButton.addEventListener('mousemove', function (event) {
            const minOffset = 50; // Minimum offset in pixels
            const maxOffset = 80; // Maximum offset in pixels
            const randomX = (Math.random() * (maxOffset - minOffset) + minOffset) * (Math.random() < 0.5 ? -1 : 1); // Random X offset
            const randomY = (Math.random() * (maxOffset - minOffset) + minOffset) * (Math.random() < 0.5 ? -1 : 1); // Random Y offset

            // Move the button away from the cursor
            noButton.style.transition = ''; // Re-enable transition
            noButton.style.position = 'fixed'; // Set button position to fixed
            noButton.style.transform = `translate(${randomX}px, ${randomY}px)`; // Apply random offset

            // Prevent event propagation to avoid interference with other elements
            event.stopPropagation();
        });

        // Reset button position when the mouse leaves the button area
        noButton.addEventListener('mouseleave', function (event) {
            noButton.style.transition = 'transform 0.3s'; // Apply transition for smooth movement
            noButton.style.transform = 'translate(0, 0)'; // Reset to initial position
        });

        noButton.addEventListener('click', function () {
            clickCount++;

            if (clickCount >= 4) {
                // Hide the button
                noButton.style.display = 'none';
            }
        });
        
        yesButton.addEventListener('click', function () {
            // Hide the main div
            mainDiv.style.display = 'none';
            part2Div.style.display = 'flex';
        });
        document.getElementById("phone").addEventListener("input", function() {
            var input = this.value;
            var numbers = input.replace(/\D/g, ''); // Remove non-numeric characters
            
            // Update the input field value to only include numeric characters
            this.value = numbers;
        });
        document.getElementById("extractButton").addEventListener("click", function() {
            var message = document.getElementById("messageTextarea").value;
            var date = document.getElementById("Date").value;
            var phone = document.getElementById("phone").value;
            console.log("Extracted date:", date);
            console.log("Extracted message:", message);
            console.log("Extracted Phone No.:", phone);
            
            // Do something with the extracted message, like displaying it
        });
    } else {
        console.error("Could not find one of the required elements: .no, .yes, .main");
    }
});
