$(document).ready(function() {
  $("#signup-form").submit(function(event) {
    event.preventDefault(); // Prevent form submission
  
    var name = $("#name").val();
    var email = $("#email").val();
  
    if (name === "" || email === "") {
      alert("Please fill in all fields.");
      return;
    }
  
    var formData = {
      name: name,
      email: email
    };

    var submitButton = $("#subscribe-button");
    submitButton.prop("disabled", true); // Disable the button
    submitButton.html("Subscribing..."); // Change the button text
  
    $.ajax({
      url: "https://script.google.com/macros/s/AKfycbzhwIWkXsogbRxlZrCvMDXM8-k1_LDgJsXpEWt7_-DBv4s4Fq7VE1Gr2RBRxoPQu6IflA/exec",
      type: "POST",
      data: formData,
      dataType: "json",
      success: function(response) {
        console.log("Form submitted successfully");
        submitButton.html("Subscribed"); // Change the button text
        $("#name").val("");
        $("#email").val("");
        $("#success-message").text("Thank you for subscribing!");
      },
      error: function(error) {
        console.error("Error submitting form:", error);
        submitButton.prop("disabled", false); // Re-enable the button
        submitButton.html("Subscribe"); // Change the button text back
      }
    });
  });
});
