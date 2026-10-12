// Import the Express framework
const express = require("express");

// Create an Express application
const app = express();

// Port on which the server will listen
const PORT = 3000;

// Define a route for the home page
app.get("/", (req, res) => {
  res.send("Hello from Docker multi-stage build!");
});

// Start the server and print a message in the console
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
