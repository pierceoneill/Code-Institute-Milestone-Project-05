function sendMail(contactForm) {
    emailjs.send("gmail", "minderfinder", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "booking_request": contactForm.booking_request.value,
        "mobile": contactForm.mobile.value,
        "date": contactForm.date.value,
        "time": contactForm.time.value
    })
    .then(
        function(response) {
          messages.success(request, 'Form submission successful')
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
}