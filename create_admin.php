<?php
// Database connection
$conn = new mysqli("localhost", "root", "", "kafan_digitals");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Admin credentials
$username = 'kafan'; // or any username you want
$password = 'kafan123'; // change this to a secure password

// Hash the password for security
$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// Insert the admin user into the database
$sql = "INSERT INTO users (username, password) VALUES ('$username', '$hashed_password')";

if ($conn->query($sql) === TRUE) {
    echo "Admin user created successfully!";
} else {
    echo "Error: " . $conn->error;
}

// Close connection
$conn->close();
?>
