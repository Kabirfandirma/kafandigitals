<?php
// Database connection
$conn = new mysqli("localhost", "root", "", "kafan_digitals");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Insert into database
$sql = "INSERT INTO messages (name, email, message) VALUES ('$name', '$email', '$message')";

if ($conn->query($sql) === TRUE) {
    echo "<script>alert('Message sent successfully!'); window.location.href='contact.html';</script>";
} else {
    echo "<script>alert('Error sending message!'); window.location.href='contact.html';</script>";
}

// Close connection
$conn->close();
?>
